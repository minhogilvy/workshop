# 🎨 Development Templates

## ### ⚛️ **Angular Component Template**
```markdown
Generate Angular component [ComponentName]:
- Input properties: [list @Input properties]
- Outpu### 📱 **CRUD Operations Template**
```markdown
Implement CRUD for [Entity]:
- Create: [validation, sanitization, conflict handling]
- Read: [filterin### 📚 **API Documentation Template**
```markdown
Document API for [Service/Module]:
- Overview: [API purpose and scope]
- Authentication: [how to authenticate requests]
- Base URL: [API endpoint base URL]
- Endpoints: [list all available endpoints]
- Request format: [headers, body, parameters]
- Response format: [success and error responses]
- Status codes: [HTTP status code meanings]
- Rate limiting: [usage limits and quotas]
- Examples: [practical request/response examples]
- SDKs: [available client libraries]
- Changelog: [version history and changes]
- Support: [contact information, issue reporting]
```orting, search]
- Update: [partial updates, optimistic locking]
- Delete: [soft/hard delete, cascade rules]
- Batch operations: [bulk create/update/delete]
- Data validation: [schema validation, business rules]
- Error handling: [validation errors, not found, conflicts]
- Caching: [read optimization strategy]
- Audit trail: [change tracking]
- Permissions: [user-based access control]
- API endpoints: [RESTful URL design]
- Tests: [comprehensive CRUD test coverage]
```

### 🐍 **Python SQLAlchemy CRUD Template**
```markdown
Implement SQLAlchemy CRUD for [Entity]:
- Model definition: [SQLAlchemy model with relationships]
- Schema: [Pydantic models for validation]
- Repository: [data access layer with error handling]
- Service: [business logic layer]
- Dependencies: [database session injection]
- Async operations: [async/await with asyncpg]
- Transactions: [context managers for rollback]
- Bulk operations: [bulk_insert_mappings]
- Caching: [Redis integration for reads]
- Migrations: [Alembic migration scripts]
- Tests: [pytest with test database]
- Documentation: [API docs with examples]
```@Output EventEmitters]
- Services: [inject required services]
- Lifecycle hooks: [implement needed hooks]
- Template: [describe UI structure]
- Styling: [SCSS with component styles]
- Reactive forms: [if form component]
- Testing: Jasmine/Karma unit tests
- Documentation: README with usage examples
```

### 🐍 **Python Class Template**
```markdown
Create Python class [ClassName] with:
- Attributes: [list class attributes with types]
- Methods: [list methods with parameters and return types]
- Inheritance: [base classes if applicable]
- Properties: [getter/setter methods]
- Documentation: [comprehensive docstrings]
- Type hints: [full type annotation]
- Error handling: [custom exceptions]
- Tests: [pytest test cases]
- Validation: [input validation with Pydantic]
- Async support: [async/await methods if needed]
``` Creation

### 📱 **React Component Template**
```markdown
Create React component named [ComponentName] with:
- Props: [list props with types]
- State: [list state variables]
- Functionality: [describe main features]
- Styling: [CSS modules/Tailwind/styled-components]
- Accessibility: ARIA labels and keyboard navigation
- Error boundaries: Handle component-level errors
- TypeScript: Full type definitions
- Tests: Unit tests with React Testing Library
- Storybook: Component stories with different states
```

### 🌐 **Vue Component Template**
```markdown
Create Vue 3 component [ComponentName] with Composition API:
- Props: [define props with types]
- Composables: [list reusable logic]
- Events: [emit events with payload types]
- Slots: [named slots with fallback content]
- Styling: [Scoped CSS/Tailwind classes]
- Validation: Props validation with PropTypes
- Tests: Vue Test Utils with Jest
- Documentation: Component usage examples
```

### ⚛️ **Angular Component Template**
```markdown
Generate Angular component [ComponentName]:
- Input properties: [list @Input properties]
- Output events: [list @Output EventEmitters]
- Services: [inject required services]
- Lifecycle hooks: [implement needed hooks]
- Template: [describe UI structure]
- Styling: [SCSS with component styles]
- Reactive forms: [if form component]
- Testing: Jasmine/Karma unit tests
- Documentation: README with usage examples
```

## 🔧 API Development

### 🌐 **REST API Endpoint Template**
```markdown
Create REST API endpoint for [Resource]:
- HTTP Method: [GET/POST/PUT/DELETE]
- Endpoint: /api/[version]/[resource]
- Request format: [request body schema]
- Response format: [response schema]
- Query parameters: [filtering, pagination, sorting]
- Authentication: [JWT/OAuth/API key validation]
- Authorization: [role-based access control]
- Validation: [input validation rules]
- Error handling: [comprehensive error responses]
- Rate limiting: [requests per minute/hour]
- Caching: [cache strategy if applicable]
- Logging: [request/response logging]
- Documentation: OpenAPI/Swagger specs
- Tests: Integration tests with test data
```

