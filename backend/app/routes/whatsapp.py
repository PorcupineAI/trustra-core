from fastapi import APIRouter, Request
from app.services.escrow_service import create_escrow
from app.services.trust_score import get_trust_score

router = APIRouter(prefix="/whatsapp")

@router.post("/webhook")
async def whatsapp_webhook(req: Request):
    data = await req.json()
    message = data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
    sender = data["entry"][0]["changes"][0]["value"]["messages"][0]["from"]

    if message.lower().startswith("escrow"):
        amount = int(message.split()[1])
        escrow = create_escrow(sender, amount)
        return {"reply": f"Escrow created. ID: {escrow.id}"}

    if message.lower() == "trust":
        score = get_trust_score(sender)
        return {"reply": f"Your Trust Score is {score}"}

    return {"reply": "Send: escrow <amount> or trust"}
