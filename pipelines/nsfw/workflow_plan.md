# End-to-End NSFW Pipeline Workflow

This document outlines the standard operating procedure for moving from a raw character concept to a final generated scene.

## Phase 1: Character Ingestion & Training
1.  **Source Collection:** Place 15-30 high-quality reference images in `/pipelines/nsfw/characters/[name]/references/`.
2.  **Tagging:** Use the `DanbooruConverter` to generate initial tags for the dataset.
3.  **Training:** Submit the `nsfw-character-training-pipeline` to Vertex AI.
    *   Target: `character_name` and `training_epochs`.
    *   Output: `[name]_v1.safetensors` stored in `gs://[project]-base-models/loras/`.

## Phase 2: Scene Definition (3-Tier)
1.  **Tier 1:** Define the narrative and visual goals.
2.  **Tier 2:** Translate goals into optimized Pony XL tags using `pony_prompts_guide.md`.
3.  **Tier 3:** Specify LoRA weights and ControlNet modules in a JSON config.

## Phase 3: Deployment & Execution
1.  **Infrastructure:** Ensure the Cloud Run `pony-xl-inference-service` is active (scale-to-zero).
2.  **Invocation:** Send a POST request to the `/sdapi/v1/txt2img` endpoint with the Tier 2 prompt and Tier 3 parameters.
3.  **GCSFuse:** The container mount ensures the model and LoRAs are loaded instantly without download overhead.

## Phase 4: Testing & Validation
1.  **Batch Generation:** Generate 5-10 images per scene to check for consistency.
2.  **Quality Check:** Evaluate against Tier 1 requirements (pose, gear, character fidelity).
3.  **Storage:** Final PNGs are automatically saved to `gs://[project]-image-outputs/` with a 7-day TTL.
