from fastapi import FastAPI
from app.routes import users, escrow, webhook

app = FastAPI(title="Trustra NG")

app.include_router(users)
app.include_router(escrow)
app.include_router(webhook)

@app.get("/")
def health():
    return {"status": "Trustra backend running"}
