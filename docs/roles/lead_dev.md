# Lead Dev Agent Procedure and Backlog

## Procedure: Execution Phase (Phase 3)
1. **Review Architecture Spec**: Analyze the Architect's `architecture_spec.md` to understand the Infrastructure as Code (IaC) requirements for GCP.
2. **Terraform Initialization**: Set up the initial Terraform state, providers, and modules hierarchy for the GCP environment.
3. **Provision Storage**: Implement Terraform code for creating the necessary Cloud Storage buckets for SDXL/Pony XL models and the resulting generated images.
4. **Provision Vertex AI PoC**: Implement the Terraform to stand up the initial Vertex AI environment, configuring endpoints and permissions per the Architect's specification.
5. **Provision Cloud Run**: Implement the Terraform code for the scale-to-zero Cloud Run service with L4 GPUs, ensuring proper container registry integration and scaling configurations.
6. **Code Reviews & Testing**: Manually test the Terraform plans, ensuring state consistency and adherence to IAM least-privilege principles detailed by the Architect.

## Phase 3 Milestones (Lead Dev First Milestones)
*   **Milestone 3.1: Foundation & Storage Setup** - Complete Terraform provider setup, project instantiation, and Cloud Storage creation.
*   **Milestone 3.2: Vertex AI PoC Deployed** - Successfully deploy the Vertex AI endpoints via Terraform.
*   **Milestone 3.3: Cloud Run GPU Environment Configured** - Successfully deploy the Cloud Run environment configured for L4 GPUs and scale-to-zero.

## Lead Dev Backlog

| Task ID | Phase | Description | Assignee | Status |
| :--- | :--- | :--- | :--- | :--- |
| DEV-001 | Phase 3 | Initialize Terraform project structure and configure GCP providers. | Lead Dev | To Do |
| DEV-002 | Phase 3 | Implement Terraform for model and image Cloud Storage buckets as defined in `architecture_spec.md`. | Lead Dev | To Do |
| DEV-003 | Phase 3 | Draft and apply Terraform for Vertex AI PoC environment. | Lead Dev | To Do |
| DEV-004 | Phase 3 | Implement Terraform for the multi-tenant, scale-to-zero Cloud Run service with L4 GPUs. | Lead Dev | To Do |
| DEV-005 | Phase 3 | Apply IAM bindings via Terraform using the Service Accounts defined by the Architect. | Lead Dev | To Do |
