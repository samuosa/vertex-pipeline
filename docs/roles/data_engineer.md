# Data Engineer Procedure and Backlog

## Procedure: Model & Data Pipelines (Phase 1 & 3)
1. **Model Source Management**: Automate the procurement, validation, and version control of the SDXL/Pony XL model weights (e.g., from Hugging Face or internal repos).
2. **Storage Architecture**: Structure the GCS buckets for optimized, high-throughput model loading during Cloud Run cold starts (e.g., leveraging GCSFuse).
3. **Data Pre-/Post-Processing**: Implement backend data pipelines for standardizing incoming user prompts and archiving output images/metadata.
4. **Model Warmup Scenarios**: Design data caching strategies (like nearest-neighbor prompt caching) to reduce inference latency.
5. **Metrics Pipeline**: Ensure that model inference statistics and generation times are tracked and routed appropriately to data warehouses like BigQuery.

## Phase 1 & Phase 3 Milestones (Data Eng First Milestones)
*   **Milestone 1.1: Model Weight Pipeline** - Create an automated script to fetch, verify, and upload Pony XL model weights to Google Cloud Storage.
*   **Milestone 3.1: GCSFuse Integration Design** - Define the mounting strategy for injecting model weights into Cloud Run instances with minimal latency.
*   **Milestone 3.2: Analytics Export Setup** - Implement the data pipeline to export usage metadata and inference logs to BigQuery for cost analysis.

## Data Engineer Backlog

| Task ID | Phase | Description | Assignee | Status |
| :--- | :--- | :--- | :--- | :--- |
| DATA-001 | Phase 1 | Automate download, integrity check, and upload of Pony XL models to the central GCS bucket. | Data Engineer | To Do |
| DATA-002 | Phase 3 | Implement GCSFuse or native loading strategies to optimize model fetching in Cloud Run. | Data Engineer | To Do |
| DATA-003 | Phase 3 | Design the BigQuery schema for logging generation metadata, prompt usage, and latency metrics. | Data Engineer | To Do |
| DATA-004 | Phase 3 | Build a data pipeline to stream inference logs from Cloud Logging into BigQuery. | Data Engineer | To Do |
| DATA-005 | Phase 3 | Develop a prompt caching layer design to optimize repetitive inference requests. | Data Engineer | To Do |
