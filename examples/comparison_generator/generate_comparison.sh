#!/bin/bash
# Script to generate a comparison between two topics
# IMPORTANT: This script makes API calls to OpenAI and requires an API key.

echo "⚠️  WARNING: This script will make API calls to OpenAI using your API key."
echo "    Each comparison uses API credits from your account."
read -p "Do you want to proceed? (y/n): " PROCEED

if [ "$PROCEED" != "y" ] && [ "$PROCEED" != "Y" ]; then
    echo "Operation cancelled. No API calls were made."
    exit 0
fi

# Check if two arguments were provided
if [ $# -lt 2 ]; then
    echo "Usage: $0 <topic1> <topic2> [media_id]"
    echo "Example: $0 'Bitcoin' 'Ethereum'"
    echo "Example with media ID: $0 'Python' 'JavaScript' 'your-media-id'"
    exit 1
fi

TOPIC1="$1"
TOPIC2="$2"
MEDIA_ID=""

# Check if a media ID was provided
if [ $# -eq 3 ]; then
    MEDIA_ID="$3"
fi

echo "Will compare: $TOPIC1 vs $TOPIC2"
if [ -n "$MEDIA_ID" ]; then
    echo "Using media ID: $MEDIA_ID"
fi

# Create the output directory if it doesn't exist
mkdir -p outputs

# Generate the output filename
TOPIC1_LOWER=$(echo "$TOPIC1" | tr '[:upper:]' '[:lower:]')
TOPIC2_LOWER=$(echo "$TOPIC2" | tr '[:upper:]' '[:lower:]')
SLUG=$(echo "${TOPIC1_LOWER}-vs-${TOPIC2_LOWER}" | tr ' ' '-')
OUTPUT_FILE="outputs/${SLUG}.json"

# Run the comparison directly without a temporary script
python3 -c "
import asyncio
import os
import sys
from comparison_generator import create_comparison_content
from load_env import load_dotenv

async def run_comparison():
    # Load environment variables
    load_dotenv()
    
    # Check if API key is set
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print('Error: No OpenAI API key found. Please set OPENAI_API_KEY in .env file.')
        sys.exit(1)
    
    # Get topics from arguments
    topic1 = '${TOPIC1}'
    topic2 = '${TOPIC2}'
    media_id = '${MEDIA_ID}' or None
    output_file = '${OUTPUT_FILE}'
    
    print(f'Generating comparison between {topic1} and {topic2}...')
    
    try:
        # Generate comparison
        comparison = await create_comparison_content(
            topic1=topic1,
            topic2=topic2,
            media_id=media_id,
            output_file=output_file
        )
        
        print(f'\nGeneration successful!')
        print(f'Title: {comparison.title}')
        print(f'Number of sections: {len(comparison.sections)}')
        print('\nSections:')
        for i, section in enumerate(comparison.sections, 1):
            print(f'  {i}. {section.heading}')
        
        print(f'\nComparison saved to {output_file}')
        
    except Exception as e:
        print(f'Error generating comparison: {str(e)}')
        sys.exit(1)

asyncio.run(run_comparison())
" 