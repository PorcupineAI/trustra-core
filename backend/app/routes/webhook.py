from fastapi import APIRouter, Request
from app.config import VERIFY_TOKEN

router = APIRouter()

@router.get("/whatsapp")
def verify(request: Request):
    q = request.query_params
    if q.get("hub.verify_token") == VERIFY_TOKEN:
        return int(q.get("hub.challenge"))
    return {"error": "verification failed"}
