from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import init_db
from app.routes import users, escrow, webhook

app = FastAPI(title="Trustra-NG API")

# ✅ CORS CONFIG
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace with Vercel domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Init DB
init_db()

# Register routes
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(escrow.router, prefix="/api/escrow", tags=["Escrow"])
app.include_router(webhook.router, prefix="/api/webhook", tags=["Webhook"])

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "Trustra-NG"}
