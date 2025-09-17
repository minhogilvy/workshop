# Book Management FastAPI Application

A comprehensive book management system built with FastAPI, featuring user authentication, CRUD operations for books, and reading status tracking.

## Features

- **User Management**: Registration, authentication, and profile management
- **Book Management**: Complete CRUD operations for books
- **Reading Status**: Mark books as read/unread for each user
- **Authentication**: JWT-based authentication with password hashing
- **Database**: SQLAlchemy integration with support for SQLite and PostgreSQL
- **Validation**: Pydantic models for request/response validation
- **Error Handling**: Comprehensive error handling and logging

## Project Structure

```
fastapi-book-management/
├── app/
│   ├── core/           # Core functionality (config, security, database)
│   ├── models/         # SQLAlchemy models
│   ├── schemas/        # Pydantic models
│   ├── routers/        # API route handlers
│   ├── services/       # Business logic services
│   └── main.py         # FastAPI application entry point
├── requirements.txt    # Python dependencies
├── .env.example       # Environment configuration template
└── README.md          # This file
```

## Setup Instructions

1. **Clone and navigate to the project directory**

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the API documentation**
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## API Endpoints

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and get access token

### Books
- `GET /books/` - Get all books
- `GET /books/{book_id}` - Get a specific book
- `POST /books/` - Create a new book
- `PUT /books/{book_id}` - Update a book
- `DELETE /books/{book_id}` - Delete a book

### User Reading Status
- `POST /books/{book_id}/read` - Mark book as read
- `POST /books/{book_id}/unread` - Mark book as unread
- `GET /users/me/books/read` - Get user's read books

## Models

### Book
- `id`: Unique identifier
- `title`: Book title
- `author`: Book author
- `published_year`: Year of publication
- `genre`: Book genre

### User
- `id`: Unique identifier
- `username`: Unique username
- `email`: User's email address
- `hashed_password`: Securely hashed password

### UserBookStatus
- `user_id`: Reference to user
- `book_id`: Reference to book
- `is_read`: Boolean indicating read status

## Security Features

- Password hashing using bcrypt
- JWT token authentication
- Protected routes requiring authentication
- Input validation using Pydantic
- SQL injection prevention with SQLAlchemy ORM

## Development

This application follows FastAPI best practices including:
- Dependency injection for database sessions
- Proper error handling and HTTP status codes
- Comprehensive logging
- Clean separation of concerns
- Type hints throughout the codebase