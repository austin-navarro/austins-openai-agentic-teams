# Comparison Page Generator

This document explains how to use the automated comparison page generator to create structured content for the marketing team.

## Overview

The Comparison Page Generator uses AI agents to automatically create, format, and optionally publish comparison pages that follow our Payload CMS schema. The system handles research, writing, and formatting to produce consistently structured content.

## Model Information

The comparison generator uses OpenAI's **GPT-4o-mini** model with a temperature of 0.7, which provides a good balance between:
- High-quality content generation
- Factual accuracy
- Cost efficiency (cheaper than full GPT-4)
- Faster response times

This model works well for creating structured comparison content while keeping API costs reasonable.

## Basic Usage

### Generate a Single Comparison

The simplest way to generate a comparison is to run the `simple_demo.py` script:

```bash
cd examples/comparison_generator
python simple_demo.py
```

This will generate a comparison between Bitcoin and Ethereum and save it to a JSON file.

To generate a comparison between different topics, modify the script or use the API directly:

```python
import asyncio
from comparison_generator import create_comparison_content

async def create_comparison():
    # Generate a comparison between two topics
    await create_comparison_content(
        topic1="Topic A",
        topic2="Topic B",
        media_id="your-media-id-here",  # Optional
        output_file="topic-a-vs-topic-b.json"  # Optional
    )

asyncio.run(create_comparison())
```

### Generate Multiple Comparisons in Batch

To generate multiple comparisons at once, use the batch generation functionality:

```python
import asyncio
from batch_generate_comparisons import batch_generate

async def create_multiple_comparisons():
    # Define topic pairs to compare
    comparison_pairs = [
        ("Topic A", "Topic B"),
        ("Topic C", "Topic D"),
        ("Topic E", "Topic F", "specific-media-id")  # With specific media ID
    ]
    
    # Generate all comparisons and save to the 'outputs' directory
    await batch_generate(comparison_pairs, output_dir="outputs", enable_api_call=True)

asyncio.run(create_multiple_comparisons())
```

## Output Structure

Each generated comparison follows this structure:

```json
{
  "title": "Topic A vs Topic B",
  "slug": "topic-a-vs-topic-b",
  "intro": "<p>Introduction text...</p>",
  "comparisonImage": "media_id_here",
  "sections": [
    {
      "heading": "Feature 1",
      "content": "<p>Comparison of Feature 1...</p>"
    },
    {
      "heading": "Feature 2",
      "content": "<p>Comparison of Feature 2...</p>"
    }
  ],
  "conclusion": "<p>Conclusion text...</p>",
  "published": false
}
```

## Media IDs

To add comparison images:

1. First upload the image to the Payload CMS using the Media collection
2. Copy the returned media ID (it looks like `64e8a7f9b47e8a001cc44d23`)
3. Use that ID in the `media_id` parameter when generating comparisons

## Best Practices

1. **Choose Related Topics**: Compare topics that are in the same category or field
2. **Be Specific**: More specific topic pairs yield better comparisons
3. **Review Generated Content**: Always review AI-generated content before publishing
4. **Add Media**: Visual elements improve engagement, so include relevant images
5. **Update Regularly**: For topics that change rapidly, regenerate comparisons quarterly

## Workflow Example

Here's a typical workflow for the marketing team:

1. Identify pairs of topics to compare (based on keywords, trends, or content gaps)
2. Generate comparisons using the batch generator
3. Review and edit the generated content
4. Add media IDs for relevant images
5. Upload the final JSON to the CMS (manually or via API)

## Troubleshooting

- **Invalid Media ID**: Ensure the media ID exists in your CMS
- **Poor Content Quality**: Try more specific topic pairs or manually edit the output
- **Missing Sections**: Try different topic phrasing or add custom section requirements
- **HTML Formatting Issues**: Check for unclosed tags in the generated content
- **API Costs**: Using GPT-4o-mini keeps costs lower than full GPT-4, but still incurs charges for each comparison 