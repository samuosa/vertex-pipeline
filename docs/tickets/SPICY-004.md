---
id: SPICY-004
phase: Phase X
title: Import External BDSM/Fetish and Character LoRAs
assignee: Spicy Engineer
status: To Do
---

# SPICY-004: Import External BDSM/Fetish and Character LoRAs

## Description
Source, download, and catalog high-quality community models for specific stylistic generations. We need to acquire BDSM/fetish poses and character LoRAs from public hubs like CivitAI or HuggingFace.

## Acceptance Criteria
- [ ] Identify top-performing SDXL/Pony XL LoRAs for the required niches.
- [ ] Write a script or standard operating procedure to safely download the `.safetensors` files to our GCS bucket.
- [ ] Register every imported LoRA in `/pipelines/nsfw/sources.md` with:
    - Name and Version
    - Source URL (HF/CivitAI)
    - Trigger words / required Danbooru tags
    - Brief description of the utility (e.g., "specific binding pose", "character X").

## Updates
*(Workers: Append your updates, roadblocks, or PR links below this line)*
- **[Date] - [Assignee]:** [Update text]
