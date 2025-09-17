# 🚀 Hướng dẫn sử dụng GitHub Copilot hiệu quả

## 📝 1. Tips & Tricks Cơ bản

### 🎯 Cách viết prompt hiệu quả

#### ✅ **Cụ thể và rõ ràng**
```markdown
❌ Tồi: "Tạo một function"
✅ Tốt: "Tạo function JavaScript tính tổng của một mảng số nguyên, có xử lý lỗi cho input không hợp lệ"
```

#### ✅ **Cung cấp ngữ cảnh**
```markdown
❌ Tồi: "Fix bug này"
✅ Tốt: "Trong React component UserProfile, fix lỗi state không update khi props thay đổi. Hiện tại đang dùng useState nhưng cần useEffect để sync với props"
```

#### ✅ **Sử dụng từ khóa chuyên môn**
```markdown
✅ "Implement repository pattern với TypeScript và MongoDB"
✅ "Create REST API endpoint với Express.js, validation middleware và error handling"
✅ "Setup CI/CD pipeline với GitHub Actions cho Node.js app"
```

### 🔥 Các câu lệnh mạnh mẽ

#### **Phân tích và Debug**
```markdown
# Phân tích mã
"Phân tích function này và chỉ ra các vấn đề về performance, security và maintainability"

# Review code
"Code review đoạn này theo best practices, point out code smells và suggest improvements"

# Debug
"Debug lỗi này: [mô tả lỗi]. Kiểm tra logic, data flow và edge cases"
```

#### **Refactoring và Optimization**
```markdown
# Refactor
"Refactor đoạn code này để improve readability, reduce complexity và follow SOLID principles"

# Performance
"Optimize performance của function này, focus vào time complexity và memory usage"

# Clean code
"Apply clean code principles: meaningful names, single responsibility, proper abstraction"
```

#### **Documentation và Testing**
```markdown
# Documentation
"Tạo comprehensive documentation cho API này bao gồm: endpoint specs, request/response examples, error codes"

# Testing
"Viết unit tests với Jest cho function này, cover happy path, edge cases và error scenarios"

# Type safety
"Add TypeScript types cho module này, ensure type safety và improve developer experience"
```

## 🎪 2. Techniques Nâng cao

### 📋 **Template-based Prompting**
```markdown
# Template cho tạo component
"Tạo [Framework] component có tên [ComponentName] với:
- Props: [list props]
- State: [list state]
- Features: [list features]
- Styling: [CSS/Tailwind/styled-components]
- Tests: [testing framework]"

# Template cho API design
"Design REST API cho [domain] với:
- Entity: [entity name]
- CRUD operations: [specific operations]
- Authentication: [auth method]
- Validation: [validation rules]
- Database: [database type]"
```

### 🔄 **Iterative Refinement**
```markdown
1. "Tạo basic version của [feature]"
2. "Enhance với [specific improvement]"
3. "Add error handling và edge cases"
4. "Optimize performance và add caching"
5. "Add comprehensive tests và documentation"
```

### 🎭 **Role-based Prompting**
```markdown
# Senior Developer
"Với vai trò senior developer, review architecture này và suggest scalability improvements"

# Security Expert
"Với góc nhìn security expert, audit code này và point out vulnerabilities"

# DevOps Engineer
"Với vai trò DevOps engineer, design deployment strategy cho application này"
```

## 💡 3. Best Practices cho Different Scenarios

### 🐛 **Debugging & Troubleshooting**
```markdown
# Structured debugging
"Debug issue này theo systematic approach:
1. Reproduce bug với specific steps
2. Analyze logs và error messages
3. Identify root cause
4. Propose solution với risk assessment
5. Test fix thoroughly"

# Performance investigation
"Investigate performance issue:
- Profile application với tools
- Identify bottlenecks
- Measure current metrics
- Implement optimizations
- Validate improvements"
```

### 🏗️ **Architecture & Design**
```markdown
# System design
"Design scalable system cho [use case]:
- Requirements analysis
- Component architecture
- Data flow design
- Technology stack selection
- Scalability considerations
- Security measures"

# Database design
"Design database schema cho [domain]:
- Entity relationships
- Normalization strategy
- Indexing plan
- Query optimization
- Data migration strategy"
```

### 🚀 **Feature Development**
```markdown
# End-to-end feature
"Implement complete feature [feature name]:
1. Requirements breakdown
2. API design
3. Frontend components
4. Backend services
5. Database changes
6. Testing strategy
7. Documentation
8. Deployment plan"
```

## 🎯 4. Context Management Tips

### 📂 **File Context**
- Mở files liên quan trước khi prompt
- Sử dụng `@workspace` để reference toàn bộ project
- Dùng `#file:filename` để reference specific file

### 🔍 **Code Selection**
- Select đoạn code cần focus trước khi prompt
- Sử dụng multi-file selection cho related changes
- Comment inline để clarify intention

### 💬 **Conversation Flow**
```markdown
# Khởi tạo context
"Tôi đang làm việc với [project type] sử dụng [tech stack]. Main goal là [objective]."

# Maintain context
"Continuing từ previous solution, now I need to [next step]"

# Context switching
"Switching context: Now working on [new area] của project"
```

## 🔧 5. Power Commands

### 🎨 **Code Generation**
```markdown
# Full stack feature
"/generate complete CRUD for User management với authentication"

# Boilerplate
"/scaffold React component với TypeScript, props validation, và storybook setup"

# Integration
"/integrate third-party API [API name] với error handling và retry logic"
```

### 🔄 **Refactoring**
```markdown
# Large scale refactoring
"/refactor codebase to use dependency injection pattern"

# Migration
"/migrate từ JavaScript sang TypeScript với full type coverage"

# Modernization
"/update legacy code to use modern ES6+ features và async/await"
```

### 📊 **Analysis**
```markdown
# Code quality
"/analyze code quality và provide actionable improvements"

# Security audit
"/security audit toàn bộ authentication flow"

# Performance review
"/performance analysis với specific bottleneck identification"
```

## 🎪 6. Advanced Techniques

### 🎭 **Multi-step Planning**
```markdown
# Complex task breakdown
"Break down task [complex task] thành actionable steps:
1. Analysis phase
2. Design phase
3. Implementation phase
4. Testing phase
5. Documentation phase
6. Deployment phase"
```

### 🔄 **Incremental Development**
```markdown
# Phase-based development
"Phase 1: Create basic [feature] với minimal functionality"
"Phase 2: Add [enhancement] với proper error handling"
"Phase 3: Optimize performance và add caching"
"Phase 4: Add comprehensive testing và monitoring"
```

### 🎯 **Quality Gates**
```markdown
# Built-in quality checks
"Implement [feature] ensuring:
✅ Code follows project conventions
✅ Proper error handling
✅ Unit tests coverage > 80%
✅ Performance benchmarks met
✅ Security best practices
✅ Documentation updated"
```

---

## 🏆 Pro Tips

1. **Luôn cung cấp context**: Tech stack, project structure, constraints
2. **Specific hơn generic**: "Fix React useState hook" > "Fix bug"
3. **Sử dụng examples**: Provide input/output examples khi có thể
4. **Iterative refinement**: Build up complexity gradually
5. **Quality first**: Always ask for error handling, tests, documentation
6. **Learn from responses**: Analyze và improve prompts based on results

**Remember**: Copilot là AI assistant, không phải magic wand. Quality input = Quality output! 🎯