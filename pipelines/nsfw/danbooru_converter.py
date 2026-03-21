import re

class DanbooruConverter:
    """
    A utility for optimizing standard text prompts into Danbooru-style tags
    specifically for Pony XL models.
    """
    
    def __init__(self):
        # Basic example mappings; a real implementation might load these from a larger JSON or DB
        self.tag_dictionary = {
            "photorealistic": "realistic, highres, absurdres",
            "beautiful": "masterpiece, best quality",
            "woman": "1girl",
            "man": "1boy",
            "dog": "animal, dog",
            "cat": "animal, cat"
        }
        
        # PonyXL specific quality tags
        self.pony_quality_prefix = "score_9, score_8_up, score_7_up, score_6_up"
        
    def _clean_text(self, text: str) -> str:
        """Removes punctuation and normalizes spaces."""
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return " ".join(text.split())

    def convert(self, raw_prompt: str, include_pony_quality: bool = True) -> str:
        """
        Parses raw text and attempts to map known words to Danbooru tags.
        """
        cleaned = self._clean_text(raw_prompt)
        words = cleaned.split()
        
        converted_tags = []
        for word in words:
            if word in self.tag_dictionary:
                converted_tags.append(self.tag_dictionary[word])
            else:
                converted_tags.append(word)
                
        # Join mapped tags and deduplicate
        unique_tags = []
        for tag in ", ".join(converted_tags).split(","):
            tag = tag.strip()
            if tag and tag not in unique_tags:
                unique_tags.append(tag)
                
        final_prompt = ", ".join(unique_tags)
        
        if include_pony_quality:
            final_prompt = f"{self.pony_quality_prefix}, {final_prompt}"
            
        return final_prompt

# Microservice usage example (e.g., if plugged into FastAPI or Flask)
if __name__ == "__main__":
    converter = DanbooruConverter()
    print(converter.convert("A beautiful woman photorealistic"))
