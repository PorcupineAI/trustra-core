from sqlalchemy import Column, Integer, Numeric, String, DateTime, func
from app.database import Base

class Revenue(Base):
    __tablename__ = "revenue"

    id = Column(Integer, primary_key=True)
    source = Column(String, nullable=False)  # escrow, verification
    amount = Column(Numeric, nullable=False)
    reference = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())

