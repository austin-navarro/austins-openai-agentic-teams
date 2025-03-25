#!/usr/bin/env python3
"""
Topic Pair Suggestion Utility

This script suggests pairs of topics that would make good comparisons.
It organizes suggestions by category to help marketing teams plan their content.
"""

import json
import os

# Dictionary of categories and potential topic pairs
SUGGESTED_TOPIC_PAIRS = {
    "Technology": [
        ("Python", "JavaScript"),
        ("React", "Angular"),
        ("AWS", "Azure"),
        ("MongoDB", "PostgreSQL"),
        ("iOS", "Android"),
        ("Docker", "Kubernetes"),
        ("REST API", "GraphQL"),
    ],
    
    "Cryptocurrency": [
        ("Bitcoin", "Ethereum"),
        ("Solana", "Avalanche"),
        ("DeFi", "CeFi"),
        ("Proof of Work", "Proof of Stake"),
        ("NFTs", "Traditional Art"),
        ("Crypto Wallets", "Bank Accounts"),
    ],
    
    "Business": [
        ("B2B", "B2C"),
        ("SaaS", "On-Premise Software"),
        ("Remote Work", "Office Work"),
        ("Bootstrapping", "Venture Capital"),
        ("Agile", "Waterfall"),
        ("Outsourcing", "In-house Development"),
    ],
    
    "Marketing": [
        ("SEO", "PPC"),
        ("Content Marketing", "Paid Advertising"),
        ("Email Marketing", "Social Media Marketing"),
        ("Inbound Marketing", "Outbound Marketing"),
        ("Brand Marketing", "Performance Marketing"),
        ("Influencer Marketing", "Traditional Advertising"),
    ],
    
    "Lifestyle": [
        ("Minimalism", "Maximalism"),
        ("Urban Living", "Rural Living"),
        ("Remote Work", "Office Work"),
        ("Freelancing", "Full-time Employment"),
        ("Plant-based Diet", "Omnivore Diet"),
        ("Digital Nomad", "Traditional Living"),
    ]
}

def print_topic_pairs():
    """Print the suggested topic pairs by category"""
    
    print("Suggested Topic Pairs for Comparisons")
    print("=====================================")
    print("")
    
    for category, pairs in SUGGESTED_TOPIC_PAIRS.items():
        print(f"Category: {category}")
        print("-" * (len(category) + 10))
        
        for i, pair in enumerate(pairs, 1):
            print(f"{i}. {pair[0]} vs {pair[1]}")
        
        print("")

def export_to_json(output_file="topic_pairs.json"):
    """Export the suggested topic pairs to a JSON file"""
    
    with open(output_file, "w") as f:
        json.dump(SUGGESTED_TOPIC_PAIRS, f, indent=2)
    
    print(f"Topic pairs exported to {output_file}")

def generate_batch_file(category=None, output_file="batch_comparisons.py"):
    """Generate a Python script for batch comparison of selected topics"""
    
    if category and category not in SUGGESTED_TOPIC_PAIRS:
        print(f"Category '{category}' not found. Available categories:")
        for cat in SUGGESTED_TOPIC_PAIRS.keys():
            print(f"- {cat}")
        return
    
    pairs = []
    if category:
        pairs = SUGGESTED_TOPIC_PAIRS[category]
    else:
        # Take 2 pairs from each category
        for cat_pairs in SUGGESTED_TOPIC_PAIRS.values():
            pairs.extend(cat_pairs[:2])
    
    # Create the script content
    script = f"""#!/usr/bin/env python3
\"\"\"
Batch Comparison Generator
{'for ' + category if category else 'across categories'}

This script was auto-generated to compare multiple topic pairs.
IMPORTANT: This script requires an OpenAI API key and will make API calls.
DO NOT run without explicit permission.
\"\"\"

import asyncio
import os
from batch_generate_comparisons import batch_generate

async def main():
    # Topic pairs to compare
    comparison_pairs = {pairs}
    
    # Create outputs directory
    os.makedirs("outputs", exist_ok=True)
    
    print("⚠️  WARNING: This script will make API calls to OpenAI using your API key.")
    print("    Each comparison uses API credits from your account.")
    proceed = input("Do you want to proceed? (y/n): ")
    
    if proceed.lower() != 'y':
        print("Operation cancelled. No API calls were made.")
        return
    
    # Generate all comparisons
    results = await batch_generate(
        comparison_pairs, 
        output_dir="outputs",
        enable_api_call=True  # Set to False to disable actual API calls
    )
    
    print(f"Generated {{len(results)}}/{{len(comparison_pairs)}} comparison pages")

if __name__ == "__main__":
    asyncio.run(main())
"""
    
    with open(output_file, "w") as f:
        f.write(script)
    
    print(f"Batch comparison script generated: {output_file}")
    print("You can run it with:")
    print(f"python {output_file}")
    print("\nNOTE: This script will ask for confirmation before making API calls.")

def main():
    """Main function to display and export topic pairs"""
    
    print_topic_pairs()
    
    # Ask if user wants to export to JSON
    export = input("Export topic pairs to JSON? (y/n): ").lower()
    if export == 'y':
        export_to_json()
    
    # Ask if user wants to generate a batch file
    batch = input("Generate a batch comparison script? (y/n): ").lower()
    if batch == 'y':
        print("\nCategories:")
        for i, cat in enumerate(SUGGESTED_TOPIC_PAIRS.keys(), 1):
            print(f"{i}. {cat}")
        print("0. All categories (sample)")
        
        choice = input("\nSelect category (number) or press Enter for all: ")
        if choice.strip() == "":
            category = None
        elif choice == "0":
            category = None
        else:
            try:
                index = int(choice) - 1
                category = list(SUGGESTED_TOPIC_PAIRS.keys())[index]
            except (ValueError, IndexError):
                print("Invalid choice. Using all categories.")
                category = None
        
        generate_batch_file(category)

if __name__ == "__main__":
    main() 