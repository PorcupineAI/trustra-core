from app.models.playing_with_neon import PlayingWithNeon
from app.database import SessionLocal

def predict_fraud(user_id: int):
    db = SessionLocal()
    neon_score = db.query(PlayingWithNeon).filter(PlayingWithNeon.id == user_id).first()
    if neon_score:
        # Example logic: score < 50 = high risk
        return "high" if neon_score.score < 50 else "low"
    return "unknown"
