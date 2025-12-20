# app.py - Complete WhatsApp webhook handler
from fastapi import FastAPI, Request, HTTPException, Header
import hmac
import hashlib
import json
from typing import Optional

app = FastAPI()
WEBHOOK_SECRET = "your-verify-token-here"  # Set in WhatsApp Manager

# 1️⃣ VERIFICATION ENDPOINT (GET request from Meta)
@app.get("/webhook")
async def verify_webhook(
    hub_mode: Optional[str] = None,
    hub_challenge: Optional[str] = None,
    hub_verify_token: Optional[str] = None
):
    """
    Meta sends GET request to verify your webhook
    MUST return hub.challenge exactly as received
    """
    if hub_mode == "subscribe" and hub_verify_token == WEBHOOK_SECRET:
        return int(hub_challenge)  # Return as integer!
    raise HTTPException(status_code=403, detail="Verification failed")

# 2️⃣ MESSAGE HANDLING ENDPOINT (POST request from Meta)
@app.post("/webhook")
async def handle_messages(
    request: Request,
    x_hub_signature_256: Optional[str] = Header(None)
):
    """
    Handles all incoming WhatsApp messages and status updates
    """
    body_bytes = await request.body()
    
    # Verify signature for security
    if not verify_signature(body_bytes, x_hub_signature_256):
        raise HTTPException(status_code=401, detail="Invalid signature")
    
    data = json.loads(body_bytes.decode('utf-8'))
    
    # Process different webhook types
    for entry in data.get("entry", []):
        for change in entry.get("changes", []):
            field = change.get("field")
            value = change.get("value")
            
            if field == "messages":
                await handle_incoming_message(value)
            elif field == "message_template_status_update":
                await handle_template_status(value)
    
    return {"status": "ok"}

# 3️⃣ INCOMING MESSAGE HANDLER
async def handle_incoming_message(message_data: dict):
    """
    Processes messages from users
    """
    contacts = message_data.get("contacts", [])
    messages = message_data.get("messages", [])
    
    for contact in contacts:
        wa_id = contact.get("wa_id")  # User's phone number: 2348153411414
        profile_name = contact.get("profile", {}).get("name")
        
        for message in messages:
            message_id = message.get("id")
            message_type = message.get("type")
            timestamp = message.get("timestamp")
            
            if message_type == "text":
                text_body = message.get("text", {}).get("body")
                print(f"📩 Text from {wa_id}: {text_body}")
                await send_response(wa_id, f"You said: {text_body}")
                
            elif message_type == "interactive":
                # Handle button clicks, list replies
                interactive_data = message.get("interactive", {})
                print(f"🔘 Interactive from {wa_id}: {interactive_data}")

# 4️⃣ SIGNATURE VERIFICATION
def verify_signature(payload: bytes, signature: str) -> bool:
    """
    Verifies webhook signature using HMAC SHA256
    """
    if not signature:
        return False
    
    # Signature format: "sha256=XXXXX"
    expected_signature = "sha256=" + hmac.new(
        WEBHOOK_SECRET.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(expected_signature, signature)
