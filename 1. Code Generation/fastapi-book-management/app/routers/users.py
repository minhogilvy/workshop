from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from ..core.database import get_db
from ..core.security import get_current_active_user
from ..services.user_book_service import UserBookService
from ..schemas.book import BookResponse
from ..schemas.user_book_status import UserBookStatusResponse
from ..models.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/books/{book_id}/read", response_model=UserBookStatusResponse)
async def mark_book_as_read(
    book_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Mark a book as read for the current user.

    Args:
        book_id: Book ID to mark as read
        db: Database session
        current_user: Current authenticated user

    Returns:
        UserBookStatusResponse: Updated reading status

    Raises:
        HTTPException: If book not found
    """
    user_book_service = UserBookService(db)
    status = user_book_service.mark_book_as_read(current_user.id, book_id)
    return status


@router.post("/books/{book_id}/unread", response_model=UserBookStatusResponse)
async def mark_book_as_unread(
    book_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Mark a book as unread for the current user.

    Args:
        book_id: Book ID to mark as unread
        db: Database session
        current_user: Current authenticated user

    Returns:
        UserBookStatusResponse: Updated reading status

    Raises:
        HTTPException: If book not found
    """
    user_book_service = UserBookService(db)
    status = user_book_service.mark_book_as_unread(current_user.id, book_id)
    return status


@router.get("/me/books/read", response_model=List[BookResponse])
async def get_user_read_books(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of records to return"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Get books marked as read by the current user.

    Args:
        skip: Number of records to skip
        limit: Maximum number of records to return
        db: Database session
        current_user: Current authenticated user

    Returns:
        List[BookResponse]: List of read books
    """
    user_book_service = UserBookService(db)
    books = user_book_service.get_user_books_with_status(
        current_user.id,
        is_read=True,
        skip=skip,
        limit=limit
    )
    return books


@router.get("/me/books/unread", response_model=List[BookResponse])
async def get_user_unread_books(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of records to return"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Get books marked as unread by the current user.

    Args:
        skip: Number of records to skip
        limit: Maximum number of records to return
        db: Database session
        current_user: Current authenticated user

    Returns:
        List[BookResponse]: List of unread books
    """
    user_book_service = UserBookService(db)
    books = user_book_service.get_user_books_with_status(
        current_user.id,
        is_read=False,
        skip=skip,
        limit=limit
    )
    return books


@router.get("/me/books", response_model=List[BookResponse])
async def get_user_all_books(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of records to return"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Get all books tracked by the current user (both read and unread).

    Args:
        skip: Number of records to skip
        limit: Maximum number of records to return
        db: Database session
        current_user: Current authenticated user

    Returns:
        List[BookResponse]: List of all user's books
    """
    user_book_service = UserBookService(db)
    books = user_book_service.get_user_books_with_status(
        current_user.id,
        skip=skip,
        limit=limit
    )
    return books


@router.get("/me/books/{book_id}/status", response_model=UserBookStatusResponse)
async def get_book_reading_status(
    book_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Get reading status for a specific book.

    Args:
        book_id: Book ID
        db: Database session
        current_user: Current authenticated user

    Returns:
        UserBookStatusResponse: Reading status

    Raises:
        HTTPException: If status not found
    """
    user_book_service = UserBookService(db)
    status = user_book_service.get_book_reading_status(current_user.id, book_id)

    if not status:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reading status not found"
        )

    return status


@router.get("/me/stats")
async def get_user_reading_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Get reading statistics for the current user.

    Args:
        db: Database session
        current_user: Current authenticated user

    Returns:
        dict: Reading statistics
    """
    user_book_service = UserBookService(db)
    stats = user_book_service.get_user_reading_stats(current_user.id)
    return stats