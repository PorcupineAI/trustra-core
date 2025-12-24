from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    phone = Column(String, unique=True, index=True)
    role = Column(String)  # buyer | seller
    verified = Column(Boolean, default=False)
    trust_score = Column(Integer, default=50)
