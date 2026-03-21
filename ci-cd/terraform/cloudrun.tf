# Service Account for Cloud Run execution (if not already defined in vertex.tf, though architect used vertex-pipeline-sa for both)
# Continuing with the vertex-pipeline-sa as defined by the user

# The Cloud Run V2 Service for the Pony XL Inference
resource "google_cloud_run_v2_service" "pony_xl_inference" {
  name     = "pony-xl-inference-service"
  location = var.region
  ingress  = "INGRESS_TRAFFIC_ALL"

  # The google-beta provider is often required for Cloud Run Volume Mounts (GCSFuse)
  provider = google-beta

  template {
    service_account = google_service_account.vertex_pipeline_sa.email

    # Disable GPU zonal redundancy to avoid the missing quota error
    # and require only a single zone's worth of L4 GPUs
    gpu_zonal_redundancy_disabled = true

    node_selector {
      accelerator = "nvidia-l4"
    }

    # Define the single container
    containers {
      # Placeholder Artifact Registry image (to be built by CI/CD)
      image = "us-central1-docker.pkg.dev/${var.project_id}/repo/pony-xl-inference:latest"

      resources {
        limits = {
          cpu    = "4"
          memory = "16Gi"
          # Require exactly 1 attached L4 GPU
          "nvidia.com/gpu" = "1"
        }
      }

      # GCSFuse Volume Mount mapping
      volume_mounts {
        name       = "models-volume"
        mount_path = "/models"
      }
    }

    # Connect the Cloud Storage Bucket to the Volume Mount
    volumes {
      name = "models-volume"
      gcs {
        bucket    = google_storage_bucket.base_models.name
        read_only = true
      }
    }

    # Strict scaling limits to enforce Cost-Control and Scale-To-Zero
    scaling {
      min_instance_count = 0
      max_instance_count = 10
    }

    # Ensure single concurrency per L4 GPU instance to prevent memory OOMs during inference
    max_instance_request_concurrency = 1

    # Optional: Enable Session Affinity if the model keeps conversational state
    # session_affinity = false
  }

  # Dependencies ensuring APIs and Storage are up
  depends_on = [
    google_project_service.enabled_apis,
    google_storage_bucket.base_models
  ]
}

# Allow unauthenticated invocations to the highly scalable public endpoint 
# (In production, replace with IAM bindings or API Gateway)
resource "google_cloud_run_v2_service_iam_member" "public_access" {
  project  = var.project_id
  location = google_cloud_run_v2_service.pony_xl_inference.location
  name     = google_cloud_run_v2_service.pony_xl_inference.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
