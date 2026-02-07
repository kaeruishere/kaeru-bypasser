from fastapi import FastAPI, HTTPException
import requests
from bs4 import BeautifulSoup
import re

app = FastAPI(title="Kaeru Bypasser API")

@app.get("/")
def home():
    return {"status": "online", "message": "Kaeru Bypasser is hopping!"}

@app.get("/bypass")
def bypass(url: str):
    if not url:
        raise HTTPException(status_code=400, detail="URL is required")
    
    # Simple logic for Ouo.io (example, needs full implementation)
    if "ouo.io" in url or "ouo.press" in url:
        # This is a placeholder for real bypass logic
        # Real bypassers usually require handling cookies/tokens or using external APIs
        return {"original_url": url, "bypassed_url": "Coming soon (Ouo logic is complex)", "type": "ouo"}
    
    # Generic redirect checker
    try:
        response = requests.get(url, allow_redirects=True, timeout=10)
        return {"original_url": url, "bypassed_url": response.url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
