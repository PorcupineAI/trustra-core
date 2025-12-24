import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./trustra.db")
PAYSTACK_SECRET = os.getenv("PAYSTACK_SECRET")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "trustra_verify")
BASE_URL = os.getenv("BASE_URL")
