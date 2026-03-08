# SDXL/Pony XL GCP Infrastructure - Architecture Specification

## Required GCP APIs
The following APIs must be enabled for the infrastructure:
*   `run.googleapis.com` (Cloud Run)
*   `aiplatform.googleapis.com` (Vertex AI)
*   `storage.googleapis.com` (Cloud Storage)
*   `artifactregistry.googleapis.com` (Artifact Registry)
*   `iam.googleapis.com` (IAM)
*   `cloudresourcemanager.googleapis.com` (Resource Manager)

## Security & IAM Strategy

### Service Accounts
We follow the principle of least privilege, establishing dedicated service accounts for execution and CI/CD.

*   **`cloud-run-sa` (Cloud Run Execution Identity)**
    *   **Roles:**
        *   `roles/storage.objectViewer` (Read access to the Model Bucket)
        *   `roles/storage.objectUser` (Read/Write access to the Output Bucket)
        *   `roles/aiplatform.user` (Invoking Vertex AI endpoints/pipelines if required natively)
*   **`devops-pipeline-sa` (CI/CD Identity)**
    *   **Roles:**
        *   `roles/run.admin` (Deploying Cloud Run services)
        *   `roles/iam.serviceAccountUser` (Acting as `cloud-run-sa` during deployment)
        *   `roles/artifactregistry.writer` (Pushing container images)

### Client Access Boundaries
*   Users and automated clients will not be granted direct access to buckets or internal APIs.
*   All invocations for text-to-image generation will go through the public Cloud Run HTTPS endpoint (properly authenticated via Cloud IAM or custom API gateway if defined later).

## Model Serving Architecture (TSK-005)

### Scale-to-Zero Cloud Run (L4 GPUs) Setup
The inference engine will be deployed as a containerized service on Cloud Run, optimized for rapid cold starts and cost efficiency.

*   **Compute Requirements:**
    *   **GPU:** 1x NVIDIA L4 GPU per instance.
    *   **CPU:** 4 vCPU (minimum recommended for stable inference).
    *   **Memory:** 16 GiB RAM.
    *   **Concurrency:** 1 (Strictly single-request concurrency to prevent GPU memory out-of-bounds errors on a single L4).
*   **Cold Start Optimization:**
    *   **Model Weights Loading:** We will utilize **Cloud Storage FUSE (GCSFuse)** to mount the `vertex-pipeline-base-models` bucket directly to the container at runtime. This avoids downloading multi-gigabyte safetensors on every spin-up.
    *   **Container Image:** Image Streaming will be enabled in Artifact Registry to begin container execution before the full image is downloaded.
*   **Container Dependencies:**
    *   Base Image: `nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04` (or similar compatible vLLM/Diffusers base).
    *   Python 3.10+, PyTorch, diffusers, xformers.

## Foundational Terraform Configuration

### `provider.tf`
```hcl
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}
```

### `apis.tf`
```hcl
variable "gcp_service_list" {
  description = "The list of APIs necessary for the project"
  type        = list(string)
  default = [
    "run.googleapis.com",
    "aiplatform.googleapis.com",
    "storage.googleapis.com",
    "artifactregistry.googleapis.com",
    "iam.googleapis.com",
    "cloudresourcemanager.googleapis.com"
  ]
}

resource "google_project_service" "enabled_apis" {
  for_each           = toset(var.gcp_service_list)
  project            = var.project_id
  service            = each.key
  disable_on_destroy = false
}
```

### `storage.tf`
```hcl
resource "google_storage_bucket" "base_models" {
  name          = "${var.project_id}-base-models"
  location      = var.region
  force_destroy = false

  uniform_bucket_level_access = true
}

resource "google_storage_bucket" "client_loras" {
  name          = "${var.project_id}-client-loras"
  location      = var.region
  force_destroy = false

  uniform_bucket_level_access = true
}

resource "google_storage_bucket" "image_outputs" {
  name          = "${var.project_id}-image-outputs"
  location      = var.region
  force_destroy = false

  uniform_bucket_level_access = true

  lifecycle_rule {
    condition {
      age = 7 # Delete outputs after 7 days to save cost
    }
    action {
      type = "Delete"
    }
  }
}
```

### `vertex.tf`
```hcl
resource "google_service_account" "vertex_pipeline_sa" {
  account_id   = "vertex-pipeline-sa"
  display_name = "Vertex AI Pipeline Service Account"
}

resource "google_project_iam_member" "vertex_user" {
  project = var.project_id
  role    = "roles/aiplatform.user"
  member  = "serviceAccount:${google_service_account.vertex_pipeline_sa.email}"
}

resource "google_project_iam_member" "vertex_storage_admin" {
  project = var.project_id
  role    = "roles/storage.objectAdmin"
  member  = "serviceAccount:${google_service_account.vertex_pipeline_sa.email}"
}
```

### `wif.tf`
```hcl
# Workload Identity Federation allows GitHub Actions to authenticate without a JSON service account key
resource "google_iam_workload_identity_pool" "github_pool" {
  workload_identity_pool_id = "github-actions-pool"
  display_name              = "GitHub Actions Pool"
}

resource "google_iam_workload_identity_pool_provider" "github_provider" {
  workload_identity_pool_id          = google_iam_workload_identity_pool.github_pool.workload_identity_pool_id
  workload_identity_pool_provider_id = "github-actions-provider"
  
  attribute_mapping = {
    "google.subject"       = "assertion.sub"
    "attribute.repository" = "assertion.repository"
  }
  
  oidc {
    issuer_uri = "https://token.actions.githubusercontent.com"
  }
}

resource "google_service_account" "cicd_sa" {
  account_id   = "github-actions-cd-sa"
  display_name = "Service Account for GitHub Actions CI/CD"
}

resource "google_service_account_iam_member" "workload_identity_user" {
  service_account_id = google_service_account.cicd_sa.name
  role               = "roles/iam.workloadIdentityUser"
  member             = "principalSet://iam.googleapis.com/${google_iam_workload_identity_pool.github_pool.name}/attribute.repository/samuosa/vertex-pipeline"
}

resource "google_project_iam_member" "cicd_editor" {
  project = var.project_id
  role    = "roles/editor"
  member  = "serviceAccount:${google_service_account.cicd_sa.email}"
}
```

## Vertex AI Pipelines (Phase 3)
The pipeline definitions are written in Python using the `kfp` (Kubeflow Pipelines) SDK v2. 
- **Location:** `pipelines/`
- **Configuration:** The pipeline simulates downloading base model weights and training client LoRAs. It compiles into a YAML format ready for submission to the Vertex AI Pipeline backend.

## GitHub Actions CI/CD
We use GitHub Actions to automate Terraform deployments.
- **Location:** `.github/workflows/deploy-infrastructure.yml`
- **Authentication:** Standard service account keys are disabled for security. Instead, GitHub Actions runs impersonate the `github-actions-cd-sa` via **Workload Identity Federation (WIF)** configured in `ci-cd/terraform/wif.tf`.
