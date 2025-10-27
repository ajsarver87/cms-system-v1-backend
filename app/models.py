import uuid
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, DateTime, func
from datetime import datetime
from typing import Optional

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str
    hashed_password: str
    first_name: str
    last_name: str
    email: str
    is_active: bool
    is_admin: bool
    is_superuser: bool
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
