def verify_user(user, db):
    free = is_free_registration_allowed(user.role, db)

    if not free:
        charge_verification_fee(user.phone)

    user.verified = True
    user.trust_badge = True
