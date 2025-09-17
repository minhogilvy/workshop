# 🎯 Project-Specific Templates

## 🌐 Frontend Framework Templates

### ⚛️ **React Project Templates**

#### 🎨 **Next.js App Template**
```markdown
Setup Next.js application with [Project Name]:

**Project Configuration:**
- Next.js version: [13+/14+ with App Router]
- TypeScript: Full type safety implementation
- Styling: [Tailwind CSS/CSS Modules/styled-components]
- State management: [Zustand/Redux Toolkit/Context API]
- Authentication: [NextAuth.js/Auth0/custom]
- Database: [Prisma + PostgreSQL/MongoDB/Supabase]

**Structure Requirements:**
- App router with nested layouts
- Server and client components optimization
- API routes with validation
- Middleware for authentication
- Dynamic imports for performance
- SEO optimization with metadata API

**Features:**
- Dark/light theme switching
- Responsive design with mobile-first approach
- Internationalization (i18n) setup
- Performance monitoring
- Error boundary implementation
- Progressive Web App (PWA) capabilities
```

#### 📱 **React Native Template**
```markdown
Create React Native app [App Name]:

**Tech Stack:**
- React Native version: [latest stable]
- Navigation: React Navigation v6
- State management: [Redux Toolkit/Zustand]
- Styling: [NativeWind/styled-components]
- Backend: [Firebase/Supabase/custom API]
- Storage: AsyncStorage/SecureStore

**Platform Features:**
- iOS and Android compatibility
- Push notifications setup
- Deep linking configuration
- Biometric authentication
- Offline data synchronization
- Camera and gallery integration

**Development Setup:**
- TypeScript configuration
- ESLint and Prettier setup
- Flipper debugging integration
- Automated testing with Jest
- CI/CD with GitHub Actions
- App store deployment preparation
```

### 🖼️ **Vue.js Project Templates**

#### ⚡ **Nuxt.js Application Template**
```markdown
Build Nuxt.js application [Project Name]:

**Configuration:**
- Nuxt 3 with composition API
- TypeScript support
- Server-side rendering (SSR)
- Static site generation (SSG) options
- PWA module integration
- Content management with @nuxt/content

**Features Implementation:**
- Dynamic routing with file-based system
- Middleware for authentication
- Plugin system for third-party integrations
- Auto-imports for components and composables
- SEO optimization with useSeoMeta
- Performance optimization with lazy loading

**Styling and UI:**
- [Tailwind CSS/Vuetify/PrimeVue] integration
- Component library setup
- Responsive design implementation
- Animation with CSS transitions
- Icon system setup
```

### 🅰️ **Angular Project Templates**

#### 🏗️ **Enterprise Angular Template**
```markdown
Develop enterprise Angular application:

**Architecture:**
- Angular 17+ with standalone components
- Modular architecture with feature modules
- Lazy loading strategy
- State management with NgRx
- Dependency injection patterns

**Enterprise Features:**
- Authentication with JWT
- Role-based access control (RBAC)
- Internationalization (i18n)
- Error handling with global error handler
- Logging and monitoring integration
- Performance optimization techniques

**Development Standards:**
- TypeScript strict mode
- Angular CLI schematics
- Unit testing with Jasmine/Karma
- E2E testing with Cypress
- Code quality with ESLint and Prettier
- Documentation with Compodoc
```

## 🔧 Backend Framework Templates

### 🚀 **Node.js API Templates**

#### 🌐 **Express.js REST API Template**
```markdown
Build Express.js REST API for [Domain]:

**Tech Stack:**
- Express.js with TypeScript
- Database: [PostgreSQL/MongoDB] with [Prisma/Mongoose]
- Authentication: JWT with refresh tokens
- Validation: [Joi/Zod/express-validator]
- Testing: Jest with supertest
- Documentation: Swagger/OpenAPI

**API Architecture:**
- RESTful endpoint design
- Middleware chain optimization
- Error handling middleware
- Rate limiting implementation
- CORS configuration
- Security headers with helmet

**Features:**
- User authentication and authorization
- File upload handling
- Email service integration
- Background job processing
- Caching with Redis
- Database migrations
- API versioning strategy
```

#### ⚡ **Fastify API Template**
```markdown
Create high-performance Fastify API:

**Performance Focus:**
- Fastify with TypeScript
- JSON schema validation
- Serialization optimization
- Plugin architecture
- Request/response lifecycle hooks

**Features:**
- Authentication plugins
- Database connection management
- Error handling strategies
- Logging with structured logs
- Metrics collection
- Health check endpoints
- Graceful shutdown handling
```

### 🐍 **Python Backend Templates**

#### 🚀 **FastAPI Template**
```markdown
Develop FastAPI application for [Use Case]:

**Modern Python Stack:**
- FastAPI with Pydantic models
- SQLAlchemy 2.0 with async support
- Alembic migrations
- Pytest for testing
- Celery for background tasks

**API Features:**
- Automatic OpenAPI documentation
- Type hints throughout
- Dependency injection system
- Background task processing
- WebSocket support
- Authentication with OAuth2
- CORS and security middleware

**Production Setup:**
- Docker containerization
- Redis for caching and sessions
- PostgreSQL with connection pooling
- Monitoring with Prometheus
- Logging with structured format
```

