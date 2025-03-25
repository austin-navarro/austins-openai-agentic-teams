#!/usr/bin/env python3
"""
Environment Variables Loader

This script loads environment variables from a .env file.
It's particularly useful for loading API keys without hardcoding them.
"""

import os
import sys
from pathlib import Path

def load_dotenv(env_file=None):
    """
    Load environment variables from .env file
    
    Args:
        env_file (str, optional): Path to the .env file
        
    Returns:
        bool: True if successful, False otherwise
    """
    # If no env_file is specified, look in standard locations
    if env_file is None:
        # First try the current directory
        if Path('.env').exists():
            env_file = '.env'
        else:
            # Then try the project root (up to 3 levels)
            current = Path.cwd()
            for _ in range(3):
                parent = current.parent
                if (parent / '.env').exists():
                    env_file = str(parent / '.env')
                    break
                current = parent
    
    # If we still don't have an env_file, return False
    if env_file is None or not Path(env_file).exists():
        print(f"No .env file found")
        return False
    
    # Load the .env file
    print(f"Loading environment variables from {env_file}")
    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue
            
            # Parse key-value pairs
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                
                # Remove quotes if present
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                elif value.startswith("'") and value.endswith("'"):
                    value = value[1:-1]
                
                # Set environment variable
                os.environ[key] = value
    
    return True

def get_api_key():
    """
    Get the OpenAI API key from environment variables
    
    Returns:
        str: The API key or None if not found
    """
    # Try to load from .env first
    load_dotenv()
    
    # Then check environment variables
    api_key = os.environ.get('OPENAI_API_KEY')
    
    # Mask the key for printing (only show first 3 and last 3 characters)
    if api_key:
        masked_key = f"{api_key[:3]}...{api_key[-3:]}" if len(api_key) > 6 else "***"
        print(f"OpenAI API key loaded: {masked_key}")
    else:
        print("No OpenAI API key found in environment variables")
    
    return api_key

# If this script is run directly, just load the env vars
if __name__ == "__main__":
    success = load_dotenv()
    if success:
        # Check if API key is loaded
        api_key = os.environ.get('OPENAI_API_KEY')
        if api_key:
            print("OpenAI API key loaded successfully")
        else:
            print("No OpenAI API key found in the .env file")
    else:
        print("Failed to load environment variables") 