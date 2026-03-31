"""
Finance & Crypto Routes
Documentation for cryptocurrency and financial public APIs

These endpoints demonstrate how to use the real public APIs.
LLMs should use the actual API URLs shown in the documentation.
"""

from fastapi import APIRouter, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client

router = APIRouter(prefix="/finance", tags=["Finance & Crypto"])
http_client = get_http_client()

# Real API URLs for LLM reference
REAL_API_URLS = {
    "coingecko": "https://api.coingecko.com/api/v3",
    "coincap": "https://api.coincap.io/v2",
    "binance": "https://api.binance.com/api/v3",
    "coinbase": "https://api.coinbase.com/v2",
    "exchangerate": "https://api.exchangerate-api.com/v4"
}


# ==================== CRYPTOCURRENCY ====================

@router.get("/crypto/coingecko/coins", 
            summary="List cryptocurrencies from CoinGecko",
            openapi_extra={
                "x-external-url": "https://api.coingecko.com/api/v3/coins/markets",
                "x-api-provider": "CoinGecko",
                "x-direct-call": {
                    "url": "https://api.coingecko.com/api/v3/coins/markets",
                    "method": "GET",
                    "auth_required": False,
                    "example": "curl 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=50&page=1'"
                }
            })
async def get_coingecko_coins(
    vs_currency: str = Query("usd", description="Currency to compare against"),
    per_page: int = Query(50, ge=1, le=250, description="Results per page"),
    page: int = Query(1, ge=1, description="Page number")
):
    """
    Get list of cryptocurrencies with market data from CoinGecko
    
    **Real API URL:** `https://api.coingecko.com/api/v3/coins/markets`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets',
        params={'vs_currency': 'usd', 'per_page': 50, 'page': 1}
    )
    data = response.json()
    ```
    
    **Parameters:**
    - `vs_currency`: Currency (usd, eur, btc, etc.)
    - `per_page`: Results per page (1-250)
    - `page`: Page number
    
    **No authentication required**
    """
    try:
        real_url = "https://api.coingecko.com/api/v3/coins/markets"
        response = await http_client.get(
            real_url,
            params={
                "vs_currency": vs_currency,
                "order": "market_cap_desc",
                "per_page": per_page,
                "page": page,
                "sparkline": "false"
            }
        )
        response.raise_for_status()
        
        # Return with real API URL header
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "CoinGecko"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"CoinGecko API error: {str(e)}")


@router.get("/crypto/coingecko/coin/{coin_id}",
            summary="Get specific cryptocurrency details",
            openapi_extra={
                "x-external-url": "https://api.coingecko.com/api/v3/coins/{coin_id}",
                "x-api-provider": "CoinGecko",
                "x-direct-call": {
                    "url": "https://api.coingecko.com/api/v3/coins/{coin_id}",
                    "method": "GET",
                    "auth_required": False
                }
            })
async def get_coingecko_coin(
    coin_id: str = Path(..., description="Coin ID (e.g., bitcoin, ethereum)"),
    vs_currency: str = Query("usd", description="Currency to compare against")
):
    """
    Get detailed information about a specific cryptocurrency
    
    **Real API URL:** `https://api.coingecko.com/api/v3/coins/{coin_id}`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    coin_id = 'bitcoin'
    response = requests.get(f'https://api.coingecko.com/api/v3/coins/{coin_id}')
    data = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
        response = await http_client.get(
            real_url,
            params={"localization": "false", "tickers": "false", "market_data": "true"}
        )
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "CoinGecko"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"CoinGecko API error: {str(e)}")


@router.get("/crypto/coincap/assets",
            summary="List crypto assets from CoinCap",
            openapi_extra={
                "x-external-url": "https://api.coincap.io/v2/assets",
                "x-api-provider": "CoinCap",
                "x-direct-call": {
                    "url": "https://api.coincap.io/v2/assets",
                    "method": "GET",
                    "auth_required": False
                }
            })
async def get_coincap_assets(
    limit: int = Query(50, ge=1, le=2000, description="Number of results"),
    search: str = Query(None, description="Search by asset ID or symbol")
):
    """
    Get list of crypto assets from CoinCap
    
    **Real API URL:** `https://api.coincap.io/v2/assets`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get(
        'https://api.coincap.io/v2/assets',
        params={'limit': 50, 'search': 'bitcoin'}
    )
    data = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://api.coincap.io/v2/assets"
        params = {"limit": limit}
        if search:
            params["search"] = search
        
        response = await http_client.get(real_url, params=params)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "CoinCap"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"CoinCap API error: {str(e)}")


@router.get("/crypto/binance/ticker/24hr",
            summary="Get 24hr ticker statistics from Binance",
            openapi_extra={
                "x-external-url": "https://api.binance.com/api/v3/ticker/24hr",
                "x-api-provider": "Binance",
                "x-direct-call": {
                    "url": "https://api.binance.com/api/v3/ticker/24hr",
                    "method": "GET",
                    "auth_required": False
                }
            })
async def get_binance_ticker(
    symbol: str = Query(None, description="Trading pair symbol (e.g., BTCUSDT)")
):
    """
    Get 24-hour price change statistics from Binance
    
    **Real API URL:** `https://api.binance.com/api/v3/ticker/24hr`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT')
    data = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = "https://api.binance.com/api/v3/ticker/24hr"
        if symbol:
            real_url += f"?symbol={symbol.upper()}"
        
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Binance"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Binance API error: {str(e)}")


@router.get("/crypto/coinbase/prices",
            summary="Get buy/sell prices from Coinbase")
async def get_coinbase_prices(
    currency_pair: str = Query("BTC-USD", description="Currency pair (e.g., BTC-USD)")
):
    """
    Get buy/sell prices for cryptocurrency from Coinbase
    
    **Real API URL:** `https://api.coinbase.com/v2/prices/{currency_pair}/spot`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/spot')
    data = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = f"https://api.coinbase.com/v2/prices/{currency_pair}/spot"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "Coinbase"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Coinbase API error: {str(e)}")


# ==================== EXCHANGE RATES ====================

@router.get("/exchange-rate/{base}",
            summary="Get exchange rates")
async def get_exchange_rates(
    base: str = Path(..., description="Base currency code (e.g., USD, EUR)")
):
    """
    Get latest exchange rates for a base currency
    
    **Real API URL:** `https://api.exchangerate-api.com/v4/latest/{base}`
    
    **Direct Usage Example:**
    ```python
    import requests
    
    # Call the real API directly
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    ```
    
    **No authentication required**
    """
    try:
        real_url = f"https://api.exchangerate-api.com/v4/latest/{base.upper()}"
        response = await http_client.get(real_url)
        response.raise_for_status()
        
        return JSONResponse(
            content=response.json(),
            headers={"x-api-url": real_url, "x-api-provider": "ExchangeRate-API"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"ExchangeRate API error: {str(e)}")
