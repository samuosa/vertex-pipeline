# SDXL/Pony XL Architecture

## 1. Architecture Overview
The scale-to-zero Pony XL Proof of Concept relies on Cloud Run with an attached NVIDIA L4 GPU to serve model inference, keeping costs at absolute zero when traffic is idle.
We utilize Vertex AI for configuring custom LoRA training pipelines and endpoints.
To avoid multi-gigabyte cold starts on Cloud Run, the base Pony XL model weights are mounted dynamically from Cloud Storage via GCSFuse at container spin-up, while output imagery is saved to a secondary bucket configured with a 7-day cost-saving lifecycle expiration.

## 2. Required GCP APIs
The following definitive list of `gcloud` services must be enabled:
*   `run.googleapis.com` (Cloud Run)
*   `aiplatform.googleapis.com` (Vertex AI)
*   `storage.googleapis.com` (Cloud Storage)
*   `artifactregistry.googleapis.com` (Artifact Registry)
*   `iam.googleapis.com` (IAM)
*   `cloudresourcemanager.googleapis.com` (Resource Manager)

## 3. Initial Terraform Configuration

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

## 4. Backlog Status Update

| Task ID | Phase | Description | Assignee | Status |
| :--- | :--- | :--- | :--- | :--- |
| TSK-001 | Phase 2 | Define required GCP APIs for Vertex AI, Cloud Run, and Cloud Storage | Architect | Done |
| TSK-002 | Phase 2 | Design IAM Roles and Service Accounts following the principle of least privilege | Architect | Done |
| TSK-003 | Phase 2 | Draft Initial Terraform configuration for Cloud Storage buckets | Lead Dev | To Do |
| TSK-004 | Phase 2 | Draft Terraform configuration for Vertex AI PoC environment | Lead Dev | To Do |
| TSK-005 | Phase 2 | Design scale-to-zero Cloud Run (L4 GPUs) architecture for model serving | Architect | Done |

### Next Steps for Lead/Worker Devs:
1.  **Lead Dev:** Review `architect.md` and initialize the physical Terraform repository for TSK-003 and TSK-004 utilizing the provided HCL blocks.
2.  **Lead Dev:** Begin writing the deployment pipeline scripts utilizing the `devops-pipeline-sa` service account design.
3.  **Worker Devs:** Check out the Artifact Registry for pushing the initial custom Docker image with Diffusers/vLLM dependencies.
