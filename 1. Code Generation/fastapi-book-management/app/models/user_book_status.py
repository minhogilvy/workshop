from sqlalchemy import Column, Integer, ForeignKey, Boolean, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base


class UserBookStatus(Base):
    """Junction table to track reading status of books for users."""

    __tablename__ = "user_book_status"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    is_read = Column(Boolean, default=False, nullable=False)
    read_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Ensure unique combination of user and book
    __table_args__ = (UniqueConstraint('user_id', 'book_id', name='unique_user_book'),)

    # Relationships
    user = relationship("User", back_populates="book_statuses")
    book = relationship("Book", back_populates="user_statuses")