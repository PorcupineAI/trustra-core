from fastapi import APIRouter

router = APIRouter()

@router.post("/open")
def open_dispute(escrow_id: int):
    return {
        "status": "opened",
        "resolution_fee": "₦2,000 if manual review"
    }
