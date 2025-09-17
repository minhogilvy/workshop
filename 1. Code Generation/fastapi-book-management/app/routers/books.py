from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from ..core.database import get_db
from ..core.security import get_current_active_user
from ..services.book_service import BookService
from ..schemas.book import BookCreate, BookUpdate, BookResponse
from ..models.user import User

router = APIRouter(prefix="/books", tags=["books"])


@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create_book(
    book_create: BookCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Create a new book.

    Args:
        book_create: Book creation data
        db: Database session
        current_user: Current authenticated user

    Returns:
        BookResponse: Created book information

    Raises:
        HTTPException: If ISBN already exists
    """
    book_service = BookService(db)
    book = book_service.create_book(book_create)
    return book


@router.get("/", response_model=List[BookResponse])
async def get_books(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of records to return"),
    genre: Optional[str] = Query(None, description="Filter by genre"),
    author: Optional[str] = Query(None, description="Filter by author"),
    title: Optional[str] = Query(None, description="Filter by title"),
    db: Session = Depends(get_db)
):
    """
    Get books with optional filtering.

    Args:
        skip: Number of records to skip
        limit: Maximum number of records to return
        genre: Filter by genre
        author: Filter by author
        title: Filter by title (partial match)
        db: Database session

    Returns:
        List[BookResponse]: List of books
    """
    book_service = BookService(db)
    books = book_service.get_books(
        skip=skip,
        limit=limit,
        genre=genre,
        author=author,
        title=title
    )
    return books


@router.get("/{book_id}", response_model=BookResponse)
async def get_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific book by ID.

    Args:
        book_id: Book ID
        db: Database session

    Returns:
        BookResponse: Book information

    Raises:
        HTTPException: If book not found
    """
    book_service = BookService(db)
    book = book_service.get_book(book_id)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    return book


@router.put("/{book_id}", response_model=BookResponse)
async def update_book(
    book_id: int,
    book_update: BookUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Update a book.

    Args:
        book_id: Book ID to update
        book_update: Book update data
        db: Database session
        current_user: Current authenticated user

    Returns:
        BookResponse: Updated book information

    Raises:
        HTTPException: If book not found or ISBN already exists
    """
    book_service = BookService(db)
    book = book_service.update_book(book_id, book_update)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    return book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Delete a book.

    Args:
        book_id: Book ID to delete
        db: Database session
        current_user: Current authenticated user

    Raises:
        HTTPException: If book not found
    """
    book_service = BookService(db)
    deleted = book_service.delete_book(book_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )


@router.get("/stats/count")
async def get_books_count(
    genre: Optional[str] = Query(None, description="Filter by genre"),
    author: Optional[str] = Query(None, description="Filter by author"),
    title: Optional[str] = Query(None, description="Filter by title"),
    db: Session = Depends(get_db)
):
    """
    Get total count of books with optional filtering.

    Args:
        genre: Filter by genre
        author: Filter by author
        title: Filter by title (partial match)
        db: Database session

    Returns:
        dict: Total count of books
    """
    book_service = BookService(db)
    count = book_service.get_books_count(genre=genre, author=author, title=title)
    return {"count": count}