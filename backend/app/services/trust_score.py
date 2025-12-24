def calculate_trust_score(user):
    score = 50
    score += user.completed_escrows * 10
    score -= user.disputes * 20
    if user.verified:
        score += 15
    score -= user.flags * 30
    score += user.months_active
    return max(0, min(score, 100))
