"""
Public API Explorer - Main Application
Documentation hub for public APIs (no proxy - direct API usage)
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from contextlib import asynccontextmanager

from app.core.config import settings
from app.api.routes import ALL_ROUTERS


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    # Startup
    print(f"🚀 {settings.APP_NAME} v{settings.APP_VERSION} is starting up...")
    print(f"📚 API Documentation Hub - Direct access to public APIs")
    yield
    # Shutdown
    print(f"👋 {settings.APP_NAME} is shutting down...")


# Initialize FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    servers=[
        {"url": "http://127.0.0.1:8003", "description": "Local API Explorer (Proxy)"},
        {"url": "https://api.coingecko.com/api/v3", "description": "CoinGecko API (Direct)"},
        {"url": "https://api.coincap.io/v2", "description": "CoinCap API (Direct)"},
        {"url": "https://api.frankfurter.app", "description": "Frankfurter Exchange Rates (Direct)"},
        {"url": "https://api.open-meteo.com/v1", "description": "Open-Meteo Weather (Direct)"},
        {"url": "https://hacker-news.firebaseio.com/v0", "description": "HackerNews API (Direct)"},
        {"url": "https://restcountries.com/v3.1", "description": "REST Countries (Direct)"},
    ],
    description="""
**Public API Documentation Hub for LLMs & Developers**

This is a documentation catalog of public APIs. All endpoints documented here call the **real public APIs directly**.

## For LLMs & AI Agents:
- Each endpoint shows the actual public API URL
- Use these URLs directly in your code
- No authentication required for most APIs
- Check the `x-api-url` header in responses to see the real endpoint

## Categories:
1. **Finance & Crypto** - CoinGecko, CoinCap, Binance, Coinbase, Exchange Rates
2. **Weather** - Open-Meteo, 7Timer, National Weather Service
3. **News** - HackerNews
4. **Location** - REST Countries, Nominatim, IP APIs
5. **Entertainment** - TMDB Movies, Deezer Music, JokeAPI, Chuck Norris, Quotable
6. **Sports** - NBA Stats, Formula 1, Football/Soccer
7. **AI & NLP** - Translation, Random User Generator, Text Analysis
8. **Travel** - Places of Interest, Timezone, Country Info
9. **Food** - MealDB Recipes, CocktailDB Drinks
10. **Images** - Unsplash, Lorem Picsum, Dog/Cat Photos
5. **Entertainment** - Jokes, Quotes, Facts
6. **Sports** - NBA, Formula 1
7. **AI & NLP** - Translation, QR Codes, Random Data
8. **Travel** - OpenTripMap, Timezone
9. **Food** - TheMealDB, TheCocktailDB
10. **Images** - Unsplash, Picsum, Dog CEO, Cat API

## Usage Example:
```python
# Instead of calling this proxy:
response = requests.get('http://localhost:8000/finance/crypto/coingecko/coins')

# Call the real API directly:
response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd')
```
    """,
    version=settings.APP_VERSION,
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

# Register all routers
for router in ALL_ROUTERS:
    app.include_router(router)


@app.get("/api-urls", response_class=JSONResponse, tags=["Documentation"])
async def get_all_api_urls():
    """
