# 🎯 GitHub Copilot Instructions - Python Backend Project

## 📋 Project Context

### 🏗️ Project Overview
- **Project Name**: [Project Name]
- **Project Type**: Backend API / Microservice / Web Application
- **Tech Stack**: Python Backend Stack
- **Framework**: FastAPI / Django / Flask
- **Database**: PostgreSQL / MySQL / MongoDB
- **Deployment**: Docker + AWS/Azure/GCP

### 🎨 Architecture & Patterns
- **Architecture Pattern**: Clean Architecture / Layered Architecture
- **Design Patterns**: Repository, Factory, Dependency Injection
- **Code Organization**: Feature-based modules with clear separation

## 🔧 Development Guidelines

### 📝 Coding Standards
```markdown
- **Language**: Python 3.11+
- **Style Guide**: PEP 8, Black formatter, isort
- **Type Hints**: Required for all public APIs
- **Naming Convention**: snake_case for functions/variables, PascalCase for classes
- **File Structure**: Module-based with clear imports
```

### 🎯 Code Quality Requirements
- **Test Coverage**: Minimum 85% for business logic
- **Documentation**: Comprehensive docstrings for all public APIs
- **Error Handling**: Custom exceptions with proper error codes
- **Performance**: Database query optimization and caching
- **Security**: Input validation, SQL injection prevention, auth security

### 🐍 Python-Specific Guidelines
```markdown
- **Framework**: FastAPI (preferred) / Django / Flask
- **ORM**: SQLAlchemy with Alembic / Django ORM / Tortoise ORM
- **Testing**: pytest with fixtures and factories
- **Code Style**: Black, flake8, mypy, pre-commit hooks
- **Dependencies**: Poetry for dependency management
- **Async**: async/await patterns for I/O operations
- **Validation**: Pydantic models for data validation
- **Background Tasks**: Celery with Redis/RabbitMQ
```

### 🗄️ Database Guidelines
```markdown
- **Migrations**: Alembic/Django migrations with proper versioning
- **Queries**: Optimize N+1 queries, use proper indexing
- **Transactions**: Use database transactions for data integrity
- **Connection Pooling**: Configure proper connection pools
- **Caching**: Redis for session/query caching
```

### 🔒 Security Guidelines
```markdown
- **Authentication**: JWT with refresh tokens / OAuth2
- **Authorization**: Role-based access control (RBAC)
- **Input Validation**: Pydantic schemas for all inputs
- **SQL Injection**: Use ORM parameterized queries
- **CORS**: Proper CORS configuration for frontend
- **Rate Limiting**: API rate limiting per user/IP
- **Secrets**: Environment variables for sensitive data
```

## 🎪 Project-Specific Context

### 🏢 Business Domain
```markdown
- **Industry**: [E-commerce, FinTech, HealthTech, etc.]
- **Target Users**: API consumers, web/mobile clients
- **Key Features**: [Core API functionality]
- **Business Rules**: [Domain-specific validation and workflows]
- **Compliance**: [GDPR, HIPAA, PCI-DSS requirements]
```

### 📊 Data Models
```markdown
- **Core Entities**: [User, Product, Order, etc.]
- **Relationships**: SQLAlchemy relationships with proper lazy loading
- **Business Logic**: Service layer with domain validation
- **Data Transfer**: Pydantic schemas for API serialization
```

## 🎯 AI Assistant Behavior Guidelines

### 💬 Communication Preferences
- **Language**: English for explanations and code comments
- **Code Style**: Production-ready code with comprehensive error handling
- **Examples**: Include practical examples with real-world scenarios
- **Testing**: Always include test examples for new code

### 🔄 Development Workflow
```markdown
1. **Analysis**: Understand business requirements and constraints
2. **Design**: Plan database schema and API endpoints
3. **Implementation**: Write clean, tested, documented code
4. **Testing**: Unit tests, integration tests, API tests
5. **Documentation**: API docs, code comments, README updates
```

## 🚀 Project-Specific Commands

### 🎨 Quick Scaffolding
```markdown
"/create-fastapi-endpoint [resource]" - Create FastAPI CRUD endpoint
"/create-django-viewset [model]" - Create Django REST ViewSet
"/create-pydantic-schema [entity]" - Create Pydantic model with validation
"/create-sqlalchemy-model [entity]" - Create SQLAlchemy model with relationships
"/create-service-class [domain]" - Create business logic service
"/create-repository [entity]" - Create repository pattern implementation
```

