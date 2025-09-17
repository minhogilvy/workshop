#!/bin/bash

# Python Backend Project Copilot Setup Script
# Usage: ./setup-copilot-instructions.sh [project-name] [framework]

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
DEFAULT_FRAMEWORK="fastapi"
DEFAULT_DATABASE="postgresql"
DEFAULT_DEPLOYMENT="docker"

# Function to print colored output
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Function to get user input with default
get_input() {
    local prompt="$1"
    local default="$2"
    local response
    
    if [ -n "$default" ]; then
        read -p "$prompt [$default]: " response
        echo "${response:-$default}"
    else
        read -p "$prompt: " response
        echo "$response"
    fi
}

# Function to create directory if it doesn't exist
create_dir() {
    if [ ! -d "$1" ]; then
        mkdir -p "$1"
        print_info "Created directory: $1"
    fi
}

# Function to detect project structure
detect_project_structure() {
    local project_dir="$1"
    
    # Check for existing Python project files
    if [ -f "$project_dir/pyproject.toml" ]; then
        echo "poetry"
    elif [ -f "$project_dir/requirements.txt" ]; then
        echo "pip"
    elif [ -f "$project_dir/Pipfile" ]; then
        echo "pipenv"
    elif [ -f "$project_dir/setup.py" ]; then
        echo "setuptools"
    else
        echo "new"
    fi
}

# Function to detect framework
detect_framework() {
    local project_dir="$1"
    
    if [ -f "$project_dir/manage.py" ] || grep -q "django" "$project_dir/requirements.txt" 2>/dev/null; then
        echo "django"
    elif grep -q "fastapi" "$project_dir/requirements.txt" 2>/dev/null || grep -q "fastapi" "$project_dir/pyproject.toml" 2>/dev/null; then
        echo "fastapi"
    elif grep -q "flask" "$project_dir/requirements.txt" 2>/dev/null || grep -q "flask" "$project_dir/pyproject.toml" 2>/dev/null; then
        echo "flask"
    else
        echo "unknown"
    fi
}

# Function to generate copilot instructions based on framework
generate_copilot_instructions() {
    local project_name="$1"
    local framework="$2"
    local database="$3"
    local deployment="$4"
    local business_domain="$5"
    local target_dir="$6"
    
    # Determine framework-specific configurations
    case "$framework" in
        "fastapi")
            framework_display="FastAPI"
            orm_preference="SQLAlchemy with Alembic"
            testing_framework="pytest with FastAPI TestClient"
            async_support="async/await patterns for I/O operations"
            api_docs="OpenAPI (Swagger) auto-generated"
            ;;
        "django")
            framework_display="Django + Django REST Framework"
            orm_preference="Django ORM with migrations"
            testing_framework="pytest-django / Django TestCase"
            async_support="Django async views and middleware"
            api_docs="DRF Spectacular for OpenAPI"
            ;;
        "flask")
            framework_display="Flask + Flask-RESTful"
            orm_preference="SQLAlchemy with Flask-Migrate"
            testing_framework="pytest with Flask test client"
            async_support="Quart for async support"
            api_docs="Flask-RESTX for Swagger"
            ;;
        *)
            framework_display="Python Framework"
            orm_preference="SQLAlchemy"
            testing_framework="pytest"
            async_support="async/await patterns"
            api_docs="OpenAPI documentation"
            ;;
    esac
    
    # Create the .github directory
    create_dir "$target_dir/.github"
    
    # Generate the copilot-instructions.md file
    cat > "$target_dir/.github/copilot-instructions.md" << EOF
# 🎯 GitHub Copilot Instructions - ${project_name}

## 📋 Project Context

### 🏗️ Project Overview
- **Project Name**: ${project_name}
- **Project Type**: Backend API / Microservice
- **Tech Stack**: Python Backend Stack
- **Framework**: ${framework_display}
- **Database**: ${database}
- **Deployment**: ${deployment}

### 🎨 Architecture & Patterns
- **Architecture Pattern**: Clean Architecture / Layered Architecture
- **Design Patterns**: Repository, Factory, Dependency Injection
- **Code Organization**: Feature-based modules with clear separation

## 🔧 Development Guidelines