#### 🌶️ **Django REST Template**
```markdown
Build Django REST API with best practices:

**Django Ecosystem:**
- Django REST Framework
- Django ORM with optimizations
- Celery with Redis/RabbitMQ
- Django Channels for real-time features
- pytest-django for testing

**Features:**
- ViewSets and serializers
- Permission classes
- Filtering and pagination
- API versioning
- Throttling and rate limiting
- Custom authentication backends
- Admin interface customization
```

#### 🐍 **Flask API Template**
```markdown
Create Flask API with modern practices:

**Flask Stack:**
- Flask with Flask-RESTful
- SQLAlchemy with Flask-Migrate
- Marshmallow for serialization
- Flask-JWT-Extended for auth
- Flask-CORS for cross-origin
- Celery for background tasks

**Project Structure:**
- Blueprint-based organization
- Factory pattern for app creation
- Configuration management
- Error handling with custom exceptions
- API documentation with Flask-RESTX
- Testing with pytest and factory_boy
```

#### 📊 **Python Data Science Template**
```markdown
Create Python Data Science project for [Domain]:

**Data Science Stack:**
- Pandas for data manipulation
- NumPy for numerical computing
- Scikit-learn for machine learning
- Matplotlib/Seaborn for visualization
- Jupyter notebooks for exploration
- MLflow for experiment tracking

**Project Structure:**
- Data pipeline with Prefect/Airflow
- Feature engineering modules
- Model training and evaluation
- Model serving with FastAPI
- Configuration management with Hydra
- Version control with DVC

**MLOps Features:**
- Model versioning and registry
- Automated testing for data/models
- CI/CD for model deployment
- Monitoring and drift detection
- A/B testing framework
- Documentation with Sphinx
```

## 🗄️ Database Templates

### 🐘 **PostgreSQL Setup Template**
```markdown
Setup PostgreSQL database for [Application]:

**Database Design:**
- Schema design with normalization
- Index strategy for performance
- Constraint definitions
- Foreign key relationships
- Stored procedures and functions

**Performance Optimization:**
- Query optimization techniques
- Connection pooling setup
- Partitioning strategy
- Backup and recovery procedures
- Monitoring and alerting

**Security:**
- User role management
- Row-level security policies
- SSL/TLS configuration
- Audit logging setup
- Data encryption strategies
```

### 🍃 **MongoDB Setup Template**
```markdown
Configure MongoDB for [Application]:

**Document Design:**
- Collection schema design
- Embedding vs referencing strategy
- Index optimization
- Aggregation pipeline design
- GridFS for file storage

**Scalability:**
- Replica set configuration
- Sharding strategy
- Read preferences
- Write concerns
- Connection pooling

**Operations:**
- Backup and restore procedures
- Performance monitoring
- Security configuration
- Data migration strategies
```

## ☁️ Cloud Platform Templates

### ☁️ **AWS Deployment Template**
```markdown
Deploy application to AWS:

**Infrastructure:**
- EC2/ECS/Lambda deployment strategy
- RDS/DynamoDB database setup
- S3 for static assets
- CloudFront CDN configuration
- VPC and security groups

**CI/CD Pipeline:**
- GitHub Actions/AWS CodePipeline
- Docker containerization
- Blue-green deployment
- Rolling updates strategy
- Environment management

**Monitoring:**
- CloudWatch logs và metrics
- Application performance monitoring
- Cost optimization
- Security best practices
- Backup và disaster recovery
```

### 🔵 **Azure Deployment Template**
```markdown
Deploy to Azure cloud platform:

**Azure Services:**
- App Service/Container Instances/Functions
- Azure SQL/CosmosDB setup
- Blob Storage için assets
- CDN configuration
- Virtual Network setup

**DevOps:**
- Azure DevOps pipelines
- Container registry
- Key Vault för secrets
- Application Insights monitoring
- Resource group organization
```

## 📱 Mobile Development Templates

### 📱 **Flutter Project Template**
```markdown
Create Flutter application [App Name]:

**Development Stack:**
- Flutter with Dart
- State management: [Bloc/Provider/Riverpod]
- Navigation: GoRouter
- Local storage: Hive/SQLite
- HTTP client: Dio with interceptors

**Features:**
- Cross-platform compatibility
- Responsive design with adaptive layouts
- Offline data synchronization
- Push notifications
- Deep linking
- Biometric authentication
- Camera and media handling

**Architecture:**
- Clean architecture implementation
- Repository pattern
- Dependency injection with GetIt
- Error handling strategies
- Testing strategy with widget tests
```

### 🍎 **iOS Swift Template**
```markdown
Develop iOS app with Swift:

**iOS Development:**
- SwiftUI with Combine
- Core Data/SQLite integration
- URLSession networking
- Keychain services
- Push notifications setup

**Architecture:**
- MVVM pattern implementation
- Protocol-oriented programming
- Dependency injection
- Error handling with Result type
- Unit testing with XCTest

**Features:**
- iOS-specific integrations
- Watch app companion
- Widget extensions
- Shortcuts support
- Accessibility implementation
```

---

## 🎯 Template Usage Guide

### 📋 **Template Selection**
1. Choose template based on project type
2. Customize technology stack preferences
3. Add project-specific requirements
4. Include business domain context
5. Specify performance and security needs

### 🛠️ **Customization Process**
1. Replace placeholder values
2. Add domain-specific features
3. Include team preferences
4. Specify deployment environment
5. Add compliance requirements

### 🚀 **Implementation Strategy**
1. Start with MVP features
2. Implement core functionality first
3. Add advanced features incrementally
4. Focus on testing and documentation
5. Plan deployment and monitoring

**Remember**: Templates are starting points - customize to fit your specific needs! 🎯