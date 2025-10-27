import uuid
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, DateTime, func
from datetime import datetime
from typing import Optional

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str = Field(unique=True, index=True, max_length=50, nullable=False)
    hashed_password: str
    first_name: str = Field(max_length=50, nullable=False)
    last_name: str = Field(max_length=50, nullable=False)
    email: str = Field(unique=True, index=True)
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=False)
    is_superuser: bool = Field(default=False)
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), nullable=True
        )
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), onupdate=func.now(), nullable=True
        )
    )

class UserCreate(SQLModel):
    """Model used for user creation"""
    username: str
    email: str
    password: str
    first_name: str
    last_name: str

class UserRead(SQLModel):
    """Model used for user retrieval"""
    id: uuid.UUID
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool
