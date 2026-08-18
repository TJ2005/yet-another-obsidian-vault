# CF Unit 2 - Complete Exam Notes (Keyword Dense)

---

# 1. THREATS AND ATTACKS

## Threats - Definition & Classification

**Threat:** Object/Person/Entity posing **constant danger** to asset. Understanding threats enables **preparedness** for adverse situations.

### Types of Threats:
- **Human Failure** - Unintentional mistakes
- **Human Error** - Operational mistakes  
- **Intellectual Property Compromise** - Theft of proprietary information
- **Deliberate Acts:**
  - **Espionage** - Information gathering
  - **Trespassing** - Unauthorized access
  - **Extortion** - Coercion for gain
  - **Sabotage** - Intentional damage
  - **Vandalism** - Property destruction
  - **Theft** - Stealing assets
- **Force of Nature** - Natural disasters

---

## Classification of Attacks

### **Passive Attacks**
- **Eavesdropping/Monitoring** transmissions
- **Release of message contents** - Reading confidential data
- **Traffic analysis** - Monitoring communication patterns
- **Goal:** Information gathering WITHOUT modification
- **Characteristics:** Difficult to detect, focus on confidentiality breach

### **Active Attacks**  
- **Modification of data stream**
- **Masquerade** - Impersonation
- **Replay** - Retransmission of previous messages
- **Denial of Service (DoS)** - Service disruption
- **Goal:** Alteration or disruption
- **Characteristics:** Detectable but hard to prevent

---

### Specific Attack Types

**Social Engineering** - Psychological manipulation for information extraction

**Phishing** - Fraudulent communication mimicking legitimate sources

**Spoofing:**
- **Web Spoofing** - Fake websites mimicking legitimate ones
- **Email Spoofing** - Forged sender addresses

**Malware** - Malicious software (viruses, trojans, ransomware)

---

## Advanced Persistent Threat (APT)

**Definition:** Sophisticated, prolonged, targeted attack campaign

### APT Kill Chain Phases:

1. **Reconnaissance** 
   - Attacker leverages **multiple factors**
   - **Identifies target** through research
   - Information gathering phase

2. **Incursion**
   - **Entry attempt** via social engineering
   - **Initial access** establishment
   - Exploiting human vulnerabilities

3. **Discovery**  
   - **Mapping internal defenses**
   - Network topology identification
   - **Curating attack kill chain**
   - Understanding security controls

4. **Capture**
   - **Information capturing**
   - **Malware installation**
   - Establishing persistence
   - Privilege escalation

5. **Exfiltration**
   - **Captured information sent back** to attacker
   - **Malware gives device control**
   - Data extraction
   - Maintaining access

---

# 2. METHODS OF DEFENSE - PDDMDR FRAMEWORK

## **P - Prevent Attack**

**Goal:** Stop attack **BEFORE it starts**, eliminate vulnerabilities

**Key Methods:**
- **Code Review** - Manual inspection removing bugs/insecure logic
- **Penetration Testing** - Ethical hackers simulate attacks, uncover weak points
- **Strong Authentication** - MFA prevents login even with stolen passwords
- **Regular Patching** - Updating systems, closing known security holes
- **Vulnerability elimination** - Proactive security

**Keywords:** Prevention, Vulnerability Elimination, Proactive Security, Code Review, Penetration Testing, MFA, Patching

---

## **D - Deter Attack**

**Goal:** Make attackers **think twice**, increase risk/difficulty

**Key Methods:**
- **Warning Banners** - "Unauthorized access prosecuted" on login screens
- **Visible Security Controls** - CCTV cameras, monitored firewalls
- **Rate-Limiting Login** - Brute-force becomes slow/frustrating
- **Legal Consequences** - Outlined in company policy
- **Security awareness displays**

**Keywords:** Deterrence, Warning Banners, Visible Controls, Rate-Limiting, Legal Consequences, Psychological Barrier

---

## **D - Deflect Attack**

**Goal:** Redirect attackers toward **fake/less valuable targets**, waste time

**Key Methods:**
- **Honeypots** - Fake servers attracting attackers, monitoring behavior
- **Honeytokens** - Fake credentials/files triggering alerts when used
- **Sandbox Environments** - Isolated fake environments for attacker interaction
- **Decoy systems**

