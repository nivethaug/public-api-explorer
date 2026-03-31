"""
OpenAPI Spec Exporter for External APIs
Generates OpenAPI specs that point to real external APIs instead of localhost proxy
"""

from typing import Dict, Any, List
import json


class ExternalAPIExporter:
    """Generate OpenAPI specs for external APIs"""
    
    # Mapping of our routes to external APIs
    API_MAPPINGS = {
        "/finance/crypto/coingecko/coins": {
            "external_url": "https://api.coingecko.com/api/v3/coins/markets",
            "server": "https://api.coingecko.com/api/v3",
            "path": "/coins/markets",
            "provider": "CoinGecko"
        },
        "/finance/crypto/coingecko/coin/{coin_id}": {
            "external_url": "https://api.coingecko.com/api/v3/coins/{coin_id}",
            "server": "https://api.coingecko.com/api/v3",
            "path": "/coins/{coin_id}",
            "provider": "CoinGecko"
        },
        "/finance/crypto/coincap/assets": {
            "external_url": "https://api.coincap.io/v2/assets",
            "server": "https://api.coincap.io/v2",
            "path": "/assets",
            "provider": "CoinCap"
        },
        "/finance/crypto/binance/ticker/24hr": {
            "external_url": "https://api.binance.com/api/v3/ticker/24hr",
            "server": "https://api.binance.com/api/v3",
            "path": "/ticker/24hr",
            "provider": "Binance"
        },
        "/finance/currency/rates/{base}": {
            "external_url": "https://api.frankfurter.app/latest",
            "server": "https://api.frankfurter.app",
            "path": "/latest",
            "provider": "Frankfurter"
        },
        "/weather/forecast": {
            "external_url": "https://api.open-meteo.com/v1/forecast",
            "server": "https://api.open-meteo.com/v1",
            "path": "/forecast",
            "provider": "Open-Meteo"
        },
        "/news/hackernews/topstories": {
            "external_url": "https://hacker-news.firebaseio.com/v0/topstories.json",
            "server": "https://hacker-news.firebaseio.com/v0",
            "path": "/topstories.json",
            "provider": "HackerNews"
        },
        "/location/countries": {
            "external_url": "https://restcountries.com/v3.1/all",
            "server": "https://restcountries.com/v3.1",
            "path": "/all",
            "provider": "REST Countries"
        }
    }
    
    @staticmethod
    def generate_external_openapi(app, base_url: str = None) -> Dict[str, Any]:
        """
        Generate OpenAPI spec that points to external APIs
        
        Args:
            app: FastAPI application
            base_url: Optional base URL to override
        
        Returns:
            Modified OpenAPI spec with external API URLs
        """
        # Get the base OpenAPI spec
        openapi_spec = app.openapi()
        
        # Group endpoints by their external API server
        server_groups = {}
        
        for path, path_item in openapi_spec.get("paths", {}).items():
            # Find mapping for this path
            mapping = ExternalAPIExporter.API_MAPPINGS.get(path)
            
            if mapping:
                external_server = mapping["server"]
                external_path = mapping["path"]
                
                if external_server not in server_groups:
                    server_groups[external_server] = {
                        "server": external_server,
                        "paths": {}
                    }
                
                # Add x-external-url extension to each operation
                for method, operation in path_item.items():
                    if isinstance(operation, dict):
                        # Add external URL as OpenAPI extension
                        operation["x-external-url"] = mapping["external_url"]
                        operation["x-api-provider"] = mapping["provider"]
                        operation["x-direct-call"] = {
                            "url": mapping["external_url"],
                            "description": f"Call this URL directly instead of proxy",
                            "auth_required": False
                        }
                
                # Store the path with external mapping
                server_groups[external_server]["paths"][external_path] = path_item
        
        # Add external URLs to info section
        openapi_spec["info"]["x-external-apis"] = {
            "description": "This documentation shows real public API URLs. Use the x-external-url extension to call APIs directly.",
            "usage": "For LLMs and AI agents: Extract the x-external-url from each endpoint to call the real API directly.",
            "servers": list(set([m["server"] for m in ExternalAPIExporter.API_MAPPINGS.values()]))
        }
        
        return openapi_spec
    
    @staticmethod
    def generate_llm_friendly_spec(app) -> Dict[str, Any]:
        """
        Generate a simplified OpenAPI spec optimized for LLM consumption
        
        This spec:
        1. Shows only the real external API URLs
        2. Includes direct call examples
        3. Removes proxy information
        """
        openapi_spec = app.openapi()
        
        llm_spec = {
            "openapi": "3.0.0",
            "info": {
                "title": f"{openapi_spec['info']['title']} - External APIs (For LLMs)",
                "version": openapi_spec['info']['version'],
                "description": "Direct access to public APIs. No proxy. No authentication required for most endpoints.",
                "x-llm-instructions": {
                    "usage": "Extract x-external-url from each endpoint to call the real API",
                    "example": "GET https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd",
                    "note": "All URLs in x-external-url are real public APIs you can call directly"
                }
            },
            "servers": [
                {"url": "https://api.coingecko.com/api/v3", "description": "CoinGecko"},
                {"url": "https://api.coincap.io/v2", "description": "CoinCap"},
                {"url": "https://api.frankfurter.app", "description": "Frankfurter"},
                {"url": "https://api.open-meteo.com/v1", "description": "Open-Meteo"},
                {"url": "https://hacker-news.firebaseio.com/v0", "description": "HackerNews"},
            ],
            "paths": {}
        }
        
        # Add each path with external URL
        for path, path_item in openapi_spec.get("paths", {}).items():
            mapping = ExternalAPIExporter.API_MAPPINGS.get(path)
            
            if mapping:
                for method, operation in path_item.items():
                    if isinstance(operation, dict):
                        # Add external URL prominently
                        operation["x-external-url"] = mapping["external_url"]
                        operation["x-api-provider"] = mapping["provider"]
                        
                        # Add to LLM spec
                        if path not in llm_spec["paths"]:
                            llm_spec["paths"][path] = {}
                        llm_spec["paths"][path][method] = operation
        
        return llm_spec
