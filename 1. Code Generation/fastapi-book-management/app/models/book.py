from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base


class Book(Base):
    """Book model for storing book information."""

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    author = Column(String(100), nullable=False, index=True)
    published_year = Column(Integer, nullable=False)
    genre = Column(String(50), nullable=False, index=True)
    description = Column(String(1000))
    isbn = Column(String(20), unique=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationship to user book status
    user_statuses = relationship("UserBookStatus", back_populates="book", cascade="all, delete-orphan")