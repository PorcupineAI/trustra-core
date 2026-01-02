#!/usr/bin/env python3
"""
Database migration script for Render.
Run this before starting the application.
"""
import os
import sys
from alembic.config import Config
from alembic import command

def run_migrations():
    """Run database migrations."""
    # Get the absolute path to alembic.ini
    alembic_ini_path = os.path.join(os.path.dirname(__file__), 'alembic.ini')
    
    # Create Alembic config
    alembic_cfg = Config(alembic_ini_path)
    
    print("Running database migrations...")
    try:
        # Stamp head (if needed)
        command.stamp(alembic_cfg, "head")
        
        # Run migrations
        command.upgrade(alembic_cfg, "head")
        print("✅ Database migrations completed successfully!")
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_migrations()