Get a list of all public API base URLs documented in this hub
    
    LLMs can use this to discover which APIs are available
    """
    return {
        "message": "These are the real public API URLs. Use them directly in your code.",
        "apis": {
            "coingecko": "https://api.coingecko.com/api/v3",
            "coincap": "https://api.coincap.io/v2",
            "binance": "https://api.binance.com/api/v3",
            "coinbase": "https://api.coinbase.com/v2",
            "exchangerate": "https://api.exchangerate-api.com/v4",
            "open_meteo": "https://api.open-meteo.com/v1",
            "7timer": "http://www.7timer.info/bin",
            "nws": "https://api.weather.gov",
            "hackernews": "https://hacker-news.firebaseio.com/v0",
            "restcountries": "https://restcountries.com/v3.1",
            "nominatim": "https://nominatim.openstreetmap.org",
            "ip_api": "http://ip-api.com/json",
            "ipify": "https://api.ipify.org",
            "jokeapi": "https://v2.jokeapi.dev",
            "chucknorris": "https://api.chucknorris.io",
            "quotable": "https://api.quotable.io",
            "balldontlie": "https://www.balldontlie.io/api/v1",
            "ergast_f1": "https://ergast.com/api/f1",
            "mymemory": "https://api.mymemory.translated.net",
            "randomuser": "https://randomuser.me/api",
            "opentripmap": "https://api.opentripmap.com",
            "themealdb": "https://www.themealdb.com/api/json/v1",
            "thecocktaildb": "https://www.thecocktaildb.com/api/json/v1",
            "unsplash": "https://api.unsplash.com",
            "picsum": "https://picsum.photos",
            "dog_ceo": "https://dog.ceo/api",
            "cataas": "https://cataas.com"
        }
    }


@app.get("/openapi-external.json", response_class=JSONResponse, tags=["Documentation"])
async def get_external_openapi():
    """
    Get OpenAPI spec with external API URLs (for LLMs and external tools)
    
    This spec includes `x-external-url` extensions that show the real public API URLs.
    LLMs should extract and use these URLs to call APIs directly.
    
    **Example usage for LLMs:**
    ```python
    import requests
    
    # Get the spec
    spec = requests.get('http://localhost:8003/openapi-external.json').json()
    
    # Extract external URL from any endpoint
    for path, methods in spec['paths'].items():
        for method, operation in methods.items():
            external_url = operation.get('x-external-url')
            if external_url:
                # Call the real API directly
                response = requests.get(external_url)
    ```
    """
    from app.core.openapi_exporter import ExternalAPIExporter
    return ExternalAPIExporter.generate_external_openapi(app)


@app.get("/openapi-llm.json", response_class=JSONResponse, tags=["Documentation"])
async def get_llm_openapi():
    """
    Get simplified OpenAPI spec optimized for LLM consumption
    
    This endpoint returns a cleaned-up OpenAPI spec that:
    1. Shows only real external API URLs
    2. Includes `x-external-url` for each endpoint
    3. Removes proxy-related information
    4. Optimized for AI agents to understand and use
    
    **For LLMs:**
    - Download this JSON spec
    - Extract `x-external-url` from each endpoint
    - Call those URLs directly - no authentication needed for most APIs
    """
    from app.core.openapi_exporter import ExternalAPIExporter
    return ExternalAPIExporter.generate_llm_friendly_spec(app)


@app.get("/external-apis", response_class=JSONResponse, tags=["External APIs"])
async def list_external_apis():
    """
    List all available external API Swagger UI endpoints
    
    Each external API has its own OpenAPI spec with correct paths for direct execution.
    """
    return {
        "message": "Click any URL to access the dedicated Swagger UI for that API",
        "apis": {
            "coingecko": {
                "swagger_ui": "http://127.0.0.1:8003/external/coingecko/docs",
                "openapi_spec": "http://127.0.0.1:8003/external/coingecko/openapi.json",
                "description": "CoinGecko Cryptocurrency Data",
                "base_url": "https://api.coingecko.com/api/v3"
            },
            "coincap": {
                "swagger_ui": "http://127.0.0.1:8003/external/coincap/docs",
                "openapi_spec": "http://127.0.0.1:8003/external/coincap/openapi.json",
                "description": "CoinCap Crypto Assets",
                "base_url": "https://api.coincap.io/v2"
            },
            "frankfurter": {
                "swagger_ui": "http://127.0.0.1:8003/external/frankfurter/docs",
                "openapi_spec": "http://127.0.0.1:8003/external/frankfurter/openapi.json",
                "description": "Frankfurter Exchange Rates",
                "base_url": "https://api.frankfurter.app"
            },
            "openmeteo": {
                "swagger_ui": "http://127.0.0.1:8003/external/openmeteo/docs",
                "openapi_spec": "http://127.0.0.1:8003/external/openmeteo/openapi.json",
                "description": "Open-Meteo Weather",
                "base_url": "https://api.open-meteo.com/v1"
            },
            "hackernews": {
                "swagger_ui": "http://127.0.0.1:8003/external/hackernews/docs",
                "openapi_spec": "http://127.0.0.1:8003/external/hackernews/openapi.json",
                "description": "HackerNews Stories",
                "base_url": "https://hacker-news.firebaseio.com/v0"
            }
        }
    }


@app.get("/external/{api_name}/openapi.json", response_class=JSONResponse, tags=["External APIs"])
async def get_external_api_spec(api_name: str):
    """
    Get OpenAPI spec for a specific external API
    
    These specs have the CORRECT paths for direct execution in Swagger UI.
    
    **Available APIs:** coingecko, coincap, frankfurter, openmeteo, hackernews
    """
    from app.core.external_specs import EXTERNAL_API_SPECS
    
    if api_name not in EXTERNAL_API_SPECS:
        raise HTTPException(status_code=404, detail=f"External API '{api_name}' not found. Available: {list(EXTERNAL_API_SPECS.keys())}")
    
    spec_generator = EXTERNAL_API_SPECS[api_name]
    return spec_generator()


@app.get("/external/{api_name}/docs", response_class=HTMLResponse, tags=["External APIs"])
async def get_external_api_docs(api_name: str):
    """
    Get Swagger UI for a specific external API
    
    This Swagger UI will call the EXTERNAL API directly with correct paths!
    
    **Example:** http://127.0.0.1:8003/external/coingecko/docs
    """
    from app.core.external_specs import EXTERNAL_API_SPECS
    
    if api_name not in EXTERNAL_API_SPECS:
        raise HTTPException(status_code=404, detail=f"External API '{api_name}' not found")
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
    <title>{api_name.upper()} API - Direct Access</title>
    <style>
        .topbar {{ background-color: #1a1a1a; }}
        .topbar-wrapper img {{ content: url('https://fastapi.tiangolo.com/img/favicon.png'); }}
    </style>
    </head>
    <body>
    <div id="swagger-ui"></div>
    <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
    <script>
    const ui = SwaggerUIBundle({{
        url: '/external/{api_name}/openapi.json',
        dom_id: '#swagger-ui',
        layout: 'BaseLayout',
        deepLinking: true,
        showExtensions: true,
        showCommonExtensions: true,
        presets: [
            SwaggerUIBundle.presets.apis,
            SwaggerUIBundle.SwaggerUIStandalonePreset
        ],
    }})
    </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/llm-prompt.txt", response_class=HTMLResponse, tags=["Documentation"])
async def get_llm_prompt():
    """
    Generate a text prompt for LLMs explaining how to use these APIs
    
    Copy-paste this prompt into your LLM conversation to help it understand
    how to use the public APIs documented here.
    """
    return """
