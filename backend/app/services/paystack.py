def init_payment(phone, amount, purpose):
    return {
        "email": f"{phone}@trustra.ng",
        "amount": amount * 100,
        "metadata": {"purpose": purpose}
    }
