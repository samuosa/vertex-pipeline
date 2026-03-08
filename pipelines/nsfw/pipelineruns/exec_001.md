# Pipeline Execution Log: EXEC_001

**Date:** 2026-03-08
**Operator:** Spicy Engineer
**Task:** Full Pony XL Inference Test
**GPU Node:** NVIDIA L4 (Cloud Run gen2)

## 1. Environment Setup
*   **Target service:** `pony-xl-inference-service`
*   **Base Model:** Pony Diffusion V6 XL
*   **Storage Mount:** GCSFuse mounted `gs://vertex-pipeline-base-models` at `/models`
*   **Artifact Directory:** `pipelines/nsfw/pipelineruns/`

## 2. Prompt & LoRA Configuration
*   **Base Prompt:** `score_9, score_8_up, score_7_up, masterpiece, 1girl, victoria_albrecht, long silver hair, blue eyes, naked, chastity belt, metal collar, prisoner squat, squatting, hands tied behind head, tied to post, metal braces, mud pit, medieval courtyard, bystanders, dark fantasy, cinematic lighting, highly detailed`
*   **Negative Prompt:** `score_4, score_3, score_2, score_1, signature, watermark, username, displeasing, bad anatomy, poorly drawn`
*   **Active LoRAs:**
    *   `VictoriaAlbrecht_v1` (1.0)
    *   `Prisoner Squat Pose LoRA` (0.9)
    *   `Female Chastity Belt Pony XL` (1.0)
    *   `Heavy Metal Restraints & Chains` (0.8)

## 3. Execution Trace
1.  **[07:01:10]** Request sent to `/sdapi/v1/txt2img`.
2.  **[07:01:15]** GPU Instance allocated.
3.  **[07:01:20]** Model weights validated in `/models`.
4.  **[07:01:25]** Inference started (Euler a, 25 steps, CFG 7).
5.  **[07:02:10]** Rendering iteration 1 complete.
6.  **[07:03:00]** Final batch of 5 PNGs generated and verified.

## 4. Output Summary
| Filename | Resolution | Scene | Character |
| :--- | :--- | :--- | :--- |
| `victoria_albrecht_the_pit_1.png` | 1024x1024 | The Pit | Victoria Albrecht |
| `victoria_albrecht_the_pit_2.png` | 1024x1024 | The Pit | Victoria Albrecht |
| `victoria_albrecht_the_pit_3.png` | 1024x1024 | The Pit | Victoria Albrecht |
| `victoria_albrecht_the_pit_4.png` | 1024x1024 | The Pit | Victoria Albrecht |
| `victoria_albrecht_the_pit_5.png` | 1024x1024 | The Pit | Victoria Albrecht |

## 5. Verification
Status: **SUCCESSFUL**
All images successfully copied to `pipelines/nsfw/pipelineruns/`. Physical verification of `.png` headers complete.
