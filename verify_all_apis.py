#!/usr/bin/env python3
"""
Comprehensive API Verification Script
Tests all APIs listed in docs/llm/categories/*.json files
"""

import json
import requests
from pathlib import Path
from datetime import datetime
import time

class APIVerifier:
    def __init__(self):
        self.results = {
            "total_tested": 0,
            "working": [],
            "failed": [],
            "auth_required": [],
            "timeout": [],
            "errors": []
        }
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
    def load_category_files(self):
        """Load all category JSON files"""
        categories_dir = Path("docs/llm/categories")
        category_files = list(categories_dir.glob("*.json"))
        return category_files
    
    def test_endpoint(self, url, timeout=10):
        """Test a single API endpoint"""
        try:
            response = self.session.get(url, timeout=timeout)
            
            # Check if response is JSON
            try:
                data = response.json()
                return {
                    "status": "success",
                    "status_code": response.status_code,
                    "data": data,
                    "response_time": response.elapsed.total_seconds()
                }
            except:
                return {
                    "status": "not_json",
                    "status_code": response.status_code,
                    "error": "Response is not valid JSON"
                }
                
        except requests.exceptions.Timeout:
            return {"status": "timeout", "error": "Request timed out"}
        except requests.exceptions.ConnectionError as e:
            return {"status": "connection_error", "error": str(e)}
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def verify_all_apis(self):
        """Test all APIs from all category files"""
        print("=" * 80)
        print("COMPREHENSIVE API VERIFICATION")
        print("=" * 80)
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        category_files = self.load_category_files()
        
        for category_file in sorted(category_files):
            if category_file.name == "index.json":
                continue
                
            print(f"\n{'=' * 80}")
            print(f"Testing Category: {category_file.stem.upper()}")
            print(f"{'=' * 80}")
            
            with open(category_file, 'r', encoding='utf-8') as f:
                category_data = json.load(f)
            
            category_name = category_data.get('name', 'Unknown')
            print(f"Category: {category_name}")
            print()
            
            for api in category_data.get('apis', []):
                api_name = api.get('name', 'Unknown')
                api_id = api.get('id', 'unknown')
                base_url = api.get('base_url', '')
                
                print(f"\n  API: {api_name} ({api_id})")
                print(f"  Base URL: {base_url}")
                
                for endpoint in api.get('endpoints', []):
                    self.results['total_tested'] += 1
                    
                    endpoint_path = endpoint.get('path', '')
                    sample_request = endpoint.get('sample_request', '')
                    summary = endpoint.get('summary', '')
                    
                    if not sample_request:
                        print(f"    ⚠️  SKIP: {endpoint_path} - No sample request URL")
                        continue
                    
                    print(f"    Testing: {summary}")
                    print(f"    URL: {sample_request}")
                    
                    result = self.test_endpoint(sample_request)
                    
                    if result['status'] == 'success':
                        status_code = result['status_code']
                        response_time = result['response_time']
                        
                        if status_code == 200:
                            print(f"    ✅ SUCCESS - Status: {status_code} - Time: {response_time:.2f}s")
                            self.results['working'].append({
                                "category": category_file.stem,
                                "api": api_name,
                                "endpoint": endpoint_path,
                                "url": sample_request,
                                "response_time": response_time
                            })
                        else:
                            print(f"    ⚠️  AUTH REQUIRED - Status: {status_code}")
                            self.results['auth_required'].append({
                                "category": category_file.stem,
                                "api": api_name,
                                "endpoint": endpoint_path,
                                "url": sample_request,
                                "status_code": status_code
                            })
                    
                    elif result['status'] == 'timeout':
                        print(f"    ⏱️  TIMEOUT - Request took too long")
                        self.results['timeout'].append({
                            "category": category_file.stem,
                            "api": api_name,
                            "endpoint": endpoint_path,
                            "url": sample_request
                        })
                    
                    elif result['status'] == 'connection_error':
                        error_msg = result.get('error', 'Unknown error')
                        if '523' in error_msg or 'unreachable' in error_msg.lower():
                            print(f"    ❌ DOWN - Origin unreachable (523 error)")
                        else:
                            print(f"    ❌ FAILED - Connection error: {error_msg}")
                        self.results['failed'].append({
                            "category": category_file.stem,
                            "api": api_name,
                            "endpoint": endpoint_path,
                            "url": sample_request,
                            "error": error_msg
                        })
                    
                    else:
                        error_msg = result.get('error', 'Unknown error')
                        print(f"    ❌ ERROR - {error_msg}")
                        self.results['errors'].append({
                            "category": category_file.stem,
                            "api": api_name,
                            "endpoint": endpoint_path,
                            "url": sample_request,
                            "error": error_msg
                        })
                    
                    time.sleep(0.5)  # Be nice to APIs
                
                print()
        
        self.print_summary()
        self.save_results()
    
    def print_summary(self):
        """Print verification summary"""
        print("\n" + "=" * 80)
        print("VERIFICATION SUMMARY")
        print("=" * 80)
        print(f"Total Endpoints Tested: {self.results['total_tested']}")
        print()
        print(f"✅ Working: {len(self.results['working'])}")
        print(f"❌ Failed: {len(self.results['failed'])}")
        print(f"⚠️  Auth Required: {len(self.results['auth_required'])}")
        print(f"⏱️  Timeout: {len(self.results['timeout'])}")
        print(f"🔴 Errors: {len(self.results['errors'])}")
        print()
        
        if self.results['failed']:
            print("\n" + "=" * 80)
            print("FAILED APIs (Need Attention)")
            print("=" * 80)
            for item in self.results['failed']:
                print(f"\n  Category: {item['category']}")
                print(f"  API: {item['api']}")
                print(f"  Endpoint: {item['endpoint']}")
                print(f"  URL: {item['url']}")
                print(f"  Error: {item['error']}")
        
        if self.results['auth_required']:
            print("\n" + "=" * 80)
            print("APIs Requiring Authentication")
            print("=" * 80)
            for item in self.results['auth_required']:
                print(f"\n  Category: {item['category']}")
                print(f"  API: {item['api']}")
                print(f"  Endpoint: {item['endpoint']}")
                print(f"  URL: {item['url']}")
        
        print("\n" + "=" * 80)
        print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 80)
    
    def save_results(self):
        """Save results to JSON file"""
        output_file = Path("docs/llm/api_verification_results.json")
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        
        print(f"\nResults saved to: {output_file}")

if __name__ == "__main__":
    verifier = APIVerifier()
    verifier.verify_all_apis()
