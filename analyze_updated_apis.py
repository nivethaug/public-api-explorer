#!/usr/bin/env python3
"""
Detailed API Testing Report for Updated Categories
Includes analysis of failures and authentication requirements
"""

import json
from pathlib import Path

def analyze_category(category_name, json_file):
    """Analyze a category's APIs with detailed information"""
    print(f"\n{'='*90}")
    print(f"DETAILED ANALYSIS: {category_name.upper()}")
    print(f"{'='*90}\n")
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    apis = data.get('apis', [])
    
    for api in apis:
        print(f"🔹 API: {api.get('name', 'Unknown')}")
        print(f"  ID: {api.get('id', 'N/A')}")
        print(f"  Auth Required: {api.get('auth_required', 'N/A')}")
        print(f"  Rate Limited: {api.get('rate_limited', 'N/A')}")
        print(f"  Base URL: {api.get('base_url', 'N/A')}")
        
        if 'endpoints' in api and len(api['endpoints']) > 0:
            endpoint = api['endpoints'][0]
            print(f"  Sample Request: {endpoint.get('sample_request', 'N/A')}")
            direct_url = endpoint.get('direct_url', 'N/A')
            if direct_url != 'N/A':
                print(f"  Direct URL: {direct_url}")
        
        print()


def main():
    categories_dir = Path("docs/llm/categories")
    
    updated_categories = [
        ("Knowledge & Education", categories_dir / "knowledge.json"),
        ("AI & NLP", categories_dir / "ai.json"),
        ("Entertainment", categories_dir / "entertainment.json"),
        ("Cryptocurrency & Finance", categories_dir / "crypto_finance.json"),
    ]
    
    for category_name, json_file in updated_categories:
        analyze_category(category_name, json_file)


if __name__ == "__main__":
    main()