### 🚀 **FastAPI Endpoint Template**
```markdown
Create FastAPI endpoint for [Resource]:
- Route definition: [path with parameters]
- Request model: [Pydantic model for validation]
- Response model: [Pydantic model for serialization]
- Dependencies: [authentication, database injection]
- Query parameters: [filtering with Query models]
- Path parameters: [route parameters with validation]
- Request body: [JSON schema validation]
- Response status: [appropriate HTTP status codes]
- Error handling: [HTTPException with detail]
- Background tasks: [async task processing]
- Documentation: [docstring with examples]
- Tests: [TestClient with pytest]
```

### 🌶️ **Django REST Framework Template**
```markdown
Create Django REST API for [Resource]:
- Serializer: [model serialization with validation]
- ViewSet: [CRUD operations with permissions]
- URL patterns: [router configuration]
- Model: [Django model with relationships]
- Permissions: [custom permission classes]
- Filtering: [django-filter integration]
- Pagination: [custom pagination classes]
- Authentication: [token/session based]
- Throttling: [rate limiting configuration]
- Tests: [APITestCase with fixtures]
- Documentation: [DRF schema generation]
```

### 📊 **GraphQL Schema Template**
```markdown
Design GraphQL schema for [Domain]:
- Types: [define object types]
- Queries: [list query operations]
- Mutations: [list mutation operations]
- Subscriptions: [real-time data if needed]
- Input types: [input validation schemas]
- Resolvers: [data fetching logic]
- DataLoader: [N+1 query prevention]
- Authentication: [context-based auth]
- Authorization: [field-level permissions]
- Error handling: [custom error types]
- Testing: [resolver unit tests]
- Documentation: [schema documentation]
```

### 🗄️ **Database Schema Template**
```markdown
Design database schema for [Entity]:
- Tables/Collections: [main entities]
- Relationships: [foreign keys, references]
- Indexes: [performance optimization]
- Constraints: [data integrity rules]
- Triggers: [automated actions if needed]
- Views: [computed data representations]
- Migration scripts: [schema evolution]
- Seed data: [initial data setup]
- Backup strategy: [data protection plan]
- Performance tuning: [query optimization]
```

## 🎯 Feature Implementation

### 🔐 **Authentication System Template**
```markdown
Implement authentication system:
- User registration: [email/username, password validation]
- Login flow: [credential verification, session creation]
- Password security: [hashing, strength requirements]
- JWT tokens: [generation, validation, refresh]
- OAuth integration: [Google, GitHub, Facebook]
- Multi-factor authentication: [TOTP, SMS]
- Password reset: [email-based flow]
- Session management: [timeout, concurrent sessions]
- Rate limiting: [brute force protection]
- Security headers: [CSRF, XSS protection]
- Audit logging: [login attempts, security events]
- Tests: [auth flow integration tests]
```

### 📱 **CRUD Operations Template**
```markdown
Implement CRUD for [Entity]:
- Create: [validation, sanitization, conflict handling]
- Read: [filtering, pagination, sorting, search]
- Update: [partial updates, optimistic locking]
- Delete: [soft/hard delete, cascade rules]
- Batch operations: [bulk create/update/delete]
- Data validation: [schema validation, business rules]
- Error handling: [validation errors, not found, conflicts]
- Caching: [read optimization strategy]
- Audit trail: [change tracking]
- Permissions: [user-based access control]
- API endpoints: [RESTful URL design]
- Tests: [comprehensive CRUD test coverage]
```

### 🔍 **Search Feature Template**
```markdown
Implement search functionality for [Domain]:
- Search types: [full-text, exact match, fuzzy search]
- Search fields: [searchable attributes]
- Filters: [category, date range, status filters]
- Sorting: [relevance, date, alphabetical]
- Pagination: [cursor-based or offset-based]
- Autocomplete: [suggestion API]
- Search analytics: [query tracking, performance metrics]
- Caching: [search result caching strategy]
- Performance: [indexing strategy, query optimization]
- UI/UX: [search interface design]
- Tests: [search functionality tests]
```

## 🏗️ Architecture & Design

