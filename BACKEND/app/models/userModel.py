from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True) # SERIAL PRIMARY KEY
    name = Column(String(100), nullable=False)        # VARCHAR(100) NOT NULL
    email = Column(String(255), unique=True, nullable=False) # UNIQUE NOT NULL
    password = Column(String(255), nullable=False)    # VARCHAR(255) NOT NULL
    is_active = Column(Boolean, default=True)         # DEFAULT TRUE
    created_at = Column(DateTime(timezone=True), server_default=func.now()) # DEFAULT CURRENT_TIMESTAMP

