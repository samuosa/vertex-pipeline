terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }

  # Setup standard GCS backend for CI/CD state management
  # backend "gcs" {
  #   bucket = "YOUR_STATE_BUCKET_NAME"
  #   prefix = "terraform/state"
  # }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

variable "project_id" {
  description = "The GCP Project ID"
  type        = string
  default     = "vertex-pipeline-awfg2"
}

variable "region" {
  description = "The GCP Region"
  type        = string
  default     = "us-central1"
}
