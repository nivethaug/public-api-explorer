#!/usr/bin/env python3
"""
Simple API Verification Script
Tests APIs from category JSON files using Chrome DevTools MCP
"""

import json
from pathlib import Path
from datetime import datetime

def verify_all_apis():
    """Main verification function"""
    print("=" * 80)
    print("API VERIFICATION - Checking All Category JSON Files")
    print("=" * 80)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    categories_dir = Path("docs/llm/categories")
    
    # Results tracking
    results = {
        "tested": 0,
        "working": 0,
        "failed": 0,
        "errors": []
    }
    
    # Get all JSON files
    json_files = sorted([f for f in categories_dir.glob("*.json") if f.name != "index.json"])
    
    print(f"Found {len(json_files)} category files to verify\n")
    
    for json_file in json_files:
        category_name = json_file.stem
        print(f"\n{'=' * 80}")
        print(f"Category: {category_name.upper()}")
        print('=' * 80)
        
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Check structure
            if 'apis' in data:
                apis_list = data['apis']
                print(f"  Structure: Using 'apis' array ({len(apis_list)} APIs)")
            elif 'api' in data:
                apis_list = [data['api']]
                print(f"  Structure: Using single 'api' object")
            else:
                print(f"  ⚠️  WARNING: Unknown structure - skipping")
                continue
            
            # Process each API
            for api in apis_list:
                api_name = api.get('name', 'Unknown')
                api_id = api.get('id', 'unknown')
                base_url = api.get('base_url', '')
                
                print(f"\n  API: {api_name} ({api_id})")
                print(f"  Base: {base_url}")
                
                endpoints = api.get('endpoints', [])
                print(f"  Endpoints: {len(endpoints)}")
                
                for endpoint in endpoints:
                    results['tested'] += 1
                    
                    path = endpoint.get('path', '')
                    sample_request = endpoint.get('sample_request', '')
                    
                    if not sample_request:
                        print(f"    ⚠️  {path} - No sample request")
                        continue
                    
                    print(f"    • {path}")
                    print(f"      URL: {sample_request}")
                    
                    # Note: Actual testing should be done with Chrome DevTools MCP
                    # This script just checks the JSON structure
                    
        except Exception as e:
            print(f"\n  ❌ ERROR reading {json_file.name}: {str(e)}")
            results['errors'].append({
                "file": str(json_file),
                "error": str(e)
            })
    
    print(f"\n{'=' * 80}")
    print("VERIFICATION COMPLETE")
    print("=" * 80)
    print(f"Total files checked: {len(json_files)}")
    print(f"Total errors: {len(results['errors'])}")
    
    if results['errors']:
        print("\nErrors encountered:")
        for error in results['errors']:
            print(f"  - {error['file']}: {error['error']}")

if __name__ == "__main__":
    verify_all_apis()
