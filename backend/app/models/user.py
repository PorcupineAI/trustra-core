from sqlalchemy import Column, String, Integer, Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
    role = Column(String)  # buyer / seller
    trust_score = Column(Integer, default=50)
    verified = Column(Boolean, default=False)
    trust_badge = Column(String, default="basic")
