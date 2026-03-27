# Hybrid Pipeline — Product Backlog

> **Vision:** A two-phase character generation system — manual creative workbench for curation, fully automated serverless pipeline for production inference and LoRA training.

---

## Phase 0: Foundation & Cross-Cloud Plumbing
*Get the two clouds talking to each other securely.*

| ID | Title | Description | Priority | Status |
|---|---|---|---|---|
| HP-001 | GCP Storage Buckets | Provision `training-data`, `client-loras`, `image-outputs` buckets via Terraform | 🔴 Critical | To Do |
| HP-002 | Cross-Cloud Auth (RunPod → GCP) | Create dedicated `runpod-inference-sa` GCP service account. Provision JSON key, inject into RunPod Secrets as `GCP_SA_KEY_JSON`. Scope: `storage.objectUser` on outputs, `storage.objectViewer` on loras. | 🔴 Critical | To Do |
| HP-003 | RunPod Network Volume | Create shared Network Volume, upload Pony XL base model + ControlNet weights. Document mount path convention (`/workspace/models/`). | 🔴 Critical | To Do |
| HP-004 | Docker Base Images | Build and push lean Docker images to Docker Hub: (a) inference worker (ComfyUI headless), (b) training worker (Kohya sd-scripts). No bundled models. | 🔴 Critical | To Do |
| HP-005 | RunPod API Key in GCP | Store RunPod API key in GCP Secret Manager for Vertex Pipelines to consume. | 🟡 High | To Do |

---

## Phase 1: Creative Workbench (Manual Review)
*Build the GPU-powered creative studio for human-in-the-loop curation.*

| ID | Title | Description | Priority | Status |
|---|---|---|---|---|
| HP-010 | ComfyUI Workbench Pod | Deploy persistent RunPod Pod with ComfyUI GUI, mounted to shared Network Volume. Document access (web proxy URL). | 🔴 Critical | To Do |
| HP-011 | Character Exploration Workflow | Build ComfyUI workflow: text prompt → multi-checkpoint sampling (SDXL, Pony, Flux) → gallery output for manual pick. | 🟡 High | To Do |
| HP-012 | Variation Generation Workflow | Build ComfyUI workflow: reference image → IP-Adapter + ControlNet (OpenPose, Depth) → 30-50 pose/angle/background variations. | 🟡 High | To Do |
| HP-013 | Auto-Filter Node | Integrate aesthetic scorer + CLIP similarity node into ComfyUI. Auto-reject images below quality threshold. | 🟢 Medium | To Do |
| HP-014 | WD14 Tagging Workflow | Build ComfyUI workflow: approved images → WD14 Tagger → `.txt` caption files alongside images. | 🟡 High | To Do |
| HP-015 | Dataset Export to GCS | One-click export of curated dataset folder from Workbench Pod to `gs://training-data/{character_name}/approved/`. | 🟡 High | To Do |

---

## Phase 2: Automated Training Pipeline
*Fire-and-forget LoRA training from an approved dataset.*

| ID | Title | Description | Priority | Status |
|---|---|---|---|---|
| HP-020 | Training Endpoint Handler | Build RunPod Serverless handler: receive payload → download dataset from GCS → WD14 caption → strip identity tags → generate TOML config → run Kohya training → upload `.safetensors` to GCS. | 🔴 Critical | To Do |
| HP-021 | Tag Processor Script | Python script: remove character-defining tags from `.txt` captions, prepend trigger word (e.g., `chr_victoria`). | 🟡 High | To Do |
| HP-022 | TOML Config Template | Parameterized Kohya training config template. Variables: character name, dataset path, network dim/alpha, epochs, learning rate. | 🟡 High | To Do |
| HP-023 | Training Validation Samples | Configure Kohya to generate sample images every epoch. Upload samples alongside the final LoRA for review. | 🟢 Medium | To Do |
| HP-024 | Deploy Training Serverless Endpoint | Deploy Docker image to RunPod Serverless, attach Network Volume, configure scale-to-zero. | 🔴 Critical | To Do |
| HP-025 | Vertex Pipeline: Train Character | kfp pipeline definition: trigger RunPod training endpoint, poll for completion, register LoRA URI in metadata store. | 🟡 High | To Do |

