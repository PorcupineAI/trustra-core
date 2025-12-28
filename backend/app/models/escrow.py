from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from app.database import Base

class Escrow(Base):
    __tablename__ = "escrows"

    id = Column(Integer, primary_key=True)
    buyer = Column(String)
    seller = Column(String)
    amount = Column(Float)
    status = Column(String, default="held")
    created_at = Column(DateTime, default=datetime.utcnow)
