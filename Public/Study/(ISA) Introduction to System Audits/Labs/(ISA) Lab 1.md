---

Title: "(ISA) Lab 1"

Status:

marker:

tags:

Date: "2026.07.20"

Time: "12:24"

---
# (ISA) Lab 1

## Task 1
Categorize these assets into 7 categories and identify the threats associated with them.

|Asset|Asset Category|IT Infrastructure Domain|Possible Threats|
|---|---|---|---|
|Computers and laptops|Hardware|Workstation Domain|Malware, ransomware, theft, unauthorized access, hardware failure|
|Routers and networking equipment|Network|LAN Domain|Misconfiguration, DDoS attacks, unauthorized access, firmware exploits|
|Printers|Hardware|LAN Domain|Unauthorized printing, sensitive document leakage, network compromise|
|Cameras (digital/analog with company-sensitive photos)|Hardware / Information|System/Application Domain|Theft, unauthorized access, image leakage, espionage|
|Employee information|Information (Data)|System/Application Domain|Data breach, identity theft, unauthorized modification, privacy violations|
|Company smartphones / PDAs|Hardware|Remote Access Domain|Device theft, malware, unauthorized remote access, data leakage|
|VoIP phones, IP PBXs, related servers|Network / Software|LAN Domain|Call interception, toll fraud, VoIP attacks, service disruption|
|Phone call recordings and records|Information (Data)|System/Application Domain|Privacy breach, unauthorized disclosure, tampering|
|Email|Information / Software|System/Application Domain|Phishing, spoofing, malware, business email compromise|
|Employee daily schedules and activity logs|Information (Data)|System/Application Domain|Insider misuse, privacy violations, unauthorized modification|
|Company webpages (especially customer forms)|Software / Information|System/Application Domain|SQL injection, XSS, website defacement, credential theft|
|Web server computer|Hardware|System/Application Domain|DDoS, server compromise, ransomware, privilege escalation|
|Security cameras (CCTV)|Hardware|LAN Domain|Camera hacking, surveillance disruption, unauthorized viewing|
|Employee access cards|Information / Physical Security|User Domain|Card cloning, loss, unauthorized physical access|
|Access points / Door scanners|Hardware|LAN-to-WAN Domain (Physical Access Control Network)|Tailgating, scanner bypass, credential spoofing, denial of access|


---

# Experiment No. 1

## Aim

To study and implement Control Self-Assessment (CSA) by designing a CSA methodology and evaluating the effectiveness of internal controls in a Freight Forwarding ERP system.

---

# Part A

## Selected Domain

**Freight Forwarding ERP (Logistics Management System)**

### Description

The Freight Forwarding ERP is an enterprise application used by freight forwarding companies to manage end-to-end logistics operations. The system handles customer enquiries, quotations, bookings, shipment tracking, documentation, customs information, invoicing, payments, trucking operations, and employee management.

The ERP stores business-critical information such as:

* Customer details
* Shipment information
* Bills of Lading
* Commercial invoices
* Container details
* Financial transactions
* Employee records
* Audit logs

As this information is critical to business continuity, implementing effective internal controls is essential.

---

# Internal Controls Identified

| Control                           | Purpose                                             |
| --------------------------------- | --------------------------------------------------- |
| Role-Based Access Control (RBAC)  | Prevent unauthorized module access                  |
| Multi-Factor Authentication (MFA) | Secure user login                                   |
| Approval Workflow                 | Manager approval before quotations/invoices         |
| Audit Logging                     | Record every user activity                          |
| Daily Database Backup             | Prevent data loss                                   |
| Encryption                        | Protect sensitive customer and financial data       |
| Segregation of Duties             | Prevent fraud by separating responsibilities        |
| Password Policy                   | Strong password enforcement                         |
| Session Timeout                   | Prevent unauthorized access from unattended systems |
| Antivirus & Endpoint Protection   | Protect workstations                                |
| Firewall                          | Prevent unauthorized network access                 |
| Document Version Control          | Prevent unauthorized document modification          |
| Physical Server Security          | Restrict physical access                            |
| Disaster Recovery Plan            | Ensure business continuity                          |
| Employee Offboarding Process      | Disable accounts immediately after resignation      |

---

# CSA Methodology

### Step 1  Preparation

* Understand Freight Forwarding ERP modules
* Identify business objectives
* Identify critical assets
* Identify existing controls

---

### Step 2  Control Assessment

Evaluate whether the controls:

* Exist
* Are documented
* Are followed
* Are effective

---

### Step 3  Identify Improvement Opportunities

Identify:

* Weak passwords
* Missing approvals
* Lack of backups
* Excessive user permissions
* Missing audit trails

---

### Step 4  Improvement Plan

Assign corrective actions to responsible personnel.

Example