**Keywords:** Deflection, Honeypots, Honeytokens, Sandbox, Decoy Systems, Attacker Misdirection

---

## **M - Mitigate Attack**  

**Goal:** **Reduce damage** when attack occurs, limit impact

**Key Methods:**
- **Incident Response Plan** - Predefined step-by-step containment/control
- **Network Segmentation** - Compromised section doesn't spread easily
- **Backups** - Minimizing data loss from ransomware
- **Rate Limiting** - Minimizes DDoS impact
- **Damage containment**

**Keywords:** Mitigation, Incident Response Plan, Network Segmentation, Backups, Rate Limiting, Damage Reduction, Containment

---

## **D - Detect Attack**

**Goal:** Identify attacks **in progress or after occurrence**

**Key Methods:**
- **IDS/IPS** - Intrusion Detection/Prevention Systems alert suspicious activity
- **Log Monitoring** - Reviewing system logs for unauthorized access attempts
- **SIEM Systems** - Security Information Event Management, real-time analysis
- **File Integrity Monitoring** - Alerts on critical file changes
- **Anomaly detection**

**Keywords:** Detection, IDS, IPS, Log Monitoring, SIEM, File Integrity Monitoring, Real-time Analysis, Anomaly Detection

---

## **R - Recover from Attack**

**Goal:** **Restore systems/services** back to normal post-attack

**Key Methods:**
- **Restoring from Backups** - After ransomware/data corruption
- **Rebuilding Compromised Systems** - Clean state restoration
- **Post-Incident Analysis** - Ensuring attacker removal, fixing weaknesses
- **Disaster Recovery Procedures** - Quick operations resumption
- **System restoration**

**Keywords:** Recovery, Backup Restoration, System Rebuilding, Post-Incident Analysis, Disaster Recovery, Business Continuity

---

# 3. DESIGN PRINCIPLES

## **Separate Privilege Principle**

**Definition:** No single person has **enough authority** for critical event alone

**Core Concept:**
- **Key authorities divided** between 2+ people
- **Reduces:** Fraud, mistakes, power misuse
- **Also called:** Separation of Duties, Dual Control

**Examples:**
- **Accounting:** Maker creates payment, Checker approves (separate privileges)
- **Data Centers:** One person holds room key, another holds server rack key
- **Banking:** Multiple signatures for large transactions

**Keywords:** Separation of Duties, Dual Control, Divided Authority, Maker-Checker, Fraud Prevention

---

## **Least Privilege**

**Definition:** Users receive **minimum privileges necessary** for tasks, nothing more

**Core Concept:**
- **Reduces damage** if account compromised
- Common violation: Admins giving broad access for convenience
- **Need-to-know basis**

**Examples:**
- Receptionist shouldn't have admin rights for software installation
- Web server process reads only needed folders, not whole filesystem
- Users get access only to resources required for job function

**Keywords:** Minimum Privileges, Need-to-Know, Access Restriction, Privilege Limitation, Account Compromise Protection

---

## **Defense in Depth Principle**

**Definition:** Security implemented in **multiple layers**, cascading security

**Core Concept:**
- If one layer fails, **other layers protect**
- Layered security approach
- **Redundancy** in protection

**Example Security Layers:**
Firewall → Antivirus → Intrusion Detection → Access Control → Encryption
- Hacker must **break each layer** to reach internal system

**Keywords:** Layered Security, Multiple Barriers, Cascading Security, Redundant Protection, Defense Layers

---

## **Security Through Obscurity**

**Definition:** Assumes attacker **doesn't know internal system details**

**Core Concept:**
- "Hiding" structure hoping attackers never understand
- **NOT effective as PRIMARY** security method
- Can be used as **SECONDARY layer**

**Examples:**
- Hiding admin panels at unusual URLs (`/admin98234/`)
- Keeping configuration paths secret
- Non-standard port usage

**Limitation:** Not replacement for actual security controls

**Keywords:** Obscurity, Hidden Structure, Secondary Layer, Configuration Secrecy, Non-Standard Paths

---

## **Fail-Safe Defaults (Fail Safes)**

**Definition:** Unless subject **explicitly allowed**, access **denied by default**

