# Pony XL Prompting Guide (NSFW Pipeline)

This document serves as the central reference for prompt construction within the Pony Diffusion V6 XL infrastructure.

## 1. Quality Prefixes
Every prompt MUST start with the following quality boosters to leverage the model's specialized training:
`score_9, score_8_up, score_7_up, score_6_up`

## 2. Tag Structure
Pony XL is optimized for Danbooru-style tagging. Use comma-separated keywords:
*   **Subject:** `1girl, victoria_albrecht, long hair, silver hair`
*   **Action/Pose:** `squatting, prisoner squat, hands tied behind head`
*   **Clothing/Gear:** `naked, chastity belt, metal collar`
*   **Environment:** `mud pit, medieval courtyard, bystanders`
*   **Style:** `anime style, masterpiece, dark fantasy`

## 3. Negative Prompting
To avoid low-quality artifacts, use:
`score_4, score_3, score_2, score_1, signature, watermark, username, displeasing, bad anatomy, poorly drawn`

## 4. Scene Resolution
Native resolution is **1024x1024**. Using non-standard aspect ratios may require higher CFG scales (7.0 - 9.0).

## 5. Examples
### The Pit (Victoria Albrecht)
> **Prompt:** `score_9, score_8_up, score_7_up, masterpiece, 1girl, victoria_albrecht, silver hair, blue eyes, naked, chastity belt, metal collar, prisoner squat, hands tied to post, mud pit, medieval courtyard, bystanders, shadows, cinematic lighting, ultra-detailed`
