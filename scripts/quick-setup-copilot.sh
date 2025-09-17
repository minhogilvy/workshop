#!/bin/bash

# Quick Python Backend Copilot Setup Script
# Usage: ./quick-setup.sh [project-name]

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

# Get project name
PROJECT_NAME="${1:-my-python-api}"
TARGET_DIR="$(pwd)"

# If project name is not current directory, create subdirectory
if [ "$PROJECT_NAME" != "." ] && [ "$PROJECT_NAME" != "./" ]; then
    if [ ! -d "$PROJECT_NAME" ]; then
        mkdir -p "$PROJECT_NAME"
        TARGET_DIR="$(pwd)/$PROJECT_NAME"
    fi
fi

# Create .github directory
mkdir -p "$TARGET_DIR/.github"

# Generate simplified copilot-instructions.md
cat > "$TARGET_DIR/.github/copilot-instructions.md" << 'EOF'
# 🎯 GitHub Copilot Instructions - Python Backend

## 📋 Project Context

### 🏗️ Project Overview
- **Project Name**: [UPDATE_PROJECT_NAME]
- **Project Type**: Backend API / Microservice
- **Tech Stack**: Python Backend Stack
- **Framework**: FastAPI / Django / Flask
- **Database**: PostgreSQL / MySQL / MongoDB
- **Deployment**: Docker + Cloud Platform

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

### 🐍 Python-Specific Guidelines
```markdown
- **Framework**: FastAPI (preferred) / Django / Flask
- **ORM**: SQLAlchemy with Alembic / Django ORM
- **Testing**: pytest with fixtures and factories
- **Code Style**: Black, flake8, mypy, pre-commit hooks
- **Dependencies**: Poetry for dependency management
- **Async**: async/await patterns for I/O operations
- **Validation**: Pydantic models for data validation
```

## 📁 Standard Project Structure
```
project-root/
├── app/                        # Main application package
│   ├── __init__.py
│   ├── main.py                # Application entry point
│   ├── core/                  # Core functionality
│   │   ├── config.py          # Configuration management
│   │   ├── security.py        # Security utilities
│   │   ├── database.py        # Database configuration
│   │   └── dependencies.py    # Dependency injection
│   ├── api/                   # API layer
│   │   ├── v1/               # API version 1
│   │   └── endpoints/        # Individual endpoints
│   ├── models/                # Database models
│   ├── schemas/               # Pydantic schemas
│   ├── services/              # Business logic
│   └── utils/                 # Utility functions
├── tests/                     # Test files
├── alembic/                   # Database migrations
├── .env.example              # Environment variables template
├── pyproject.toml            # Poetry configuration
├── Dockerfile
└── README.md
```

## 🚀 Quick Commands

### 🎨 Scaffolding
```markdown
"/create-fastapi-endpoint [resource]" - Create FastAPI CRUD endpoint
"/create-model [entity]" - Create database model
"/create-schema [entity]" - Create Pydantic schema
"/create-service [domain]" - Create business service
```

### 🧪 Testing
```markdown
"/test-endpoint [endpoint]" - Generate API tests
"/test-service [service]" - Generate service tests
"/test-integration [feature]" - Generate integration tests
```

## 🎯 Code Templates

### FastAPI Endpoint Template
```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api import deps
from app.schemas import UserCreate, User
from app.services.user_service import UserService

router = APIRouter()

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: UserCreate
) -> User:
    """Create new user."""
    user_service = UserService(db)
    return await user_service.create_user(user_in)
```

### SQLAlchemy Model Template
```python
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
```

### Pydantic Schema Template
```python
from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    username: str
    is_active: bool = True

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
```

### Service Template
```python
from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

class UserService:
    def __init__(self, db: Session):
        self.db = db

    async def create_user(self, user_create: UserCreate) -> User:
        """Create a new user."""
        # Business logic here
        db_user = User(**user_create.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
```

## ✅ Definition of Done
- [ ] Code follows PEP 8 standards
- [ ] Comprehensive error handling
- [ ] Unit tests with >85% coverage
- [ ] API documentation generated
- [ ] Security considerations addressed
- [ ] Performance optimized

---

**Remember**: Update project-specific sections based on your requirements! 🎯
EOF

# Replace project name placeholder
if [ "$PROJECT_NAME" != "." ] && [ "$PROJECT_NAME" != "./" ]; then
    sed -i.bak "s/\[UPDATE_PROJECT_NAME\]/$PROJECT_NAME/g" "$TARGET_DIR/.github/copilot-instructions.md"
    rm "$TARGET_DIR/.github/copilot-instructions.md.bak" 2>/dev/null || true
fi

print_success "Created copilot-instructions.md for Python backend project"

if [ "$TARGET_DIR" != "$(pwd)" ]; then
    print_info "Project created in: $TARGET_DIR"
    print_info "To navigate: cd $PROJECT_NAME"
fi

print_info "🎯 Ready to code with GitHub Copilot!"
EOF