### 🎯 **System Architecture Template**
```markdown
Design system architecture for [Application]:
- High-level overview: [system components diagram]
- Frontend architecture: [SPA/SSR, state management]
- Backend architecture: [microservices/monolith, API design]
- Database design: [SQL/NoSQL choice, schema design]
- Caching strategy: [Redis, CDN, application cache]
- Message queues: [async processing, event-driven]
- Authentication: [SSO, JWT, session management]
- Security: [data encryption, API security, OWASP]
- Monitoring: [logging, metrics, alerting]
- Deployment: [CI/CD pipeline, containerization]
- Scalability: [horizontal/vertical scaling strategy]
- Performance: [optimization strategies]
- Documentation: [architecture decision records]
```

### 🔄 **Design Pattern Template**
```markdown
Implement [Pattern Name] pattern:
- Problem: [what problem does this solve]
- Solution approach: [how pattern addresses the problem]
- Implementation: [code structure and components]
- Benefits: [advantages of using this pattern]
- Trade-offs: [potential disadvantages]
- Use cases: [when to apply this pattern]
- Related patterns: [complementary patterns]
- Example: [practical implementation example]
- Testing strategy: [how to test pattern implementation]
- Documentation: [usage guidelines]
```

## 🧪 Testing Templates

### ✅ **Unit Test Template**
```markdown
Write unit tests for [Function/Class/Component]:
- Test setup: [mocks, fixtures, test data]
- Happy path: [normal operation scenarios]
- Edge cases: [boundary conditions, edge inputs]
- Error cases: [exception handling, invalid inputs]
- Mock dependencies: [external services, databases]
- Assertions: [expected outcomes verification]
- Coverage: [code coverage requirements]
- Performance: [execution time benchmarks]
- Cleanup: [test isolation, resource cleanup]
- Documentation: [test documentation, examples]
```

### 🔗 **Integration Test Template**
```markdown
Write integration tests for [Feature/API]:
- Test environment: [database, external services setup]
- Test data: [realistic test datasets]
- API testing: [request/response validation]
- Database testing: [data persistence verification]
- Authentication: [test with different user roles]
- Error scenarios: [network failures, timeouts]
- Performance: [response time requirements]
- Security: [authorization, input validation]
- Cleanup: [test data cleanup strategy]
- CI/CD integration: [automated test execution]
```

### 🐍 **Python Pytest Template**
```markdown
Write pytest tests for [Module/Function/Class]:
- Fixtures: [setup and teardown with @pytest.fixture]
- Parametrized tests: [@pytest.mark.parametrize]
- Mock objects: [unittest.mock or pytest-mock]
- Test data: [factories with factory_boy]
- Database tests: [pytest-django or pytest-asyncio]
- API tests: [httpx TestClient for FastAPI]
- Async tests: [@pytest.mark.asyncio]
- Coverage: [pytest-cov configuration]
- Markers: [custom test markers for categorization]
- Configuration: [pytest.ini or pyproject.toml]
```

### 🌐 **E2E Test Template**
```markdown
Implement E2E tests for [User Journey]:
- User scenarios: [complete user workflows]
- Test setup: [browser configuration, test environment]
- Page objects: [reusable page interaction models]
- Test data: [user accounts, test content]
- Navigation: [multi-page user flows]
- Form interactions: [input validation, submissions]
- Error handling: [error message verification]
- Cross-browser: [browser compatibility testing]
- Mobile testing: [responsive design verification]
- Performance: [page load times, user experience]
- Reporting: [test results, screenshots, videos]
```

## 📚 Documentation Templates

### 📖 **API Documentation Template**
```markdown
Document API cho [Service/Module]:
- Overview: [API purpose và scope]
- Authentication: [how to authenticate requests]
- Base URL: [API endpoint base URL]
- Endpoints: [list all available endpoints]
- Request format: [headers, body, parameters]
- Response format: [success và error responses]
- Status codes: [HTTP status code meanings]
- Rate limiting: [usage limits và quotas]
- Examples: [practical request/response examples]
- SDKs: [available client libraries]
- Changelog: [version history và changes]
- Support: [contact information, issue reporting]
```

### 🎯 **Feature Documentation Template**
```markdown
Document [Feature Name]:
- Purpose: [what problem this feature solves]
- User stories: [who uses this and why]
- Functionality: [detailed feature description]
- User interface: [screenshots, interaction flows]
- Configuration: [setup and customization options]
- Dependencies: [required components, services]
- Limitations: [known constraints, edge cases]
- Troubleshooting: [common issues and solutions]
- Examples: [usage examples, tutorials]
- FAQ: [frequently asked questions]
- Changelog: [feature evolution history]
```

---

## 🎯 Usage Instructions

1. **Copy template** relevant to your task
2. **Fill in placeholders** with specific requirements
3. **Customize details** based on project needs
4. **Add context** from copilot-instructions.md
5. **Execute prompt** with complete information

**Remember**: Comprehensive input = Superior output! 🚀