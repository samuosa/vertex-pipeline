# Spicy Engineer Procedure and Backlog

## Procedure: Specialized NSFW Pipeline (Phase X)
1. **Branch Management**: All development for the NSFW generation pipeline must occur on the dedicated `nsfw` branch to isolate experimental models and adult content filters from the main repository. When stable, changes will be explicitly merged into `main` and infrastructure tickets updated.
2. **Prompt Engineering & Tagging**: Implement a microservice for converting standard text prompts into Danbooru-style tags, optimizing specifically for Pony XL and SDXL NSFW capabilities.
3. **Character Training Pipeline**: Build the folder structure and orchestration scripts in `/pipelines/nsfw/characters/` to accept user-provided source images. Train character LoRAs and apply ControlNet for pose consistency.
4. **External Sourcing**: Search for, validate, and import relevant BDSM, fetish pose, and character LoRAs from HuggingFace (HF) or CivitAI into the pipeline. Track these in the internal registry.
5. **Integration**: Ensure the heavy models and custom pipelines integrate seamlessly with the existing scale-to-zero Cloud Run infrastructure designed by the Architect.

## First Milestones (Spicy Engineer)
*   **Milestone X.1: Pipeline Initialization** - The `nsfw` branch is cut, the `pipelines/nsfw` directory structure is created, and the source tracker is established.
*   **Milestone X.2: Danbooru Converter** - The text-to-Danbooru-tag microservice is deployed and tested for prompt optimization.
*   **Milestone X.3: Character Training Flow** - The ControlNet and LoRA training workflows for character references (`/characters/character_[name]`) are functional.

## Spicy Engineer Backlog

| Task ID | Phase | Description | Assignee | Status |
| :--- | :--- | :--- | :--- | :--- |
| SPICY-001 | Phase X | Initialize the `nsfw` branch and establish the specialized pipeline architecture over the existing infrastructure. | Spicy Engineer | To Do |
| SPICY-002 | Phase X | Develop the centralized text-to-Danbooru tag conversion microservice optimized for Pony XL. | Spicy Engineer | To Do |
| SPICY-003 | Phase X | Implement ControlNet and LoRA training pipeline for user-supplied character references in `/pipelines/nsfw/characters/`. | Spicy Engineer | To Do |
| SPICY-004 | Phase X | Import, validate, and document BDSM/fetish pose and character LoRAs from CivitAI/HF to the central registry. | Spicy Engineer | To Do |
