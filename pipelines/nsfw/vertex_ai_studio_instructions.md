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

### 3. Injecting Character Enforcements
Vertex AI Studio UI handles system instructions by blending them into the master prompt or negative prompt areas.
1. Open the `system_instructions.md` file from `pipelines/nsfw/characters/nano_banana/`.
2. Copy the **Master Tag List (High-Efficiency Consistency)**.
3. In the UI's main **Prompt** text box, you will prepend this tag block to all your specific scene prompts.
4. In the **Negative prompt** box, always include: `(low quality, worst quality, distorted face, bad anatomy, text, watermark, bad hands, extra limbs, blur, monochrome)`.

### 4. Subject Reference Image Setup (Image-to-Image)
If you do not have high-quality reference images yet, use the following prompts to generate them first:

**For Face Reference:**
`score_9, score_8_up, masterpiece, 1girl, nano_banana, vibrant yellow hair, short messy hair, green eyes, emerald eyes, fair skin, close-up portrait, neutral expression, white background, soft studio lighting, ultra-detailed skin.`

**For Full Body Reference:**
`score_9, score_8_up, masterpiece, 1girl, nano_banana, vibrant yellow hair, short hair, green eyes, signature black and yellow tech-wear jacket, dark grey shorts, high-top sneakers, standing, T-pose or neutral standing pose, white background, full body, highres.`

Once you have these images:
1. Look for the **Reference Image** upload section in the Vertex AI UI.
2. Upload the **Face Reference** for portrait shots or the **Full Body Reference** for wider shots.
3. If available, set the "Reference Type" to **Subject**.

### 5. Executing the 5-Shot Sequence
We use the shots defined in `few_shot_examples.md`.
1. Open `few_shot_examples.md`.
2. Select a scene (e.g., **Scene 1: Neon Cyberpunk Cityscape**).
3. Copy the prompt for **Shot 1**.
4. Combine it with your **Character Enforcement tags** and click **Generate**.
5. Iterate through all 5 shots to build a consistent project gallery.

---
**Advanced Tip:** If the character's clothing dominates the face too much, use a **Face Reference** image and lower the "Region Strength" if your model allows regional prompting, or simply rely on the text "emerald green eyes" to override any model drift.

