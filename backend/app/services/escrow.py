def hold(amount):
    return {"status": "held", "amount": amount}

def release():
    return {"status": "released"}
