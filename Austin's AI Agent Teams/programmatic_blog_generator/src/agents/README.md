# Blog Generation Agents

This directory contains the AI agents responsible for different aspects of blog generation.

## Agent Structure

Each agent is responsible for a specific aspect of blog generation:

- `content_generator/`: Main agent for generating blog content
- `seo_optimizer/`: Agent for optimizing content for search engines
- `style_manager/`: Agent for maintaining consistent writing style
- `publisher/`: Agent for handling content publishing

## Agent Communication

Agents communicate through a standardized JSON format, ensuring:
- Clear input/output interfaces
- Consistent data structure
- Easy integration between agents

## Agent Configuration

Each agent can be configured through:
- Environment variables
- Configuration files in the `config/` directory
- Runtime parameters

## Development Guidelines

1. Each agent should be self-contained
2. Use dependency injection for external services
3. Implement proper error handling
4. Include comprehensive logging
5. Write unit tests for each agent 