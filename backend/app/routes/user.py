from app.intelligence.predictor import predict_fraud_probability

@router.get("/{user_id}/fraud-risk")
def fraud_risk(user_id: int, db=Depends(get_db)):
    user = db.query(User).get(user_id)
    return {
        "fraud_probability": predict_fraud_probability(user)
    }
