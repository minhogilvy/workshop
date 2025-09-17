# 🎯 GitHub Copilot Instructions

## 📋 Project Context

### 🏗️ Project Overview
- **Project Name**: [Project Name]
- **Project Type**: [Web App / Mobile App / API / Library / CLI Tool / etc.]
- **Tech Stack**: [Main technology stack]
- **Framework**: [React, Vue, Angular, Express, FastAPI, Django, Flask, etc.]
- **Database**: [PostgreSQL, MongoDB, MySQL, SQLite, etc.]
- **Deployment**: [AWS, Azure, GCP, Vercel, Netlify, Heroku, etc.]

### 🎨 Architecture & Patterns
- **Architecture Pattern**: [MVC, Clean Architecture, Layered, Microservices, etc.]
- **Design Patterns**: [Repository, Factory, Observer, etc.]
- **Code Organization**: [Module structure, folder conventions]

## 🔧 Development Guidelines

### 📝 Coding Standards
```markdown
- **Language**: [JavaScript/TypeScript/Python/Java/etc.]
- **Style Guide**: [Airbnb, Google, Prettier, ESLint config]
- **Naming Convention**: [camelCase, PascalCase, snake_case rules]
- **File Structure**: [Component-based, feature-based, layer-based]
```

### 🎯 Code Quality Requirements
- **Test Coverage**: Minimum 80% for critical functions
- **Documentation**: JSDoc/docstrings for public APIs
- **Error Handling**: Comprehensive error handling and logging
- **Performance**: Consider performance implications for all solutions
- **Security**: Follow OWASP guidelines and security best practices

### 🏷️ Technology-Specific Guidelines

#### Frontend (if applicable)
```markdown
- **Component Structure**: Functional components with hooks
- **State Management**: [Redux, Zustand, Context API, etc.]
- **Styling**: [CSS Modules, Styled Components, Tailwind, etc.]
- **Testing**: [Jest, Testing Library, Cypress, etc.]
```

#### Backend (if applicable)
```markdown
- **API Design**: RESTful principles, proper HTTP status codes
- **Database**: [ORM/ODM preferences, migration strategy]
- **Authentication**: [JWT, OAuth, session-based]
- **Caching**: [Redis, memory cache, CDN strategy]
```

#### Python-Specific (if applicable)
```markdown
- **Framework**: [FastAPI, Django, Flask, Starlette]
- **ORM**: [SQLAlchemy, Django ORM, Tortoise ORM, Peewee]
- **Testing**: [pytest, unittest, FastAPI TestClient]
- **Code Style**: [Black, flake8, mypy, pre-commit hooks]
- **Dependencies**: [Poetry, pip-tools, pipenv]
- **Async**: [asyncio, async/await patterns]
```

#### DevOps (if applicable)
```markdown
- **CI/CD**: [GitHub Actions, GitLab CI, Jenkins workflow]
- **Containerization**: Docker best practices
- **Infrastructure**: [IaC tools, cloud services preferences]
- **Monitoring**: [Logging, metrics, alerting setup]
```

## 🎪 Project-Specific Context

### 🏢 Business Domain
```markdown
- **Industry**: [E-commerce, FinTech, HealthTech, EdTech, etc.]
- **Target Users**: [End users, admins, developers, etc.]
- **Key Features**: [Core functionality list]
- **Business Rules**: [Domain-specific constraints and requirements]
```

### 📊 Data Models
```markdown
- **Core Entities**: [User, Product, Order, etc.]
- **Relationships**: [One-to-many, many-to-many mappings]
- **Business Logic**: [Validation rules, workflows]
```

### 🔐 Security Requirements
```markdown
- **Authentication**: [Requirements and implementation details]
- **Authorization**: [Role-based, permission-based rules]
- **Data Privacy**: [GDPR, CCPA compliance requirements]
- **Security Standards**: [Industry-specific security requirements]
```

## 🎯 AI Assistant Behavior Guidelines

### 💬 Communication Preferences
- **Language**: English for explanations and code comments
- **Detail Level**: [Beginner, Intermediate, Advanced explanations]
- **Code Style**: Provide comprehensive solutions with proper error handling
- **Examples**: Always include practical examples and use cases

### 🔄 Development Workflow
```markdown
1. **Analysis**: Understand requirements before coding
2. **Design**: Suggest architecture/approach before implementation
3. **Implementation**: Clean, documented, tested code
4. **Review**: Point out potential issues and improvements
5. **Documentation**: Update relevant docs and comments
```

### 🎭 Response Format Preferences
```markdown
- **Code Blocks**: Include language specification
- **Explanations**: Step-by-step reasoning
- **Alternatives**: Provide multiple approaches when applicable
- **Best Practices**: Highlight best practices and common pitfalls
- **Testing**: Include test examples for new code
```

## 🚀 Project-Specific Commands

