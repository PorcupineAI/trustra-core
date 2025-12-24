def adaptive_fee(trust_score, base_fee=0.02):
    if trust_score > 80:
        return base_fee * 0.7
    if trust_score < 30:
        return base_fee * 1.5
    return base_fee
