# Vertex AI Studio UI Instructions: Nano Banana Few-Shot Project

This guide provides step-by-step instructions on how to use the graphical Vertex AI Studio interface to execute a few-shot prompting pipeline for the "Nano Banana" character, ensuring consistent high-fidelity results.

## Overview
We will be utilizing the **Vertex AI Studio -> Vision** section to leverage text-to-image or image-to-image models (like Imagen) to generate consistent character concepts using system instructions and reference images.

### Prerequisites Check
Before starting, ensure you have populated the reference folders located at:
- `pipelines/nsfw/references/nano_banana/face/` (Load with 3-5 high-quality, clear portraits of Nano Banana's face).
- `pipelines/nsfw/references/nano_banana/full_body/` (Load with 3-5 full body shots of the character in signature clothing).

---

## Step-by-Step UI Execution

### 1. Navigate to Vertex AI Vision
1. Open the [Google Cloud Console](https://console.cloud.google.com/).
2. Select your active GCP project (e.g., `vertex-ai-489604`).
3. In the search bar or left-hand hamburger menu, navigate to **Vertex AI** -> **Vertex AI Studio** -> **Vision**.

### 2. Set Up the Model and Generation Parameters
1. Select **Generate Images** (Text-to-Image).
2. On the right-hand parameter pane, ensure you have selected the latest stable **Imagen model** (e.g., `imagen-3.0-generate` or `imagen-3.0-fast-generate`).
3. Set the **Aspect Ratio** according to your scene needs (e.g., `1:1` for portraits, `16:9` for wide shots).
4. Set the **Output format** (e.g., PNG for highest fidelity).
5. Enable the **Advanced Options** toggle at the bottom of the parameter pane to reveal negative prompts and seed controls.

### 3. Injecting System Instructions
Vertex AI Studio UI handles system instructions by blending them into the master prompt or negative prompt areas.
1. Open the `system_instructions.md` file from `pipelines/nsfw/characters/nano_banana/`.
2. Copy the **Character Master Description**.
3. In the UI's main **Prompt** text box, you will prepend this master description to all your specific scene prompts.
4. *Recommendation:* In the **Negative prompt** box, add standard safety constraints or visual fail-safes (e.g., `distorted face, mutated, bad anatomy, text, watermark, bad hands, extra limbs`).

### 4. Subject Reference Image Setup (Image-to-Image / Few-Shot Image Prompting)
To force absolute consistency, you should use the Imagen **Subject Reference** or **Style Reference** feature if available in your Vertex AI UI, or use the base image feature.
1. Look for the **Reference Image** or **Provide an image** upload section below the main prompt box.
2. Click **Upload** and navigate to your local `pipelines/nsfw/references/nano_banana/face/` folder.
3. Select an optimized reference image.
4. If there is a "Reference Type" dropdown, select **Subject** (so the model focuses on the character, not just the art style). 

### 5. Executing the 5-Shot Sequence
We use the shots defined in `few_shot_examples.md`.
1. Open `few_shot_examples.md`.
2. Navigate to **Scene 1: Neon Cyberpunk Cityscape**.
3. Copy **Shot 1** text.
4. Paste it into the Vertex AI Studio **Prompt** box, directly *after* your pasted System Instructions from Step 3. (Alternatively, if using an Agent/Chat interface for generation, pass the System Instruction once, then pass the Shots iteratively).
5. Click **Generate**.
6. Review the outputs. Adjust the `Seed` in Advanced settings if you want to lock onto a specific structural composition you like, then advance to **Shot 2**.
7. Keep the reference image uploaded throughout all 5 shots in a scene to maintain the character's face.

### 6. Changing Scenes
When transitioning from Scene 1 to Scene 3 (Tropical Beach):
1. Clear the previous prompt (but keep the Character Master Description).
2. (Optional but recommended): If the scene fundamentally changes the character's clothing (e.g., swimwear instead of streetwear), you may need to update your **Subject Reference Image**. Upload a new reference from `pipelines/nsfw/references/nano_banana/full_body/` that better reflects the new scene, or rely heavily on the text prompt to override the clothing while keeping the face reference.
3. Proceed with generating the 5 shots for the new scene.

---
**Troubleshooting Tip:** If the character's appearance diverges during the 5-shot batch, increase the *Reference Image Weight* (if the slider is available in your UI version) or add stronger descriptive keywords (e.g., `vibrant yellow hair`, `bright green eyes`) redundantly into the individual shot prompts.
