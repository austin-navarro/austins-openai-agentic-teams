"""
Orchestrator Agent for coordinating the comparison workflow.
"""

import os
import json
import logging
from pathlib import Path
from typing import Dict, Tuple, Optional
from slugify import slugify
from .image_generator import ImageGeneratorAgent
from .comparison_generator import ComparisonGenerator
from openai import AsyncOpenAI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OrchestratorAgent:
    """
    Agent responsible for orchestrating the comparison workflow.
    """
    
    def __init__(self, base_dir: str = "."):
        """
        Initialize the Orchestrator Agent.
        
        Args:
            base_dir (str): Base directory for all operations
        """
        self.base_dir = Path(base_dir)
        self.media_dir = self.base_dir / "media"
        self.outputs_dir = self.base_dir / "outputs"
        
        # Ensure directories exist
        self.media_dir.mkdir(exist_ok=True)
        self.outputs_dir.mkdir(exist_ok=True)
        
        # Initialize sub-agents
        self.image_generator = ImageGeneratorAgent(str(self.media_dir))
        self.comparison_generator = ComparisonGenerator()
        self.client = AsyncOpenAI()
        
    def generate_media_id(self, item1: str, item2: str) -> str:
        """
        Generate a consistent mediaId from comparison items.
        
        Args:
            item1 (str): First item in comparison
            item2 (str): Second item in comparison
            
        Returns:
            str: Generated mediaId
        """
        # Sort items to ensure consistent ordering
        items = sorted([item1.lower(), item2.lower()])
        return slugify(f"{items[0]}-vs-{items[1]}")

    async def _generate_creative_image_prompt(
        self,
        item1: str,
        item2: str,
        comparison_data: dict
    ) -> str:
        """
        Generate a simple cartoon-style image prompt for the comparison.
        
        Args:
            item1 (str): First item to compare
            item2 (str): Second item to compare
            comparison_data (dict): The generated comparison content
            
        Returns:
            str: Simple image prompt
        """
        # Create the simplest possible prompt with cartoon style
        return f"Generate a cute cartoon image of a {item1} and a {item2}, 1600x900 pixels."
        
    async def generate_comparison(
        self,
        item1: str,
        item2: str
    ) -> Tuple[bool, Dict[str, str]]:
        """
        Generate a complete comparison including image and content.
        
        Args:
            item1 (str): First item to compare
            item2 (str): Second item to compare
            
        Returns:
            Tuple[bool, Dict[str, str]]: (success status, results/error info)
        """
        try:
            # Generate mediaId
            media_id = self.generate_media_id(item1, item2)
            logger.info(f"Starting comparison generation for {media_id}")
            
            # Generate comparison content first
            comparison_success, comparison_result = await self.comparison_generator.generate(
                item1,
                item2,
                media_id
            )
            
            if not comparison_success:
                return False, {
                    "error": f"Comparison generation failed: {comparison_result}",
                    "media_id": media_id
                }
                
            # Load the comparison data to use for creative prompt
            with open(comparison_result) as f:
                comparison_data = json.load(f)
                
            # Generate creative image prompt
            creative_prompt = await self._generate_creative_image_prompt(
                item1,
                item2,
                comparison_data
            )
            logger.info(f"Generated creative prompt: {creative_prompt}")
            
            # Generate image using creative prompt
            image_success, image_result = await self.image_generator.generate_comparison_image(
                item1,
                item2,
                media_id,
                creative_prompt
            )
            
            if not image_success:
                return False, {
                    "error": f"Image generation failed: {image_result}",
                    "media_id": media_id
                }
                
            # Return success result
            return True, {
                "media_id": media_id,
                "image_path": image_result,
                "comparison_path": comparison_result,
                "status": "completed"
            }
            
        except Exception as e:
            error_msg = f"Error in comparison workflow: {str(e)}"
            logger.error(error_msg)
            return False, {"error": error_msg}
            
    async def cleanup(self, days: int = 30) -> None:
        """
        Clean up old files.
        
        Args:
            days (int): Number of days to keep files
        """
        try:
            await self.image_generator.cleanup_old_images(days)
            logger.info("Cleanup completed successfully")
        except Exception as e:
            logger.error(f"Error during cleanup: {str(e)}")

# Example usage
if __name__ == "__main__":
    import asyncio
    
    async def test_workflow():
        orchestrator = OrchestratorAgent()
        success, result = await orchestrator.generate_comparison(
            "Python",
            "JavaScript"
        )
        print(f"Success: {success}")
        print(f"Result: {result}")
        
    asyncio.run(test_workflow()) 