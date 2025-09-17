# 🎯 Quản lý Copilot Instructions cho nhiều dự án

## 🏗️ Chiến lược tổ chức Multi-Project

### 📂 **Cấu trúc thư mục tiêu chuẩn**
```
~/copilot-workspace/
├── templates/                          # Base templates
│   ├── copilot-instructions-base.md   # Common foundation
│   ├── frontend-instructions.md       # Frontend-specific
│   ├── backend-instructions.md        # Backend-specific
│   ├── mobile-instructions.md         # Mobile-specific
│   └── fullstack-instructions.md      # Full-stack projects
├── projects/
│   ├── ecommerce-web/
│   │   ├── .github/
│   │   │   └── copilot-instructions.md
│   │   └── project-specific-prompts.md
│   ├── mobile-banking-app/
│   │   ├── .github/
│   │   │   └── copilot-instructions.md
│   │   └── flutter-specific-prompts.md
│   └── enterprise-api/
│       ├── .github/
│       │   └── copilot-instructions.md
│       └── microservice-prompts.md
└── scripts/
    ├── sync-instructions.sh           # Auto-sync templates
    ├── validate-instructions.py       # Quality validation
    └── generate-project.sh            # New project setup
```

### 🎯 **Template Hierarchy Strategy**

#### 🏭 **Base Template (Foundation)**
```markdown
# copilot-instructions-base.md
Chứa:
- Universal coding standards
- Common security practices
- General development workflow
- Base error handling patterns
- Documentation standards
- Testing philosophy
```

#### 🎨 **Technology-Specific Templates**
```markdown
# frontend-instructions.md (kế thừa base)
Additional:
- React/Vue/Angular patterns
- Component architecture
- State management
- UI/UX guidelines
- Performance optimization
- Accessibility standards

# backend-instructions.md (kế thừa base)
Additional:
- API design principles
- Database patterns
- Authentication/authorization
- Microservices architecture
- Caching strategies
- Monitoring/logging

# mobile-instructions.md (kế thừa base)
Additional:
- Platform-specific guidelines
- Mobile UX patterns
- Performance considerations
- Device integration
- Store submission requirements
```

#### 🏢 **Project-Specific Customization**
```markdown
# project/copilot-instructions.md (kế thừa technology template)
Project-specific:
- Business domain context
- Specific tech stack versions
- Project constraints
- Team preferences
- Custom workflows
- Integration requirements
```

## 🔄 Template Management System

### 📋 **Template Versioning**
```bash
# Git-based versioning
~/copilot-workspace/
├── .git/                    # Version control
├── CHANGELOG.md            # Template evolution history
├── VERSION                 # Current template version
└── templates/
    ├── v1.0/               # Stable versions
    │   ├── base.md
    │   └── frontend.md
    ├── v1.1/
    │   ├── base.md
    │   └── frontend.md
    └── current/            # Symlink to latest stable
        ├── base.md
        └── frontend.md
```

### 🛠️ **Automated Template Management**

#### 🔄 **sync-instructions.sh**
```bash
#!/bin/bash
# Sync base template changes to all projects

TEMPLATE_VERSION="v1.1"
BASE_TEMPLATE="templates/current/copilot-instructions-base.md"

for project in projects/*/; do
    echo "Updating $project"

    # Backup current instructions
    cp "$project/.github/copilot-instructions.md" \
       "$project/.github/copilot-instructions.md.backup"

    # Merge base template với project-specific content
    python scripts/merge-templates.py \
        --base "$BASE_TEMPLATE" \
        --project "$project/.github/copilot-instructions.md" \
        --output "$project/.github/copilot-instructions.md.new"

    # Validate merged content
    if python scripts/validate-instructions.py \
        "$project/.github/copilot-instructions.md.new"; then
        mv "$project/.github/copilot-instructions.md.new" \
           "$project/.github/copilot-instructions.md"
        echo "✅ Updated $project successfully"
    else
        echo "❌ Validation failed for $project"
        rm "$project/.github/copilot-instructions.md.new"
    fi
done
```

