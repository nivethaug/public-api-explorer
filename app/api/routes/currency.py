""" Currency Routes - Documentation for currency and exchange rate public APIs """
from fastapi import APIRouter, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client

router = APIRouter(prefix="/currency", tags=["Currency"])
http_client = get_http_client()

@router.get("/frankfurter/latest", summary="Get latest exchange rates")
async def get_latest_rates(base: str = Query("USD", description="Base currency")):
    try:
        real_url = f"https://api.frankfurter.app/latest?from={base}"
        response = await http_client.get(real_url)
        response.raise_for_status()
        return JSONResponse(content=response.json(), headers={"x-api-url": real_url, "x-api-provider": "Frankfurter"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Frankfurter API error: {str(e)}")

@router.get("/frankfurter/{date}", summary="Get historical exchange rates")
async def get_historical_rates(date: str = Path(..., description="Date (YYYY-MM-DD)"), base: str = Query("USD", description="Base currency")):
    try:
        real_url = f"https://api.frankfurter.app/{date}?from={base}"
        response = await http_client.get(real_url)
        response.raise_for_status()
        return JSONResponse(content=response.json(), headers={"x-api-url": real_url, "x-api-provider": "Frankfurter"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Frankfurter API error: {str(e)}")

@router.get("/convert", summary="Convert currency")
async def convert_currency(amount: float = Query(..., ge=0.01, description="Amount to convert"), from_currency: str = Query(..., description="Source currency"), to_currency: str = Query(..., description="Target currency")):
    try:
        real_url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
        response = await http_client.get(real_url)
        response.raise_for_status()
        return JSONResponse(content=response.json(), headers={"x-api-url": real_url, "x-api-provider": "Frankfurter"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Currency conversion error: {str(e)}")
