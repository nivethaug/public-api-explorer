#!/usr/bin/env python3
"""
Extract all sample_request URLs from category JSON files
"""

import json
import os
from pathlib import Path

def extract_urls():
    categories_dir = Path('docs/llm/categories')
    urls = []

    for json_file in categories_dir.glob('*.json'):
        if json_file.name == 'index.json':
            continue

        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            category = data.get('category', json_file.stem)

            for api in data.get('apis', []):
                for endpoint in api.get('endpoints', []):
                    sample_url = endpoint.get('sample_request')
                    if sample_url:
                        urls.append({
                            'category': category,
                            'api': api.get('name', api.get('id', 'unknown')),
                            'endpoint': endpoint.get('path', endpoint.get('summary', 'unknown')),
                            'url': sample_url
                        })
        except Exception as e:
            print(f"Error processing {json_file}: {e}")
            continue

    return urls

if __name__ == "__main__":
    urls = extract_urls()
    print(f'Found {len(urls)} URLs to test')

    # Group by category
    by_category = {}
    for item in urls:
        cat = item['category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(item)

    print("\nURLs by category:")
    for cat, items in by_category.items():
        print(f"{cat}: {len(items)} URLs")

    # Save to file
    with open('test_urls.json', 'w') as f:
        json.dump(urls, f, indent=2)

    print("\nSaved to test_urls.json")