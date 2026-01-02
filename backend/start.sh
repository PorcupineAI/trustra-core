#!/bin/bash
# Wait for database to be ready
echo "Starting Trustra NG backend..."
python -m app.database.init_db
uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-10000}
