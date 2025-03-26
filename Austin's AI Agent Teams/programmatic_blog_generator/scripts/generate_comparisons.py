"""
Script to process CSV data and generate comparison blog posts.
"""
import csv
from pathlib import Path
import logging
from typing import Dict, List
import time
import argparse
import sys

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.agents.comparison_agent import ComparisonAgent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def process_csv(csv_path: Path, agent: ComparisonAgent, batch_size: int = 1, test_mode: bool = False) -> List[Dict]:
    """Process the CSV file and generate blog posts."""
    results = []
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)  # Convert to list to get total count
            
            total_rows = len(rows)
            logger.info(f"Found {total_rows} rows to process")
            
            # In test mode, only process the first row
            if test_mode:
                rows = rows[:1]
                logger.info("Running in test mode - processing only first row")
            
            for i, row in enumerate(rows, start=1):
                # Extract terms from the row using the correct column names
                term_a = row.get('Term 1', '').strip()
                term_b = row.get('Term 2', '').strip()
                
                if not term_a or not term_b:
                    logger.warning(f"Skipping row {i}: Missing terms")
                    continue
                    
                logger.info(f"Processing row {i}/{total_rows}: {term_a} vs {term_b}")
                
                # Generate blog post
                result = agent.generate_blog_post(term_a, term_b)
                if result:
                    results.append(result)
                    logger.info(f"Successfully generated blog post for {term_a} vs {term_b}")
                else:
                    logger.error(f"Failed to generate blog post for {term_a} vs {term_b}")
                
                # Add delay between requests to avoid rate limiting
                time.sleep(2)
                
                # Process in batches if specified
                if batch_size > 1 and i % batch_size == 0:
                    logger.info(f"Completed batch of {batch_size} posts")
                    time.sleep(5)  # Longer delay between batches
                    
    except Exception as e:
        logger.error(f"Error processing CSV: {str(e)}")
        
    return results

def main():
    """Main function to run the comparison generation process."""
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate comparison blog posts from CSV data')
    parser.add_argument('--test', action='store_true', help='Run in test mode (process only first row)')
    parser.add_argument('--batch-size', type=int, default=1, help='Number of posts to generate in each batch')
    args = parser.parse_args()
    
    # Initialize paths
    data_dir = Path(__file__).parent.parent / "data"
    csv_path = data_dir / "crypto_comparison_pairs_cleaned.csv"
    
    if not csv_path.exists():
        logger.error(f"CSV file not found at {csv_path}")
        return
        
    # Initialize agent
    agent = ComparisonAgent()
    
    # Process CSV
    logger.info("Starting blog post generation process...")
    results = process_csv(csv_path, agent, batch_size=args.batch_size, test_mode=args.test)
    
    # Log results
    logger.info(f"Completed processing. Generated {len(results)} blog posts.")
    
if __name__ == "__main__":
    main() 