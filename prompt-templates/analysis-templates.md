# 🔍 Analysis & Optimization Templates

## 🐛 Debugging & Troubleshooting

### 🔎 **Bug Investigation Template**
```markdown
Debug issue: [Brief description]

**Current Situation:**
- Expected behavior: [what should happen]
- Actual behavior: [what's happening instead]
- Steps to reproduce: [detailed reproduction steps]
- Environment: [browser, OS, version, etc.]
- Error messages: [exact error text, stack traces]

**Investigation Plan:**
1. Log analysis: [check application và server logs]
2. Network inspection: [API calls, network requests]
3. State debugging: [application state, data flow]
4. Browser debugging: [console errors, network tab]
5. Database queries: [check data integrity, performance]

**Analysis Requirements:**
- Root cause identification
- Impact assessment
- Fix strategy với risk evaluation
- Prevention measures cho future
- Test plan để verify fix
- Rollback plan if needed
```

### 🔧 **Performance Investigation Template**
```markdown
Analyze performance issue trong [Component/Feature]:

**Performance Metrics:**
- Current performance: [load times, response times]
- Performance targets: [acceptable thresholds]
- User impact: [affected user scenarios]
- Resource usage: [CPU, memory, network]

**Investigation Areas:**
- Frontend performance: [render times, bundle size]
- Backend performance: [API response times, database queries]
- Network performance: [payload size, request count]
- Caching effectiveness: [cache hit rates, strategies]

**Analysis Output:**
- Performance bottlenecks identification
- Optimization recommendations với priority
- Implementation complexity assessment
- Expected performance improvements
- Monitoring strategy cho ongoing tracking
```

### 🛡️ **Security Audit Template**
```markdown
Security audit cho [System/Component]:

**Audit Scope:**
- Authentication mechanisms
- Authorization controls
- Data validation và sanitization
- Session management
- API security
- Data encryption
- Input/output security

**Security Checklist:**
- [ ] SQL injection prevention
- [ ] XSS protection
- [ ] CSRF token implementation
- [ ] Rate limiting
- [ ] Secure headers configuration
- [ ] Data encryption at rest/transit
- [ ] Access control implementation
- [ ] Audit logging

**Deliverables:**
- Vulnerability assessment report
- Risk prioritization matrix
- Remediation recommendations
- Security testing strategy
- Compliance validation
```

## 📊 Code Quality & Refactoring

### 🔄 **Code Review Template**
```markdown
Comprehensive code review cho [Module/Feature]:

**Review Criteria:**
- Code style consistency
- Design patterns adherence
- Performance implications
- Security considerations
- Error handling robustness
- Test coverage adequacy
- Documentation completeness

**Focus Areas:**
- SOLID principles application
- DRY principle compliance
- Code readability và maintainability
- Function/class complexity
- Dependency management
- Resource management

**Output Requirements:**
- Issues categorized by severity
- Actionable improvement suggestions
- Best practices recommendations
- Refactoring opportunities
- Code quality metrics
- Learning opportunities identification
```

### ♻️ **Refactoring Planning Template**
```markdown
Plan refactoring cho [Codebase/Module]:

**Current State Analysis:**
- Code smells identification
- Technical debt assessment
- Complexity metrics
- Performance bottlenecks
- Maintainability issues

**Refactoring Strategy:**
- Phase-based approach
- Risk assessment cho each phase
- Backward compatibility plan
- Testing strategy throughout
- Rollback procedures

**Success Metrics:**
- Code quality improvements
- Performance enhancements
- Maintainability gains
- Technical debt reduction
- Team productivity impact
```

### 📏 **Code Metrics Analysis Template**
```markdown
Analyze code metrics cho [Project/Module]:

**Metrics to Evaluate:**
- Cyclomatic complexity
- Code coverage percentage
- Duplicate code percentage
- Function/class size distribution
- Dependency graph complexity
- Technical debt ratio

**Analysis Goals:**
- Identify high-complexity areas
- Locate testing gaps
- Find refactoring candidates
- Assess architectural health
- Track quality trends over time

**Actionable Insights:**
- Priority areas cho improvement
- Specific refactoring recommendations
- Testing strategy enhancements
- Architectural improvements
- Quality gates establishment
```

## 🏗️ Architecture & Design Analysis