### 📝 Coding Standards
\`\`\`markdown
- **Language**: Python 3.11+
- **Style Guide**: PEP 8, Black formatter, isort
- **Type Hints**: Required for all public APIs
- **Naming Convention**: snake_case for functions/variables, PascalCase for classes
- **File Structure**: Module-based with clear imports
\`\`\`

### 🎯 Code Quality Requirements
- **Test Coverage**: Minimum 85% for business logic
- **Documentation**: Comprehensive docstrings for all public APIs
- **Error Handling**: Custom exceptions with proper error codes
- **Performance**: Database query optimization and caching
- **Security**: Input validation, SQL injection prevention, auth security

### 🐍 Python-Specific Guidelines
\`\`\`markdown
- **Framework**: ${framework_display}
- **ORM**: ${orm_preference}
- **Testing**: ${testing_framework}
- **Code Style**: Black, flake8, mypy, pre-commit hooks
- **Dependencies**: Poetry for dependency management
- **Async**: ${async_support}
- **Validation**: Pydantic models for data validation
- **Background Tasks**: Celery with Redis/RabbitMQ
\`\`\`

### 🗄️ Database Guidelines
\`\`\`markdown
- **Database**: ${database}
- **Migrations**: Proper versioning and rollback support
- **Queries**: Optimize N+1 queries, use proper indexing
- **Transactions**: Use database transactions for data integrity
- **Connection Pooling**: Configure proper connection pools
- **Caching**: Redis for session/query caching
\`\`\`

## 🎪 Project-Specific Context

### 🏢 Business Domain
\`\`\`markdown
- **Industry**: ${business_domain}
- **Target Users**: API consumers, web/mobile clients
- **Key Features**: [Core API functionality - TO BE DEFINED]
- **Business Rules**: [Domain-specific validation - TO BE DEFINED]
- **Compliance**: [Regulatory requirements - TO BE DEFINED]
\`\`\`

### 📊 Data Models
\`\`\`markdown
- **Core Entities**: [Define your main entities]
- **Relationships**: ${orm_preference} relationships with proper lazy loading
- **Business Logic**: Service layer with domain validation
- **Data Transfer**: Pydantic schemas for API serialization
\`\`\`

## 🚀 Project-Specific Commands

### 🎨 Quick Scaffolding
\`\`\`markdown
"/create-${framework}-endpoint [resource]" - Create ${framework_display} CRUD endpoint
"/create-model [entity]" - Create database model with relationships
"/create-schema [entity]" - Create Pydantic model with validation
"/create-service [domain]" - Create business logic service
"/create-repository [entity]" - Create repository pattern implementation
\`\`\`

### 🧪 Testing Commands
\`\`\`markdown
"/test-endpoint [endpoint]" - Generate API endpoint tests
"/test-service [service]" - Generate service layer tests
"/test-integration [feature]" - Generate integration tests
"/test-database [model]" - Generate database model tests
\`\`\`

### 📚 Documentation Commands
\`\`\`markdown
"/document-api [endpoint]" - Generate ${api_docs}
"/document-service [service]" - Generate service documentation
"/document-setup" - Generate project setup documentation
\`\`\`

EOF

    # Add framework-specific project structure
    if [ "$framework" = "fastapi" ]; then
        cat >> "$target_dir/.github/copilot-instructions.md" << 'EOF'
## 📁 FastAPI Project Structure

### 🗂️ Standard Project Structure
```
project-root/
├── app/                        # Main application package
│   ├── __init__.py
│   ├── main.py                # FastAPI app entry point
│   ├── core/                  # Core functionality
│   │   ├── __init__.py
│   │   ├── config.py          # Pydantic settings
│   │   ├── security.py        # JWT, OAuth2 utilities
│   │   ├── database.py        # SQLAlchemy setup
│   │   └── dependencies.py    # FastAPI dependencies
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
│   ├── models/                # SQLAlchemy models
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
├── .env.example              # Environment variables template
├── pyproject.toml            # Poetry configuration
├── Dockerfile
├── docker-compose.yml
└── README.md
```

### 🚀 FastAPI Code Templates

#### FastAPI Endpoint Template
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
    """Create new user."""
    try:
        user_service = UserService(db)
        user = await user_service.create_user(user_in)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
```
EOF
    elif [ "$framework" = "django" ]; then
        cat >> "$target_dir/.github/copilot-instructions.md" << 'EOF'
## 📁 Django Project Structure

