def hold_funds(ref):
    return {"status": "HELD", "reference": ref}

def release_funds(ref):
    return {"status": "RELEASED", "reference": ref}
