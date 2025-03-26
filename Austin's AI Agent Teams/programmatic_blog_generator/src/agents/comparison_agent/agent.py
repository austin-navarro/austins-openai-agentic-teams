"""
Comparison Blog Post Generation Agent implementation.
"""
import os
from typing import Dict, Optional
import json
from pathlib import Path
import logging
from openai import OpenAI
from dotenv import load_dotenv

from .schema import ComparisonBlogPost

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ComparisonAgent:
    def __init__(self):
        """Initialize the comparison agent with OpenAI client."""
        # Try to load from local .env first
        load_dotenv()
        
        # If API key not found, try loading from root project directory
        if not os.getenv("OPENAI_API_KEY"):
            root_env = Path(__file__).parent.parent.parent.parent.parent / ".env"
            if root_env.exists():
                load_dotenv(root_env)
        
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OpenAI API key not found in environment variables")
            
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.output_dir = Path(__file__).parent.parent.parent.parent / "blog_output"
        self.output_dir.mkdir(exist_ok=True)
        
    def _get_prompt(self, term_a: str, term_b: str) -> str:
        """Generate the prompt for the comparison blog post."""
        schema_json = json.dumps({
            "title": "string",
            "slug": "string",
            "published_date": "YYYY-MM-DD",
            "read_time": "string (e.g. '8 min read')",
            "author": {
                "name": "Moso Panda",
                "role": "Web3 Specialist"
            },
            "media": {
                "term_a": "string",
                "term_b": "string"
            },
            "introduction": "string",
            "jump_link_text": "string",
            "background": {
                "heading": "string",
                "content": "string"
            },
            "key_differences": {
                "heading": "string",
                "items": [
                    {
                        "feature_title": "string",
                        "a_description": "string",
                        "b_description": "string"
                    }
                ]
            },
            "comparison_table": {
                "heading": "string",
                "features": [
                    {
                        "label": "string",
                        "a_value": "string",
                        "b_value": "string"
                    }
                ],
                "ideal_for": {
                    "a": "string",
                    "b": "string"
                }
            },
            "conclusion": {
                "heading": "string",
                "summary_paragraphs": [
                    "string",
                    "string"
                ]
            }
        }, indent=2)
        
        return f"""🧠 Prompt: Generate an SEO-Optimized Comparison Blog Post (Crypto Project A vs. Crypto Project B)

Important Callout: For the media property make the name all lowercase and hyphenate between the words of the terms. For example, Ethereum Classic would be "ethereum-classic".

You are writing a detailed, well-researched, SEO-optimized blog post that compares two major crypto entities: {term_a} and {term_b}.

These may be cryptocurrencies, crypto companies, or a combination of both. Some comparisons may involve a company with an associated token (e.g., Solana or Avalanche), while others may focus solely on the token itself (e.g., Bitcoin). Be clear about the nature of each project throughout the article.

Your output must follow the strict JSON schema provided below. The blog post should be structured, comprehensive, written in a clear and professional tone, and optimized for search engines (SEO). You are writing as Moso Panda, a Web3 Specialist and trusted authority on crypto and blockchain technology.

⸻

🔍 Goal

Create a full blog post in JSON format that compares {term_a} vs {term_b}.

The goal is to help readers understand the key differences between the two — whether they are comparing two tokens, two ecosystems, or one token vs a broader company or platform. This content should help readers decide which project aligns better with their goals (investing, transacting, building, holding, etc.).

The blog post should rank for high-intent SEO search terms like:
• "{term_a} vs {term_b}"
• "Best crypto for [function] 2025"
• "Which is better: {term_a} or {term_b}?"
• "{term_a} comparison"
• "{term_b} pros and cons"
• "Is {term_a} better than {term_b}?"

⸻

✍️ Tone & Style
• Author: Moso Panda
• Role: Web3 Specialist
• Tone: Knowledgeable but friendly, easy to follow, and focused on clarity
• Audience: Crypto-curious readers, beginner to intermediate users
• Avoid unnecessary technical jargon unless essential.
• Keep sections digestible and value-packed. Prioritize SEO-friendly structure and formatting.

⸻

📐 Format & Structure

The blog post must follow the structure below and be delivered as a valid JSON object using the comparison_blog_post schema.

Word Count Guidelines
• Title: Short and clear (6–10 words)
• Introduction: ~100–150 words
• Background: ~150–200 words
• Each Key Difference: ~80–120 words per feature
• Comparison Table: 4–5 rows + "Ideal For" section
• Conclusion: ~150–200 words
• Total Word Count: ~800–1,200 words

⸻

📊 Topics to Cover in Key Differences (Suggestions)

Customize based on the comparison, but here are common comparison points to consider:
• Project Type: Cryptocurrency, protocol, platform, or company
• Consensus Mechanism or Tech Stack
• Token Utility or Use Case
• Ecosystem & Developer Activity
• Network Speed & Fees
• Security Model
• Tokenomics & Supply Cap
• Real-World Adoption & Integrations
• Exchange Support & Wallet Compatibility
• Investment/Value Potential

Each key_differences item must include:
• feature_title
• a_description
• b_description

Descriptions should reflect each project's nature (e.g., token-only vs full platform).

⸻

📄 JSON Schema Structure

Your output must be a valid JSON object matching this structure:

{schema_json}

⸻

🧠 Final Prompt Summary

Create a well-structured, SEO-optimized comparison blog post between {term_a} and {term_b} following the JSON schema above. These projects may be tokens, companies, or platforms — explain their nature clearly. The post should include a strong introduction, relevant background, 4–6 key differences, a detailed comparison table, and a thoughtful conclusion. Write as Moso Panda, Web3 Specialist. Output must be a valid JSON object and total between 800–1,200 words."""

    def generate_blog_post(self, term_a: str, term_b: str) -> Optional[Dict]:
        """Generate a comparison blog post for the given terms."""
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini-2024-07-18",
                messages=[
                    {"role": "system", "content": "You are a professional crypto content writer specializing in comparison articles. You must output ONLY valid JSON that exactly matches the required schema structure. Do not include any other text or formatting in your response - just the raw JSON object."},
                    {"role": "user", "content": self._get_prompt(term_a, term_b)}
                ],
                temperature=0.7,
                max_tokens=4000
            )
            
            # Extract and parse the JSON response
            content = response.choices[0].message.content
            blog_post = json.loads(content)
            
            # Validate against our schema
            validated_post = ComparisonBlogPost(**blog_post)
            
            # Save to output directory
            output_file = self.output_dir / f"{validated_post.slug}.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(validated_post.model_dump(), f, indent=2)
                
            logger.info(f"Successfully generated and saved blog post: {output_file}")
            return validated_post.model_dump()
            
        except Exception as e:
            logger.error(f"Error generating blog post: {str(e)}")
            return None 