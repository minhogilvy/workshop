from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class BookBase(BaseModel):
    """Base book schema with common fields."""
    title: str = Field(..., min_length=1, max_length=200, description="Book title")
    author: str = Field(..., min_length=1, max_length=100, description="Book author")
    published_year: int = Field(..., ge=1000, le=9999, description="Year of publication (1000-9999)")
    genre: str = Field(..., min_length=1, max_length=50, description="Book genre")
    description: Optional[str] = Field(None, max_length=1000, description="Book description")
    isbn: Optional[str] = Field(None, min_length=10, max_length=20, description="ISBN (10-20 characters)")


class BookCreate(BookBase):
    """Schema for creating a new book."""
    pass


class BookUpdate(BaseModel):
    """Schema for updating book information."""
    title: Optional[str] = Field(None, min_length=1, max_length=200, description="Book title")
    author: Optional[str] = Field(None, min_length=1, max_length=100, description="Book author")
    published_year: Optional[int] = Field(None, ge=1000, le=9999, description="Year of publication (1000-9999)")
    genre: Optional[str] = Field(None, min_length=1, max_length=50, description="Book genre")
    description: Optional[str] = Field(None, max_length=1000, description="Book description")
    isbn: Optional[str] = Field(None, min_length=10, max_length=20, description="ISBN (10-20 characters)")


class BookResponse(BookBase):
    """Schema for book response."""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class BookWithReadStatus(BookResponse):
    """Schema for book response with user reading status."""
    is_read: Optional[bool] = None
    read_at: Optional[datetime] = None