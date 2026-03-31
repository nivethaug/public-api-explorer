# API Routes

This directory contains all API route modules organized by category.

## Current Categories

| Module | Prefix | Description |
|--------|--------|-------------|
| `health.py` | `/` | Health check and system status |
| `finance_crypto.py` | `/finance` | Cryptocurrency and financial data |
| `weather.py` | `/weather` | Weather forecasts and alerts |
| `news.py` | `/news` | News and stories (HackerNews) |
| `location.py` | `/location` | Geocoding, IP location, countries |

## Adding a New Category

1. **Copy the template**:
   ```bash
   cp category_template.py your_category.py
   ```

2. **Edit the file**:
   - Change `prefix="/category-name"` to your desired path
   - Change `tags=["Category Name"]` to your category
   - Add your endpoints

3. **Register the router** in `__init__.py`:
   ```python
   from app.api.routes.your_category import router as your_category_router
   
   ALL_ROUTERS = [
       # ... existing routers
       your_category_router,
   ]
   ```

4. **Test your endpoints**:
   - Start the server: `python run.py`
   - Visit `/docs` to test interactively

## Endpoint Best Practices

1. **Use descriptive names**: `get_crypto_prices` not `get_data`
2. **Add summaries**: Brief one-liner for each endpoint
3. **Add descriptions**: Detailed docstrings with parameter explanations
4. **Handle errors**: Wrap API calls in try/except blocks
5. **Validate inputs**: Use Query/Path with validation constraints
6. **Document parameters**: Add description to every Query/Path parameter

## Example Categories to Add

Future categories that could be implemented:
- Entertainment (movies, music, games)
- Sports (scores, schedules, standings)
- AI/NLP (text analysis, sentiment, translation)
- Travel (flights, hotels, points of interest)
- Food (recipes, restaurants, nutrition)
- Jobs (job listings, companies)
- Images (photos, memes, avatars)
- Science (NASA, space, research)
- Security (breaches, vulnerabilities)
- Utilities (QR codes, color palettes, timezone)