**Core Concept:**
- Default settings must be **secure, not permissive**
- Deny-all approach
- Explicit permission required

**Examples:**
- Firewall **blocks all ports**, only opens explicitly allowed
- File system **denies all users** unless permissions granted
- Default deny policy

**Keywords:** Default Deny, Explicit Allow, Secure Defaults, Deny-All Approach, Permission-Based Access

---

## **Economy of Mechanism**

**Definition:** Security mechanisms should be **as simple as possible**

**Core Concept:**
- Complex systems introduce bugs, misconfigurations, vulnerabilities
- Simplicity = Security

**Benefits:**
- **Fewer bugs**
- **Easier auditing/testing**
- **Easier maintenance**
- **Harder for attackers** to find weaknesses

**Example:**
Small, clear access control policy safer than long, complicated one with exceptions

**Keywords:** Simplicity, Minimal Complexity, Bug Reduction, Easy Auditing, Simple Mechanisms, Maintainability

---

## **Complete Mediation**

**Definition:** **Every access** to object must be **checked every time**

**Core Concept:**
- No reliance on cached permissions
- Don't assume earlier checks still hold
- Continuous verification

**Example:**
User removed from group → system must **check permissions on every file access**
Otherwise user may still access resources until next refresh

**Keywords:** Continuous Verification, Every Access Check, No Cached Permissions, Real-time Authorization, Permission Verification

---

## **Psychological Acceptability**

**Definition:** Security mechanisms should **NOT make systems harder to use**

**Core Concept:**
- Inconvenient security → users ignore/bypass it
- **Usability balanced with security**
- User-friendly security

**Examples:**
- **Too strict password rules** → users write passwords on sticky notes
- Simple, clean login system more secure than confusing one
- Security shouldn't frustrate users

**Keywords:** User-Friendly Security, Usability Balance, Convenience, User Acceptance, Practical Security

---

## **Least Common Mechanism**

**Definition:** Resource access mechanisms should **NOT be shared** across users

**Core Concept:**
- Shared mechanisms increase: Interference, information leakage, unintended access
- **Isolation** between users
- Minimize shared resources

**Examples:**
- Each user has **own isolated temp directory** (not shared temp folder)
- Avoid shared system-wide services with high privileges
- User-specific resources

**Keywords:** Isolation, No Sharing, User-Specific Resources, Interference Prevention, Information Leakage Protection

---

# 4. SECURITY TRADEOFFS

## **Security as a Tradeoff**

**Core Concept:** Balance between **Risk, Benefit, Cost, User Convenience**

### Tradeoff Factors:

**Risk:**
- Likelihood of attack
- Impact of attack

**Benefit:**
- Protection level provided by mechanism

**Cost:**
- Financial cost
- Time investment
- Training requirements
- Performance impact

**User Convenience:**
- Usability
- Productivity impact

**Example:** Biometric authentication = secure but expensive and slower
Business must decide if added security worth the cost

**Keywords:** Risk-Benefit Analysis, Cost-Effectiveness, Security Balance, Trade-off Analysis

---

## **Key Tradeoff Factors**

1. **Security Level Required** - Protection degree needed
2. **User Convenience** - Ease of use
3. **Business Goals** - Organizational objectives
4. **Financial Cost** - Budget constraints

**Example:** Strong encryption = secure but slows high-volume processing

**Keywords:** Security Requirements, Usability, Business Alignment, Budget Considerations

---

## **User Convenience vs. Security**

### Problems with Overly Complicated Security:

- Users **avoid using** the system
- Users find **shortcuts**
- Users **disable security features**
- System becomes **MORE vulnerable**

### Real-World Issues:

**Overly Strict Password Rules:**
- Users reuse passwords
- Users store passwords insecurely

**Complicated Multi-Factor:**
- Employees switch to personal devices outside controls

**Keywords:** Security Friction, User Workarounds, Bypass Behaviors, Security Fatigue

---

## **Bottom Line - Ideal Security Design**

**Must Balance:**
- **Protection** - Adequate security
- **Usability** - User-friendly
- **Business Requirements** - Organizational needs
- **Costs** - Financial feasibility

**Goal:** Protect system **WITHOUT blocking** people from work