### 🎨 Custom Shortcuts
```markdown
# Quick scaffolding
"/create-component [name]" - Create React component with boilerplate
"/create-api [resource]" - Create REST API endpoints
"/create-model [entity]" - Create database model with validations
"/create-fastapi [resource]" - Create FastAPI endpoint with validation
"/create-django-view [name]" - Create Django view with serializer
"/create-pydantic [model]" - Create Pydantic model with validation

# Testing shortcuts
"/test-component [name]" - Generate component tests
"/test-api [endpoint]" - Generate API integration tests
"/test-e2e [feature]" - Generate E2E test scenarios
"/test-pytest [function]" - Generate pytest test cases

# Documentation
"/document-api [endpoint]" - Generate API documentation
"/document-component [name]" - Generate component documentation
"/document-python [module]" - Generate Python module documentation
```

### 🔧 Development Commands
```markdown
# Code quality
"/review" - Comprehensive code review
"/refactor" - Suggest refactoring opportunities
"/optimize" - Performance optimization suggestions

# Debugging
"/debug [issue]" - Systematic debugging approach
"/troubleshoot [error]" - Error investigation and resolution
"/analyze [performance]" - Performance analysis
"/debug-python [traceback]" - Python-specific debugging
"/profile-python [function]" - Python performance profiling
```

## 📁 File Structure Context

### 🗂️ Project Structure
```
project-root/
├── src/                    # Source code
│   ├── components/     # Reusable UI components (frontend)
│   ├── pages/          # Page components/routes (frontend)
│   ├── services/       # API calls and business logic
│   ├── utils/          # Helper functions
│   ├── hooks/          # Custom React hooks (if React)
│   ├── types/          # TypeScript type definitions
│   ├── models/         # Database models (Python)
│   ├── routers/        # API routers (FastAPI)
│   ├── schemas/        # Pydantic schemas (Python)
│   └── core/           # Core functionality (Python)
├── tests/              # Test files
├── docs/               # Documentation
├── config/             # Configuration files
└── requirements/       # Python dependencies (if Python)
```

### 🎯 File Naming Conventions
```markdown
- **Components**: PascalCase (UserProfile.tsx)
- **Services**: camelCase (userService.ts)
- **Utilities**: camelCase (dateUtils.ts)
- **Types**: PascalCase (UserTypes.ts)
- **Tests**: [filename].test.[ext]
- **Python Modules**: snake_case (user_service.py)
- **Python Classes**: PascalCase (UserService)
- **Python Functions**: snake_case (get_user_profile)
- **Python Constants**: UPPER_SNAKE_CASE (DATABASE_URL)
```

## 🎪 Examples & Templates

### 🎨 Component Template
```typescript
// Template cho React functional component
interface [ComponentName]Props {
  // Props definition
}

export const [ComponentName]: React.FC<[ComponentName]Props> = ({
  // Destructured props
}) => {
  // Component logic

  return (
    // JSX template
  );
};
```

### 🔧 Service Template
```typescript
// Template for TypeScript service class
export class [ServiceName]Service {
  constructor(private readonly dependency: Dependency) {}

  async [methodName](): Promise<ReturnType> {
    try {
      // Implementation with error handling
    } catch (error) {
      // Error handling
    }
  }
}
```

### 🐍 Python Service Template
```python
# Template for Python service class
from typing import Optional, List
from sqlalchemy.orm import Session
from .models import [ModelName]
from .schemas import [SchemaName]

class [ServiceName]Service:
    def __init__(self, db: Session):
        self.db = db

    async def [method_name](self, item_id: int) -> Optional[[ModelName]]:
        """Method description with proper docstring."""
        try:
            # Implementation with error handling
            return self.db.query([ModelName]).filter([ModelName].id == item_id).first()
        except Exception as e:
            # Error handling
            raise e
```

## 🏆 Success Criteria

### ✅ Definition of Done
- [ ] Code follows project conventions
- [ ] Comprehensive error handling implemented
- [ ] Unit tests written và passing
- [ ] Documentation updated
- [ ] Performance impact assessed
- [ ] Security considerations addressed
- [ ] Code review completed

### 🎯 Quality Gates
- **Functionality**: Solution meets requirements completely
- **Reliability**: Robust error handling và edge case coverage
- **Performance**: Acceptable performance characteristics
- **Maintainability**: Clean, readable, well-documented code
- **Testability**: Easy to test và verify

---

## 🚨 Important Notes

### ⚠️ Constraints
- **Legacy Code**: [Any legacy system constraints]
- **Performance**: [Critical performance requirements]
- **Browser Support**: [Required browser compatibility]
- **Mobile Support**: [Mobile responsiveness requirements]

### 🔄 Regular Updates
- Review and update instructions quarterly
- Add new patterns and conventions as project evolves
- Document lessons learned and best practices

---

**Remember**: Update this file when project requirements change to ensure AI assistant always has accurate context! 🎯