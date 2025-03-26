"""
Image Generator Agent for creating comparison images using DALL-E 2.
"""

import os
import time
import logging
import httpx
from pathlib import Path
from typing import Optional, Tuple
from openai import AsyncOpenAI
from tenacity import retry, stop_after_attempt, wait_exponential

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ImageGeneratorAgent:
    """
    Agent responsible for generating comparison images using DALL-E 2.
    """
    
    def __init__(self, output_dir: str = "media"):
        """
        Initialize the Image Generator Agent.
        
        Args:
            output_dir (str): Directory to store generated images
        """
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
            
        self.client = AsyncOpenAI()
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Image generation settings
        self.image_size = "1024x1024"  # We'll resize to 1600x900 after generation
        self.image_quality = "standard"
        self.image_style = "vivid"
        
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        reraise=True
    )
    async def generate_comparison_image(
        self,
        item1: str,
        item2: str,
        media_id: str,
        creative_prompt: str
    ) -> Tuple[bool, str]:
        """
        Generate a comparison image using DALL-E 2.
        
        Args:
            item1 (str): First item to compare
            item2 (str): Second item to compare
            media_id (str): Unique identifier for the image
            creative_prompt (str): Creative prompt for image generation
            
        Returns:
            Tuple[bool, str]: (success status, file path or error message)
        """
        try:
            logger.info(f"Generating image for comparison: {item1} vs {item2}")
            logger.info(f"Using creative prompt: {creative_prompt}")
            
            # Enhance the creative prompt with some artistic direction
            enhanced_prompt = (
                f"{creative_prompt} "
                "Create this scene with dramatic lighting, rich colors, and professional composition. "
                "Ensure the image has a high-end, editorial quality suitable for a blog header."
            )
            
            # Generate the image
            response = await self.client.images.generate(
                model="dall-e-2",
                prompt=enhanced_prompt,
                size=self.image_size,
                quality=self.image_quality,
                style=self.image_style,
                n=1
            )
            
            # Get the image URL
            image_url = response.data[0].url
            if not image_url:
                raise ValueError("No image URL received from DALL-E 2")
                
            # Download and save the image
            async with httpx.AsyncClient() as client:
                response = await client.get(image_url)
                if response.status_code != 200:
                    raise ValueError(f"Failed to download image: {response.status_code}")
                image_data = response.content
            
            output_path = self.output_dir / f"{media_id}.png"
            with open(output_path, "wb") as f:
                f.write(image_data)
                
            logger.info(f"Successfully generated and saved image: {output_path}")
            return True, str(output_path)
            
        except Exception as e:
            error_msg = f"Error generating image: {str(e)}"
            logger.error(error_msg)
            return False, error_msg
            
    async def cleanup_old_images(self, days: int = 30) -> None:
        """
        Clean up images older than specified days.
        
        Args:
            days (int): Number of days to keep images
        """
        try:
            current_time = time.time()
            for image_path in self.output_dir.glob("*.png"):
                if (current_time - image_path.stat().st_mtime) > (days * 86400):
                    image_path.unlink()
                    logger.info(f"Deleted old image: {image_path}")
        except Exception as e:
            logger.error(f"Error during cleanup: {str(e)}")

# Example usage
if __name__ == "__main__":
    import asyncio
    
    async def test_image_generation():
        agent = ImageGeneratorAgent()
        test_prompt = "A cozy cafe scene with morning light streaming through windows"
        success, result = await agent.generate_comparison_image(
            "Coffee",
            "Tea",
            "coffee-vs-tea",
            test_prompt
        )
        print(f"Success: {success}")
        print(f"Result: {result}")
        
    asyncio.run(test_image_generation()) 