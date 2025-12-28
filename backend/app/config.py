import os

NEON_DB_URL = os.getenv("NEON_DB_URL", "postgresql://username:password@host:port/dbname")
PAYSTACK_SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
