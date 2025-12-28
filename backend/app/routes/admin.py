from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.escrow import Escrow
from app.models.revenue import Revenue

router = APIRouter(prefix="/admin")

@router.get("/metrics")
def metrics(db: Session = Depends(get_db)):
    return {
        "escrows": db.query(Escrow).count(),
        "revenue": db.query(Revenue).count(),
    }


