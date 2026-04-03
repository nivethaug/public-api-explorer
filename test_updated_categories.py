#!/usr/bin/env python3
"""
Test Updated Categories - Focused Verification
Tests the 4 categories with recent updates:
1. knowledge.json (fixed Wikipedia opensearch)
2. ai.json (replaced TextGain with Twinword)
3. entertainment.json (replaced Quotable with Forismatic)
4. crypto_finance.json (replaced CoinCap with CoinStats)
"""

import json
import requests
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def extract_test_url(api_obj):
    """Extract test URL from API object"""
    # Check for direct_url or sample_request in endpoints
    if 'endpoints' in api_obj and len(api_obj['endpoints']) > 0:
        endpoint = api_obj['endpoints'][0]
        if 'direct_url' in endpoint:
            return endpoint['direct_url']
        if 'sample_request' in endpoint:
            return endpoint['sample_request']
    
    # Check for direct properties
    if 'test_url' in api_obj:
        return api_obj['test_url']
    if 'sample_request' in api_obj:
        return api_obj['sample_request']
    
    return None


def test_api_endpoint(api_obj):
    """Test if an API endpoint is working"""
    try:
        test_url = extract_test_url(api_obj)
        
        if not test_url:
            return None, "No test URL"
        
        # Replace placeholder variables if needed
        test_url = test_url.replace('{API_KEY}', 'test_key')
        test_url = test_url.replace('{KEY}', 'test_key')
        test_url = test_url.replace('{api_key}', 'test_key')
        
        response = requests.get(test_url, timeout=5, headers={
            'User-Agent': 'Public API Explorer Test'
        })
        
        if response.status_code == 200:
            # Try to parse as JSON to verify it returns valid data
            try:
                response.json()
                return True, f"HTTP 200 - Valid JSON"
            except:
                # Some APIs return plain text or other formats
                if len(response.text) > 0:
                    return True, f"HTTP 200 - {len(response.text)} bytes"
                return False, "HTTP 200 but no content"
        else:
            return False, f"HTTP {response.status_code}"
    
    except requests.Timeout:
        return False, "Timeout"
    except requests.ConnectionError:
        return False, "Connection Error"
    except Exception as e:
        return False, str(e)[:50]


def test_category(category_name, json_file):
    """Test all APIs in a category"""
    print(f"\n{'='*80}")
    print(f"Testing: {category_name.upper()}")
    print(f"{'='*80}")
    
    if not json_file.exists():
        print(f"❌ File not found: {json_file}")
        return None
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None
    
    # Extract APIs
    if 'apis' in data:
        apis_list = data['apis']
    elif 'api' in data:
        apis_list = [data['api']]
    else:
        print(f"⚠️  Unknown structure")
        return None
    
    print(f"Found {len(apis_list)} APIs in this category\n")
    
    results = {
        'total': len(apis_list),
        'working': 0,
        'failed': 0,
        'no_test': 0,
        'apis': []
    }
    
    for api in apis_list:
        api_name = api.get('name', 'Unknown')
        api_id = api.get('id', 'unknown')
        
        status, details = test_api_endpoint(api)
        
        # Format output
        if status is None:
            symbol = "⚠️ "
            status_text = "SKIPPED"
            results['no_test'] += 1
        elif status:
            symbol = "✅"
            status_text = "WORKING"
            results['working'] += 1
        else:
            symbol = "❌"
            status_text = "FAILED"
            results['failed'] += 1
        
        print(f"{symbol} {api_name:30s} - {status_text:10s} ({details})")
        results['apis'].append({
            'name': api_name,
            'id': api_id,
            'status': status_text,
            'details': details
        })
    
    # Calculate success rate
    if results['total'] > results['no_test']:
        success_rate = (results['working'] / (results['total'] - results['no_test'])) * 100
    else:
        success_rate = 0
    
    print(f"\n{'─'*80}")
    print(f"Results for {category_name}:")
    print(f"  Working: {results['working']}/{results['total'] - results['no_test']}")
    print(f"  Failed: {results['failed']}")
    print(f"  Skipped: {results['no_test']}")
    print(f"  Success Rate: {success_rate:.1f}%")
    
    return results


def main():
    """Main test runner"""
    categories_dir = Path("docs/llm/categories")
    
    # Define the 4 updated categories to test
    updated_categories = [
        ("Knowledge & Education", categories_dir / "knowledge.json"),
        ("AI & NLP", categories_dir / "ai.json"),
        ("Entertainment", categories_dir / "entertainment.json"),
        ("Cryptocurrency & Finance", categories_dir / "crypto_finance.json"),
    ]
    
    print("\n" + "="*80)
    print("TESTING UPDATED API CATEGORIES")
    print("="*80)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\nUpdates tested:")
    print("  1. knowledge.json (fixed Wikipedia opensearch)")
    print("  2. ai.json (replaced TextGain with Twinword)")
    print("  3. entertainment.json (replaced Quotable with Forismatic)")
    print("  4. crypto_finance.json (replaced CoinCap with CoinStats)")
    
    all_results = {}
    total_working = 0
    total_failed = 0
    total_apis = 0
    
    for category_name, json_file in updated_categories:
        results = test_category(category_name, json_file)
        if results:
            all_results[category_name] = results
            total_working += results['working']
            total_failed += results['failed']
            total_apis += (results['total'] - results['no_test'])
    
    # Print summary
    print(f"\n\n{'='*80}")
    print("SUMMARY REPORT")
    print(f"{'='*80}\n")
    
    for category_name, results in all_results.items():
        working = results['working']
        total = results['total'] - results['no_test']
        if total > 0:
            success_rate = (working / total) * 100
            status = "✅" if success_rate == 100 else "⚠️ " if success_rate >= 75 else "❌"
            print(f"{status} {category_name:30s} {working:2d}/{total:2d} working ({success_rate:5.1f}%)")
    
    # Overall success rate
    print(f"\n{'─'*80}")
    if total_apis > 0:
        overall_success = (total_working / total_apis) * 100
        print(f"Overall Success Rate: {total_working}/{total_apis} = {overall_success:.1f}%")
    else:
        print("No APIs tested")
    
    print(f"\n✅ Testing completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    return 0 if total_failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