### 🧪 Testing Commands
```markdown
"/test-fastapi-endpoint [endpoint]" - Generate FastAPI endpoint tests
"/test-service-class [service]" - Generate service layer tests
"/test-repository [repo]" - Generate repository tests with mocks
"/test-integration [feature]" - Generate integration tests
"/test-database [model]" - Generate database model tests
```

### 📚 Documentation Commands
```markdown
"/document-api [endpoint]" - Generate OpenAPI documentation
"/document-service [service]" - Generate service documentation
"/document-setup" - Generate project setup documentation
"/create-api-examples [endpoint]" - Create API usage examples
```

## 📁 Python Backend Project Structure

### 🗂️ Standard Project Structure
```
project-root/
├── app/                        # Main application package
│   ├── __init__.py
│   ├── main.py                # Application entry point
│   ├── core/                  # Core functionality
│   │   ├── __init__.py
│   │   ├── config.py          # Configuration management
│   │   ├── security.py        # Security utilities
│   │   ├── database.py        # Database configuration
│   │   └── dependencies.py    # Dependency injection
│   ├── api/                   # API layer
│   │   ├── __init__.py
│   │   ├── deps.py           # API dependencies
│   │   └── v1/               # API version 1
│   │       ├── __init__.py
│   │       ├── api.py        # API router
│   │       └── endpoints/    # Individual endpoints
│   │           ├── users.py
│   │           ├── auth.py
│   │           └── items.py
│   ├── crud/                  # Database operations
│   │   ├── __init__.py
│   │   ├── base.py           # Base CRUD class
│   │   ├── crud_user.py
│   │   └── crud_item.py
│   ├── models/                # Database models
│   │   ├── __init__.py
│   │   ├── base.py           # Base model class
│   │   ├── user.py
│   │   └── item.py
│   ├── schemas/               # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── item.py
│   ├── services/              # Business logic
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── item_service.py
│   └── utils/                 # Utility functions
│       ├── __init__.py
│       ├── email.py
│       └── helpers.py
├── tests/                     # Test files
│   ├── __init__.py
│   ├── conftest.py           # Pytest configuration
│   ├── test_api/
│   ├── test_crud/
│   ├── test_services/
│   └── test_utils/
├── alembic/                   # Database migrations
│   ├── versions/
│   ├── env.py
│   └── alembic.ini
├── scripts/                   # Utility scripts
│   ├── format.sh             # Code formatting
│   ├── lint.sh               # Code linting
│   └── test.sh               # Test runner
├── docs/                      # Documentation
├── .env.example              # Environment variables template
├── .gitignore
├── .pre-commit-config.yaml   # Pre-commit hooks
├── pyproject.toml            # Poetry configuration
├── Dockerfile
├── docker-compose.yml
└── README.md
```

### 🎯 File Naming Conventions
```markdown
- **Python Modules**: snake_case (user_service.py)
- **Python Classes**: PascalCase (UserService, UserModel)
- **Python Functions**: snake_case (get_user_by_id, create_user)
- **Python Constants**: UPPER_SNAKE_CASE (DATABASE_URL, SECRET_KEY)
- **API Endpoints**: kebab-case (/api/v1/user-profiles)
- **Test Files**: test_[module_name].py
- **Migration Files**: alembic auto-generated names
```

## 🎪 Code Templates

### 🚀 FastAPI Endpoint Template
```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.api import deps
from app.crud import crud_user
from app.schemas import User, UserCreate, UserUpdate
from app.services.user_service import UserService

router = APIRouter()

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: UserCreate,
    current_user: User = Depends(deps.get_current_active_superuser)
) -> User:
    """
    Create new user.
    """
    try:
        user_service = UserService(db)
        user = await user_service.create_user(user_in)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/{user_id}", response_model=User)
async def read_user(
    user_id: int,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_active_user)
) -> User:
    """
    Get user by ID.
    """
    user = crud_user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user
```

### 🗄️ SQLAlchemy Model Template
```python
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    items = relationship("Item", back_populates="owner")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"
```

### 📝 Pydantic Schema Template
```python
from typing import Optional
from pydantic import BaseModel, EmailStr, validator
from datetime import datetime

# Shared properties
class UserBase(BaseModel):
    email: EmailStr
    username: str
    is_active: bool = True
    is_superuser: bool = False

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return v

# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None

# Properties to return via API
class User(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Properties stored in DB
class UserInDB(User):
    hashed_password: str
```

