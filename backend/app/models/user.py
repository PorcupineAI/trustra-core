from sqlalchemy import Column, String, Boolean, Integer
from app.database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    trust_score = Column(Integer, default=50)
    verification_status = Column(Boolean, default=False)
