from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register_user(phone: str, name: str = "", db: Session = Depends(get_db)):
    user = User(phone=phone, name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {
        "id": user.id,
        "phone": user.phone,
        "name": user.name
    }