**Keywords:** Balanced Approach, Protection Without Obstruction, Practical Security, Business-Aligned Security

---

# 5. INFORMATION SECURITY POLICIES

## **Policy Fundamentals**

**Cornerstone of Security Effort:**
- Implementing proper **security policies**
- **Educating users** about policies

### Effective Policy Requirements:

**FCAR Characteristics:**
- **Flexible** - Doesn't require frequent rewrites
- **Comprehensive** - Covers all relevant situations
- **Accessible** - Available to everyone in organization
- **Readable** - Clear, easy for users to understand

**Keywords:** Policy Foundation, User Education, FCAR, Flexibility, Comprehensiveness, Accessibility, Readability

---

## **Definition of Information Security Policies**

**Policy:** Documented, **high-level management instructions**

**Nature:**
- Formal statement: **"This is how we do things here"**
- Provides **general requirement statements** to reduce risk
- Operates at **HIGHER level** than standards/procedures

### Policy Attributes:

- **Mandatory** - Compliance required
- **Non-compliance** → Disciplinary action
- Focus on **desired results**, not implementation details
- Supported by **standards** and **guidelines**

**Keywords:** Management Instructions, High-Level Directives, Mandatory Compliance, Desired Outcomes, Formal Documentation

---

## **Standards**

**Definition:** **Mandatory action/rule** supporting policy

**Characteristics:**
- Makes policy **practical and enforceable**
- Includes **specific specifications** for hardware/software/behavior
- **Mandatory compliance**

**Example:**
- **Policy:** Requires strong passwords
- **Standard Defines:**
  - Minimum 12 characters
  - Must include symbols, numbers, uppercase letters

**Keywords:** Mandatory Rules, Specific Specifications, Policy Support, Enforceable Requirements, Technical Details

---

## **Guidelines**

**Definition:** General **recommendations** or **best practices**

**Characteristics:**
- Provide **framework** for implementing procedures
- **NOT mandatory** (unlike policies/standards)
- **Easier to update** than policies/standards
- Advisory nature

**Examples:**
- "Use encryption when sharing sensitive files"
- "Drill pilot hole before hammering nail to avoid wood splitting"

**Keywords:** Recommendations, Best Practices, Advisory, Non-Mandatory, Framework, Flexible Guidance

---

## **Relationship: Policies → Standards → Guidelines**

**Hierarchy:**
1. **Policies** → High-level rules (WHAT must be done)
2. **Standards** → Mandatory specifications (HOW it must be done)
3. **Guidelines** → Recommended best practices (SUGGESTED ways)

**Keywords:** Policy Hierarchy, Mandatory vs Advisory, Implementation Framework

---

## **Policy Analogy - Cabinet Construction**

### **Policy:**
"All boards must be nailed together using company-issued hammers to ensure consistency and worker safety"

### **Standard:**
- Use 11-inch fiberglass hammers
- Use hardened steel nails  
- Use automatic hammers for repetitive work >1 hour

### **Guideline:**
"To avoid splitting wood, drill pilot hole before hammering"

### **Procedure:**
1. Position nail upright on board
2. Strike nail with hammer
3. Repeat until flush
4. If thumb hit → refer to "Nail First Aid Procedure"

**Keywords:** Policy Example, Hierarchical Implementation, Practical Application

---

## **Policies Are NOT...**

**Common Misconceptions:**

- NOT **system settings** for firewalls/security devices
- NOT **optional** (unlike guidelines)
- NOT **product-dependent** (unlike architectures)

**Policies Are:**
- Strategic documents
- Implementation-independent
- Mandatory directives

**Keywords:** Policy Clarification, Strategic Documents, Implementation-Independent

---

## **Characteristics of Effective Policies**

**CODUCT Framework:**

1. **Complete** - Cover all major risk areas
2. **Organized** - Follow standard framework (e.g., ISO 27002)
3. **Documented** - Have ownership, version history
4. **Communicated** - Understood by all users
5. **Updated** - Reviewed periodically

**Keywords:** Effective Policies, CODUCT, Completeness, Organization, Documentation, Communication, Regular Updates

---

## **Types of Security Policies (NIST Classification)**

### Three Main Types:

