# Few-Shot Prompt Engineering Examples: Nano Banana

This document provides structured few-shot examples for generating the "Nano Banana" character, optimized for Danbooru-style models (like Pony XL). These examples combine scene instructions, intrinsic character traits, and specific Danbooru tags to ensure high-fidelity consistency.

## Prompt Architecture Template
A highly effective prompt for Nano Banana follows this structure:
`[Quality Tags] + [Character Enforcements] + [Scene Description] + [Action/Pose] + [Lighting/Style]`

---

## Example 1: Neon Cyberpunk Cityscape (Default Look)

**Context:** Nano Banana navigating a futuristic, glowing city environment at night in her signature outfit.

*   **System/Quality Tags:** `score_9, score_8_up, score_7_up, masterpiece, best quality, ultra-detailed, photorealistic.`
*   **Character Enforcements:** `1girl, nano_banana, vibrant yellow hair, short messy hair, green eyes, fair skin, black and yellow tech-wear jacket, yellow inner lining, glowing neon yellow accents, black athletic crop top, dark grey cargo shorts, yellow utility straps, high-top sneakers, yellow digital goggles on forehead, fingerless black gloves.`
*   **Scene Description:** `cyberpunk city, neon lights, rain, wet streets, night, glowing holographic billboard, crowded market.`
*   **Action/Pose:** `running, looking at viewer, dynamic pose, smiling.`
*   **Final Combined Prompt:**
    ```text
    score_9, score_8_up, score_7_up, masterpiece, best quality, ultra-detailed, photorealistic, 1girl, nano_banana, vibrant yellow hair, short messy hair, green eyes, fair skin, black and yellow tech-wear jacket, yellow inner lining, glowing neon yellow accents, black athletic crop top, dark grey cargo shorts, yellow utility straps, high-top sneakers, yellow digital goggles on forehead, fingerless black gloves, cyberpunk city, neon lights, rain, wet streets, night, glowing holographic billboard, crowded market, running, looking at viewer, dynamic pose, smiling.
    ```

---

## Example 2: High-Octane Arcade (Action Focus)

**Context:** Nano Banana intensely playing an arcade game. Tests dynamic interaction with objects while retaining her core facial features.

*   **System/Quality Tags:** `score_9, score_8_up, score_7_up, highres, vibrant colors, nostalgic 90s anime aesthetic.`
*   **Character Enforcements:** `1girl, nano_banana, bright yellow hair, messy bangs, emerald green eyes, petite toned build, signature black and yellow cropped jacket, fingerless gloves.`
*   **Scene Description:** `retro arcade, colorful LED lighting, arcade cabinet, glowing buttons, indoor.`
*   **Action/Pose:** `playing arcade game, mashing buttons, leaning forward, intense focus, dramatic lighting from screen reflecting in eyes.`
*   **Final Combined Prompt:**
    ```text
    score_9, score_8_up, score_7_up, highres, vibrant colors, nostalgic 90s anime aesthetic, 1girl, nano_banana, bright yellow hair, messy bangs, emerald green eyes, petite toned build, signature black and yellow cropped jacket, fingerless gloves, retro arcade, colorful LED lighting, arcade cabinet, glowing buttons, indoor, playing arcade game, mashing buttons, leaning forward, intense focus, dramatic lighting from screen reflecting in eyes.
    ```

---

## Example 3: Tropical Beach Vacation (Outfit Override)

**Context:** Nano Banana out of her usual streetwear, proving the model can decouple her physical traits (hair/face/eyes) from her default clothing.

*   **System/Quality Tags:** `score_9, score_8_up, score_7_up, masterpiece, highly detailed skin texture, cinematic.`
*   **Character Enforcements:** `1girl, nano_banana, yellow hair, short hair, green eyes, athletic build, fair skin.`
*   **Target Outfit:** `sporty yellow and black two-piece swimsuit, yellow digital goggles resting on towel.`
*   **Scene Description:** `tropical beach, white sand, clear blue sky, palm trees, golden hour sunset, bright summer lighting.`
*   **Action/Pose:** `walking on beach, looking away, side profile, relaxed expression, splashing water.`
*   **Final Combined Prompt:**
    ```text
    score_9, score_8_up, score_7_up, masterpiece, highly detailed skin texture, cinematic, 1girl, nano_banana, yellow hair, short hair, green eyes, athletic build, fair skin, sporty yellow and black two-piece swimsuit, yellow digital goggles resting on towel, tropical beach, white sand, clear blue sky, palm trees, golden hour sunset, bright summer lighting, walking on beach, looking away, side profile, relaxed expression, splashing water.
    ```

---

## Example 4: Combat Ready (Extreme Close-Up)

**Context:** Detailed portrait highlighting facial structure and lighting constraints.

*   **System/Quality Tags:** `score_9, score_8_up, score_7_up, hyper-detailed face, 85mm lens, sharp focus.`
*   **Character Enforcements:** `1girl, nano_banana, vibrant yellow hair with subtle neon streak, emerald green eyes, warm undertone, digital goggles down over eyes, tech-wear collar.`
*   **Scene Description:** `dark alleyway, rim lighting, dramatic shadows.`
*   **Action/Pose:** `extreme close-up face, looking at viewer, serious expression, glowing reflection in goggles.`
*   **Final Combined Prompt:**
    ```text
    score_9, score_8_up, score_7_up, hyper-detailed face, 85mm lens, sharp focus, 1girl, nano_banana, vibrant yellow hair with subtle neon streak, emerald green eyes, warm undertone, digital goggles down over eyes, tech-wear collar, dark alleyway, rim lighting, dramatic shadows, extreme close-up face, looking at viewer, serious expression, glowing reflection in goggles.
    ```
