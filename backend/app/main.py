from fastapi import FastAPI
from app.database import engine, Base
from app.models import user, escrow, revenue

app = FastAPI(title="Trustra-NG API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "Trustra-NG backend running"}
