import os
from google.cloud import aiplatform

print("Initializing Vertex AI SDK...")
project_id = "vertex-ai-489604"
location = "us-central1"
aiplatform.init(project=project_id, location=location)

pipeline_root = f"gs://{project_id}-pipeline-root/pipeline_root"
template_path = "pony_xl_lora_pipeline.yaml"

if not os.path.exists(template_path):
    print(f"Error: {template_path} not found. Please compile the pipeline first.")
    exit(1)

print(f"Submitting pipeline {template_path} to {project_id}...")
job = aiplatform.PipelineJob(
    display_name="pony-xl-lora-training-test",
    template_path=template_path,
    pipeline_root=pipeline_root,
)

job.submit(service_account="pipeline-runner@vertex-ai-489604.iam.gserviceaccount.com")
print("Pipeline submitted successfully! Please check the Vertex AI UI for the execution.")
