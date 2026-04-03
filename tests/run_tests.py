"""
Test Runner for Public API Explorer
Runs all category tests and generates coverage report
"""
import pytest
import sys
from pathlib import Path

# Test categories in order
TEST_CATEGORIES = [
    ("Finance & Crypto", "test_finance_crypto.py"),
    ("Weather", "test_weather.py"),
    ("News", "test_news.py"),
    ("Location", "test_location.py"),
    ("Entertainment", "test_entertainment.py"),
    ("Sports", "test_sports.py"),
    ("AI & NLP", "test_ai_nlp.py"),
    ("Utilities", "test_utilities.py"),
    ("Travel", "test_travel.py"),
    ("Food", "test_food.py"),
    ("Currency", "test_currency.py"),
    ("Stocks", "test_stocks.py"),
    ("Jobs", "test_jobs.py"),
    ("Health & Fitness", "test_health_fitness.py"),
    ("Knowledge", "test_knowledge.py"),
    ("Images", "test_images.py"),
    ("E-commerce", "test_ecommerce.py"),
    ("Security", "test_security.py"),
    ("Science", "test_science.py"),
]


def run_all_tests():
    """Run all test files"""
    test_dir = Path(__file__).parent
    test_files = [str(test_dir / test_file) for _, test_file in TEST_CATEGORIES]
    
    # Add conftest.py
    test_files.insert(0, str(test_dir / "conftest.py"))
    
    # Run pytest
    exit_code = pytest.main([
        *test_files,
        "-v",  # Verbose output
        "--tb=short",  # Short traceback format
        "--color=yes",  # Colored output
        "-p", "no:warnings",  # Disable warnings
    ])
    
    return exit_code


def run_category_test(category_name: str):
    """Run tests for a specific category"""
    test_file = None
    for name, file in TEST_CATEGORIES:
        if name.lower() == category_name.lower():
            test_file = file
            break
    
    if not test_file:
        print(f"❌ Category '{category_name}' not found")
        print(f"Available categories: {', '.join([name for name, _ in TEST_CATEGORIES])}")
        return 1
    
    test_dir = Path(__file__).parent
    test_path = str(test_dir / test_file)
    
    print(f"\n🧪 Running tests for: {category_name}")
    print("=" * 60)
    
    exit_code = pytest.main([
        test_path,
        "-v",
        "--tb=short",
        "--color=yes",
    ])
    
    return exit_code


def list_categories():
    """List all available test categories"""
    print("\n📋 Available Test Categories:")
    print("=" * 60)
    for i, (name, _) in enumerate(TEST_CATEGORIES, 1):
        print(f"{i:2d}. {name}")
    print()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        
        if arg in ["--list", "-l", "list"]:
            list_categories()
        elif arg in ["--all", "-a", "all"]:
            exit_code = run_all_tests()
            sys.exit(exit_code)
        else:
            # Run specific category
            exit_code = run_category_test(arg)
            sys.exit(exit_code)
    else:
        # Default: run all tests
        print("🚀 Running all API category tests...")
        print("=" * 60)
        exit_code = run_all_tests()
        sys.exit(exit_code)
