from fastapi import FastAPI
from app.routes.users import router as users_router
from app.routes.escrow import router as escrow_router
from app.routes.webhook import router as webhook_router
from app.legal.terms import router as terms_router
from app.legal.privacy import router as privacy_router

app = FastAPI(title="Trustra-NG API", version="1.0.0")

@app.get("/")
def root():
    return {"status": "Trustra-NG backend running"}

app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(escrow_router, prefix="/escrow", tags=["Escrow"])
app.include_router(webhook_router, prefix="/webhook", tags=["Webhook"])
app.include_router(terms_router, prefix="/legal", tags=["Legal"])
app.include_router(privacy_router, prefix="/legal", tags=["Legal"])
