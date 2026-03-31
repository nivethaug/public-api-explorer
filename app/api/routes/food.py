""" Food Routes - Documentation for food and recipe public APIs """
from fastapi import APIRouter, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from app.core.http_client import get_http_client

router = APIRouter(prefix="/food", tags=["Food"])
http_client = get_http_client()

@router.get("/meals/search", summary="Search meals by ingredient")
async def search_meals(ingredient: str = Query(..., description="Main ingredient")):
    try:
        real_url = f"https://www.themealdb.com/api/json/v1/filter.php?i={ingredient}"
        response = await http_client.get(real_url)
        response.raise_for_status()
        return JSONResponse(content=response.json(), headers={"x-api-url": real_url, "x-api-provider": "TheMealDB"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TheMealDB API error: {str(e)}")

@router.get("/meals/{meal_id}", summary="Get meal details by ID")
async def get_meal_details(meal_id: str = Path(..., description="Meal ID")):
    try:
        real_url = f"https://www.themealdb.com/api/json/v1/lookup.php?i={meal_id}"
        response = await http_client.get(real_url)
        response.raise_for_status()
        return JSONResponse(content=response.json(), headers={"x-api-url": real_url, "x-api-provider": "TheMealDB"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TheMealDB API error: {str(e)}")

@router.get("/meals/random", summary="Get random meal")
async def get_random_meal():
    try:
        real_url = "https://www.themealdb.com/api/json/v1/random.php"
        response = await http_client.get(real_url)
        response.raise_for_status()
        return JSONResponse(content=response.json(), headers={"x-api-url": real_url, "x-api-provider": "TheMealDB"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TheMealDB API error: {str(e)}")

@router.get("/cocktails/search", summary="Search cocktails by ingredient")
async def search_cocktails(ingredient: str = Query(..., description="Ingredient name")):
    try:
        real_url = f"https://www.thecocktaildb.com/api/json/v1/filter.php?i={ingredient}"
        response = await http_client.get(real_url)
        response.raise_for_status()
        return JSONResponse(content=response.json(), headers={"x-api-url": real_url, "x-api-provider": "TheCocktailDB"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TheCocktailDB API error: {str(e)}")

@router.get("/cocktails/{cocktail_id}", summary="Get cocktail details by ID")
async def get_cocktail_details(cocktail_id: str = Path(..., description="Cocktail ID")):
    try:
        real_url = f"https://www.thecocktaildb.com/api/json/v1/lookup.php?i={cocktail_id}"
        response = await http_client.get(real_url)
        response.raise_for_status()
        return JSONResponse(content=response.json(), headers={"x-api-url": real_url, "x-api-provider": "TheCocktailDB"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TheCocktailDB API error: {str(e)}")

@router.get("/breweries/search", summary="Search breweries")
async def search_breweries(query: str = Query(..., description="Search query (city, name, or state)")):
    try:
        real_url = "https://api.openbrewerydb.org/breweries"
        response = await http_client.get(real_url, params={"by_city": query})
        response.raise_for_status()
        return JSONResponse(content=response.json(), headers={"x-api-url": f"{real_url}?by_city={query}", "x-api-provider": "Open Brewery DB"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Open Brewery DB error: {str(e)}")

@router.get("/breweries/{brewery_id}", summary="Get brewery details by ID")
async def get_brewery_details(brewery_id: str = Path(..., description="Brewery ID")):
    try:
        real_url = f"https://api.openbrewerydb.org/breweries/{brewery_id}"
        response = await http_client.get(real_url)
        response.raise_for_status()
        return JSONResponse(content=response.json(), headers={"x-api-url": real_url, "x-api-provider": "Open Brewery DB"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Open Brewery DB error: {str(e)}")

@router.get("/breweries/random", summary="Get random brewery")
async def get_random_brewery():
    try:
        real_url = "https://api.openbrewerydb.org/breweries/random"
        response = await http_client.get(real_url)
        response.raise_for_status()
        return JSONResponse(content=response.json(), headers={"x-api-url": real_url, "x-api-provider": "Open Brewery DB"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Open Brewery DB error: {str(e)}")
