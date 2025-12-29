# backend/app/services/monetization.py

ESCROW_FEE_PERCENT = 0.02   # 2%
ESCROW_FEE_CAP = 3000       # ₦3,000 cap

def escrow_fee(amount: int) -> int:
    """
    Calculate escrow fee:
    - 2% of amount
    - capped at ₦3,000
    """
    return min(int(amount * ESCROW_FEE_PERCENT), ESCROW_FEE_CAP)

FREE_SELLERS = 1000
FREE_BUYERS = 500

def calculate_fee(amount):
    return min(amount * 0.02, 3000)  # 2% capped ₦3,000
