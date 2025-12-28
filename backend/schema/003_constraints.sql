-- Trust score must be between 0 and 100
ALTER TABLE users
ADD CONSTRAINT trust_score_range
CHECK (trust_score >= 0 AND trust_score <= 100);

-- Escrow amount must be positive
ALTER TABLE escrow
ADD CONSTRAINT escrow_amount_positive
CHECK (amount > 0);

-- Revenue amount must be positive
ALTER TABLE revenue
ADD CONSTRAINT revenue_amount_positive
CHECK (amount > 0);

-- Escrow status control
ALTER TABLE escrow
ADD CONSTRAINT escrow_status_enum
CHECK (status IN ('pending', 'funded', 'released', 'disputed', 'cancelled'));
