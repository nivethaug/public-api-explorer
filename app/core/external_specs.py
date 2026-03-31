"""
Generate individual OpenAPI specs for external APIs
These specs have the correct paths for direct execution in Swagger UI
"""

from typing import Dict, Any
import json


def generate_coingecko_spec() -> Dict[str, Any]:
    """Generate OpenAPI spec for CoinGecko API with correct paths"""
    return {
        "openapi": "3.0.0",
        "info": {
            "title": "CoinGecko API",
            "version": "3.0.0",
            "description": "Cryptocurrency data API - Direct access to CoinGecko",
            "x-website": "https://www.coingecko.com/",
            "x-api-docs": "https://docs.coingecko.com/"
        },
        "servers": [
            {
                "url": "https://api.coingecko.com/api/v3",
                "description": "CoinGecko Public API"
            }
        ],
        "paths": {
            "/coins/markets": {
                "get": {
                    "summary": "List all coins with market data",
                    "description": "Get list of cryptocurrencies with market data",
                    "operationId": "getCoinsMarkets",
                    "parameters": [
                        {
                            "name": "vs_currency",
                            "in": "query",
                            "description": "Currency to compare against (usd, eur, btc, etc.)",
                            "required": True,
                            "schema": {"type": "string", "default": "usd"}
                        },
                        {
                            "name": "order",
                            "in": "query",
                            "description": "Order results",
                            "schema": {"type": "string", "default": "market_cap_desc"}
                        },
                        {
                            "name": "per_page",
                            "in": "query",
                            "description": "Results per page (1-250)",
                            "schema": {"type": "integer", "default": 50, "minimum": 1, "maximum": 250}
                        },
                        {
                            "name": "page",
                            "in": "query",
                            "description": "Page number",
                            "schema": {"type": "integer", "default": 1, "minimum": 1}
                        },
                        {
                            "name": "sparkline",
                            "in": "query",
                            "description": "Include sparkline data",
                            "schema": {"type": "boolean", "default": False}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content": {
                                "application/json": {
                                    "schema": {"type": "array", "items": {"type": "object"}}
                                }
                            }
                        }
                    }
                }
            },
            "/coins/{id}": {
                "get": {
                    "summary": "Get coin details by ID",
                    "description": "Get detailed information about a specific cryptocurrency",
                    "operationId": "getCoinById",
                    "parameters": [
                        {
                            "name": "id",
                            "in": "path",
                            "description": "Coin ID (e.g., bitcoin, ethereum)",
                            "required": True,
                            "schema": {"type": "string"}
                        },
                        {
                            "name": "localization",
                            "in": "query",
                            "description": "Include localization data",
                            "schema": {"type": "boolean", "default": True}
                        },
                        {
                            "name": "tickers",
                            "in": "query",
                            "description": "Include ticker data",
                            "schema": {"type": "boolean", "default": True}
                        },
                        {
                            "name": "market_data",
                            "in": "query",
                            "description": "Include market data",
                            "schema": {"type": "boolean", "default": True}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content": {
                                "application/json": {
                                    "schema": {"type": "object"}
                                }
                            }
                        }
                    }
                }
            },
            "/ping": {
                "get": {
                    "summary": "API status check",
                    "description": "Check API server status",
                    "operationId": "ping",
                    "responses": {
                        "200": {
                            "description": "API is working",
                            "content": {
                                "application/json": {
                                    "schema": {"type": "object", "properties": {"gecko_says": {"type": "string"}}}
                                }
                            }
                        }
                    }
                }
            }
        }
    }


def generate_coincap_spec() -> Dict[str, Any]:
    """Generate OpenAPI spec for CoinCap API with correct paths"""
    return {
        "openapi": "3.0.0",
        "info": {
            "title": "CoinCap API",
            "version": "2.0.0",
            "description": "Cryptocurrency market data - Direct access to CoinCap",
            "x-website": "https://coincap.io/",
            "x-api-docs": "https://docs.coincap.io/"
        },
        "servers": [
            {
                "url": "https://api.coincap.io/v2",
                "description": "CoinCap Public API"
            }
        ],
        "paths": {
            "/assets": {
                "get": {
                    "summary": "List all crypto assets",
                    "description": "Get list of cryptocurrency assets",
                    "operationId": "getAssets",
                    "parameters": [
                        {
                            "name": "limit",
                            "in": "query",
                            "description": "Limit results (max 2000)",
                            "schema": {"type": "integer", "default": 100, "maximum": 2000}
                        },
                        {
                            "name": "search",
                            "in": "query",
                            "description": "Search by asset ID or symbol",
                            "schema": {"type": "string"}
                        },
                        {
                            "name": "ids",
                            "in": "query",
                            "description": "Comma-separated asset IDs",
                            "schema": {"type": "string"}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content": {
                                "application/json": {
                                    "schema": {"type": "object"}
                                }
                            }
                        }
                    }
                }
            },
            "/assets/{id}": {
                "get": {
                    "summary": "Get asset by ID",
                    "description": "Get single cryptocurrency asset",
                    "operationId": "getAssetById",
                    "parameters": [
                        {
                            "name": "id",
                            "in": "path",
                            "description": "Asset ID (e.g., bitcoin, ethereum)",
                            "required": True,
                            "schema": {"type": "string"}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content": {
                                "application/json": {
                                    "schema": {"type": "object"}
                                }
                            }
                        }
                    }
                }
            }
        }
    }