| Action                       | Owner                  |
| ---------------------------- | ---------------------- |
| Enable MFA                   | IT Administrator       |
| Weekly Backup Testing        | Database Administrator |
| Quarterly User Access Review | Security Officer       |
| Firewall Rule Review         | Network Administrator  |

---

# Part B

## Case Study

### Organization

**Oceanic Freight Forwarding Pvt. Ltd.**

The company manages export and import shipments globally. Employees use the ERP for quotations, bookings, customs documentation, invoicing, trucking management, and shipment tracking.

Since all operational data is stored digitally, protecting data confidentiality, integrity, and availability is essential.

---

# Data as an Asset (Seven Attributes)

| Attribute       | ERP Example                                                       |
| --------------- | ----------------------------------------------------------------- |
| Confidentiality | Customer quotations should only be visible to authorized staff.   |
| Integrity       | Shipment details must not be altered without authorization.       |
| Availability    | ERP should remain available during office hours.                  |
| Authenticity    | Only verified employees can create or approve bookings.           |
| Accuracy        | Invoice amounts must exactly match shipment charges.              |
| Consistency     | Shipment status must remain synchronized across all modules.      |
| Privacy         | Employee and customer personal information must remain protected. |

---

# Assessment Questionnaire

**Response Options: Yes / No / N/A**

### General Controls

1. Is Role-Based Access Control implemented?
2. Is Multi-Factor Authentication enabled?
3. Are audit logs maintained?
4. Are user accounts reviewed periodically?
5. Is there a documented Information Security Policy?

### Data Security

6. Is customer data encrypted?
7. Are financial records encrypted?
8. Are daily database backups performed?
9. Are backup restoration tests conducted?
10. Is database access restricted?

### Network Security

11. Is a firewall deployed?
12. Is antivirus installed on all systems?
13. Is VPN required for remote access?

### Operational Controls

14. Are quotations approved before sending to customers?
15. Are invoices approved before generation?
16. Are Bills of Lading version-controlled?
17. Are shipment modifications logged?

### Human Resource Controls

18. Are employee accounts disabled immediately after resignation?
19. Are passwords changed periodically?
20. Is cybersecurity awareness training conducted?
21. Are phishing awareness certifications submitted?

---

# Control Self-Assessment Evaluation

| Question                          | Yes |  No | N/A |
| --------------------------------- | :-: | :-: | :-: |
| RBAC implemented                  |  ✓  |     |     |
| MFA enabled                       |  ✓  |     |     |
| Audit logs maintained             |  ✓  |     |     |
| Daily backups performed           |  ✓  |     |     |
| Backup restoration tested         |     |  ✓  |     |
| Firewall deployed                 |  ✓  |     |     |
| Antivirus installed               |  ✓  |     |     |
| Database encrypted                |  ✓  |     |     |
| Customer data encrypted           |  ✓  |     |     |
| Invoice approval workflow         |  ✓  |     |     |
| Quotation approval workflow       |  ✓  |     |     |
| Employee offboarding process      |  ✓  |     |     |
| Password policy enforced          |  ✓  |     |     |
| Quarterly access review           |     |  ✓  |     |
| Security awareness training       |  ✓  |     |     |
| Disaster recovery plan documented |  ✓  |     |     |
| DR drills conducted               |     |  ✓  |     |
| VPN for remote users              |     |     |     |
| Physical server access restricted |     |     |     |
| Database activity monitoring      |     |     |     |

---

# Assessment Summary

| Result         | Count |
| -------------- | ----: |
| Total Controls |    20 |
| Yes            |    17 |
| No             |     3 |
| N/A            |     0 |

---

# Findings

1. Backup restoration testing is not performed regularly.
2. User access rights are not reviewed quarterly.
3. Disaster recovery drills have not been conducted.

These weaknesses could reduce resilience against cyber incidents or operational failures.

---

# Recommendations

* Perform quarterly backup restoration testing.
* Conduct periodic user access reviews to remove excessive privileges.
* Schedule annual disaster recovery drills.
* Continuously monitor audit logs using a SIEM solution.
* Conduct phishing and cybersecurity awareness training every six months.
* Review firewall rules and endpoint security policies quarterly.

---