1. **Program Policy**
   - Creates organization's **overall security program**
   - Highest level

2. **Issue-Specific Policies**
   - Address **specific topic** (Email, Social Media)
   - Topic-focused

3. **System-Specific Policies**
   - Protect **individual systems/technologies**
   - Technology-focused

**Keywords:** Policy Types, NIST Framework, Program Level, Issue-Specific, System-Specific

---

# 6. PROGRAM-LEVEL POLICIES

## **Definition & Purpose**

**Program Policy:** Establishes organization-wide security program

### Key Functions:

- **Establishes security program**
- **Assigns responsibility** to specific management roles
- **States organization-wide objectives**
- **Establishes compliance/enforcement** rules

**Keywords:** Security Program, Organization-Wide, Management Responsibility, Compliance Framework

---

## **Components of Program-Level Policy**

### **1. Purpose**

**Objectives May Include:**
- **Improved recovery times** - Faster incident response
- **Reduced downtime** - Business continuity
- **Regulatory compliance** - Meeting legal requirements
- **Protecting CIA Triad:**
  - **Confidentiality** - Information secrecy
  - **Integrity** - Data accuracy
  - **Availability** - Resource accessibility

**Keywords:** Policy Purpose, Recovery Times, Downtime Reduction, Regulatory Compliance, CIA Triad

---

### **2. Scope**

**Specifies Coverage:**
- **Facilities** - Physical locations
- **Employees** - Personnel categories
- **Departments** - Organizational units
- **Technologies** - IT systems
- **Processes** - Business operations

**Keywords:** Policy Scope, Coverage Areas, Organizational Boundaries, Applicability

---

### **3. Responsibilities**

**Defines:**
- **Who implements** policy
- **Who maintains** policy
- **Accountability structure**
- **Role assignments**

**Keywords:** Accountability, Role Definition, Implementation Responsibility, Maintenance Ownership

---

### **4. Compliance**

**Covers:**
- **Enforcement methods** - How policy enforced
- **Oversight** - Monitoring mechanisms
- **Penalties for violation** - Disciplinary actions
- **Audit requirements**

**Keywords:** Policy Enforcement, Oversight Mechanisms, Penalties, Disciplinary Action, Audit Requirements

---

## **Examples of Program-Level Policies**

1. **Business Continuity Planning (BCP) Framework**
   - Ensures business operations continue during/after disruption

2. **Physical Security Requirements for Data Centers**
   - Protects physical infrastructure

3. **Application Development Security Framework**
   - Secure software development lifecycle

**Keywords:** BCP, Physical Security, Application Security, SDLC Framework

---

## **Example: Application Development Policy**

### **Topics Covered:**

- **Development Methodology** - SDLC approach
- **Access to Program Source Library** - Code repository controls
- **Requirement Definitions** - Specifications
- **Risk Assessment** - Security analysis
- **Installation Processes** - Deployment procedures
- **Software Acquisition Rules** - Third-party software
- **User Training** - End-user education
- **Change Restrictions** - Change management
- **Application Testing** - Quality assurance
- **Logging** - Audit trails
- **UAT (User Acceptance Testing)** - Validation
- **Post-Implementation Review** - Evaluation
- **Protection of Test Data** - Test environment security

**Keywords:** Application Development, SDLC, Source Control, Risk Assessment, UAT, Change Management, Test Data Protection

---

# 7. ISSUE-SPECIFIC SECURITY POLICIES

## **Definition & Characteristics**

**Issue-Specific Policy:** Focus on **particular technology areas**

### Characteristics:
- **Frequent updates** needed
- Contains organization's **stance on specific issue**
- **Topic-focused**
- More detailed than program policies

**Keywords:** Issue-Specific, Technology Focus, Frequent Updates, Organizational Stance

---

## **Examples of Issue-Specific Policies**

**Common Policy Types:**
- **Email Policy** - Email usage rules
- **Backup Policy** - Data backup requirements
- **Wireless Device Policy** - Mobile device management
- **BYOD Policy** - Bring Your Own Device
- **Social Media Policy** - Social platform usage
- **Telecommunications Policy** - Communication systems

**Keywords:** Email, Backup, Wireless, BYOD, Social Media, Telecommunications

