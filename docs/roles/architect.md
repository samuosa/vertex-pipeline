# Architect Agent Procedure and Backlog

## Procedure: Design Phase (Phase 2)
1. **Review Requirements**: Analyze the Product Owner's `product_owner.md` to understand the business goal (multi-tenant, scale-to-zero Pony XL infrastructure).
2. **Infrastructure Design**: Create technical architecture diagrams for GCP, focusing on Cloud Run (L4 GPUs) and Vertex AI integration.
3. **Security & IAM**: Formulate a least-privilege IAM strategy for service accounts and user roles.
4. **API & Services Definition**: Identify and list all necessary GCP APIs and services required for the infrastructure.
5. **Handoff to Lead Dev**: Finalize the architectural specifications and hand off the execution to the Lead Dev for Terraform/IaC implementation.

## Phase 2 Milestones (Architect First Milestones)
*   **Milestone 2.1: Initial Architecture Draft** - Complete a high-level system overview defining interaction between Vertex AI, Cloud Run, and Cloud Storage.
*   **Milestone 2.2: Security Model Defined** - Document the exact IAM roles, Service Accounts, and network security boundaries.
*   **Milestone 2.3: Final Architecture Handoff** - Deliver the finalized architectural specifications (`architecture_spec.md`) to the Lead Dev.

## Architect Backlog

| Task ID | Phase | Description | Assignee | Status |
| :--- | :--- | :--- | :--- | :--- |
| ARCH-001 | Phase 2 | Define required GCP APIs for Vertex AI, Cloud Run, and Cloud Storage. | Architect | To Do |
| ARCH-002 | Phase 2 | Design IAM Roles and Service Accounts following the principle of least privilege. | Architect | To Do |
| ARCH-003 | Phase 2 | Design scale-to-zero Cloud Run (L4 GPUs) architecture for model serving, including cold-start optimization. | Architect | To Do |
| ARCH-004 | Phase 2 | Formulate storage strategy for SDXL/Pony XL model weights and generated images on Cloud Storage. | Architect | To Do |
| ARCH-005 | Phase 2 | Aggregate architectural decisions into an `architecture_spec.md` document for the Lead Dev. | Architect | To Do |
