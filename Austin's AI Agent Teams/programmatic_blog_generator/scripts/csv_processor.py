"""
CSV Processor for handling crypto comparison pairs data.
"""
import os
import csv
from typing import List, Dict, Optional
from pathlib import Path
import logging
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CSVProcessor:
    def __init__(self):
        """Initialize the CSV processor with configuration."""
        load_dotenv()
        self.data_dir = Path(__file__).parent.parent / "data"
        self.csv_file = self.data_dir / "crypto_comparison_pairs_cleaned.csv"
        
    def validate_csv(self) -> bool:
        """Validate the CSV file exists and is properly formatted."""
        if not self.csv_file.exists():
            logger.error(f"CSV file not found at {self.csv_file}")
            return False
            
        try:
            with open(self.csv_file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader)  # Skip header row
                if not header:
                    logger.error("CSV file is empty")
                    return False
                return True
        except Exception as e:
            logger.error(f"Error validating CSV: {str(e)}")
            return False
            
    def read_comparison_pairs(self) -> List[Dict[str, str]]:
        """Read and process the comparison pairs from CSV."""
        if not self.validate_csv():
            return []
            
        comparison_pairs = []
        try:
            with open(self.csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Clean and validate each row
                    cleaned_row = {
                        k: v.strip() for k, v in row.items() if v.strip()
                    }
                    if cleaned_row:
                        comparison_pairs.append(cleaned_row)
                        
            logger.info(f"Successfully processed {len(comparison_pairs)} comparison pairs")
            return comparison_pairs
            
        except Exception as e:
            logger.error(f"Error reading CSV: {str(e)}")
            return []
            
    def get_next_pair(self) -> Optional[Dict[str, str]]:
        """Get the next unprocessed comparison pair."""
        pairs = self.read_comparison_pairs()
        if pairs:
            return pairs[0]
        return None

def main():
    """Main function to test CSV processing."""
    processor = CSVProcessor()
    pairs = processor.read_comparison_pairs()
    
    if pairs:
        logger.info(f"Found {len(pairs)} comparison pairs")
        logger.info(f"Sample pair: {pairs[0]}")
    else:
        logger.warning("No comparison pairs found")

if __name__ == "__main__":
    main() 