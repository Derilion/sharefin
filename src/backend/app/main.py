#! /usr/bin/env python3

from fastapi import FastAPI
from app.routers.expense import router as expenses_router
import uvicorn

app = FastAPI()
app.include_router(expenses_router)
@app.get("/")
def index():
    return {"message": "Hello World!"}

def debug():
    main()

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == '__main__':
    debug()
