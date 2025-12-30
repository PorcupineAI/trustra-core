from sqlalchemy import Column, Integer, Numeric, String, DateTime, func
from app.database import Base

class Escrow(Base):
    __tablename__ = "escrow"

    id = Column(Integer, primary_key=True)
    buyer_id = Column(Integer, nullable=False)
    seller_id = Column(Integer, nullable=False)
    amount = Column(Numeric, nullable=False)
    status = Column(String, default="HELD")  
    created_at = Column(DateTime, server_default=func.now())
