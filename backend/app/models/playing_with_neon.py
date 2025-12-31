from sqlalchemy import Column, Integer, Float
from app.services.constraints import NeonScoreConstraints
from app.database import Base

class PlayingWithNeon(Base, NeonScoreConstraints):
    __tablename__ = 'playing_with_neon'
    id = Column(Integer, primary_key=True, autoincrement=True)
    score = Column(Float, default=0)
