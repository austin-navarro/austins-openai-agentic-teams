#!/usr/bin/env python3
"""
CLI interface for the Comparison Generator Agent Framework.
"""

import os
import asyncio
import argparse
from dotenv import load_dotenv
from agents.orchestrator import OrchestratorAgent

def main():
    # Load environment variables
    load_dotenv()
    
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Generate comparisons with images using AI"
    )
    parser.add_argument(
        "item1",
        help="First item to compare"
    )
    parser.add_argument(
        "item2",
        help="Second item to compare"
    )
    parser.add_argument(
        "--cleanup",
        type=int,
        help="Clean up files older than specified days",
        default=None
    )
    
    args = parser.parse_args()
    
    # Ensure OPENAI_API_KEY is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set")
        return 1
        
    async def run():
        # Initialize orchestrator
        orchestrator = OrchestratorAgent()
        
        # Handle cleanup if requested
        if args.cleanup is not None:
            print(f"Cleaning up files older than {args.cleanup} days...")
            await orchestrator.cleanup(args.cleanup)
            return 0
            
        # Generate comparison
        print(f"Generating comparison for {args.item1} vs {args.item2}...")
        success, result = await orchestrator.generate_comparison(
            args.item1,
            args.item2
        )
        
        if success:
            print("\nComparison generated successfully!")
            print(f"Media ID: {result['media_id']}")
            print(f"Image Path: {result['image_path']}")
            print(f"Comparison Path: {result['comparison_path']}")
            print(f"Status: {result['status']}")
            return 0
        else:
            print("\nError generating comparison:")
            print(result.get("error", "Unknown error"))
            return 1
            
    return asyncio.run(run())

if __name__ == "__main__":
    exit(main()) 