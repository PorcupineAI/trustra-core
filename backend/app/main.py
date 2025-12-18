from fastapi import FastAPI
from .webhook import router as webhook

app = FastAPI(title="Trustra NG")

# Root endpoint (IMPORTANT)
@app.get("/")
def root():
    return {
        "status": "Trustra NG Live",
        "service": "WhatsApp Trust & Escrow API"
    }

# Webhook
app.include_router(webhook)
