from sqlalchemy import Column, Integer, Float, String
from app.database import Base

class Revenue(Base):
    __tablename__ = "revenue"

    id = Column(Integer, primary_key=True)
    source = Column(String)
    amount = Column(Float)
