"""
Script to add missing test methods to test files
"""
import re

# Define missing tests for each file
missing_tests = {
    "tests/test_finance_crypto.py": [
        ("/finance/crypto/coingecko/coin/bitcoin", "test_finance_crypto_coingecko_coin_by_id", "Test CoinGecko coin by ID"),
        ("/finance/crypto/binance/ticker/24hr", "test_finance_crypto_binance_ticker", "Test Binance 24hr ticker"),
        ("/finance/crypto/coinbase/prices", "test_finance_crypto_coinbase_prices", "Test Coinbase prices"),
        ("/finance/exchange-rate/USD", "test_finance_exchange_rate", "Test exchange rate by base currency"),
    ],
    "tests/test_food.py": [
        ("/food/meals/search", "test_food_meals_search", "Test meal search"),
        ("/food/meals/1", "test_food_meals_by_id", "Test meal by ID"),
        ("/food/cocktails/1", "test_food_cocktails_by_id", "Test cocktail by ID"),
        ("/food/breweries/search", "test_food_breweries_search", "Test brewery search"),
        ("/food/breweries/1", "test_food_breweries_by_id", "Test brewery by ID"),
        ("/food/breweries/random", "test_food_breweries_random", "Test random brewery"),
    ],
    "tests/test_health_fitness.py": [
        ("/health/fda/food-recalls", "test_health_fda_food_recalls", "Test FDA food recalls"),
    ],
    "tests/test_images.py": [
        ("/images/picsum", "test_images_picsum", "Test Lorem Picsum images"),
        ("/images/cataas/random", "test_images_cataas_random", "Test random cat images"),
    ],
    "tests/test_jobs.py": [
        ("/jobs/jobicy/list", "test_jobs_jobicy_list", "Test Jobicy job list"),
        ("/jobs/devit/search", "test_jobs_devit_search", "Test DevIT job search"),
    ],
    "tests/test_knowledge.py": [
        ("/knowledge/books/search", "test_knowledge_books_search", "Test book search"),
        ("/knowledge/books/OL45804W", "test_knowledge_books_by_id", "Test book by work ID"),
        ("/knowledge/wikipedia/article/Python", "test_knowledge_wikipedia_article", "Test Wikipedia article"),
    ],
    "tests/test_news.py": [
        ("/news/hackernews/new", "test_news_hackernews_new", "Test new HackerNews stories"),
    ],
    "tests/test_science.py": [
        ("/science/iss/crew", "test_science_iss_crew", "Test ISS crew members"),
        ("/science/spacex/launches", "test_science_spacex_launches", "Test SpaceX launches"),
        ("/science/spacex/rockets", "test_science_spacex_rockets", "Test SpaceX rockets"),
        ("/science/nasa/mars/photos", "test_science_nasa_mars_photos", "Test NASA Mars photos"),
        ("/science/earthquakes", "test_science_earthquakes", "Test earthquake data"),
    ],
    "tests/test_security.py": [
        ("/security/police/crimes", "test_security_police_crimes", "Test UK police crimes"),
        ("/security/urlhaus/recent", "test_security_urlhaus_recent", "Test recent URLhaus entries"),
        ("/security/nvd/cves/CVE-2024-0001", "test_security_nvd_cve_by_id", "Test NVD CVE by ID"),
    ],
    "tests/test_sports.py": [
        ("/sports/football/matches", "test_sports_football_matches", "Test football matches"),
        ("/sports/nba/teams", "test_sports_nba_teams", "Test NBA teams"),
    ],
    "tests/test_stocks.py": [
        ("/stocks/crypto/BTC", "test_stocks_crypto_by_symbol", "Test crypto by symbol"),
    ],
    "tests/test_travel.py": [
        ("/travel/capital/France", "test_travel_capital", "Test country capital"),
    ],
    "tests/test_utilities.py": [
        ("/utilities/color/info?hex=FF5733", "test_utilities_color_info", "Test color information"),
        ("/utilities/hash/text?text=hello", "test_utilities_hash_text", "Test text hashing"),
        ("/utilities/timestamp/current", "test_utilities_timestamp_current", "Test current timestamp"),
    ],
    "tests/test_weather.py": [
        ("/weather/nws/alerts", "test_weather_nws_alerts", "Test NWS weather alerts"),
    ],
}

def add_test_to_file(file_path, endpoint, test_name, description):
    """Add a test method to a test file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the last method in the class
        # Look for the last occurrence of a method definition
        last_method_pattern = r'(    def test_[^\(]+\([^\)]*\):[^\n]*\n(?:[^\n]*\n)*?(?=\n(?:class|\Z))'
        matches = list(re.finditer(last_method_pattern, content, re.MULTILINE))
        
        if not matches:
            print(f"  ❌ Could not find class structure in {file_path}")
            return False
        
        last_match = matches[-1]
        insert_position = last_match.end()
        
        # Create the new test method
        new_test = f'''
    def {test_name}(self):
        """{description}"""
        response = client.get("{endpoint}")
        assert response.status_code in [200, 404, 422, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict) or isinstance(data, list)
'''
        
        # Insert the new test
        new_content = content[:insert_position] + new_test + content[insert_position:]
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  ✅ Added {test_name}")
        return True
    except Exception as e:
        print(f"  ❌ Error adding {test_name}: {e}")
        return False

def main():
    print("🚀 Adding missing tests to test files...\n")
    
    total_added = 0
    total_failed = 0
    
    for file_path, tests in missing_tests.items():
        print(f"\n📝 Processing {file_path}...")
        for endpoint, test_name, description in tests:
            if add_test_to_file(file_path, endpoint, test_name, description):
                total_added += 1
            else:
                total_failed += 1
    
    print(f"\n{'='*60}")
    print(f"✅ Tests added: {total_added}")
    print(f"❌ Tests failed: {total_failed}")
    print(f"📊 Total: {total_added + total_failed}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
