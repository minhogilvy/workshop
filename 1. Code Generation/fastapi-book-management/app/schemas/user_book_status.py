from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class UserBookStatusBase(BaseModel):
    """Base schema for user book status."""
    is_read: bool = False


class UserBookStatusCreate(UserBookStatusBase):
    """Schema for creating user book status."""
    book_id: int


class UserBookStatusUpdate(BaseModel):
    """Schema for updating user book status."""
    is_read: bool


class UserBookStatusResponse(UserBookStatusBase):
    """Schema for user book status response."""
    id: int
    user_id: int
    book_id: int
    read_at: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True