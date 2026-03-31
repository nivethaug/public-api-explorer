# Quick Start: Direct API Access

## 🎯 TL;DR

**For direct API execution in Swagger UI, use these URLs:**

| API | Swagger UI URL | OpenAPI Spec |
|-----|---------------|--------------|
| **CoinGecko** | http://127.0.0.1:8003/external/coingecko/docs | http://127.0.0.1:8003/external/coingecko/openapi.json |
| **CoinCap** | http://127.0.0.1:8003/external/coincap/docs | http://127.0.0.1:8003/external/coincap/openapi.json |
| **Frankfurter** | http://127.0.0.1:8003/external/frankfurter/docs | http://127.0.0.1:8003/external/frankfurter/openapi.json |
| **Open-Meteo** | http://127.0.0.1:8003/external/openmeteo/docs | http://127.0.0.1:8003/external/openmeteo/openapi.json |
| **HackerNews** | http://127.0.0.1:8003/external/hackernews/docs | http://127.0.0.1:8003/external/hackernews/openapi.json |

## ✅ How to Use

1. Open `http://127.0.0.1:8003/external/coingecko/docs`
2. Click **GET /coins/markets**
3. Click **"Try it out"**
4. Click **"Execute"**
5. ✅ **It calls the real CoinGecko API directly!**

## ❌ What NOT to Do

Don't use the server dropdown in the main Swagger UI (`http://127.0.0.1:8003/docs`) for direct execution - the paths won't match!

---

## 🔗 List All Available APIs

**Endpoint:** `http://127.0.0.1:8003/external-apis`

Returns JSON with all external API Swagger UI URLs and their base URLs.

---

## 🤖 For LLMs and AI Agents

**Option 1:** Use the `/api-urls` endpoint
```python
import requests

# Get all API base URLs
apis = requests.get('http://127.0.0.1:8003/api-urls').json()['apis']

# Call CoinGecko directly
response = requests.get(
    f"{apis['coingecko']}/coins/markets",
    params={'vs_currency': 'usd'}
)
```

**Option 2:** Extract `x-external-url` from OpenAPI spec
```python
# Get the LLM-optimized spec
spec = requests.get('http://127.0.0.1:8003/openapi-llm.json').json()

# Extract external URL
external_url = spec['paths']['/finance/crypto/coingecko/coins']['get']['x-external-url']

# Call directly
response = requests.get(external_url, params={'vs_currency': 'usd'})
```

**Option 3:** Copy-paste the LLM prompt
- Visit `http://127.0.0.1:8003/llm-prompt.txt`
- Copy the text
- Paste into ChatGPT, Claude, or any LLM

---

## 📖 Full Documentation

See `LLM_INTEGRATION.md` for complete details on all integration methods.
