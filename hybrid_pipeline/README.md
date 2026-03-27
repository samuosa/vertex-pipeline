# Hybrid Pipeline

**Character-consistent image generation using a two-phase GPU pipeline.**

Phase 1 (Workbench) provides a GPU-powered ComfyUI creative studio for manual curation.  
Phase 2 (Production) provides headless, scale-to-zero serverless endpoints for automated LoRA training and batch inference.

## Quick Links

| Document | Description |
|---|---|
| [TECHSTACK.md](./TECHSTACK.md) | Full technology stack across all layers |
| [BACKLOG.md](./BACKLOG.md) | Product backlog (HP-001 → HP-054) |

## Project Structure (Planned)

```
hybrid_pipeline/
├── README.md
├── TECHSTACK.md
├── BACKLOG.md
├── workers/
│   ├── inference/          # ComfyUI headless Docker image
│   │   ├── Dockerfile
│   │   ├── handler.py      # RunPod serverless handler
│   │   └── workflows/      # Frozen ComfyUI workflow JSONs
│   └── training/           # Kohya sd-scripts Docker image
│       ├── Dockerfile
│       ├── handler.py      # RunPod serverless handler
│       ├── tag_processor.py
│       └── configs/        # TOML training templates
├── pipelines/              # Vertex AI Pipeline definitions (kfp v2)
│   ├── train_character.py
│   ├── generate_scenes.py
│   └── master_pipeline.py
└── workbench/              # ComfyUI workflow exports + setup scripts
    ├── setup_pod.sh
    └── workflows/
```
