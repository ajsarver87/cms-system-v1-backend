from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """Hashes plain text password"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password:str) -> bool:
    """Verifies plain text password against the password hash"""
    return pwd_context.verify(plain_password, hashed_password)
