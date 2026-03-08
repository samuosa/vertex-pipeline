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
