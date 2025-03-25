#!/usr/bin/env python3
"""
Batch Comparison Generator

This script generates multiple comparisons at once.
IMPORTANT: This script requires an OpenAI API key and will make API calls.
DO NOT run without explicit permission.
"""

import asyncio
import json
import os
from comparison_generator import create_comparison_content
from load_env import load_dotenv

async def batch_generate(comparison_pairs, output_dir=None, enable_api_call=False):
    """
    Generate multiple comparisons and optionally save them to files
    
    Args:
        comparison_pairs (list): List of topic pairs to compare
        output_dir (str, optional): Directory to save outputs
        enable_api_call (bool): Set to True to actually make API calls
        
    Returns:
        list: Generated comparison pages
    """
    if not enable_api_call:
        print("⚠️  API calls are disabled. This is just a demonstration of what would happen.")
        print("    To enable API calls, set enable_api_call=True when calling this function.")
        
        print("\nWould generate the following comparisons:")
        for i, pair in enumerate(comparison_pairs, 1):
            if len(pair) == 2:
                topic1, topic2 = pair
                print(f"  {i}. {topic1} vs {topic2}")
            else:
                topic1, topic2, media_id = pair
                print(f"  {i}. {topic1} vs {topic2} (with media ID)")
        
        return []
    
    # First, make sure we have our API key
    load_dotenv()
    
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("Error: No OpenAI API key found. Please set OPENAI_API_KEY in .env file.")
        return []
        
    results = []
    
    # Create output directory if needed
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for i, pair in enumerate(comparison_pairs):
        if len(pair) == 2:
            topic1, topic2 = pair
            media_id = None
        else:
            topic1, topic2, media_id = pair
            
        # Determine output file path if needed
        output_file = None
        if output_dir:
            slug = f"{topic1.lower().replace(' ', '-')}-vs-{topic2.lower().replace(' ', '-')}"
            output_file = os.path.join(output_dir, f"{slug}.json")
        
        try:
            # Generate the comparison
            comparison = await create_comparison_content(
                topic1=topic1,
                topic2=topic2,
                media_id=media_id,
                output_file=output_file
            )
            results.append(comparison)
            print(f"✅ [{i+1}/{len(comparison_pairs)}] Generated: {topic1} vs {topic2}")
            
        except Exception as e:
            print(f"❌ [{i+1}/{len(comparison_pairs)}] Error generating {topic1} vs {topic2}: {str(e)}")
    
    print(f"\nCompleted batch generation: {len(results)}/{len(comparison_pairs)} successful")
    return results

# When run directly, show the help message but don't make API calls
if __name__ == "__main__":
    print("⚠️  This script needs to be imported and called explicitly with enable_api_call=True.")
    print("    Example usage in Python:")
    print("    ```")
    print("    import asyncio")
    print("    from batch_generate_comparisons import batch_generate")
    print("    ")
    print("    comparison_pairs = [")
    print("        ('Topic1', 'Topic2'),")
    print("        ('Topic3', 'Topic4')")
    print("    ]")
    print("    ")
    print("    # Enable API calls only when ready to make OpenAI API requests")
    print("    asyncio.run(batch_generate(comparison_pairs, output_dir='outputs', enable_api_call=True))")
    print("    ```")
    print("\nTo run from command line with more control, use generate_comparison.sh instead.") 