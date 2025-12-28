-- Test trust_score bounds
INSERT INTO users (email, trust_score) VALUES ('test@example.com', 150); -- Should fail

-- Test escrow status
INSERT INTO escrow (buyer_id, seller_id, amount, status) 
VALUES (gen_random_uuid(), gen_random_uuid(), 1000, 'hacked'); -- Should fail
