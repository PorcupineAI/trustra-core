FREE_SELLERS = 1000
FREE_BUYERS = 500

def is_free_registration_allowed(role, db):
    if role == "seller":
        return db.count("sellers") < FREE_SELLERS
    if role == "buyer":
        return db.count("buyers") < FREE_BUYERS
    return False

def registration_fee(role):
    return 2000 if role == "seller" else 1000
