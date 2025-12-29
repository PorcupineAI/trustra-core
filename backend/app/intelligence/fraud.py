def assess_risk(amount, velocity):
    risk = 0
    if amount > 500000:
        risk += 30
    if velocity > 5:
        risk += 40
    return risk
