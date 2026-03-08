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

## Master Tag List (High-Efficiency Consistency)
Copy and paste this tag block into your Vertex AI prompt as the **Character Enforcement** base:

`1girl, nano_banana, vibrant yellow hair, short messy hair, green eyes, emerald green eyes, yellow bangs, neon streak, fair skin, warm skin tone, petite toned athletic build, signature black and yellow tech-wear jacket, yellow jacket inner lining, neon yellow glowing accents, black crop top, dark grey cargo shorts, yellow utility straps, high-top sneakers, yellow digital goggles on forehead, fingerless black gloves.`

## Enforcement Guidelines for the Model
*When generating images of 'Nano Banana', strictly adhere to the physical traits and signature attire unless a specific scene prompt overrides the clothing. The yellow hair, green eyes, and facial structure must remain absolutely consistent across all angles, lighting conditions, and expressions.*

## Instructions for Use in Vertex AI Studio
1. **System Prompt / Positive Base:** Use the **Master Tag List** above as the first part of your prompt.
2. **Few-Shot Anchor:** For each new project, use one "Wide Shot" from the `few_shot_examples.md` as an anchor to ground the character's proportions and primary colors.
3. **Negative Prompting:** In the **Negative prompt** box in Vertex AI Studio, always use: `(distorted, bad anatomy, flat color, monochrome, text, watermark, bad hands, extra limbs, dull eyes)`.
4. **Consistency Lock:** Use the same `Seed` for the first 3 shots of a scene if you want to lock the environmental lighting, then vary the seed for the action/pose shots.

