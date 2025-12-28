from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.models.escrow import Escrow

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/stats")
def platform_stats():
    db: Session = SessionLocal()
    return {
        "users": db.query(User).count(),
        "escrows": db.query(Escrow).count()
    }

@router.get("/users")
def all_users():
    db: Session = SessionLocal()
    return db.query(User).all()

@router.get("/escrows")
def all_escrows():
    db: Session = SessionLocal()
    return db.query(Escrow).all()