| Control                                              | Evidence                                                                                                                | Observation                                                                                                                                                                                                                           | Improvements                                                                                                                   | Action                                                                                                                                   | Owner                                        | Date              |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ----------------- |
| **Role-Based Access Control (RBAC)**                 | User-role matrix, employee accounts, module permission settings and access logs were reviewed.                          | Access is assigned according to roles such as Sales, Pricing, Documentation, Accounts and Administrator. However, access rights are not reviewed periodically, and some users may retain unnecessary permissions after a role change. | Conduct quarterly access reviews and apply the principle of least privilege.                                                   | Review all active user accounts, remove excessive permissions and establish a quarterly access-certification process.                    | System Administrator and Department Managers | 31 July 2026      |
| **Multi-Factor Authentication and Password Control** | Login settings, password policy configuration and authentication records were examined.                                 | Strong passwords are required, but MFA is not enabled for every user, particularly users accessing the ERP remotely.                                                                                                                  | Make MFA compulsory for administrators, finance users and remote users. Introduce account lockout and password-reset controls. | Enable MFA, configure account lockout after repeated failed attempts and document the authentication policy.                             | IT Administrator                             | 10 August 2026    |
| **Quotation and Rate Approval Control**              | Quotation records, pricing sheets, approval history and user activity logs were reviewed.                               | Quotations are prepared by the Sales or Pricing team, but urgent quotations may be sent without recorded managerial approval. This can result in incorrect rates or reduced profit margins.                                           | Configure a mandatory approval workflow based on value, margin and shipment type.                                              | Prevent quotations from being issued until the Pricing Manager or authorized approver has approved them electronically.                  | Pricing Manager and ERP Administrator        | 15 August 2026    |
| **Invoice and Payment Approval Control**             | Customer invoices, vendor bills, payment requests, approval records and accounting reports were examined.               | Invoices are generated through the ERP, but the same employee may sometimes prepare and approve a financial transaction. This weakens segregation of duties.                                                                          | Separate invoice preparation, verification and approval responsibilities.                                                      | Configure different roles for invoice creator, verifier and final approver. Restrict users from approving transactions they created.     | Accounts Manager                             | 20 August 2026    |
| **Shipment and Document Version Control**            | Bills of Lading, Shipping Instructions, invoices, packing lists, document versions and modification logs were reviewed. | Shipment documents are stored in the ERP, but users may download and circulate outdated document versions through email or messaging applications.                                                                                    | Introduce version numbering, draft/final status, approval locking and visible watermarks.                                      | Configure the ERP to mark documents as Draft, Approved or Superseded and prevent editing of approved documents without authorization.    | Documentation Manager and ERP Administrator  | 25 August 2026    |
| **Audit Logging**                                    | User login logs, record modification history, deletion records and approval logs were inspected.                        | Important activities are logged, but logs are not regularly reviewed. Suspicious modifications may therefore remain undetected.                                                                                                       | Establish periodic review of high-risk activities and alerts for unusual actions.                                              | Create alerts for repeated login failures, deleted records, bank-detail changes, rate changes and modifications after approval.          | Information Security Officer                 | 31 August 2026    |
| **Database Backup and Recovery**                     | Backup schedules, backup files, cloud or off-site storage records and restoration reports were examined.                | Daily backups are performed, but no recent evidence of a complete restoration test was available. A backup may therefore exist without being usable during an incident.                                                               | Conduct quarterly restoration testing and retain copies in separate locations.                                                 | Perform a full restoration test, document the recovery time and maintain one encrypted off-site backup.                                  | Database Administrator                       | 5 September 2026  |
| **Employee Account Offboarding**                     | Resignation records, HR notifications, disabled user accounts, access-card records and system logs were reviewed.       | Accounts are disabled after HR informs IT, but delays may occur between the employee’s final working day and account deactivation.                                                                                                    | Automate offboarding and establish a checklist covering all physical and digital access.                                       | Link the HR exit workflow with ERP account disabling, email access removal, VPN revocation and access-card deactivation.                 | HR Manager and IT Administrator              | 10 September 2026 |
| **Remote Access and VPN Control**                    | VPN configuration, remote-login records, device inventory and remote-access permissions were reviewed.                  | Remote access is available to selected employees, but device compliance and connection security are not always verified.                                                                                                              | Allow remote access only through VPN and approved company devices.                                                             | Enforce VPN, endpoint protection, device encryption and automatic session timeout for all remote ERP access.                             | Network Administrator                        | 15 September 2026 |
| **Disaster Recovery and Business Continuity**        | Disaster recovery plan, server architecture, emergency contact list and previous drill records were examined.           | A basic recovery plan exists, but no formal disaster recovery drill has been conducted. Employees may not know their responsibilities during a major outage or cyberattack.                                                           | Define recovery objectives and conduct annual disaster recovery exercises.                                                     | Establish Recovery Time Objective and Recovery Point Objective values, assign responsibilities and conduct a simulated ERP outage drill. | IT Head and Business Continuity Team         | 30 September 2026 |
# Conclusion

The Control Self-Assessment indicates that the Freight Forwarding ERP has a mature internal control environment with strong access controls, approval workflows, encryption, and audit logging. However, improvements are required in backup validation, periodic access reviews, and disaster recovery testing to further strengthen the confidentiality, integrity, availability, and resilience of business-critical data.

---


  

# References
- Own ERP Platform
###### Information
- date: 2026.07.20
- time: 12:24