---

## **Components of Issue-Specific Policies**

**IOARC Structure:**

1. **Issue Statement** - Defines the issue
2. **Organization's Position** - Clear stance
3. **Applicability** - Who/What/When applies
4. **Roles & Responsibilities** - Accountability
5. **Compliance & Penalties** - Enforcement
6. **Points of Contact** - Support/questions
7. **Related Guidelines** - Supporting documents

**Keywords:** Issue Statement, Organizational Position, Applicability, Roles, Compliance, Contact Points

---

# 8. SPECIFIC ISSUE-BASED POLICIES

## **1. Acceptable Use Policy (AUP)**

**Definition:** Defines **allowed and prohibited** usage of company IT resources

### Key Questions Answered:

**Q1:** What activities are **allowed**?
- Legitimate business use
- Approved personal use (if any)

**Q2:** What is **prohibited**?
- Illegal activities
- Unauthorized access
- Resource misuse

**Q3:** Where do users **report violations**?
- Security team contact
- Reporting procedures

**Keywords:** AUP, Acceptable Use, Prohibited Activities, Usage Rules, IT Resources, Violation Reporting

---

## **2. Backup Policy**

**Goal:** Ensures **availability and integrity**

### Key Questions Answered:

**Q1:** What data must be **backed up**?
- Critical systems
- User data
- Configuration files

**Q2:** Where are backups **stored**?
- Primary location
- Offsite storage
- Cloud backup

**Q3:** Who can **access** backups?
- Authorized personnel
- Access controls

**Q4:** How long are backups **kept**?
- Retention period
- Rotation schedule

**Keywords:** Backup Policy, Data Protection, Availability, Integrity, Backup Storage, Retention Period, Access Control

---

## **3. Confidentiality Policy**

**Goal:** Protects **sensitive information** in all forms

### Forms of Information:
- **Verbal** - Spoken conversations
- **Print** - Paper documents
- **Digital** - Electronic data

### Key Questions:

**Q1:** What is **confidential**?
- Classification levels
- Sensitive data types

**Q2:** How should it be **handled or released**?
- Handling procedures
- Release authorization

**Q3:** What happens if it is **leaked**?
- Incident response
- Penalties

**Keywords:** Confidentiality, Sensitive Information, Data Classification, Information Handling, Leak Response

---

## **4. Data Retention Policy**

**Goal:** Defines **data lifecycle management**

### Defines:

**Data Categories:**
- Financial records
- Customer data
- Employee records
- Operational data

**Retention Times:**
- **Minimum retention** - Legal requirements
- **Maximum retention** - Privacy compliance
- Often legally mandated

**Example:**
Financial data for tax purposes → **7 years retention** (legal requirement)

**Keywords:** Data Retention, Lifecycle Management, Legal Requirements, Retention Period, Data Categories, Compliance

---

## **5. Wireless Device Policy**

**Goal:** Manages **mobile/wireless** device usage

### Covers:

**Q1:** What devices may employees **bring**?
- Approved device types
- BYOD specifications

**Q2:** Permitted and **prohibited activities**?
- Allowed usage
- Restricted actions

**Q3:** **Approval requirements** for exceptions?
- Exception process
- Management approval

**Keywords:** Wireless Policy, Mobile Devices, BYOD, Device Management, Permitted Activities, Exception Handling

---

# 9. SYSTEM-SPECIFIC POLICIES

## **Definition & Scope**

**System-Specific Policy:** Apply to **one system or platform**

### Defines:

- **Security objectives** for specific system
- **Acceptable operation** parameters
- **Technical controls**

**Keywords:** System-Specific, Platform-Focused, Technical Controls, Operational Parameters

---

## **Key Questions Addressed**

### **Access Control:**
**ACL Rules:**
- Who can **read** data?
- Who can **modify** data?
- Permission levels

### **Remote Access:**
- Can users access system **remotely**?
- Under what **conditions** is remote access allowed?
- Authentication requirements

**Keywords:** ACL, Access Control List, Remote Access, Permission Levels, Authentication Requirements

---

## **System-Specific Examples**

1. **Database Security Policy**
   - Access controls
   - Encryption requirements
   - Backup procedures

