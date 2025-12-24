class User:
    def __init__(self, phone, role):
        self.phone = phone
        self.role = role  # buyer | seller
        self.verified = False
        self.trust_badge = False
        self.paid = False
