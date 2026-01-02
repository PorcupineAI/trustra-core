from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import users, escrow, webhook, auth, admin, dispute, whatsapp

app = FastAPI(title="Trustra NG")

# Add CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users)
app.include_router(escrow)
app.include_router(webhook)
app.include_router(auth)
app.include_router(admin)
app.include_router(dispute)
app.include_router(whatsapp)

@app.get("/")
def health():
    return {"status": "Trustra backend running"}

@app.get("/api/health")
def api_health():
    return {"status": "healthy", "service": "Trustra NG"}

# Add catch-all for frontend routing in production
@app.get("/api/{path:path}")
def catch_all(path: str):
    return {"error": f"API endpoint /api/{path} not found"}
