# 🎯 Python Backend Copilot Setup Scripts

Automated toolkit for generating `copilot-instructions.md` files for Python backend projects, optimizing GitHub Copilot for your development workflow.

## 📁 Toolkit Contents

```
workshop/
├── setup-python-backend-copilot.sh     # Full interactive setup script
├── quick-setup-copilot.sh               # Quick setup with basic template
├── python-backend-copilot-instructions.md  # Detailed Python backend template
└── README-python-setup.md              # This guide
```

## 🚀 Usage

### Option 1: Quick Setup (Recommended for rapid start)

```bash
# Create copilot config in current directory
./quick-setup-copilot.sh

# Create new project with copilot config
./quick-setup-copilot.sh my-api-project

# Create config in current directory (use ".")
./quick-setup-copilot.sh .
```

**Result**: Creates basic `.github/copilot-instructions.md` with Python backend template.

### Option 2: Full Interactive Setup (For detailed customization)

```bash
# Interactive mode - script will prompt for each setting
./setup-python-backend-copilot.sh

# With existing project name
./setup-python-backend-copilot.sh my-api-project

# With project name and framework
./setup-python-backend-copilot.sh my-api-project fastapi

# Setup in current directory
./setup-python-backend-copilot.sh . django
```

**Result**: Creates complete project setup with:
- `.github/copilot-instructions.md` (customized for framework)
- `.env.example`
- `.gitignore`
- `.pre-commit-config.yaml`

### Option 3: Manual Copy Template

```bash
# Copy template for manual customization
cp python-backend-copilot-instructions.md .github/copilot-instructions.md

# Edit file to match your project
vim .github/copilot-instructions.md
```

## 🎯 Framework Support

### FastAPI (Recommended)
```bash
./setup-python-backend-copilot.sh my-api fastapi
```
- Async/await patterns
- Pydantic validation
- SQLAlchemy with Alembic
- OpenAPI documentation
- JWT authentication

### Django
```bash
./setup-python-backend-copilot.sh my-api django
```
- Django REST Framework
- Django ORM with migrations
- Class-based views
- Django admin integration
- Built-in authentication

### Flask
```bash
./setup-python-backend-copilot.sh my-api flask
```
- Flask-RESTful
- SQLAlchemy with Flask-Migrate
- Marshmallow serialization
- Blueprint organization
- JWT extensions

## 📊 Template Features

### 🎨 Code Generation Commands
```markdown
"/create-fastapi-endpoint [resource]" - Create FastAPI CRUD endpoint
"/create-django-viewset [model]" - Create Django REST ViewSet
"/create-pydantic-schema [entity]" - Create Pydantic model with validation
"/create-sqlalchemy-model [entity]" - Create SQLAlchemy model with relationships
"/create-service-class [domain]" - Create business logic service
```

### 🧪 Testing Commands
```markdown
"/test-fastapi-endpoint [endpoint]" - Generate FastAPI tests
"/test-service-class [service]" - Generate service tests
"/test-integration [feature]" - Generate integration tests
"/test-database [model]" - Generate database tests
```

### 📚 Documentation Commands
```markdown
"/document-api [endpoint]" - Generate OpenAPI docs
"/document-service [service]" - Generate service docs
"/create-api-examples [endpoint]" - Create API examples
```

## 🏗️ Project Structure Standards

### FastAPI Structure
```
app/
├── main.py                    # FastAPI app entry
├── core/                      # Core config & dependencies
├── api/v1/endpoints/          # API endpoints
├── crud/                      # Database operations
├── models/                    # SQLAlchemy models
├── schemas/                   # Pydantic schemas
├── services/                  # Business logic
└── utils/                     # Utilities
```

### Django Structure
```
config/                        # Django settings
apps/                          # Django applications
├── users/                     # User management
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
└── core/                      # Core functionality
```

### Flask Structure
```
app/
├── __init__.py               # Flask factory
├── models/                   # SQLAlchemy models
├── api/                      # API blueprints
├── schemas/                  # Marshmallow schemas
├── services/                 # Business logic
└── utils/                    # Utilities
```

## 🔧 Advanced Configuration

### Auto-detection Features
Script automatically detects:
- **Existing framework**: From `requirements.txt`, `pyproject.toml`, `manage.py`
- **Project structure**: Poetry, pip, pipenv, setuptools
- **Dependencies**: Framework-specific packages

### Customization Options
- **Business domain**: E-commerce, FinTech, HealthTech, EdTech
- **Database**: PostgreSQL, MySQL, MongoDB, SQLite
- **Deployment**: Docker, AWS, Azure, GCP, Heroku
- **Authentication**: JWT, OAuth2, Session-based

## 📝 Example Usage Scenarios

### Scenario 1: New FastAPI Project
```bash
./setup-python-backend-copilot.sh ecommerce-api fastapi
# Interactive prompts:
# Database: postgresql
# Deployment: docker
# Domain: e-commerce
```

### Scenario 2: Existing Django Project
```bash
cd my-existing-django-project
./quick-setup-copilot.sh .
# Create copilot config in current project
```

### Scenario 3: Multiple Microservices
```bash
# User service
./setup-python-backend-copilot.sh user-service fastapi

# Product service
./setup-python-backend-copilot.sh product-service fastapi

# Order service
./setup-python-backend-copilot.sh order-service fastapi
```

## 🎯 Best Practices

### 1. **Project-Specific Customization**
- Update business domain specifics in copilot-instructions.md
- Define core entities and relationships
- Specify compliance requirements (GDPR, HIPAA, etc.)

### 2. **Framework Optimization**
- Use framework-specific templates
- Leverage auto-completion for common patterns
- Follow naming conventions for each framework

### 3. **Code Quality**
- Setup pre-commit hooks
- Configure proper testing with fixtures
- Use type hints consistently

### 4. **Security Considerations**
- Environment variables for sensitive data
- Proper input validation
- Authentication/authorization patterns

## 🔄 Updates and Maintenance

### Regular Updates
```bash
# Update template files when framework changes
cp python-backend-copilot-instructions.md .github/copilot-instructions.md

# Review and update project-specific sections
# - Business rules
# - Core entities
# - Security requirements
```

### Version Control
- Commit copilot-instructions.md to git
- Track changes according to project evolution
- Share templates across team projects

## 🚨 Troubleshooting

### Common Issues

1. **Permission Denied**
   ```bash
   chmod +x setup-python-backend-copilot.sh
   chmod +x quick-setup-copilot.sh
   ```

2. **Script Not Found**
   ```bash
   # Ensure you are in the correct directory
   ls -la *.sh
   ```

3. **Framework Detection Issues**
   ```bash
   # Manually specify framework
   ./setup-python-backend-copilot.sh my-project fastapi
   ```

## 📞 Support

If you have issues or suggestions:
1. Check existing templates in `python-backend-copilot-instructions.md`
2. Review script parameters with `--help`
3. Customize manually for specific requirements

---

**Happy Coding with GitHub Copilot! 🎯🚀**