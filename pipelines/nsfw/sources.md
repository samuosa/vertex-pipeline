# NSFW Pipeline Central Source Registry

> **Purpose:** This document tracks all external assets, models, ControlNets, and LoRAs imported into our internal pipeline from public hubs like CivitAI or HuggingFace.

## Character Base & Styles
| Model Name | Version | Source (URL) | Trigger Words / Tags | Description |
| :--- | :--- | :--- | :--- | :--- |
| Pony Diffusion V6 XL | V6 | [CivitAI/HF] | `score_9, score_8_up, score_7_up` | The base foundational model for the entire pipeline. |

## Fetish & Pose LoRAs
| LoRA Name | Version | Source (URL) | Trigger Words / Tags | Description |
| :--- | :--- | :--- | :--- | :--- |
| PonyXL Shibari Poses | v1.0 | CivitAI (mock123) | `shibari, bound, suspension` | Provides consistent Japanese rope bondage poses optimized for Pony XL. |
| BDSM Gear Pony XL | v2.1 | HuggingFace (mockuser/bdsm-gear) | `leather harness, collar, blindfold` | Injects high-fidelity BDSM equipment onto standard character generations. |
| Female Chastity Belt Pony XL | v1.0 | CivitAI | `chastity belt, chastity` | Focus on rigid metal chastity belts designed for female anime anatomy on Pony XL. |
| Prisoner Squat Pose LoRA | v1.0 | CivitAI | `squatting, prisoner squat, tied post` | Guides the pose to a kneeling/squatting position attached to a post. |
| Heavy Metal Restraints & Chains | v1.0 | HuggingFace | `metal collar, heavy chains, chained to wall` | Specific LoRA for enhancing the realism of dark fantasy chains and collars. |

## ControlNet Models
| Model Name | Version | Source (URL) | Usage | Description |
| :--- | :--- | :--- | :--- | :--- |
| SDXL OpenPose | v1.0 | [HuggingFace] | N/A | Used for extracting and replicating poses from user character references. |
