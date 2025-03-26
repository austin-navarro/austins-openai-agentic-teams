"""
Comparison Generator for creating structured comparison content.
"""

import json
import logging
from typing import List, Optional
from pathlib import Path
from pydantic import BaseModel
from openai import AsyncOpenAI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the output structure model
class ComparisonSection(BaseModel):
    heading: str
    content: str

class ComparisonPage(BaseModel):
    title: str
    slug: str
    intro: str
    comparisonImage: str  # Media ID
    sections: List[ComparisonSection]
    conclusion: str
    published: bool = True

class ComparisonGenerator:
    """
    Generator for creating structured comparisons between two topics.
    """
    
    def __init__(self, output_dir: str = "outputs"):
        """
        Initialize the Comparison Generator.
        
        Args:
            output_dir (str): Directory to store generated comparisons
        """
        self.client = AsyncOpenAI()
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
    def _create_prompt(self, item1: str, item2: str, media_id: str) -> str:
        """
        Create a detailed prompt for the comparison.
        
        Args:
            item1 (str): First item to compare
            item2 (str): Second item to compare
            media_id (str): Media ID for the comparison image
            
        Returns:
            str: Generated prompt
        """
        return f"""Create a detailed comparison between {item1} and {item2}.

Your task is to:
1. Research factual information about both topics
2. Create high-quality comparison content with multiple sections
3. Format the output exactly according to the specified schema

The comparison must include:
- Title in "{item1} vs {item2}" format
- Slug: "{media_id}"
- Engaging introduction (80-120 words)
- 4-6 comparison sections
- Balanced conclusion (60-100 words)

Use HTML formatting for rich text (p, ul, li tags).
Each section should be 120-200 words.
Focus on key differences and similarities.

Return the content in this exact JSON structure:
{{
    "title": "string",
    "slug": "{media_id}",
    "intro": "string with <p> tags",
    "comparisonImage": "{media_id}",
    "sections": [
        {{"heading": "string", "content": "string with HTML"}}
    ],
    "conclusion": "string with <p> tags",
    "published": true
}}"""

    async def generate(
        self,
        item1: str,
        item2: str,
        media_id: str
    ) -> tuple[bool, str]:
        """
        Generate a comparison between two items.
        
        Args:
            item1 (str): First item to compare
            item2 (str): Second item to compare
            media_id (str): Media ID for the comparison
            
        Returns:
            tuple[bool, str]: (success status, file path or error message)
        """
        try:
            # Generate the comparison
            prompt = self._create_prompt(item1, item2, media_id)
            
            response = await self.client.chat.completions.create(
                model="gpt-4o-mini-2024-07-18",
                messages=[
                    {"role": "system", "content": "You are a comparison content expert."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            # Parse the response
            content = response.choices[0].message.content
            comparison_data = json.loads(content)
            
            # Validate with Pydantic
            comparison = ComparisonPage(**comparison_data)
            
            # Save to file
            output_path = self.output_dir / f"{media_id}.json"
            with open(output_path, "w") as f:
                json.dump(comparison.model_dump(), f, indent=2)
                
            logger.info(f"Generated comparison saved to {output_path}")
            return True, str(output_path)
            
        except Exception as e:
            error_msg = f"Error generating comparison: {str(e)}"
            logger.error(error_msg)
            return False, error_msg

# Example usage
if __name__ == "__main__":
    import asyncio
    
    async def test_comparison():
        generator = ComparisonGenerator()
        success, result = await generator.generate(
            "Python",
            "JavaScript",
            "python-vs-javascript"
        )
        print(f"Success: {success}")
        print(f"Result: {result}")
        
    asyncio.run(test_comparison()) 