### 🎯 **Architecture Review Template**
```markdown
Architecture review cho [System/Application]:

**Current Architecture Assessment:**
- Component separation of concerns
- Data flow và dependencies
- Scalability bottlenecks
- Performance characteristics
- Maintainability factors

**Review Dimensions:**
- Scalability: Can system handle growth?
- Reliability: How robust is the system?
- Performance: Does it meet SLA requirements?
- Security: Are there architectural vulnerabilities?
- Maintainability: How easy is it to modify?

**Recommendations:**
- Architectural improvements
- Technology stack updates
- Design pattern applications
- Infrastructure optimizations
- Development process enhancements
```

### 🔗 **Dependency Analysis Template**
```markdown
Analyze dependencies cho [Project]:

**Dependency Review:**
- Direct dependencies audit
- Transitive dependencies analysis
- Version compatibility check
- Security vulnerability scan
- License compliance verification

**Analysis Focus:**
- Outdated packages identification
- Unused dependencies cleanup
- Bundle size impact assessment
- Alternative library evaluation
- Upgrade strategy planning

**Optimization Plan:**
- Dependency pruning strategy
- Update prioritization
- Breaking changes impact assessment
- Migration planning
- Monitoring setup cho future
```

## 📈 Performance Optimization

### ⚡ **Frontend Performance Template**
```markdown
Optimize frontend performance cho [Application/Component]:

**Performance Audit:**
- Bundle size analysis
- Render performance profiling
- Network request optimization
- Image và asset optimization
- Caching strategy evaluation

**Optimization Areas:**
- Code splitting implementation
- Lazy loading strategy
- Image optimization
- CSS và JS minification
- CDN utilization
- Service worker implementation

**Metrics Tracking:**
- First Contentful Paint (FCP)
- Largest Contentful Paint (LCP)
- First Input Delay (FID)
- Cumulative Layout Shift (CLS)
- Time to Interactive (TTI)
```

### 🗄️ **Database Performance Template**
```markdown
Optimize database performance cho [Database/Queries]:

**Performance Analysis:**
- Slow query identification
- Index usage analysis
- Query execution plan review
- Connection pool optimization
- Cache hit rate evaluation

**Optimization Strategy:**
- Index optimization
- Query rewriting
- Database schema improvements
- Partitioning strategy
- Caching layer implementation

**Monitoring Setup:**
- Query performance tracking
- Resource utilization monitoring
- Alert configuration
- Performance baseline establishment
- Regular performance reviews
```

### 🌐 **API Performance Template**
```markdown
Optimize API performance cho [API/Service]:

**Performance Baseline:**
- Response time measurements
- Throughput analysis
- Error rate tracking
- Resource utilization assessment

**Optimization Targets:**
- Response time reduction
- Throughput improvement
- Error rate minimization
- Resource efficiency

**Implementation Plan:**
- Caching strategy
- Database query optimization
- Rate limiting implementation
- Load balancing configuration
- Monitoring và alerting setup
```

## 🔬 Testing Strategy Analysis

### 🧪 **Test Coverage Analysis Template**
```markdown
Analyze test coverage cho [Codebase/Module]:

**Coverage Assessment:**
- Line coverage percentage
- Branch coverage analysis
- Function coverage evaluation
- Integration test coverage
- E2E test coverage

**Gap Analysis:**
- Untested code identification
- Critical path coverage verification
- Edge case testing gaps
- Error scenario coverage

**Improvement Plan:**
- Test writing prioritization
- Testing strategy refinement
- Test automation enhancement
- Coverage target establishment
- Quality gate implementation
```

### 🎯 **Testing Strategy Optimization Template**
```markdown
Optimize testing strategy cho [Project]:

**Current Testing Assessment:**
- Test pyramid analysis
- Test execution time
- Test maintenance overhead
- Flaky test identification
- Test environment stability

**Strategy Improvements:**
- Test categorization optimization
- Test data management
- Test environment standardization
- CI/CD integration enhancement
- Test reporting improvement

**Implementation Roadmap:**
- Quick wins identification
- Long-term improvements planning
- Resource allocation
- Timeline establishment
- Success metrics definition
```

---

## 🎯 Usage Guidelines

### 📋 **Before Analysis**
1. Gather relevant data và metrics
2. Define clear analysis objectives
3. Set success criteria
4. Identify stakeholders
5. Plan analysis timeline

### 🔍 **During Analysis**
1. Follow template structure systematically
2. Document findings thoroughly
3. Prioritize issues by impact
4. Consider implementation feasibility
5. Validate assumptions với data

### 📊 **After Analysis**
1. Create actionable recommendations
2. Estimate implementation effort
3. Define success metrics
4. Plan follow-up reviews
5. Share insights với team

**Remember**: Data-driven analysis leads to effective optimization! 📈