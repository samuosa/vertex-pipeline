# Hybrid Pipeline — Tech Stack

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                     GCP (Orchestration & Storage)                    │
│                                                                     │
│  Vertex AI Pipelines ──┬── GCS: training-data                      │
│  (kfp v2 / Python)     ├── GCS: client-loras                       │
│                         └── GCS: image-outputs                      │
└───────────┬──────────────────────────────────────┬──────────────────┘
            │ HTTP POST (RunPod API)               │
┌───────────▼──────────────────────────────────────▼──────────────────┐
│                     RunPod (GPU Compute)                             │
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌────────────────────┐  │
│  │ Workbench (Pod)  │  │ Inference Srvls │  │ Training Srvls     │  │
│  │ ComfyUI GUI      │  │ ComfyUI Headless│  │ Kohya sd-scripts   │  │
│  │ (Manual Review)  │  │ (REST API)      │  │ (Headless CLI)     │  │
│  └────────┬─────────┘  └────────┬────────┘  └────────┬───────────┘  │
│           └──────────┬──────────┴─────────────────────┘             │
│                      ▼                                               │
│           RunPod Network Volume                                      │
│           (Base Models, ControlNets)                                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Layer-by-Layer Stack

### 1. Orchestration Layer (GCP)

| Component | Technology | Purpose |
|---|---|---|
| Pipeline engine | **Vertex AI Pipelines** (kfp v2) | DAG-based orchestration of training + inference jobs |
| Pipeline SDK | **Python 3.11** + `kfp==2.x` | Define, compile, submit pipelines |
| Object storage | **Google Cloud Storage** | Training data, LoRA artifacts, generated images |
| Auth (GCP → RunPod) | **RunPod API Key** (stored in GCP Secret Manager) | Authenticate HTTP calls to RunPod endpoints |
| Auth (RunPod → GCP) | **GCP SA JSON Key** (injected via RunPod Secrets) | Allow RunPod workers to read/write GCS buckets |

### 2. Creative Workbench (RunPod Pod — Persistent)

| Component | Technology | Purpose |
|---|---|---|
| UI | **ComfyUI** (latest) | Node-based visual workflow for manual review |
| GPU | **RTX 4090 / A5000** (RunPod Pod) | Interactive generation + LoRA test inference |
| Model storage | **RunPod Network Volume** (mounted at `/workspace/models`) | Shared base models, ControlNet weights |
| Access | **RunPod Web Terminal + HTTP proxy** | Remote browser access to ComfyUI GUI |

### 3. Inference Engine (RunPod Serverless — Scale-to-Zero)

| Component | Technology | Purpose |
|---|---|---|
| Runtime | **ComfyUI** (headless, API mode) | Execute frozen workflow JSONs |
| Container | **Docker** → Docker Hub (lean image, code only) | Fast pulls, no bundled models |
| Model storage | **RunPod Network Volume** (shared) | Base models + ControlNets mount instantly |
| API | RunPod Serverless `/runsync` endpoint | Synchronous inference, returns on completion |
| ControlNet | **ControlNet SDXL** (OpenPose, Canny, Depth) | Pose/composition conditioning |
| LoRA loading | Dynamic download from GCS at inference time | Character + style LoRAs |

### 4. Training Engine (RunPod Serverless — Scale-to-Zero)

| Component | Technology | Purpose |
|---|---|---|
| Training framework | **Kohya sd-scripts** (`sdxl_train_network.py`) | SDXL/Pony LoRA training via CLI |
| Config | **TOML** templates with variable substitution | Reproducible, parameterized training runs |
| Auto-captioning | **WD14 Tagger** (Kohya built-in CLI) | Danbooru-style tags from images |
| Tag processing | Custom Python script (`tag_processor.py`) | Strip identity tags, prepend trigger word |
| Container | **Docker** → Docker Hub | Kohya + deps, no bundled models |
| Model storage | **RunPod Network Volume** (shared) | Base checkpoint for training |

### 5. Prompt Engineering

| Component | Technology | Purpose |
|---|---|---|
| Prompt → Danbooru | `danbooru_converter.py` (existing) | Natural language to Pony XL tag format |
| Prompt expansion | **LLM** (Gemini API or local) | Enrich short prompts into detailed scene descriptions |

### 6. Quality Assurance

| Component | Technology | Purpose |
|---|---|---|
| Aesthetic scoring | **LAION Aesthetic Predictor** | Auto-filter low-quality generations |
| Similarity check | **CLIP cosine similarity** | Verify character consistency against reference |
| Overfitting detection | Sample images at each training epoch | Visual + CLIP-score regression check |

### 7. CI/CD & Infrastructure

| Component | Technology | Purpose |
|---|---|---|
| IaC | **Terraform** | GCS buckets, IAM, Vertex AI config |
| CI/CD | **GitHub Actions** + WIF | Automated Terraform deploy + Docker build/push |
| Container registry | **Docker Hub** (free private) | Store lean compute images |
| Secrets | **GCP Secret Manager** + **RunPod Secrets** | Cross-cloud credential management |

---

## Key Dependencies

```
# Python (Orchestration)
kfp>=2.0
google-cloud-storage
google-cloud-aiplatform
runpod  # RunPod Python SDK for endpoint invocation

# Python (RunPod Inference Worker)
comfyui  # or raw torch + diffusers
runpod   # Serverless handler wrapper
google-cloud-storage

# Python (RunPod Training Worker)
kohya-ss/sd-scripts  # LoRA training
accelerate
torch>=2.0
safetensors
google-cloud-storage
```
