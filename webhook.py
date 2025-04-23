# main.py
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/ebay-webhook")
async def handle_ebay_webhook(request: Request):
    body = await request.json()
    print("Received eBay event:", body)
    return {"status": "ok"}
