from fastapi import FastAPI
from app.routes import users, escrow, webhook

app = FastAPI(title="Trustra NG API")

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(escrow.router, prefix="/escrow", tags=["Escrow"])
app.include_router(webhook.router, prefix="/webhook", tags=["Webhook"])


@app.get("/")
def root():
    return {"status": "Trustra NG backend running"}