#### ✅ **validate-instructions.py**
```python
#!/usr/bin/env python3
import yaml
import re
import sys

def validate_instructions(file_path):
    """Validate copilot instructions file"""
    with open(file_path, 'r') as f:
        content = f.read()

    errors = []

    # Check required sections
    required_sections = [
        "Project Overview",
        "Development Guidelines",
        "Code Quality Requirements",
        "Success Criteria"
    ]

    for section in required_sections:
        if section not in content:
            errors.append(f"Missing required section: {section}")

    # Check for placeholder values
    placeholders = re.findall(r'\[([^\]]+)\]', content)
    unfilled = [p for p in placeholders if p.isupper()]

    if unfilled:
        errors.append(f"Unfilled placeholders: {unfilled}")

    # Validate YAML frontmatter if present
    if content.startswith('---'):
        try:
            yaml_end = content.find('---', 3)
            yaml.safe_load(content[3:yaml_end])
        except yaml.YAMLError as e:
            errors.append(f"Invalid YAML frontmatter: {e}")

    return errors

if __name__ == "__main__":
    errors = validate_instructions(sys.argv[1])
    if errors:
        print("❌ Validation errors:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print("✅ Instructions valid")
```

### 🚀 **New Project Setup**

#### 🎨 **generate-project.sh**
```bash
#!/bin/bash
# Generate new project với appropriate template

PROJECT_NAME=$1
PROJECT_TYPE=$2  # frontend/backend/mobile/fullstack
TECH_STACK=$3    # react/vue/nodejs/flutter/etc

echo "🚀 Creating new project: $PROJECT_NAME"

# Create project directory
mkdir -p "projects/$PROJECT_NAME/.github"

# Select appropriate template
case $PROJECT_TYPE in
    "frontend")
        TEMPLATE="templates/current/frontend-instructions.md"
        ;;
    "backend")
        TEMPLATE="templates/current/backend-instructions.md"
        ;;
    "mobile")
        TEMPLATE="templates/current/mobile-instructions.md"
        ;;
    "fullstack")
        TEMPLATE="templates/current/fullstack-instructions.md"
        ;;
    *)
        TEMPLATE="templates/current/copilot-instructions-base.md"
        ;;
esac

# Copy và customize template
cp "$TEMPLATE" "projects/$PROJECT_NAME/.github/copilot-instructions.md"

# Interactive customization
echo "📝 Customizing template for $PROJECT_NAME..."
python scripts/customize-template.py \
    --project "$PROJECT_NAME" \
    --type "$PROJECT_TYPE" \
    --tech "$TECH_STACK" \
    --file "projects/$PROJECT_NAME/.github/copilot-instructions.md"

echo "✅ Project $PROJECT_NAME created successfully!"
echo "📁 Location: projects/$PROJECT_NAME/"
echo "📝 Edit: projects/$PROJECT_NAME/.github/copilot-instructions.md"
```

## 🎯 Project Classification System

### 🏷️ **Project Categories**

#### 🌐 **Frontend Projects**
```yaml
category: frontend
templates:
  - copilot-instructions-base.md
  - frontend-instructions.md
tech_stacks:
  react:
    - Next.js patterns
    - React hooks guidelines
    - State management (Redux/Zustand)
  vue:
    - Vue 3 Composition API
    - Nuxt.js conventions
    - Pinia state management
  angular:
    - Angular 17+ patterns
    - NgRx state management
    - Angular Material guidelines
```

#### 🔧 **Backend Projects**
```yaml
category: backend
templates:
  - copilot-instructions-base.md
  - backend-instructions.md
tech_stacks:
  nodejs:
    - Express.js/Fastify patterns
    - TypeScript configuration
    - Database integration
  python:
    - FastAPI/Django patterns
    - Async/await best practices
    - SQLAlchemy patterns
  java:
    - Spring Boot conventions
    - Microservices patterns
    - JPA/Hibernate guidelines
```

