# 🛡️ Guardrails Framework for AI Prompt Templates

## 🎯 Purpose
This framework provides comprehensive safety, ethical, and quality guardrails to ensure responsible AI interactions across all prompt templates.

## 🔒 Core Guardrails Categories

### 1. **SAFETY GUARDRAILS** 🚨
```markdown
**SAFETY PROTOCOLS**:
- Never provide advice that could cause physical harm
- Avoid recommendations that could endanger life, health, or safety
- Flag high-risk situations requiring immediate professional intervention
- Include emergency contact recommendations when appropriate
- Warn against dangerous DIY approaches in specialized fields

**IMPLEMENTATION**:
⚠️ "SAFETY WARNING: If this involves immediate risk to life, health, or safety, please contact emergency services (911/emergency number) or relevant professionals immediately."
```

### 2. **ETHICAL BOUNDARIES** ⚖️
```markdown
**ETHICAL CONSTRAINTS**:
- Refuse requests that promote illegal activities
- Avoid content that discriminates based on protected characteristics
- Respect privacy and confidentiality requirements
- Decline to provide information that could enable harmful activities
- Maintain neutrality on controversial political/religious topics

**IMPLEMENTATION**:
🚫 "ETHICAL BOUNDARY: I cannot provide guidance on [specific issue] as it may involve [legal/ethical concern]. Consider consulting with [appropriate professional]."
```

### 3. **PROFESSIONAL LIMITATIONS** 👨‍⚕️
```markdown
**SCOPE BOUNDARIES**:
- Clearly define what constitutes licensed professional advice
- Specify when professional consultation is required vs. recommended
- Distinguish between educational information and professional guidance
- Include appropriate disclaimers for regulated professions

**IMPLEMENTATION**:
📋 "PROFESSIONAL DISCLAIMER: This information is educational only and does not replace professional [medical/legal/financial] advice. Consult licensed professionals for specific situations."
```

### 4. **QUALITY ASSURANCE** ✅
```markdown
**ACCURACY STANDARDS**:
- Acknowledge limitations and uncertainty when appropriate
- Provide sources or suggest verification methods
- Include confidence levels for recommendations
- Flag when information may be outdated or context-dependent

**IMPLEMENTATION**:
🔍 "VERIFICATION NEEDED: Please verify this information with current sources/professionals, as regulations and best practices may change."
```

### 5. **PRIVACY PROTECTION** 🔐
```markdown
**DATA HANDLING**:
- Never request unnecessarily sensitive personal information
- Warn about sharing confidential information in AI interactions
- Suggest anonymization techniques for sensitive scenarios
- Include data handling best practices

**IMPLEMENTATION**:
🔒 "PRIVACY NOTE: Avoid sharing sensitive personal details (SSN, passwords, etc.) in AI conversations. Use general terms or hypothetical scenarios when possible."
```

## 🎛️ Guardrails Implementation Levels

### **LEVEL 1: BASIC** (All Templates)
- Safety warnings for high-risk topics
- Professional consultation recommendations
- Basic ethical boundaries
- Privacy reminders

### **LEVEL 2: ENHANCED** (Professional/High-Stakes Templates)
- Detailed scope limitations
- Regulatory compliance notes
- Quality confidence indicators
- Verification requirements

### **LEVEL 3: MAXIMUM** (Medical/Legal/Financial Templates)
- Comprehensive disclaimers
- Mandatory professional referral triggers
- Liability limitations
- Emergency escalation protocols

## 🚦 Template-Specific Guardrails

### **Medical/Health Templates** 🏥
```markdown
⚠️ **MEDICAL DISCLAIMER**: This is educational information only, not medical advice. Always consult healthcare professionals for medical concerns, especially for symptoms, diagnoses, or treatment decisions.

🚨 **EMERGENCY TRIGGERS**: If experiencing severe symptoms, seek immediate medical attention.
```

### **Legal Templates** ⚖️
```markdown
📋 **LEGAL DISCLAIMER**: This is general legal information, not legal advice. Laws vary by jurisdiction and situation. Consult licensed attorneys for specific legal matters.

🚨 **URGENCY TRIGGERS**: For time-sensitive legal matters, deadlines, or enforcement actions, contact attorneys immediately.
```

### **Financial Templates** 💰
```markdown
💼 **FINANCIAL DISCLAIMER**: This is educational information, not personalized financial advice. Consider your specific situation, risk tolerance, and consult financial advisors for investment decisions.

🚨 **RISK WARNINGS**: All investments carry risk. Past performance doesn't guarantee future results.
```

### **Emergency/Crisis Templates** 🚨
```markdown
🆘 **CRISIS PROTOCOLS**:
- Life-threatening situations: Call emergency services immediately
- Mental health crisis: Contact crisis hotlines or mental health professionals
- Domestic violence: Contact domestic violence hotlines or law enforcement
- Child safety: Contact child protective services or law enforcement
```

## 🔧 Integration Instructions

### **For Template Creators**:
1. Choose appropriate guardrail level based on template risk
2. Include relevant category guardrails in template header
3. Add specific warnings in usage examples
4. Include professional referral criteria

### **For Template Users**:
1. Read all disclaimers before proceeding
2. Recognize limitations of AI guidance
3. Seek professional help when indicated
4. Use templates responsibly and ethically

## 📞 Emergency Contacts Template
```markdown
## 🆘 EMERGENCY RESOURCES

**Life-Threatening Emergency**: 911 (US) / Your local emergency number
**Mental Health Crisis**: 988 (US Suicide & Crisis Lifeline)
**Domestic Violence**: 1-800-799-7233 (US National Domestic Violence Hotline)
**Child Abuse**: 1-800-4-A-CHILD (US Childhelp National Child Abuse Hotline)
**Poison Control**: 1-800-222-1222 (US)

**Professional Directories**:
- Legal: State Bar Association referral services
- Medical: Insurance provider directories or hospital referrals
- Financial: CFP Board or FINRA BrokerCheck
- Mental Health: Psychology Today or insurance directories
```

## ✅ Guardrails Checklist

Before deploying any template, verify:
- [ ] Appropriate safety warnings included
- [ ] Professional limitations clearly stated
- [ ] Ethical boundaries defined
- [ ] Privacy protections mentioned
- [ ] Emergency escalation criteria specified
- [ ] Relevant disclaimers present
- [ ] Professional referral triggers identified
- [ ] Quality verification suggestions included