def generate_frankfurter_spec() -> Dict[str, Any]:
    """Generate OpenAPI spec for Frankfurter Exchange Rates API"""
    return {
        "openapi": "3.0.0",
        "info": {
            "title": "Frankfurter Exchange Rates API",
            "version": "1.0.0",
            "description": "Foreign exchange rates - Direct access to Frankfurter",
            "x-website": "https://www.frankfurter.app/",
            "x-api-docs": "https://www.frankfurter.app/docs/"
        },
        "servers": [
            {
                "url": "https://api.frankfurter.app",
                "description": "Frankfurter Public API"
            }
        ],
        "paths": {
            "/latest": {
                "get": {
                    "summary": "Get latest exchange rates",
                    "description": "Get latest foreign exchange rates",
                    "operationId": "getLatestRates",
                    "parameters": [
                        {
                            "name": "from",
                            "in": "query",
                            "description": "Base currency (e.g., USD, EUR)",
                            "schema": {"type": "string", "default": "EUR"}
                        },
                        {
                            "name": "to",
                            "in": "query",
                            "description": "Target currency or currencies (comma-separated)",
                            "schema": {"type": "string"}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content": {
                                "application/json": {
                                    "schema": {"type": "object"}
                                }
                            }
                        }
                    }
                }
            },
            "/{date}": {
                "get": {
                    "summary": "Get historical rates",
                    "description": "Get exchange rates for a specific date",
                    "operationId": "getHistoricalRates",
                    "parameters": [
                        {
                            "name": "date",
                            "in": "path",
                            "description": "Date in YYYY-MM-DD format",
                            "required": True,
                            "schema": {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$"}
                        },
                        {
                            "name": "from",
                            "in": "query",
                            "description": "Base currency",
                            "schema": {"type": "string"}
                        },
                        {
                            "name": "to",
                            "in": "query",
                            "description": "Target currency",
                            "schema": {"type": "string"}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content": {
                                "application/json": {
                                    "schema": {"type": "object"}
                                }
                            }
                        }
                    }
                }
            }
        }
    }


def generate_openmeteo_spec() -> Dict[str, Any]:
    """Generate OpenAPI spec for Open-Meteo Weather API"""
    return {
        "openapi": "3.0.0",
        "info": {
            "title": "Open-Meteo Weather API",
            "version": "1.0.0",
            "description": "Free weather forecast API - Direct access to Open-Meteo",
            "x-website": "https://open-meteo.com/",
            "x-api-docs": "https://open-meteo.com/en/docs"
        },
        "servers": [
            {
                "url": "https://api.open-meteo.com/v1",
                "description": "Open-Meteo Public API"
            }
        ],
        "paths": {
            "/forecast": {
                "get": {
                    "summary": "Get weather forecast",
                    "description": "Get weather forecast for coordinates",
                    "operationId": "getForecast",
                    "parameters": [
                        {
                            "name": "latitude",
                            "in": "query",
                            "description": "Latitude (-90 to 90)",
                            "required": True,
                            "schema": {"type": "number", "minimum": -90, "maximum": 90}
                        },
                        {
                            "name": "longitude",
                            "in": "query",
                            "description": "Longitude (-180 to 180)",
                            "required": True,
                            "schema": {"type": "number", "minimum": -180, "maximum": 180}
                        },
                        {
                            "name": "current_weather",
                            "in": "query",
                            "description": "Include current weather",
                            "schema": {"type": "boolean", "default": True}
                        },
                        {
                            "name": "hourly",
                            "in": "query",
                            "description": "Hourly variables (comma-separated)",
                            "schema": {"type": "string"}
                        },
                        {
                            "name": "daily",
                            "in": "query",
                            "description": "Daily variables (comma-separated)",
                            "schema": {"type": "string"}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content": {
                                "application/json": {
                                    "schema": {"type": "object"}
                                }
                            }
                        }
                    }
                }
            }
        }
    }


def generate_hackernews_spec() -> Dict[str, Any]:
    """Generate OpenAPI spec for HackerNews API"""
    return {
        "openapi": "3.0.0",
        "info": {
            "title": "HackerNews API",
            "version": "0.0.0",
            "description": "HackerNews stories and comments - Direct access",
            "x-website": "https://news.ycombinator.com/",
            "x-api-docs": "https://github.com/HackerNews/API"
        },
        "servers": [
            {
                "url": "https://hacker-news.firebaseio.com/v0",
                "description": "HackerNews Public API"
            }
        ],
        "paths": {
            "/topstories.json": {
                "get": {
                    "summary": "Get top story IDs",
                    "description": "Get list of up to 500 top story IDs",
                    "operationId": "getTopStories",
                    "responses": {
                        "200": {
                            "description": "Array of story IDs",
                            "content": {
                                "application/json": {
                                    "schema": {"type": "array", "items": {"type": "integer"}}
                                }
                            }
                        }
                    }
                }
            },
            "/newstories.json": {
                "get": {
                    "summary": "Get new story IDs",
                    "description": "Get list of up to 500 new story IDs",
                    "operationId": "getNewStories",
                    "responses": {
                        "200": {
                            "description": "Array of story IDs",
                            "content": {
                                "application/json": {
                                    "schema": {"type": "array", "items": {"type": "integer"}}
                                }
                            }
                        }
                    }
                }
            },
            "/item/{itemId}.json": {
                "get": {
                    "summary": "Get item by ID",
                    "description": "Get story, comment, or poll item",
                    "operationId": "getItem",
                    "parameters": [
                        {
                            "name": "itemId",
                            "in": "path",
                            "description": "Item ID",
                            "required": True,
                            "schema": {"type": "integer"}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Item details",
                            "content": {
                                "application/json": {
                                    "schema": {"type": "object"}
                                }
                            }
                        }
                    }
                }
            }
        }
    }


# Dictionary of all external API specs
EXTERNAL_API_SPECS = {
    "coingecko": generate_coingecko_spec,
    "coincap": generate_coincap_spec,
    "frankfurter": generate_frankfurter_spec,
    "openmeteo": generate_openmeteo_spec,
    "hackernews": generate_hackernews_spec
}
