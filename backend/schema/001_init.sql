CREATE TABLE users (
    id UUID PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    trust_score INTEGER DEFAULT 50,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE escrow (
    id UUID PRIMARY KEY,
    buyer_id UUID,
    seller_id UUID,
    amount NUMERIC,
    status TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
