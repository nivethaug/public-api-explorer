"""
API Routes Package
All route modules are imported and exposed here for easy registration
"""

from app.api.routes.health import router as health_router
from app.api.routes.finance_crypto import router as finance_crypto_router
from app.api.routes.weather import router as weather_router
from app.api.routes.news import router as news_router
from app.api.routes.location import router as location_router
from app.api.routes.entertainment import router as entertainment_router
from app.api.routes.sports import router as sports_router
from app.api.routes.ai_nlp import router as ai_nlp_router
from app.api.routes.travel import router as travel_router
from app.api.routes.food import router as food_router
from app.api.routes.images import router as images_router
from app.api.routes.currency import router as currency_router
from app.api.routes.stocks import router as stocks_router

# List of all routers to be included in the app
ALL_ROUTERS = [
    health_router,
    finance_crypto_router,
    weather_router,
    news_router,
    location_router,
    entertainment_router,
    sports_router,
    ai_nlp_router,
    travel_router,
    food_router,
    images_router,
    currency_router,
    stocks_router,
]

__all__ = [
    "health_router",
    "finance_crypto_router", 
    "weather_router",
    "news_router",
    "location_router",
    "entertainment_router",
    "sports_router",
    "ai_nlp_router",
    "travel_router",
    "food_router",
    "images_router",
    "currency_router",
    "stocks_router",
    "ALL_ROUTERS",
]

# Real Public API URLs for LLMs
# This list helps AI understand which APIs are documented
PUBLIC_API_URLS = {
    "finance_crypto": {
        "coingecko": "https://api.coingecko.com/api/v3",
        "coincap": "https://api.coincap.io/v2",
        "binance": "https://api.binance.com/api/v3",
        "coinbase": "https://api.coinbase.com/v2",
        "exchangerate": "https://api.exchangerate-api.com/v4"
    },
    "weather": {
        "open_meteo": "https://api.open-meteo.com/v1",
        "7timer": "http://www.7timer.info/bin",
        "nws": "https://api.weather.gov"
    },
    "news": {
        "hackernews": "https://hacker-news.firebaseio.com/v0"
    },
    "location": {
        "restcountries": "https://restcountries.com/v3.1",
        "nominatim": "https://nominatim.openstreetmap.org",
        "ip_api": "http://ip-api.com/json",
        "ipify": "https://api.ipify.org"
    },
    "entertainment": {
        "jokeapi": "https://v2.jokeapi.dev",
        "chucknorris": "https://api.chucknorris.io",
        "quotable": "https://api.quotable.io",
        "uselessfacts": "https://uselessfacts.jsph.pl"
    },
    "sports": {
        "balldontlie": "https://www.balldontlie.io/api/v1",
        "ergast_f1": "https://ergast.com/api/f1"
    },
    "ai": {
        "mymemory": "https://api.mymemory.translated.net",
        "randomuser": "https://randomuser.me/api"
    },
    "travel": {
        "opentripmap": "https://api.opentripmap.com",
        "timezoneapi": "https://timezoneapi.io/api"
    },
    "food": {
        "themealdb": "https://www.themealdb.com/api/json/v1",
        "thecocktaildb": "https://www.thecocktaildb.com/api/json/v1"
    },
    "images": {
        "unsplash": "https://api.unsplash.com",
        "picsum": "https://picsum.photos",
        "dog_ceo": "https://dog.ceo/api",
        "cataas": "https://cataas.com"
    }
}
