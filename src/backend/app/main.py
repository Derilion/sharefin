#! /usr/bin/env python3

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World!"}

def debug():
    main()

def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == '__main__':
    debug()
