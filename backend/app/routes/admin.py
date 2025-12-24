from fastapi import APIRouter, Depends
from app.database import db

router = APIRouter(prefix="/admin")

@router.get("/stats")
def stats():
    return {
        "sellers": db.count("sellers"),
        "buyers": db.count("buyers"),
        "escrows": db.count("escrows"),
        "revenue": db.sum("revenue")
    }
