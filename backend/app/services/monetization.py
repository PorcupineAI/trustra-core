def calculate_fee(amount: float):
    """
    2% fee, capped at ₦3,000
    """
    return min(amount * 0.02, 3000)

