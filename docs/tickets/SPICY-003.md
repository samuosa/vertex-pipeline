---
id: SPICY-003
phase: Phase X
title: Implement ControlNet and LoRA Training for Character References
assignee: Spicy Engineer
status: To Do
---

# SPICY-003: Implement ControlNet and LoRA Training for Character References

## Description
Develop the automated pipeline to consume user-supplied character references and output trained LoRAs and ControlNet conditionings for consistent character/pose generation within the specific NSFW pipeline.

## Acceptance Criteria
- [ ] Implement the expected folder structure: `/pipelines/nsfw/characters/character_[charactername]/(/poses/charactertextandtagdescriptions/base)`.
- [ ] Build the script to automatically ingest images from this structure.
- [ ] Integrate a LoRA training script (e.g., kohya_ss) to train on the character faces/details.
- [ ] Integrate ControlNet (OpenPose/Depth/Canny) preprocessing for the reference pose images.
- [ ] Ensure the final models are saved to the correct GCS buckets.

## Updates
*(Workers: Append your updates, roadblocks, or PR links below this line)*
- **[2026-03-08] - Spicy Engineer:** Developed the `nsfw-character-training-pipeline` in `pipelines/nsfw/character_training_pipeline.py`. The pipeline handles ingestion from the character directory structure, implements Kohya-style LoRA training, and includes ControlNet preprocessing. SPICY-003 completed.
