from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from ..models.book import Book
from ..schemas.book import BookCreate, BookUpdate


class BookService:
    """Service class for book operations."""

    def __init__(self, db: Session):
        self.db = db

    def create_book(self, book_create: BookCreate) -> Book:
        """
        Create a new book.

        Args:
            book_create: Book creation data

        Returns:
            Book: The created book

        Raises:
            HTTPException: If ISBN already exists
        """
        # Check if ISBN already exists
        if book_create.isbn and self.db.query(Book).filter(Book.isbn == book_create.isbn).first():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Book with this ISBN already exists"
            )

        db_book = Book(**book_create.model_dump())
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)

        return db_book

    def get_book(self, book_id: int) -> Optional[Book]:
        """
        Get a book by ID.

        Args:
            book_id: Book ID

        Returns:
            Book: Found book or None
        """
        return self.db.query(Book).filter(Book.id == book_id).first()

    def get_books(self, skip: int = 0, limit: int = 100, genre: Optional[str] = None,
                  author: Optional[str] = None, title: Optional[str] = None) -> List[Book]:
        """
        Get books with optional filtering.

        Args:
            skip: Number of records to skip
            limit: Maximum number of records to return
            genre: Filter by genre
            author: Filter by author
            title: Filter by title (partial match)

        Returns:
            List[Book]: List of books
        """
        query = self.db.query(Book)

        if genre:
            query = query.filter(Book.genre.ilike(f"%{genre}%"))
        if author:
            query = query.filter(Book.author.ilike(f"%{author}%"))
        if title:
            query = query.filter(Book.title.ilike(f"%{title}%"))

        return query.offset(skip).limit(limit).all()

    def update_book(self, book_id: int, book_update: BookUpdate) -> Optional[Book]:
        """
        Update a book.

        Args:
            book_id: Book ID to update
            book_update: Update data

        Returns:
            Book: Updated book or None if not found

        Raises:
            HTTPException: If ISBN already exists for another book
        """
        db_book = self.get_book(book_id)
        if not db_book:
            return None

        # Check if ISBN already exists for another book
        update_data = book_update.model_dump(exclude_unset=True)
        if "isbn" in update_data and update_data["isbn"]:
            existing_book = self.db.query(Book).filter(
                Book.isbn == update_data["isbn"],
                Book.id != book_id
            ).first()
            if existing_book:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Book with this ISBN already exists"
                )

        # Update book fields
        for field, value in update_data.items():
            setattr(db_book, field, value)

        self.db.commit()
        self.db.refresh(db_book)

        return db_book

    def delete_book(self, book_id: int) -> bool:
        """
        Delete a book.

        Args:
            book_id: Book ID to delete

        Returns:
            bool: True if deleted, False if not found
        """
        db_book = self.get_book(book_id)
        if not db_book:
            return False

        self.db.delete(db_book)
        self.db.commit()

        return True

    def get_books_count(self, genre: Optional[str] = None, author: Optional[str] = None,
                       title: Optional[str] = None) -> int:
        """
        Get total count of books with optional filtering.

        Args:
            genre: Filter by genre
            author: Filter by author
            title: Filter by title (partial match)

        Returns:
            int: Total count of books
        """
        query = self.db.query(Book)

        if genre:
            query = query.filter(Book.genre.ilike(f"%{genre}%"))
        if author:
            query = query.filter(Book.author.ilike(f"%{author}%"))
        if title:
            query = query.filter(Book.title.ilike(f"%{title}%"))

        return query.count()