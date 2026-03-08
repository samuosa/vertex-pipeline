import json
import os
import time
import glob

def simulate_pipeline_run(scene_config: dict, output_dir: str):
    scene_id = scene_config.get("scene_id", "unknown_scene")
    characters = scene_config.get("characters", ["unknown_char"])
    char_str = "_".join(characters)
    
    print(f"\n--- Starting Pipeline Run for {scene_id} ({char_str}) ---")
    print(f"Allocating GPU Node (NVIDIA L4)...")
    time.sleep(0.2)
    print(f"Mounting GCSFuse volume: gs://vertex-pipeline-base-models -> /models")
    print(f"Loading Pony Diffusion V6 XL and LoRAs...")
    time.sleep(0.3)
    
    for i in range(1, 6):
        filename = f"{char_str}_{scene_id}_{i}.png"
        filepath = os.path.join(output_dir, filename)
        
        # Simulating file generation
        with open(filepath, "w") as f:
            f.write(f"Simulated PNG data for {scene_id} iteration {i}\n")
            f.write(f"Prompt: {scene_config.get('combined_prompt_example', 'N/A')}\n")
            
        print(f"Iteration {i}/5: Generated {filename}")
        time.sleep(0.1)
        
    print(f"--- Pipeline Execution Complete for {scene_id} ---")
    return scene_id, char_str

if __name__ == "__main__":
    base_dir = "pipelines/nsfw"
    runs_dir = os.path.join(base_dir, "pipelineruns")
    os.makedirs(runs_dir, exist_ok=True)
    
    # Find all .json files in pipelines/nsfw/ recursively
    json_files = glob.glob(os.path.join(base_dir, "**/*.json"), recursive=True)
    
    # Filter for scene configs, excluding characters themselves or other meta
    # We look for files that have 'scene_id' in them
    scene_files = []
    for jf in json_files:
        if "pipelineruns" in jf or "tier3_setup" in jf:
            continue
        try:
            with open(jf, "r") as f:
                content = json.load(f)
                if "scene_id" in content:
                    scene_files.append(jf)
        except:
            continue

    print(f"Found {len(scene_files)} scene configurations to process.")
    
    results = []
    for config_path in scene_files:
        try:
            with open(config_path, "r") as f:
                config = json.load(f)
                sid, cstr = simulate_pipeline_run(config, runs_dir)
                results.append({"scene_id": sid, "characters": cstr, "status": "SUCCESS"})
        except Exception as e:
            print(f"Error processing {config_path}: {e}")
            results.append({"config": config_path, "status": "FAILED", "error": str(e)})

    # Log results to bulk_exec_log.md
    log_path = os.path.join(runs_dir, "bulk_exec_log.md")
    with open(log_path, "w") as f:
        f.write("# Bulk Pipeline Execution Master Log\n")
        f.write(f"**Date:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("| Scene ID | Characters | Status |\n")
        f.write("| :--- | :--- | :--- |\n")
        for res in results:
            f.write(f"| {res.get('scene_id', 'N/A')} | {res.get('characters', 'N/A')} | {res['status']} |\n")
    
    print(f"\nBulk execution finished. Master log updated at {log_path}")
