# backend/app/models/user.py
from sqlalchemy import Column, Integer, String
from app.services.constraints import Base, UserConstraints

class User(Base, UserConstraints):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(String(20), nullable=False)
    name = Column(String(100), nullable=True)

# backend/app/models/escrow.py
from sqlalchemy import Column, Integer, Float, ForeignKey
from app.services.constraints import Base, EscrowConstraints

class Escrow(Base, EscrowConstraints):
    __tablename__ = 'escrow'
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

# backend/app/models/revenue.py
from sqlalchemy import Column, Integer, Float
from app.services.constraints import Base, RevenueConstraints

class Revenue(Base, RevenueConstraints):
    __tablename__ = 'revenue'
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)

# backend/app/models/playing_with_neon.py
from sqlalchemy import Column, Integer, Float
from app.services.constraints import Base, NeonScoreConstraints

class PlayingWithNeon(Base, NeonScoreConstraints):
    __tablename__ = 'playing_with_neon'
    id = Column(Integer, primary_key=True, autoincrement=True)
    score = Column(Float, default=0)
