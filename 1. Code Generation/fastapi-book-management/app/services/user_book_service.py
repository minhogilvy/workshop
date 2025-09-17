from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException, status

from ..models.user import User
from ..models.book import Book
from ..models.user_book_status import UserBookStatus


class UserBookService:
    """Service class for user book reading status operations."""

    def __init__(self, db: Session):
        self.db = db

    def mark_book_as_read(self, user_id: int, book_id: int) -> UserBookStatus:
        """
        Mark a book as read for a user.

        Args:
            user_id: User ID
            book_id: Book ID

        Returns:
            UserBookStatus: The updated or created status

        Raises:
            HTTPException: If book doesn't exist
        """
        # Check if book exists
        book = self.db.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
            )

        # Get or create user book status
        user_book_status = self.db.query(UserBookStatus).filter(
            UserBookStatus.user_id == user_id,
            UserBookStatus.book_id == book_id
        ).first()

        if user_book_status:
            user_book_status.is_read = True
            user_book_status.read_at = datetime.utcnow()
        else:
            user_book_status = UserBookStatus(
                user_id=user_id,
                book_id=book_id,
                is_read=True,
                read_at=datetime.utcnow()
            )
            self.db.add(user_book_status)

        self.db.commit()
        self.db.refresh(user_book_status)

        return user_book_status

    def mark_book_as_unread(self, user_id: int, book_id: int) -> UserBookStatus:
        """
        Mark a book as unread for a user.

        Args:
            user_id: User ID
            book_id: Book ID

        Returns:
            UserBookStatus: The updated or created status

        Raises:
            HTTPException: If book doesn't exist
        """
        # Check if book exists
        book = self.db.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
            )

        # Get or create user book status
        user_book_status = self.db.query(UserBookStatus).filter(
            UserBookStatus.user_id == user_id,
            UserBookStatus.book_id == book_id
        ).first()

        if user_book_status:
            user_book_status.is_read = False
            user_book_status.read_at = None
        else:
            user_book_status = UserBookStatus(
                user_id=user_id,
                book_id=book_id,
                is_read=False
            )
            self.db.add(user_book_status)

        self.db.commit()
        self.db.refresh(user_book_status)

        return user_book_status

    def get_user_books_with_status(self, user_id: int, is_read: Optional[bool] = None,
                                  skip: int = 0, limit: int = 100) -> List[Book]:
        """
        Get books with reading status for a user.

        Args:
            user_id: User ID
            is_read: Filter by read status (None for all books)
            skip: Number of records to skip
            limit: Maximum number of records to return

        Returns:
            List[Book]: List of books with reading status
        """
        query = self.db.query(Book).join(UserBookStatus).filter(
            UserBookStatus.user_id == user_id
        )

        if is_read is not None:
            query = query.filter(UserBookStatus.is_read == is_read)

        return query.offset(skip).limit(limit).all()

    def get_book_reading_status(self, user_id: int, book_id: int) -> Optional[UserBookStatus]:
        """
        Get reading status for a specific book and user.

        Args:
            user_id: User ID
            book_id: Book ID

        Returns:
            UserBookStatus: Reading status or None if not found
        """
        return self.db.query(UserBookStatus).filter(
            UserBookStatus.user_id == user_id,
            UserBookStatus.book_id == book_id
        ).first()

    def get_user_reading_stats(self, user_id: int) -> dict:
        """
        Get reading statistics for a user.

        Args:
            user_id: User ID

        Returns:
            dict: Reading statistics
        """
        total_books = self.db.query(UserBookStatus).filter(
            UserBookStatus.user_id == user_id
        ).count()

        read_books = self.db.query(UserBookStatus).filter(
            UserBookStatus.user_id == user_id,
            UserBookStatus.is_read == True
        ).count()

        unread_books = total_books - read_books

        return {
            "total_books": total_books,
            "read_books": read_books,
            "unread_books": unread_books,
            "reading_percentage": round((read_books / total_books) * 100, 2) if total_books > 0 else 0
        }