def platform_health(users, escrows):
    return {
        "users": len(users),
        "escrows": len(escrows),
        "conversion_rate": len(escrows)/max(len(users),1)
    }
