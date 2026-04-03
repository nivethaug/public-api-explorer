"""
Comprehensive Test Runner for Public API Explorer
Runs tests for all categories and generates summary
"""
import subprocess
import sys
from pathlib import Path

# Test categories
TEST_FILES = [
    "test_finance_crypto.py",
    "test_weather.py", 
    "test_news.py",
    "test_ai_nlp.py",
    "test_currency.py",
    "test_ecommerce.py",
    "test_entertainment.py",
    "test_sports.py",
    "test_location.py",
    "test_travel.py",
    "test_food.py",
    "test_images.py",
    "test_jobs.py",
    "test_health_fitness.py",
    "test_knowledge.py",
    "test_security.py",
    "test_science.py",
    "test_stocks.py",
    "test_utilities.py",
]

def run_all_tests():
    """Run all test files"""
    test_dir = Path(__file__).parent
    
    print("=" * 70)
    print("Public API Explorer - Comprehensive Test Suite")
    print("=" * 70)
    print()
    
    results = []
    total_passed = 0
    total_failed = 0
    
    for test_file in TEST_FILES:
        test_path = test_dir / test_file
        
        if not test_path.exists():
            print(f"⚠️  {test_file:30s} - SKIPPED (not found)")
            continue
        
        # Run pytest for this file
        cmd = [
            sys.executable, "-m", "pytest",
            str(test_path),
            "-v",
            "--tb=no",
            "-q",
            "--color=no"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Parse output
        output = result.stdout + result.stderr
        
        # Count passed/failed
        passed = output.count(" PASSED")
        failed = output.count(" FAILED")
        
        total_passed += passed
        total_failed += failed
        
        # Status icon
        if failed == 0:
            status = "✅"
        elif passed == 0:
            status = "❌"
        else:
            status = "⚠️"
        
        print(f"{status} {test_file:30s} - {passed:2d} passed, {failed:2d} failed")
        
        results.append({
            "file": test_file,
            "passed": passed,
            "failed": failed,
            "status": status
        })
    
    # Summary
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total Categories Tested: {len(results)}/20")
    print(f"Total Tests Passed:      {total_passed}")
    print(f"Total Tests Failed:      {total_failed}")
    print(f"Pass Rate:               {total_passed}/{total_passed + total_failed} ({100*total_passed/(total_passed + total_failed) if (total_passed + total_failed) > 0 else 0:.1f}%)")
    print("=" * 70)
    
    return total_failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
