---
id: SPICY-002
phase: Phase X
title: Develop Text-to-Danbooru Tag Conversion Microservice
assignee: Spicy Engineer
status: To Do
---

# SPICY-002: Develop Text-to-Danbooru Tag Conversion Microservice

## Description
Pony XL models rely heavily on Danbooru-style tagging for optimal generation. Build a central microservice that takes raw user text prompts, parameterizes them, and optimizes the task for Pony LoRAs by converting them into the Danbooru tag format.

## Acceptance Criteria
- [ ] Create the text parsing logic.
- [ ] Implement a tag translation dictionary or leverage an LLM for translation optimized for Danbooru styles.
- [ ] Ensure the prompt output interfaces correctly with the Stable Diffusion text encoders.
- [ ] Expose this as an internal utility or microservice for the main image generation API.

## Updates
*(Workers: Append your updates, roadblocks, or PR links below this line)*
- **[Date] - [Assignee]:** [Update text]