---

## Phase 3: Automated Inference Pipeline
*Prompt-to-image at scale using trained character LoRAs.*

| ID | Title | Description | Priority | Status |
|---|---|---|---|---|
| HP-030 | Inference Endpoint Handler | Build RunPod Serverless handler: receive payload → load base model (Network Vol) → download LoRA from GCS → optionally apply ControlNet → generate image → upload PNG to GCS → return metadata. | 🔴 Critical | To Do |
| HP-031 | ComfyUI Workflow JSON (Frozen) | Export production inference workflow from Workbench as API JSON. Parameterize: prompt, negative_prompt, lora_uri, controlnet_image_uri, output_path. | 🟡 High | To Do |
| HP-032 | Danbooru Prompt Converter Integration | Integrate `danbooru_converter.py` into inference handler. Accept natural language prompt → auto-convert to Pony XL tags. | 🟡 High | To Do |
| HP-033 | Multi-Shot Batch Generation | Accept N prompts per request, generate one image per prompt, upload all to GCS under a batch folder. | 🟢 Medium | To Do |
| HP-034 | Deploy Inference Serverless Endpoint | Deploy Docker image to RunPod Serverless, attach Network Volume, configure scale-to-zero. | 🔴 Critical | To Do |
| HP-035 | Vertex Pipeline: Generate Scenes | kfp pipeline definition: accept scene config (prompts + character + LoRAs + ControlNet params) → fan-out to RunPod inference endpoint → collect results in GCS. | 🟡 High | To Do |

---

## Phase 4: End-to-End Orchestration
*Chain workbench → training → inference into a seamless flow.*

| ID | Title | Description | Priority | Status |
|---|---|---|---|---|
| HP-040 | Vertex Master Pipeline | kfp mega-pipeline: (1) check for approved dataset → (2) trigger training → (3) wait for LoRA → (4) run inference batch → (5) upload results. | 🟡 High | To Do |
| HP-041 | Notification Webhooks | Send Slack/Discord notification when training completes or batch generation finishes. | 🟢 Medium | To Do |
| HP-042 | Cost Dashboard | Simple GCS-hosted report: RunPod spend per job, GCS storage costs, per-character cost breakdown. | 🟢 Medium | To Do |

---

## Phase 5: Quality & Polish
*Hardening, testing, and UX improvements.*

| ID | Title | Description | Priority | Status |
|---|---|---|---|---|
| HP-050 | Auto Quality Gate | After batch inference, run CLIP similarity + aesthetic score. Auto-reject below threshold, flag for manual review. | 🟢 Medium | To Do |
| HP-051 | LoRA A/B Testing | Generate same prompts with different epoch checkpoints. Side-by-side comparison in Workbench. | 🟢 Medium | To Do |
| HP-052 | ControlNet Pose Library | Curate a library of reusable OpenPose/Depth maps for common poses (standing, sitting, action, portrait). Store in GCS. | 🟢 Medium | To Do |
| HP-053 | Style LoRA Stacking | Test and document multi-LoRA inference (character + style + environment LoRAs simultaneously). | 🟢 Medium | To Do |
| HP-054 | CI/CD for Worker Images | GitHub Actions workflow: on push to `hybrid_pipeline/workers/`, rebuild + push Docker images to Docker Hub. | 🟢 Medium | To Do |

---

## Summary

| Phase | Items | Focus |
|---|---|---|
| **Phase 0** | HP-001 – HP-005 | Infrastructure plumbing |
| **Phase 1** | HP-010 – HP-015 | Creative workbench (human-in-loop) |
| **Phase 2** | HP-020 – HP-025 | Automated LoRA training |
| **Phase 3** | HP-030 – HP-035 | Automated inference |
| **Phase 4** | HP-040 – HP-042 | End-to-end orchestration |
| **Phase 5** | HP-050 – HP-054 | Quality hardening |
