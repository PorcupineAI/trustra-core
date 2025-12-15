from fastapi import FastAPI
from app.webhook import router as webhook_router

app = FastAPI(title="TRUSTRA Core API")

@app.get("/")
def root():
    return {"status": "TRUSTRA backend running"}

app.include_router(webhook_router)
