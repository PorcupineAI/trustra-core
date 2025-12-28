def update_trust_score(user, event: str):
    rules = {
        "register": 10,
        "verify": 10,
        "escrow_success": 5,
        "first_escrow": 15,
        "dispute": -20,
        "timeout": -10,
        "fraud": -50,
    }

    delta = rules.get(event, 0)
    user.trust_score = max(0, min(100, user.trust_score + delta))
    return user.trust_score
