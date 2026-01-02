from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import QueuePool
from app.config import settings
import ssl

# Handle SSL for Render PostgreSQL
def create_database_engine():
    db_url = settings.DATABASE_URL
    
    # For Render PostgreSQL with SSL
    if "render.com" in db_url:
        # Create SSL context
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        
        engine = create_engine(
            db_url,
            poolclass=QueuePool,
            pool_size=5,
            max_overflow=10,
            pool_pre_ping=True,
            connect_args={
                "ssl": ssl_context,
                "connect_timeout": 10
            },
            echo=False,  # Set to True for debugging
            future=True,
        )
    else:
        # Local development
        engine = create_engine(
            db_url,
            poolclass=QueuePool,
            pool_size=5,
            max_overflow=10,
            pool_pre_ping=True,
            echo=False,
            future=True,
        )
    
    return engine

engine = create_database_engine()
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
