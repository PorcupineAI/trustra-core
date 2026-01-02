from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

class RiskLog(Base):
    __tablename__ = "risk_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_phone = Column(String, index=True)
    reason = Column(String)
    score = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
