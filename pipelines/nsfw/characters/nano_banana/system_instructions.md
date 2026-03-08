# System Instructions: Nano Banana

These system instructions are designed to enforce a consistent character appearance for "Nano Banana" across any image generation or image-to-image pipeline using Vertex AI (e.g., Imagen 3).

## Character Master Description

**Name/Trigger:** Nano Banana
**Core Identity:** A vibrant, highly energetic character with a distinct yellow-and-black cyber-streetwear aesthetic.

**Physical Traits:**
- **Face/Head:** Youthful, expressive face. Bright emerald green eyes. 
- **Hair:** Short, vibrant yellow hair with slightly messy bangs and a subtle neon-yellow streak. Sometimes styled with small symmetrical hair-clips.
- **Body Type:** Athletic, petite but toned build.
- **Skin Tone:** Fair complexion with a warm undertone.

**Signature Attire (Default Outfit):**
- **Top:** A cropped, high-tech black jacket with bright yellow inner lining and neon yellow glowing accents seamlessly integrated into the fabric. Underneath, a sleek, form-fitting athletic crop top.
- **Bottom:** Tactical dark grey or black cargo shorts or tech-wear skirt with yellow utility straps.
- **Footwear:** Chunky futuristic high-top sneakers with yellow soles and glowing laces.
- **Accessories:** A pair of yellow-tinted digital goggles resting either on her forehead or around her neck. Fingerless black gloves.

## Enforcement Guidelines for the Model
*When generating images of 'Nano Banana', strictly adhere to the physical traits and signature attire unless a specific scene prompt overrides the clothing. The yellow hair, green eyes, and facial structure must remain absolutely consistent across all angles, lighting conditions, and expressions.*

## Instructions for Use in Vertex AI
1. Copy the "Character Master Description" above.
2. Paste this text into the **System Instructions** or **Negative/Positive Prompt Base** in your Vertex AI Studio visual interface (under the text-to-image or image-to-image advanced settings depending on model version).
3. Ensure these traits are continuously appended/prepended to your few-shot prompts.
