# LLM Integration Guide

## 🎯 What We Built

Your API Explorer now has **5 ways** for LLMs and AI agents to discover and use the real public APIs:

---

## 1. **Individual Swagger UIs for Each External API** ⭐⭐⭐ BEST FOR DIRECT EXECUTION

**URLs:**
- CoinGecko: `http://127.0.0.1:8003/external/coingecko/docs`
- CoinCap: `http://127.0.0.1:8003/external/coincap/docs`
- Frankfurter: `http://127.0.0.1:8003/external/frankfurter/docs`
- Open-Meteo: `http://127.0.0.1:8003/external/openmeteo/docs`
- HackerNews: `http://127.0.0.1:8003/external/hackernews/docs`

### How to Use:
1. Open `http://127.0.0.1:8003/external/coingecko/docs`
2. Click on any endpoint (e.g., `GET /coins/markets`)
3. Click "Try it out"
4. Click "Execute"
5. **It calls the REAL API directly!** ✅

### Why This Works:
Each external API has its own OpenAPI spec with the **correct paths**:
- Server: `https://api.coingecko.com/api/v3`
- Path: `/coins/markets`
- Full URL: `https://api.coingecko.com/api/v3/coins/markets` ✅

**vs. the old approach (doesn't work):**
- Server: `https://api.coingecko.com/api/v3`
- Path: `/finance/crypto/coingecko/coins` (your local path)
- Full URL: `https://api.coingecko.com/api/v3/finance/crypto/coingecko/coins` ❌ 404 Error

---

## 2. **List All External API Swagger UIs**

**URL:** `http://127.0.0.1:8003/external-apis`

Returns JSON with all external API Swagger UI URLs:

```json
{
  "message": "Click any URL to access the dedicated Swagger UI for that API",
  "apis": {
    "coingecko": {
      "swagger_ui": "http://127.0.0.1:8003/external/coingecko/docs",
      "openapi_spec": "http://127.0.0.1:8003/external/coingecko/openapi.json",
      "description": "CoinGecko Cryptocurrency Data",
      "base_url": "https://api.coingecko.com/api/v3"
    },
    ...
  }
}
```

---

## 3. **Swagger UI with Server Selection** ⭐ Easiest for Humans

**URL:** `http://127.0.0.1:8003/docs`

### ⚠️ IMPORTANT LIMITATION:
The server dropdown in your main Swagger UI **will NOT work for direct execution** because:
- Your local paths (e.g., `/finance/crypto/coingecko/coins`) don't match external API paths
- Swagger UI always appends your local path to the server URL
- This causes 404 errors

### Use Individual Swagger UIs Instead:
Use `http://127.0.0.1:8003/external/coingecko/docs` for direct execution.

---

## 4. **API URLs Endpoint** 📋 Simple List

**URL:** `http://127.0.0.1:8003/api-urls`

Returns a JSON object with all public API base URLs:

```json
{
  "message": "These are the real public API URLs. Use them directly in your code.",
  "apis": {
    "coingecko": "https://api.coingecko.com/api/v3",
    "coincap": "https://api.coincap.io/v2",
    "binance": "https://api.binance.com/api/v3",
    "open_meteo": "https://api.open-meteo.com/v1",
    "hackernews": "https://hacker-news.firebaseio.com/v0",
    ...
  }
}
```

**LLM Usage:**
```python
import requests

# Get list of all APIs
apis = requests.get('http://127.0.0.1:8003/api-urls').json()['apis']

# Use any API directly
coingecko_url = apis['coingecko']
response = requests.get(f'{coingecko_url}/coins/markets', params={'vs_currency': 'usd'})
```

---

## 3. **LLM Prompt Text** 🤖 Copy-Paste for AI

**URL:** `http://127.0.0.1:8003/llm-prompt.txt`

Returns a formatted text prompt you can copy-paste into any LLM conversation:

```
# Public API Explorer - LLM Instructions

You have access to a collection of public REST APIs. Here's how to use them:

## Available APIs

### Finance & Crypto
- **CoinGecko**: https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=50&page=1
- **CoinCap**: https://api.coincap.io/v2/assets?limit=50
...

## How to Use
1. **No authentication required** for most endpoints
2. **Call URLs directly** using GET requests
3. **Rate limits apply** - be respectful of free APIs
```

**Use Case:** Paste this into ChatGPT, Claude, or any LLM to give it context about available APIs.

---

## 4. **OpenAPI Specs with External URLs** 🔧 For AI Agents

### A. Standard OpenAPI with Extensions

**URL:** `http://127.0.0.1:8003/openapi.json`

Every endpoint now includes `x-external-url` extension:

```json
{
  "paths": {
    "/finance/crypto/coingecko/coins": {
      "get": {
        "x-external-url": "https://api.coingecko.com/api/v3/coins/markets",
        "x-api-provider": "CoinGecko",
        "x-direct-call": {
          "url": "https://api.coingecko.com/api/v3/coins/markets",
          "method": "GET",
          "auth_required": false,
          "example": "curl 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=50&page=1'"
        }
      }
    }
  }
}
```

### B. External OpenAPI Spec

**URL:** `http://127.0.0.1:8003/openapi-external.json`

Same as above but includes metadata for LLMs:

```json
{
  "info": {
    "x-external-apis": {
      "description": "This documentation shows real public API URLs",
      "usage": "Extract the x-external-url from each endpoint to call the real API directly",
      "servers": ["https://api.coingecko.com/api/v3", ...]
    }
  }
}
```

### C. LLM-Optimized OpenAPI Spec

**URL:** `http://127.0.0.1:8003/openapi-llm.json`

Simplified spec optimized for AI consumption:

```json
{
  "info": {
    "title": "Public API Explorer - External APIs (For LLMs)",
    "x-llm-instructions": {
      "usage": "Extract x-external-url from each endpoint to call the real API",
      "example": "GET https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd",
      "note": "All URLs in x-external-url are real public APIs you can call directly"
    }
  }
}
```

---

## 🚀 How LLMs Should Use This

### Example Python Code for AI Agents:

```python
import requests

# Step 1: Get the LLM-optimized spec
spec = requests.get('http://127.0.0.1:8003/openapi-llm.json').json()

# Step 2: Extract external URLs from endpoints
for path, methods in spec['paths'].items():
    for method, operation in methods.items():
        external_url = operation.get('x-external-url')
        if external_url:
            print(f"Endpoint: {path}")
            print(f"Real API: {external_url}")
            
            # Step 3: Call the real API directly
            response = requests.get(external_url, params={'vs_currency': 'usd', 'per_page': 10})
            data = response.json()
            print(f"Got {len(data)} results\n")
```

### Example for ChatGPT/Claude:

1. Copy the prompt from `http://127.0.0.1:8003/llm-prompt.txt`
2. Paste it into your LLM conversation
3. The LLM now knows all available APIs and their direct URLs
4. Ask it to make API calls using the real URLs

---

## ✅ What's Implemented

- [x] Server dropdown in Swagger UI for direct API calls
- [x] `/api-urls` endpoint listing all API base URLs
- [x] `/llm-prompt.txt` with copy-paste instructions for LLMs
- [x] `/openapi.json` with `x-external-url` extensions
- [x] `/openapi-external.json` with LLM metadata
- [x] `/openapi-llm.json` simplified for AI consumption
- [x] All crypto endpoints have `x-external-url` extensions
- [x] Response headers include `x-api-url` showing real API URL

---

## 📝 Next Steps (Optional)

To make all endpoints LLM-friendly, add `openapi_extra` to other route files:

```python
@router.get("/weather/forecast",
            openapi_extra={
                "x-external-url": "https://api.open-meteo.com/v1/forecast",
                "x-api-provider": "Open-Meteo"
            })
async def get_weather(...):
    ...
```

This makes it easy for any LLM or AI agent to:
1. Discover available APIs
2. Understand what each endpoint does
3. Extract the real external API URL
4. Call the API directly without going through your proxy
