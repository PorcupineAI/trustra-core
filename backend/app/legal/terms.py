from fastapi import APIRouter

router = APIRouter()

@router.get("/terms")
def terms():
    return {"terms": "Trustra-NG provides escrow coordination only."}
