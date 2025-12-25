from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register_user(phone: str, role: str):
    return {"phone": phone, "role": role, "status": "registered"}