### 🏢 Service Layer Template
```python
from typing import Optional, List
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.crud import crud_user
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password

class UserService:
    def __init__(self, db: Session):
        self.db = db

    async def create_user(self, user_create: UserCreate) -> User:
        """Create a new user with validation."""
        # Check if user already exists
        existing_user = crud_user.get_by_email(self.db, email=user_create.email)
        if existing_user:
            raise ValueError("User with this email already exists")

        # Hash password and create user
        hashed_password = get_password_hash(user_create.password)
        user_data = user_create.dict()
        del user_data["password"]
        user_data["hashed_password"] = hashed_password

        user = crud_user.create(self.db, obj_in=user_data)
        return user

    async def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """Authenticate user credentials."""
        user = crud_user.get_by_email(self.db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID."""
        return crud_user.get(self.db, id=user_id)

    async def update_user(self, user_id: int, user_update: UserUpdate) -> User:
        """Update user information."""
        user = await self.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        update_data = user_update.dict(exclude_unset=True)
        if "password" in update_data:
            update_data["hashed_password"] = get_password_hash(update_data["password"])
            del update_data["password"]

        updated_user = crud_user.update(self.db, db_obj=user, obj_in=update_data)
        return updated_user
```

### 🧪 Pytest Test Template
```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
from app.core.config import settings
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_email, random_lower_string

client = TestClient(app)

class TestUserAPI:
    def test_create_user(self, db: Session) -> None:
        email = random_email()
        password = random_lower_string()
        data = {"email": email, "password": password, "username": "testuser"}

        response = client.post(f"{settings.API_V1_STR}/users/", json=data)
        assert response.status_code == 201

        created_user = response.json()
        assert created_user["email"] == email
        assert "id" in created_user

    def test_get_user(self, db: Session) -> None:
        user = create_random_user(db)

        response = client.get(f"{settings.API_V1_STR}/users/{user.id}")
        assert response.status_code == 200

        api_user = response.json()
        assert api_user["email"] == user.email
        assert api_user["id"] == user.id

    def test_user_not_found(self, db: Session) -> None:
        response = client.get(f"{settings.API_V1_STR}/users/99999")
        assert response.status_code == 404

@pytest.fixture
def user_service(db: Session):
    return UserService(db)

class TestUserService:
    def test_create_user_success(self, user_service: UserService) -> None:
        email = random_email()
        user_create = UserCreate(
            email=email,
            username="testuser",
            password="testpassword123"
        )

        user = await user_service.create_user(user_create)
        assert user.email == email
        assert user.username == "testuser"

    def test_create_user_duplicate_email(self, user_service: UserService, db: Session) -> None:
        # Create first user
        existing_user = create_random_user(db)

        # Try to create user with same email
        user_create = UserCreate(
            email=existing_user.email,
            username="differentuser",
            password="testpassword123"
        )

        with pytest.raises(ValueError, match="User with this email already exists"):
            await user_service.create_user(user_create)
```

## 🏆 Success Criteria

### ✅ Definition of Done
- [ ] Code follows Python PEP 8 standards
- [ ] Comprehensive error handling with custom exceptions
- [ ] Unit tests with >85% coverage
- [ ] API documentation auto-generated
- [ ] Database migrations created and tested
- [ ] Performance requirements met
- [ ] Security vulnerabilities addressed
- [ ] Code review completed

### 🎯 Quality Gates
- **Functionality**: All API endpoints work as specified
- **Reliability**: Handles edge cases and errors gracefully
- **Performance**: Response times under 200ms for simple queries
- **Maintainability**: Clean, documented, testable code
- **Security**: No security vulnerabilities in dependencies
- **Scalability**: Database queries optimized for growth

---

## 🚨 Important Notes

### ⚠️ Performance Considerations
- **Database**: Use connection pooling, optimize queries
- **Caching**: Implement Redis for frequently accessed data
- **Async**: Use async/await for I/O operations
- **Background Tasks**: Use Celery for heavy processing

### 🔄 Development Practices
- **Git**: Feature branches with descriptive commit messages
- **Code Review**: All changes reviewed before merge
- **Testing**: Test-driven development approach
- **Documentation**: Keep API docs and README updated

---

**Remember**: This configuration is optimized for Python backend development. Update project-specific sections based on your domain requirements! 🎯