# Webcrawler Cloud Architect Procedure and Backlog

## Procedure: Parameterized Scraper & Dashboard (Phase S)
1. **Parameterized Engine Development**: Build a Cloud Run service in `webcrawler/pipelines` that accepts a dynamic list of URLs and transformation rules. Integration with Playwright is mandatory for modern web compatibility.
2. **Resilient Filtering (LLM-Based)**: Implement few-shot prompting to guide the LLM in extracting data based on structural HTML elements (e.g., `ul`, `table`) rather than volatile CSS selectors.
3. **Data Transformation & Storage**: Convert results into CSON/JSON format and stream directly to crawler-specific GCP buckets.
4. **Infrastructure as Code**: Manage all webcrawler-related GCP resources (buckets, Pub/Sub, Cloud Run) using Terraform in `webcrawler/terraform`.
5. **QA & Alerting Layer**: Integrate a validation step in every pipeline run to compare output against expected results. Use Google Cloud Pub/Sub to trigger alerts on breakage.
6. **Dashboard Development**: Build a React + Tailwind frontend in `webcrawler/frontend` to visualize pipeline status, run health, and metrics.

## First Milestones (Webcrawler Cloud Architect)
*   **Milestone S.1: Infrastructure & Core Engine** - Terraform setup in `webcrawler/terraform` and functional Playwright + LLM engine in `webcrawler/pipelines`.
*   **Milestone S.2: QA & Pub/Sub Integration** - Automated health checks and alerting for broken scraper pipelines.
*   **Milestone S.3: Scraper Dashboard v1** - React UI in `webcrawler/frontend` displaying real-time metrics and pipeline history.

## Webcrawler Cloud Architect Backlog

| Task ID | Phase | Description | Assignee | Status |
| :--- | :--- | :--- | :--- | :--- |
| SCRAPE-001 | Phase S | Build parameterized scraper engine with Playwright and LLM-based resilient filtering rules. | Webcrawler Cloud Architect | To Do |
| SCRAPE-002 | Phase S | Implement output transformation to CSON/JSON and dynamic GCP bucket provisioning via Terraform. | Webcrawler Cloud Architect | To Do |
| SCRAPE-003 | Phase S | Develop QA validation phase per pipeline run with input/output comparison logic. | Webcrawler Cloud Architect | To Do |
| SCRAPE-004 | Phase S | Configure Pub/Sub alerting for scraper breakage and detailed cloud logging. | Webcrawler Cloud Architect | To Do |
| SCRAPE-005 | Phase S | Implement Scraper Dashboard (React + Tailwind) in `webcrawler/frontend`. | Webcrawler Cloud Architect | To Do |
| SCRAPE-006 | Phase S | Integrate Dashboard with Cloud Storage backend for metric persistence. | Webcrawler Cloud Architect | To Do |
