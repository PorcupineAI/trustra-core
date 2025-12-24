from app.ai.pricing_engine import adaptive_fee

FREE_SELLERS = 1000
FREE_BUYERS = 500

def escrow_fee(amount, trust_score):
    rate = adaptive_fee(trust_score)
    return round(amount * rate, 2)

def verification_fee(required):
    return 1000 if required else 0  # ₦1000 only if flagged
