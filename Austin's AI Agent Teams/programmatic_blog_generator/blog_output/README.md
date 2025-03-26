# Blog Output Directory

This directory stores all generated blog posts in JSON format.

## File Structure

Each blog post is stored as a JSON file with the following naming convention:
```
YYYY-MM-DD--slugified-title.json
```

Example: `2024-03-26--getting-started-with-ai-blogging.json`

## JSON Schema

Each blog post JSON file follows this structure:
```json
{
    "metadata": {
        "title": "string",
        "slug": "string",
        "author": "string",
        "date": "YYYY-MM-DD",
        "tags": ["string"],
        "category": "string",
        "status": "draft|published"
    },
    "content": {
        "body": "string",
        "excerpt": "string",
        "seo": {
            "meta_title": "string",
            "meta_description": "string",
            "keywords": ["string"]
        }
    },
    "style": {
        "tone": "string",
        "reading_level": "string",
        "word_count": "integer"
    }
}
```

## Usage

- Generated blogs are automatically saved here
- Each file is versioned with a timestamp
- Files can be used for:
  - Publishing to various platforms
  - Content review
  - Analytics
  - Backup purposes 