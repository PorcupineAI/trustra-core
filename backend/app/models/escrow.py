from sqlalchemy import Column, Integer, Float, String, ForeignKey, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Escrow(Base):
    __tablename__ = "escrow"

    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer)
    seller_id = Column(Integer)
    amount = Column(Float)
    status = Column(String, default="pending")
    fee = Column(Float, default=0.0)
    is_disputed = Column(Boolean, default=False)
    requires_admin = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