#### 📱 **Mobile Projects**
```yaml
category: mobile
templates:
  - copilot-instructions-base.md
  - mobile-instructions.md
tech_stacks:
  react_native:
    - Navigation patterns
    - State management
    - Platform-specific code
  flutter:
    - Widget composition
    - State management (Bloc/Provider)
    - Platform channels
  native:
    - iOS Swift patterns
    - Android Kotlin patterns
    - Platform-specific guidelines
```

## 🔧 Maintenance Workflows

### 📅 **Regular Maintenance Schedule**

#### **Weekly Tasks**
- [ ] Review new prompts và patterns from projects
- [ ] Update common templates với learnings
- [ ] Sync changes to active projects
- [ ] Validate template consistency

#### **Monthly Tasks**
- [ ] Comprehensive template review
- [ ] Update technology-specific guidelines
- [ ] Review project feedback
- [ ] Update automation scripts

#### **Quarterly Tasks**
- [ ] Major template refactoring
- [ ] Technology stack updates
- [ ] Best practices evolution
- [ ] Training material updates

### 🎯 **Quality Assurance Process**

#### 📝 **Template Review Checklist**
```markdown
- [ ] All placeholders filled appropriately
- [ ] Technology versions are current
- [ ] Security guidelines updated
- [ ] Performance benchmarks realistic
- [ ] Documentation standards clear
- [ ] Examples are practical
- [ ] Integration requirements specified
- [ ] Success criteria measurable
```

#### 🧪 **Testing Process**
1. **Template Validation**: Automated checks cho syntax và completeness
2. **Project Testing**: Deploy template trong test project
3. **AI Response Quality**: Test prompts với generated templates
4. **Team Feedback**: Collect feedback từ development teams
5. **Performance Metrics**: Track prompt effectiveness

## 🚀 Advanced Management Strategies

### 🎭 **Role-Based Templates**

#### 👥 **Team Role Customization**
```markdown
# Senior Developer Instructions
- Complex architecture decisions
- Performance optimization focus
- Code review guidelines
- Mentoring responsibilities

# Junior Developer Instructions
- Learning-focused prompts
- Best practices emphasis
- Step-by-step guidance
- Safety guardrails

# DevOps Engineer Instructions
- Infrastructure automation
- Deployment procedures
- Monitoring setup
- Security compliance
```

### 🌍 **Environment-Specific Instructions**

#### 🏢 **Environment Templates**
```markdown
# Development Environment
- Debug information enabled
- Verbose logging
- Development tools integration
- Hot reloading preferences

# Staging Environment
- Production-like settings
- Performance testing focus
- Integration testing emphasis
- User acceptance testing guidelines

# Production Environment
- Security-first approach
- Performance monitoring
- Error tracking
- Compliance requirements
```

### 📊 **Analytics và Optimization**

#### 📈 **Template Effectiveness Metrics**
```python
class TemplateAnalytics:
    def track_metrics(self):
        return {
            'prompt_success_rate': 0.95,
            'code_quality_score': 8.7,
            'development_velocity': '+23%',
            'bug_reduction': '-31%',
            'team_satisfaction': 4.2
        }

    def optimize_templates(self):
        # A/B test different approaches
        # Analyze successful patterns
        # Update templates based on data
        pass
```

---

## 🏆 Success Strategies

### ✅ **Best Practices**
1. **Start Simple**: Begin với basic templates, evolve based on usage
2. **Consistent Updates**: Regular template maintenance prevents drift
3. **Team Feedback**: Actively collect và incorporate team input
4. **Automated Validation**: Prevent errors với automated checks
5. **Version Control**: Track changes và enable rollbacks
6. **Documentation**: Maintain clear usage guidelines

### 🎯 **Common Pitfalls to Avoid**
- ❌ Over-complex initial templates
- ❌ Inconsistent updates across projects
- ❌ Ignoring team feedback
- ❌ Manual synchronization processes
- ❌ Lack of validation checks
- ❌ Unclear template hierarchy

### 🚀 **Scaling Strategy**
1. **Phase 1**: Manual templates cho key projects
2. **Phase 2**: Automated sync và validation
3. **Phase 3**: Advanced customization và analytics
4. **Phase 4**: AI-powered template optimization

**Remember**: Effective multi-project management requires balance between consistency và flexibility! 🎯