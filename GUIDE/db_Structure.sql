CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

--------------------Testing Data---------------------------
INSERT INTO users (name, email, password, is_active, created_at) VALUES
('John Doe', 'john.doe@example.com', '$2b$12$dQw4w9WgXcQ...hashed_password_1', TRUE, '2026-01-15 08:30:00+00'),
('Jane Smith', 'jane.smith@example.com', '$2b$12$eX4mP7eR2tY...hashed_password_2', TRUE, '2026-02-20 14:15:22+00'),
('Alice Johnson', 'alice.j@example.net', '$2b$12$uVwXYZ12345...hashed_password_3', FALSE, '2026-03-05 09:45:00+00'),
('Bob Miller', 'bob.miller@example.org', '$2b$12$pQrStU67890...hashed_password_4', TRUE, '2026-04-12 18:22:11+00'),
('Charlie Brown', 'charlie.b@example.com', '$2b$12$aBcDeF34567...hashed_password_5', TRUE, '2026-05-19 11:05:43+00'),
('Diana Prince', 'diana.p@example.io', '$2b$12$gHiJkL89012...hashed_password_6', FALSE, '2026-06-25 16:40:19+00'),
('Evan Wright', 'evan.wright@example.com', '$2b$12$mNoPqR34567...hashed_password_7', TRUE, '2026-07-01 07:12:55+00'),
('Fiona Gallagher', 'fiona.g@example.co.uk', '$2b$12$sTuVwX89012...hashed_password_8', TRUE, '2026-07-14 21:33:04+00'),
('George Clark', 'george.clark@example.com', '$2b$12$yZaBcD34567...hashed_password_9', TRUE, '2026-08-22 13:50:12+00'),
('Hannah Abbott', 'hannah.a@example.edu', '$2b$12$eFgHiJ89012...hashed_password_10', FALSE, '2026-08-29 10:00:00+00');
-------------------------------------------------------------