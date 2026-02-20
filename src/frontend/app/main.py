#/usr/bin/env python3

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
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

@app.post("/expense")
async def create_expense(
    amount: float = Form(...),
    date: str = Form(...),
    description: str = Form(...),
    paid_by_id: int = Form(...),
    splits: str = Form(...)
):
    split_ids = [int(s.strip()) for s in splits.split(",")]
    payload = {
        "amount": amount,
        "date": date,
        "description": description,
        "paid_by_id": paid_by_id,
        "splits": [{"person_id": pid} for pid in split_ids]
    }

    async with httpx.AsyncClient() as client:
        await client.post(f"{BACKEND_URL}/expense/", json=payload)

    return RedirectResponse(url="/", status_code=303)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)