# Public API Explorer - LLM Instructions

You have access to a collection of public REST APIs. Here's how to use them:

## Available APIs

### Finance & Crypto
- **CoinGecko**: https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=50&page=1
- **CoinCap**: https://api.coincap.io/v2/assets?limit=50
- **Binance**: https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT
- **Frankfurter (Exchange Rates)**: https://api.frankfurter.app/latest?from=USD

### Weather
- **Open-Meteo**: https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41
- **7Timer**: http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=civil&output=json

### News
- **HackerNews**: https://hacker-news.firebaseio.com/v0/topstories.json
- **Item Details**: https://hacker-news.firebaseio.com/v0/item/{item_id}.json

### Location
- **REST Countries**: https://restcountries.com/v3.1/all
- **Search Country**: https://restcountries.com/v3.1/name/{name}

### Entertainment
- **JokeAPI**: https://v2.jokeapi.dev/joke/Any
- **Chuck Norris**: https://api.chucknorris.io/jokes/random
- **Quotable**: https://api.quotable.io/random

### Images
- **Unsplash**: https://api.unsplash.com/photos/random
- **Dog CEO**: https://dog.ceo/api/breeds/image/random
- **Cat API**: https://cataas.com/cat

## How to Use

1. **No authentication required** for most endpoints
2. **Call URLs directly** using GET requests
3. **Rate limits apply** - be respectful of free APIs
4. **All responses are JSON**

## Example Code

```python
import requests

# Get cryptocurrency prices
response = requests.get('https://api.coingecko.com/api/v3/coins/markets', params={
    'vs_currency': 'usd',
    'per_page': 10
})
coins = response.json()

# Get weather
response = requests.get('https://api.open-meteo.com/v1/forecast', params={
    'latitude': 52.52,
    'longitude': 13.41,
    'current_weather': True
})
weather = response.json()
```

## Important Notes

- These are **real public APIs** - call them directly, not through a proxy
- **Respect rate limits** - don't make too many requests too quickly
- Some APIs may require **CORS headers** if called from a browser
- For full documentation, visit: http://localhost:8003/docs
"""


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