2. **Web Server Security Policy**
   - Hardening standards
   - Port configurations
   - Logging requirements

3. **Email Server Policy**
   - Spam filtering
   - Attachment restrictions
   - Encryption standards

**Keywords:** Database Security, Web Server, Email Server, Technical Specifications, System Hardening

---

# 10. EXAM-FOCUSED KEY TERMS SUMMARY

## **Threats & Attacks:**
Threat, Passive Attack, Active Attack, Eavesdropping, Traffic Analysis, Masquerade, Replay, DoS, Social Engineering, Phishing, Spoofing, Malware, APT, Reconnaissance, Incursion, Discovery, Capture, Exfiltration

## **Defense Methods (PDDMDR):**
Prevent, Deter, Deflect, Mitigate, Detect, Recover, Code Review, Penetration Testing, MFA, Patching, Warning Banners, Rate-Limiting, Honeypots, Honeytokens, Sandbox, Incident Response Plan, Network Segmentation, Backups, IDS, IPS, SIEM, Log Monitoring, File Integrity Monitoring, Disaster Recovery

## **Design Principles:**
Separate Privilege, Least Privilege, Defense in Depth, Security Through Obscurity, Fail-Safe Defaults, Economy of Mechanism, Complete Mediation, Psychological Acceptability, Least Common Mechanism, Separation of Duties, Dual Control, Maker-Checker, Need-to-Know, Layered Security, Default Deny, Simplicity, Continuous Verification, Usability Balance, Isolation

## **Security Tradeoffs:**
Risk, Benefit, Cost, User Convenience, Risk-Benefit Analysis, Security Balance, Trade-off Analysis, Security Friction, Bypass Behaviors, Balanced Approach, Protection Without Obstruction

## **Policies:**
Information Security Policy, Standards, Guidelines, Program Policy, Issue-Specific Policy, System-Specific Policy, Mandatory Compliance, FCAR (Flexible, Comprehensive, Accessible, Readable), CODUCT (Complete, Organized, Documented, Communicated, Updated), Purpose, Scope, Responsibilities, Compliance, CIA Triad (Confidentiality, Integrity, Availability)

## **Issue-Specific Policies:**
AUP (Acceptable Use Policy), Backup Policy, Confidentiality Policy, Data Retention Policy, Wireless Device Policy, BYOD, Email Policy, Social Media Policy, Issue Statement, Organizational Position, Applicability, Roles & Responsibilities, Penalties

## **System-Specific:**
ACL (Access Control List), Remote Access, Technical Controls, System Hardening, Permission Levels, Authentication Requirements

---

# EXAM TIPS

✅ **Use these exact keywords** in answers
✅ **Define terms completely** before explaining
✅ **Give examples** for each concept
✅ **Use framework names** (PDDMDR, FCAR, CODUCT, IOARC)
✅ **Mention relationships** between policies, standards, guidelines
✅ **Include all components** when describing policies
✅ **Use abbreviations after first mention** (e.g., Advanced Persistent Threat (APT))
✅ **Structured answers** with headings/subheadings
✅ **Connect concepts** (e.g., how Defense in Depth relates to PDDMDR)

---

**END OF UNIT 2 EXAM NOTES**
Give examples** for each concept
✅ **Use framework names** (PDDMDR, FCAR, CODUCT, IOARC)
✅ **Mention relationships** between policies, standards, guidelines
✅ **Include all components** when describing policies
✅ **Use abbreviations after first mention** (e.g., Advanced Persistent Threat (APT))
✅ **Structured answers** with headings/subheadings
✅ **Connect concepts** (e.g., how Defense in Depth relates to PDDMDR)

---

# QUICK REFERENCE - LINKING GUIDE

## **Unit 2 Source Notes:**

1. **[[Various Security Threats and Attacks]]** - Threats, Attack Classifications, APT
2. **[[Methods of Defense]]** - PDDMDR Framework (Prevent, Deter, Deflect, Mitigate, Detect, Recover)
3. **[[Design Principles]]** - 9 Security Design Principles + Security Tradeoffs
4. **[[Security Policies]]** - Policy Types, Standards, Guidelines, Program/Issue/System-Specific Policies

---

**END OF UNIT 2 EXAM NOTES**