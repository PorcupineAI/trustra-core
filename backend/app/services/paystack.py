def initiate_escrow(amount):
    fee = min(amount * 0.02, 3000)
    hold_amount = amount + fee
    return {
        "amount": hold_amount,
        "fee": fee,
        "status": "held"
    }
