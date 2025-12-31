# backend/app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.user import User
from app.models.escrow import Escrow
from app.models.revenue import Revenue
from app.models.playing_with_neon import PlayingWithNeon

DATABASE_URL = "postgresql://username:password@<your_neon_host>:5432/trustra_ng"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables with constraints
def init_db():
    User.metadata.create_all(bind=engine)
    Escrow.metadata.create_all(bind=engine)
    Revenue.metadata.create_all(bind=engine)
    PlayingWithNeon.metadata.create_all(bind=engine)
