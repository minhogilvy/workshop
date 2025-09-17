# 🎯 Hướng dẫn sử dụng copilot-instructions.md

## 🤔 Tại sao cần copilot-instructions.md?

### ✅ **Lợi ích chính**
1. **Context Persistence**: GitHub Copilot tự động đọc file này để hiểu project context
2. **Consistency**: Đảm bảo all responses follow cùng một standards và patterns
3. **Efficiency**: Không cần repeat context mỗi lần conversation
4. **Team Alignment**: Toàn team có cùng một understanding về project requirements

### 🎪 **Automatic Context Loading**
- GitHub Copilot **TỰ ĐỘNG** đọc `.github/copilot-instructions.md`
- Không cần manually attach file mỗi lần
- Context được load trong mọi conversation trong project
- Works across all Copilot features: Chat, Inline suggestions, Code completions

## 📍 Vị trí file quan trọng

### 🏗️ **Standard Locations** (theo thứ tự ưu tiên)
```
1. .github/copilot-instructions.md    ← Recommended (repository-wide)
2. .copilot/instructions.md           ← Alternative location
3. copilot-instructions.md            ← Root level (less preferred)
```

### 🎯 **Best Practice**: Luôn đặt trong `.github/copilot-instructions.md`
- Standard convention được GitHub recommend
- Clear separation với other project files
- Visible cho all repository contributors
- Consistent với GitHub workflows và configurations

## 🔄 Khi nào cần reference files cụ thể?

### 🎪 **Automatic Context** (Không cần manual reference)
- Project overview và general guidelines
- Tech stack và architecture patterns
- Coding standards và conventions
- Development workflow preferences

### 📎 **Manual Reference** (Cần explicitly mention)
- Specific implementation details trong particular files
- Complex legacy code cần detailed analysis
- Large codebases với multiple domains
- Debugging specific issues trong particular modules

## 💡 Examples sử dụng hiệu quả

### ✅ **Với copilot-instructions.md**
```markdown
# Simple prompt - Copilot đã có context
"Tạo user authentication API endpoint"

# Copilot biết:
- Tech stack từ instructions
- Security requirements
- Error handling patterns
- Testing conventions
- Documentation standards
```

### ✅ **Manual reference khi cần**
```markdown
# Khi work với specific file
"Review file src/auth/userService.ts và optimize performance"

# Khi debug specific issue
"Debug lỗi trong @workspace components/UserProfile.tsx line 45"

# Khi cần multiple file context
"Refactor authentication flow across #file:authController.ts và #file:authMiddleware.ts"
```

## 🎯 Template usage patterns

### 🏗️ **Initial Setup** (One-time)
1. Copy template copilot-instructions.md
2. Customize theo project specifics
3. Commit vào repository
4. All future Copilot interactions có context

### 🔄 **Ongoing Usage**
```markdown
# Normal development - không cần reference
"Add user profile feature với avatar upload"

# Specific file work - reference when needed
"Update #file:userProfile.tsx to use new API response format"

# Cross-file changes - reference multiple files
"Implement user roles across @workspace auth module"
```

### 🎪 **Advanced Patterns**
```markdown
# Workspace-wide analysis
"Analyze @workspace for security vulnerabilities"

# Multi-file refactoring
"Refactor error handling pattern across all #file:*.service.ts files"

# Feature implementation
"Implement notification system following project patterns in copilot-instructions"
```

## 🏆 Best Practices Summary

### ✅ **DO**
- Maintain updated copilot-instructions.md trong `.github/`
- Include comprehensive project context
- Update instructions khi project evolves
- Use manual references cho specific file work
- Keep instructions focused và actionable

### ❌ **DON'T**
- Include sensitive information (API keys, passwords)
- Make instructions too verbose (focus on essentials)
- Forget to update khi tech stack changes
- Reference files unnecessarily khi context đã clear

### 🎯 **Golden Rule**
> copilot-instructions.md = Project DNA
> Manual references = Specific surgery

**Context once, use everywhere! 🚀**

---

## 🔧 Practical Implementation

### 📋 **Setup Checklist**
- [ ] Create `.github/copilot-instructions.md`
- [ ] Fill in project-specific details
- [ ] Test với simple prompts
- [ ] Train team on usage patterns
- [ ] Establish update schedule

### 🎪 **Maintenance Schedule**
- **Weekly**: Review recent changes
- **Monthly**: Update major patterns
- **Quarterly**: Complete review và refresh
- **Major releases**: Sync với new features

Với setup này, bạn sẽ có trải nghiệm Copilot consistent và efficient across toàn bộ project! 🎯