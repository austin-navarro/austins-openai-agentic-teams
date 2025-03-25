# Comparison Page Generator

A simple tool for automatically generating structured comparison content for marketing purposes using the OpenAI Agents framework.

## Overview

This tool uses AI to generate high-quality comparison pages between any two topics. The output follows a structured format compatible with CMS systems, making it easy to publish content with minimal editing required.

## AI Model Used

This generator uses the **GPT-4o-mini** model from OpenAI with the following configuration:
```python
model_config={
    "model": "gpt-4o-mini",
    "temperature": 0.7
}
```

GPT-4o-mini provides a good balance of quality and cost-effectiveness for this type of content generation.

## Features

- Generate detailed comparisons between any two topics
- Automatically structure content with sections, intro, and conclusion
- Format content with HTML for rich text fields
- Save output as JSON for easy CMS import
- Process multiple comparisons in batch

## Files in this Package

- `comparison_generator.py` - Core implementation of the comparison generator
- `simple_demo.py` - Basic demonstration of generating a single comparison
- `generate_comparison_example.py` - More detailed example showing different options
- `batch_generate_comparisons.py` - Tool for generating multiple comparisons in batch
- `test_comparison_structure.py` - Test utility for validating structure without API calls
- `topic_pair_suggestions.py` - Utility that suggests good topic pairs for comparisons
- `load_env.py` - Utility for loading API keys from .env file
- `generate_comparison.sh` - Shell script for easy command-line generation of comparisons

## Getting Started

### Prerequisites

1. Make sure you have the OpenAI Agents SDK installed:
   ```
   pip install openai-agents
   ```

2. Set your OpenAI API key in a `.env` file:
   ```
   OPENAI_API_KEY=sk-...
   ```

### Basic Usage

#### Generate a Single Comparison

The simplest way to get started is to use the shell script:

```bash
./generate_comparison.sh "Bitcoin" "Ethereum"
```

This will generate a comparison between the specified topics and save it to a JSON file.

To use it in your own code:

```python
import asyncio
from comparison_generator import create_comparison_content
from load_env import load_dotenv

async def generate_example():
    # Load API key from .env file
    load_dotenv()
    
    # Generate a comparison between two topics
    comparison = await create_comparison_content(
        topic1="Bitcoin",
        topic2="Ethereum",
        media_id="your-media-id-here",  # Optional
        output_file="bitcoin-vs-ethereum.json"  # Optional
    )
    
    print(f"Generated comparison with {len(comparison.sections)} sections")

# Run the function
if __name__ == "__main__":
    asyncio.run(generate_example())
```

#### Generate Multiple Comparisons

To generate multiple comparisons at once:

```python
import asyncio
from batch_generate_comparisons import batch_generate
from load_env import load_dotenv

async def generate_multiple():
    # Load API key from .env file
    load_dotenv()
    
    # Define topic pairs to compare
    comparison_pairs = [
        ("Topic A", "Topic B"),
        ("Topic C", "Topic D"),
        ("Topic E", "Topic F", "specific-media-id")  # With specific media ID
    ]
    
    # Generate all comparisons and save to the 'outputs' directory
    await batch_generate(comparison_pairs, output_dir="outputs", enable_api_call=True)

# Run the function
if __name__ == "__main__":
    asyncio.run(generate_multiple())
```

#### Generate Topic Pair Suggestions

If you need ideas for good comparisons to generate, use the topic suggestion utility:

```bash
python topic_pair_suggestions.py
```

This will display a list of suggested topic pairs organized by category and allow you to generate a batch script for a specific category.

## Output Format

The generator produces structured JSON that matches a standard CMS schema:

```json
{
  "title": "Bitcoin vs Ethereum",
  "slug": "bitcoin-vs-ethereum",
  "intro": "<p>Introduction text here...</p>",
  "comparisonImage": "media_id_here",
  "sections": [
    {
      "heading": "Technology",
      "content": "<p>Detailed comparison of technologies...</p>"
    },
    {
      "heading": "Use Cases",
      "content": "<p>Different use cases for each...</p>"
    }
  ],
  "conclusion": "<p>Conclusion text here...</p>",
  "published": false
}
```

## Tips for Better Results

1. **Be Specific**: The more specific your topic pair, the better the comparison
2. **Media IDs**: You need to add media IDs manually or provide them when generating
3. **Review Before Publishing**: Always review the generated content before publishing
4. **HTML Content**: The content includes HTML formatting for rich text fields
5. **API Costs**: Each comparison uses the gpt-4o-mini model, which incurs API costs

## Documentation

For more detailed information, see the [marketing documentation](../../docs/marketing/comparison_generator.md). 