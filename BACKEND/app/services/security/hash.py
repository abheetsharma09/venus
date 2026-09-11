# security.py
from pwdlib import PasswordHash

# Automatically uses the most secure recommended algorithm available (Argon2id)
password_hash = PasswordHash.recommended()

def get_password_hash(password: str) -> str:
    """Hashes a plain text password."""
    return password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plain text password against its stored hash."""
    return password_hash.verify(plain_password, hashed_password)
