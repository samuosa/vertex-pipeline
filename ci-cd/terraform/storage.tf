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
