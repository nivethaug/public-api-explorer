""" Stocks Routes - Documentation for stock market public APIs """
from fastapi import APIRouter, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client

router = APIRouter(prefix="/stocks", tags=["Stocks"])
http_client = get_http_client()

@router.get("/crypto/list", summary="List crypto stocks")
async def list_crypto_stocks():
    try:
        real_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc"
        response = await http_client.get(real_url)
        response.raise_for_status()
        return JSONResponse(content=response.json(), headers={"x-api-url": real_url, "x-api-provider": "CoinGecko"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"CoinGecko API error: {str(e)}")

@router.get("/crypto/{symbol}", summary="Get crypto stock price")
async def get_crypto_stock(symbol: str = Path(..., description="Crypto symbol (e.g., bitcoin)")):
    try:
        real_url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart"
        response = await http_client.get(real_url)
        response.raise_for_status()
        return JSONResponse(content=response.json(), headers={"x-api-url": real_url, "x-api-provider": "CoinGecko"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"CoinGecko API error: {str(e)}")

@router.get("/trending", summary="Get trending cryptos")
async def get_trending_cryptos():
    try:
        real_url = "https://api.coingecko.com/api/v3/search/trending"
        response = await http_client.get(real_url)
        response.raise_for_status()
        return JSONResponse(content=response.json(), headers={"x-api-url": real_url, "x-api-provider": "CoinGecko"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"CoinGecko API error: {str(e)}")