### 🗂️ Standard Project Structure
```
project-root/
├── config/                    # Django project settings
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py           # Base settings
│   │   ├── development.py    # Dev settings
│   │   ├── production.py     # Prod settings
│   │   └── testing.py        # Test settings
│   ├── urls.py               # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── apps/                      # Django applications
│   ├── __init__.py
│   ├── users/                # User management app
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   ├── tests/
│   │   └── migrations/
│   └── core/                 # Core functionality
│       ├── __init__.py
│       ├── models.py         # Base models
│       ├── permissions.py
│       ├── pagination.py
│       └── utils.py
├── tests/                     # Test files
├── requirements/              # Requirements files
│   ├── base.txt
│   ├── development.txt
│   ├── production.txt
│   └── testing.txt
├── manage.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

### 🚀 Django Code Templates

#### Django REST ViewSet Template
```python
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import User
from .serializers import UserSerializer, UserCreateSerializer
from .filters import UserFilter

class UserViewSet(viewsets.ModelViewSet):
    """User management ViewSet."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer
```
EOF
    elif [ "$framework" = "flask" ]; then
        cat >> "$target_dir/.github/copilot-instructions.md" << 'EOF'
## 📁 Flask Project Structure

### 🗂️ Standard Project Structure
```
project-root/
├── app/                       # Main application package
│   ├── __init__.py           # Flask app factory
│   ├── models/               # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── base.py
│   ├── api/                  # API blueprints
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── users.py
│   │   └── errors.py
│   ├── services/             # Business logic
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── auth_service.py
│   ├── schemas/              # Marshmallow schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── auth.py
│   └── utils/                # Utility functions
│       ├── __init__.py
│       └── helpers.py
├── migrations/               # Flask-Migrate files
├── tests/                    # Test files
├── config.py                 # Configuration
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

### 🚀 Flask Code Templates

#### Flask API Resource Template
```python
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError

from app.services.user_service import UserService
from app.schemas.user import UserSchema, UserCreateSchema

class UserListResource(Resource):
    def __init__(self):
        self.user_service = UserService()
        self.user_schema = UserSchema()
        self.user_create_schema = UserCreateSchema()

    @jwt_required()
    def get(self):
        """Get list of users."""
        users = self.user_service.get_all_users()
        return self.user_schema.dump(users, many=True)

    @jwt_required()
    def post(self):
        """Create new user."""
        try:
            user_data = self.user_create_schema.load(request.json)
            user = self.user_service.create_user(user_data)
            return self.user_schema.dump(user), 201
        except ValidationError as e:
            return {'errors': e.messages}, 400
```
EOF
    fi

    # Add common footer
    cat >> "$target_dir/.github/copilot-instructions.md" << 'EOF'

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
EOF

    print_success "Generated copilot-instructions.md for $project_name"
}

# Function to create additional project files
create_additional_files() {
    local target_dir="$1"
    local framework="$2"
    
    # Create .env.example
    if [ ! -f "$target_dir/.env.example" ]; then
        cat > "$target_dir/.env.example" << EOF
# Database
DATABASE_URL=postgresql://username:password@localhost:5432/database_name

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Redis
REDIS_URL=redis://localhost:6379/0

# Environment
ENVIRONMENT=development
DEBUG=True

# CORS
ALLOWED_ORIGINS=["http://localhost:3000", "http://localhost:8080"]

# Email (optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
EOF
        print_success "Created .env.example file"
    fi
    
    # Create .gitignore for Python
    if [ ! -f "$target_dir/.gitignore" ]; then
        cat > "$target_dir/.gitignore" << 'EOF'
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Virtual environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Database
*.db
*.sqlite3

# Logs
logs/
*.log

# Docker
.dockerignore

# Alembic
alembic/versions/*.py
!alembic/versions/
EOF
        print_success "Created .gitignore file"
    fi
    
    # Create pre-commit config
    if [ ! -f "$target_dir/.pre-commit-config.yaml" ]; then
        cat > "$target_dir/.pre-commit-config.yaml" << 'EOF'
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
        language_version: python3

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: ["--profile", "black"]

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
        args: ["--max-line-length=88", "--extend-ignore=E203,W503"]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.3.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
EOF
        print_success "Created .pre-commit-config.yaml file"
    fi
}

# Main script
main() {
    print_info "🚀 Python Backend Project Copilot Setup"
    echo
    
    # Get project information
    if [ -n "$1" ]; then
        PROJECT_NAME="$1"
    else
        PROJECT_NAME=$(get_input "Enter project name" "my-python-api")
    fi
    
    # Determine target directory
    if [ "$PROJECT_NAME" = "." ] || [ "$PROJECT_NAME" = "./" ]; then
        TARGET_DIR="$(pwd)"
        PROJECT_NAME=$(basename "$(pwd)")
    else
        TARGET_DIR="$(pwd)/$PROJECT_NAME"
    fi
    
    print_info "Project directory: $TARGET_DIR"
    
    # Create project directory if it doesn't exist
    if [ ! -d "$TARGET_DIR" ]; then
        create_dir "$TARGET_DIR"
    fi
    
    # Detect existing project structure
    PROJECT_STRUCTURE=$(detect_project_structure "$TARGET_DIR")
    DETECTED_FRAMEWORK=$(detect_framework "$TARGET_DIR")
    
    if [ "$DETECTED_FRAMEWORK" != "unknown" ]; then
        print_info "Detected framework: $DETECTED_FRAMEWORK"
        FRAMEWORK="$DETECTED_FRAMEWORK"
    else
        if [ -n "$2" ]; then
            FRAMEWORK="$2"
        else
            echo
            print_info "Available frameworks:"
            echo "1. FastAPI (recommended for modern async APIs)"
            echo "2. Django (full-featured web framework)"
            echo "3. Flask (lightweight and flexible)"
            echo
            FRAMEWORK=$(get_input "Choose framework (fastapi/django/flask)" "$DEFAULT_FRAMEWORK")
        fi
    fi
    
    # Get additional project information
    echo
    DATABASE=$(get_input "Database type (postgresql/mysql/sqlite/mongodb)" "$DEFAULT_DATABASE")
    DEPLOYMENT=$(get_input "Deployment method (docker/aws/azure/gcp/heroku)" "$DEFAULT_DEPLOYMENT")
    BUSINESS_DOMAIN=$(get_input "Business domain (e-commerce/fintech/healthtech/edtech/other)" "Web Application")
    
    # Confirm settings
    echo
    print_info "Project Configuration:"
    echo "  📁 Project Name: $PROJECT_NAME"
    echo "  🔧 Framework: $FRAMEWORK"
    echo "  🗄️  Database: $DATABASE"
    echo "  🚀 Deployment: $DEPLOYMENT"
    echo "  🏢 Business Domain: $BUSINESS_DOMAIN"
    echo "  📂 Target Directory: $TARGET_DIR"
    echo
    
    read -p "Continue with this configuration? (y/N): " confirm
    if [[ ! $confirm =~ ^[Yy]$ ]]; then
        print_warning "Setup cancelled by user"
        exit 0
    fi
    
    # Generate files
    echo
    print_info "Generating project files..."
    
    # Generate copilot instructions
    generate_copilot_instructions "$PROJECT_NAME" "$FRAMEWORK" "$DATABASE" "$DEPLOYMENT" "$BUSINESS_DOMAIN" "$TARGET_DIR"
    
    # Create additional files
    create_additional_files "$TARGET_DIR" "$FRAMEWORK"
    
    # Success message
    echo
    print_success "🎉 Python Backend Project Copilot Setup Complete!"
    echo
    print_info "Generated files:"
    echo "  📄 .github/copilot-instructions.md - GitHub Copilot configuration"
    echo "  📄 .env.example - Environment variables template"
    echo "  📄 .gitignore - Git ignore rules"
    echo "  📄 .pre-commit-config.yaml - Code quality hooks"
    echo
    print_info "Next steps:"
    echo "  1. Update business domain specifics in copilot-instructions.md"
    echo "  2. Copy .env.example to .env and update values"
    echo "  3. Install pre-commit hooks: pre-commit install"
    echo "  4. Start coding with GitHub Copilot! 🎯"
    echo
    
    if [ "$TARGET_DIR" != "$(pwd)" ]; then
        print_info "To navigate to your project:"
        echo "  cd $TARGET_DIR"
    fi
}

# Help function
show_help() {
    echo "Python Backend Project Copilot Setup Script"
    echo
    echo "Usage:"
    echo "  $0 [project-name] [framework]"
    echo
    echo "Arguments:"
    echo "  project-name    Name of the project (optional)"
    echo "  framework       Python framework: fastapi, django, or flask (optional)"
    echo
    echo "Examples:"
    echo "  $0                          # Interactive mode"
    echo "  $0 my-api                   # Create project 'my-api'"
    echo "  $0 my-api fastapi          # Create FastAPI project"
    echo "  $0 . django                # Setup Django in current directory"
    echo
    echo "Options:"
    echo "  -h, --help      Show this help message"
    echo
}

# Parse command line arguments
case "$1" in
    -h|--help)
        show_help
        exit 0
        ;;
    *)
        main "$@"
        ;;
esac