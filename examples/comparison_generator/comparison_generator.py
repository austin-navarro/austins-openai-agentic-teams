from agents import Agent, Runner
from pydantic import BaseModel
import asyncio
import json
import re

# Define the output structure model
class ComparisonSection(BaseModel):
    heading: str
    content: str

class ComparisonPage(BaseModel):
    title: str
    slug: str
    intro: str
    comparisonImage: str  # Media ID
    sections: list[ComparisonSection]
    conclusion: str
    published: bool

# Create a single agent that handles the entire process
comparison_agent = Agent(
    name="Comparison Content Generator",
    instructions="""
    You are a comparison content expert. Your task is to:
    
    1. Research factual information about two topics being compared
    2. Create high-quality comparison content with multiple sections
    3. Format the output exactly according to the specified schema
    
    Your content should be informative, factually accurate, and well-structured.
    Include HTML formatting for rich text fields (use <p>, <ul>, <li>, etc.).
    
    Each comparison must include:
    - A title in "[Topic1] vs [Topic2]" format
    - A slug in "topic1-vs-topic2" format
    - An engaging introduction explaining why these topics are worth comparing. 80–120 words (approx. 1–2 paragraphs)
    - 3-6 comparison sections, each with a heading and detailed content. Recommended length: 120–200 word for each section.
    - A balanced conclusion summarizing key differences and similarities. Length: 60–100 words. 
    
    The sections should cover the most important dimensions for comparison.
    """,
    output_type=ComparisonPage,
    model="gpt-4o-mini"
)

async def generate_comparison(topic1, topic2, media_id=None):
    """
    Generate a structured comparison between two topics.
    
    Args:
        topic1 (str): First topic to compare
        topic2 (str): Second topic to compare
        media_id (str, optional): Media ID for the comparison image
        
    Returns:
        ComparisonPage: The generated comparison page data
    """
    # Create the prompt
    prompt = f"""
    Create a detailed comparison between {topic1} and {topic2}.
    
    Return a structured comparison that follows the ComparisonPage schema exactly.
    Make sure to include at least 4 detailed sections covering key differences and similarities.
    Use proper HTML formatting in the content fields.
    """
    
    # Add media ID context if provided
    context = {}
    if media_id:
        context["media_id"] = media_id
        prompt += f"\n\nUse the provided media_id: {media_id} for the comparisonImage field."
    
    # Run the agent to generate the comparison
    result = await Runner.run(comparison_agent, prompt, context=context)
    
    # Get the structured output
    comparison_data = result.final_output_as(ComparisonPage)
    
    # If no slug was generated, create one
    if not comparison_data.slug:
        # Create a slug from the title
        slug = f"{topic1.lower().replace(' ', '-')}-vs-{topic2.lower().replace(' ', '-')}"
        comparison_data.slug = slug
    
    # If media_id was provided but not set in the output
    if media_id and not comparison_data.comparisonImage:
        comparison_data.comparisonImage = media_id
        
    return comparison_data

async def output_comparison_json(comparison_page, file_path=None):
    """
    Output the comparison page as JSON, ready for CMS import
    
    Args:
        comparison_page (ComparisonPage): The generated comparison
        file_path (str, optional): Path to save the JSON output
        
    Returns:
        str: The JSON string representation
    """
    # Convert to JSON
    json_data = comparison_page.model_dump()
    formatted_json = json.dumps(json_data, indent=2)
    
    # Save to file if path provided
    if file_path:
        with open(file_path, "w") as f:
            f.write(formatted_json)
        print(f"Comparison JSON saved to {file_path}")
    
    return formatted_json

# Simple function to generate and output a comparison
async def create_comparison_content(topic1, topic2, media_id=None, output_file=None):
    """
    Generate and output a comparison between two topics
    
    Args:
        topic1 (str): First topic
        topic2 (str): Second topic
        media_id (str, optional): Media ID for the image
        output_file (str, optional): File to save the JSON output
        
    Returns:
        ComparisonPage: The generated comparison
    """
    print(f"Generating comparison between {topic1} and {topic2}...")
    
    # Generate the comparison
    comparison = await generate_comparison(topic1, topic2, media_id)
    
    # Output as JSON
    json_output = await output_comparison_json(comparison, output_file)
    
    print(f"Generated '{comparison.title}' with {len(comparison.sections)} sections")
    print(f"JSON output sample (first 100 chars):\n{json_output[:100]}...")
    
    return comparison 