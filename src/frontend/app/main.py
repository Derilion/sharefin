#/usr/bin/env python3

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import httpx

# Backend configuration
BACKEND_HOST = "127.0.0.1"
BACKEND_PORT = 8000
BACKEND_URL = f"http://{BACKEND_HOST}:{BACKEND_PORT}"


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def landing_page(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BACKEND_URL}/expense/")
        expenses = response.json()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "ShareFin",
            "message": "Welcome to ShareFin",
            "expenses": expenses
        }
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)
