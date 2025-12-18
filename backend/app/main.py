from fastapi import FastAPI
from app.webhook import router as webhook
from app.admin import router as admin

app = FastAPI(title="Trustra NG")

app.include_router(webhook)
app.include_router(admin)

@app.get("/")
def health():
    return {"status": "Trustra NG Live"}
