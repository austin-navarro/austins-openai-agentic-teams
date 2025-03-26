# Processing Scripts

This directory contains Python scripts for processing data and managing the blog generation workflow.

## Script Structure

### Data Processing
- `csv_processor.py`: Handles CSV file reading and validation
- `data_validator.py`: Validates and sanitizes input data
- `term_extractor.py`: Extracts and processes comparison terms

### Content Generation
- `content_pipeline.py`: Orchestrates the content generation process
- `agent_manager.py`: Manages agent interactions and workflow
- `output_handler.py`: Handles blog post output and storage

### Utility Scripts
- `logger.py`: Centralized logging configuration
- `config_loader.py`: Loads and validates configuration
- `utils.py`: Common utility functions

## Usage

Each script can be run independently or as part of the main pipeline:

```bash
# Process CSV data
python scripts/csv_processor.py

# Run full content generation pipeline
python scripts/content_pipeline.py

# Validate data
python scripts/data_validator.py
```

## Script Dependencies
- All scripts use the project's main requirements
- Additional dependencies are documented in each script
- Environment variables are loaded from `.env`

## Error Handling
- Each script includes comprehensive error handling
- Errors are logged to the project's logging system
- Failed operations are retried with backoff 