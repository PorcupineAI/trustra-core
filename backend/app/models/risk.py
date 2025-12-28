from sqlalchemy import Column, Integer, String
from app.database import Base

class RiskLog(Base):
    __tablename__ = "risk_logs"

    id = Column(Integer, primary_key=True)
    user_phone = Column(String)
    reason = Column(String)
    score = Column(Integer)
