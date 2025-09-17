"""
Custom exceptions for the book management application.
"""

from fastapi import HTTPException, status


class BookManagementException(Exception):
    """Base exception for book management application."""
    pass


class ValidationError(BookManagementException):
    """Raised when validation fails."""
    pass


class AuthenticationError(BookManagementException):
    """Raised when authentication fails."""
    pass


class AuthorizationError(BookManagementException):
    """Raised when authorization fails."""
    pass


class NotFoundError(BookManagementException):
    """Raised when a resource is not found."""
    pass


class ConflictError(BookManagementException):
    """Raised when there's a conflict (e.g., duplicate resource)."""
    pass


class DatabaseError(BookManagementException):
    """Raised when database operations fail."""
    pass


# HTTP Exception factories
def create_not_found_exception(detail: str = "Resource not found") -> HTTPException:
    """Create a 404 Not Found HTTPException."""
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=detail
    )


def create_conflict_exception(detail: str = "Resource already exists") -> HTTPException:
    """Create a 409 Conflict HTTPException."""
    return HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=detail
    )


def create_validation_exception(detail: str = "Validation error") -> HTTPException:
    """Create a 422 Unprocessable Entity HTTPException."""
    return HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=detail
    )


def create_authentication_exception(detail: str = "Authentication failed") -> HTTPException:
    """Create a 401 Unauthorized HTTPException."""
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
        headers={"WWW-Authenticate": "Bearer"}
    )


def create_authorization_exception(detail: str = "Not enough permissions") -> HTTPException:
    """Create a 403 Forbidden HTTPException."""
    return HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=detail
    )


def create_internal_server_exception(detail: str = "Internal server error") -> HTTPException:
    """Create a 500 Internal Server Error HTTPException."""
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=detail
    )