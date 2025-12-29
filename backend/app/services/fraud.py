def mark_suspicious(user):
    if user.failed_transactions > 3:
        user.flagged = True
