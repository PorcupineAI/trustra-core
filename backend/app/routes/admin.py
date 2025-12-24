from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def admin_dashboard():
    return {
        "status": "healthy",
        "message": "Trustra-NG Autonomous Core Running"
    }

