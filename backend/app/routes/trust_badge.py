from fastapi import APIRouter, HTTPException
from app.database import get_db
from app.models.user import User

router = APIRouter(prefix="/trust")

@router.get("/{username}")
def trust_badge(username: str, db=Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404)

    return {
        "verified": user.trust_score >= 70,
        "trust_score": user.trust_score,
        "issued_by": "Trustra Digital Protocol Ltd"
    }
