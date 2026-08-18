---

Title: "ISA Class Assignment 1"

Status:

marker:

tags:

Date: "2026.07.22"

Time: "10:26"

---
# The Audit War Room

## Information Systems Audit Assignment  XYZ Bank

### Scenario

XYZ Bank suffered a ransomware attack last month. Customer accounts were accessed, critical servers were encrypted, and the Reserve Bank of India (RBI) ordered an immediate information systems audit. An external audit team has one day to investigate the incident, evaluate controls, collect evidence, and recommend corrective actions.

## Group of Five

|Team member|Assigned role|Main responsibility|
|---|---|---|
|Member 1|Audit Planning|Define scope, risks, interviews, documents and audit schedule|
|Member 2|Evidence Collection|Obtain, preserve and assess audit evidence|
|Member 3|Audit Report|Compile findings, recommendations and conclusion|
|Member 4|Application Controls|Review controls over the online transaction system|
|Member 5|Security & Disaster Recovery|Assess cybersecurity, backup, recovery and continuity controls|

---

# 1. Audit Planning

## Planning

Because the audit must be completed within one day, the team will use a risk-based approach. Priority will be given to systems affected by ransomware, customer-account access, privileged accounts, transaction integrity, backups and regulatory compliance.

### One-day audit schedule

|Time|Activity|
|---|---|
|9:00–9:30 AM|Entry meeting with management|
|9:30–11:00 AM|Interviews and collection of documents|
|11:00 AM–1:00 PM|Review of servers, applications, access and security logs|
|1:00–2:30 PM|Review of transactions, backups and disaster recovery controls|
|2:30–4:00 PM|Validate evidence and classify findings|
|4:00–5:00 PM|Exit meeting and presentation of preliminary findings|

## Audit objectives

The audit will determine:

- How the ransomware entered the bank’s environment.
- Which systems and customer accounts were affected.
- Whether unauthorized transactions or data changes occurred.
- Whether access controls were operating effectively.
- Whether backups and recovery arrangements were adequate.
- Whether the bank complied with applicable RBI requirements and internal policies.
- What immediate and long-term corrective measures are required.

## Scope

The audit covers the Core Banking Solution (CBS) and everything that powers, protects or connects to it.

### Systems to be audited

- Core Banking Solution.
- Internet and mobile banking applications.
- Customer and transaction databases.
- Application and database servers.
- Active Directory and identity-management systems.
- Employee workstations and administrative devices.
- Firewalls, routers, VPNs and network security devices.
- Email and endpoint-security systems.
- Backup servers and storage devices.
- Disaster recovery site and recovery systems.
- Security information and event management system.
- Payment interfaces, ATM systems and relevant third-party connections.
- Privileged-access and remote-access systems.

## Security perimeter

The security perimeter includes:

- Internet-facing applications.
- Internal banking network.
- Branch connections.
- Remote-access and VPN services.
- Cloud services used by the bank.
- Third-party and vendor connections.
- Employee and administrator endpoints.
- Backup and disaster recovery environments.
- Physical access to the data centre and network rooms.

The team will review network segmentation, firewall rules, exposed services, remote-access controls, privileged accounts and the separation of production systems from backup systems.

## Site survey

The audit team will inspect:

- Primary data centre.
- Disaster recovery site.
- Network operations centre.
- Security operations centre.
- Server and communication rooms.
- Backup-storage locations.
- Physical access controls, including CCTV and access-card records.
- Fire protection, power supply, cooling and environmental controls.

## Departments to interview

- Information Technology.
- Information Security/SOC.
- Core Banking Operations.
- Risk Management.
- Internal Audit.
- Compliance and Legal.
- Business Continuity and Disaster Recovery.
- Human Resources.
- Customer Service and Fraud Investigation.
- Branch Operations.
- Finance.
- Third-party/vendor management.
- Senior management and the Chief Information Security Officer.

## Documents to request

- Information security and cybersecurity policies.
- Access-control and password policies.
- User and privileged-account lists.
- Network and system architecture diagrams.
- Asset inventory.
- Firewall, VPN, server and endpoint logs.
- Core banking login and transaction logs.
- Antivirus and endpoint detection reports.
- Vulnerability-assessment and penetration-testing reports.
- Patch-management records.
- Backup schedules, backup logs and restoration-test reports.
- Business continuity and disaster recovery plans.
- Previous audit reports.
- Incident response plan and ransomware incident report.
- CCTV footage and physical-access records.
- Employee training and phishing-test records.
- Third-party contracts and service-level agreements.
- Regulatory compliance reports.
- Change-management records.

## Historical incidents

The team will examine:

- Earlier malware or ransomware infections.
- Phishing incidents.
- Unauthorized login attempts.
- Customer complaints about suspicious transactions.
- Previous data breaches.
- System outages and failed backups.
- Repeated audit findings.
- Previous vulnerability reports that were not resolved.

This review will show whether management knew about weaknesses but failed to correct them.

## Expected risks

- Weak or reused passwords.
- Shared employee accounts.
- Excessive privileged access.
- Lack of multi-factor authentication.
- Unauthorized access to customer accounts.
- Fraudulent or altered transactions.
- Missing or manipulated logs.
- Unpatched servers and applications.
- Phishing and compromised employee credentials.
- Poor network segmentation.
- Inadequate monitoring.
- Unencrypted customer data.
- Failed or nonexistent backups.
- Backups connected to the infected network.
- Untested disaster recovery arrangements.
- Non-compliance with RBI requirements.
- Reputational damage and interruption of banking services.

## Entry meeting

The entry meeting will include senior management, IT, information security, compliance, operations and internal audit.

The team will:

1. Introduce the audit team and individual responsibilities.
2. Explain the RBI-directed audit and its objectives.
3. Confirm the scope, systems and locations included.
4. Establish the ransomware incident timeline.
5. Identify system owners and contact persons.
6. Request immediate preservation of logs and devices.
7. Agree on evidence-access procedures.
8. Explain confidentiality requirements.
9. Establish deadlines for submitting information.
10. Confirm the time of the exit meeting.

---

# 2. Evidence Collection

## Purpose

Evidence is collected to support audit findings with reliable and verifiable facts. It helps the team determine what happened, identify the responsible weaknesses and defend its conclusions.

## Evidence register

|Evidence|What it may demonstrate|Collection method|
|---|---|---|
|Firewall logs|Malicious IP addresses, blocked traffic, remote connections and possible entry points|Export directly from the firewall or central log server|
|CCTV footage|Physical entry into server rooms or restricted areas|Obtain a time-stamped copy from the physical-security system|
|Antivirus/EDR report|Malware detection, infected devices, ransomware behavior and failed protection|Export reports from the security console|
|Employee interviews|Actual working practices, account sharing and incident response actions|Conduct structured interviews and document signed minutes|
|Login history|Unauthorized access, unusual login times and compromised accounts|Export from CBS, Active Directory, VPN and authentication systems|
|Asset list|Devices affected and whether systems were properly identified and managed|Obtain the approved inventory and verify it physically|
|Transaction logs|Unauthorized, duplicated or altered transactions|Export read-only records from the CBS and database|
|Policies|Expected procedures and management-approved control requirements|Obtain current approved and dated copies|
|Backup logs|Backup frequency, failures, retention and restoration status|Export from backup software and storage systems|
|Email records|Phishing messages and malicious attachments|Preserve relevant messages with headers and attachments|
|Access-card records|Physical access to sensitive areas|Export from the building access-control system|
|Change records|Unauthorized or emergency changes before the incident|Obtain tickets and system-change history|

## Evidence-collection methods

- Inspection of documents, configurations and physical locations.
- Observation of employees performing procedures.
- Interviews and written confirmations.
- Reperformance of selected controls.
- Read-only extraction of logs and reports.
- Sampling of users and transactions.
- Screenshots showing system date, time and source.
- Configuration exports from security devices.
- Forensic imaging of affected devices by qualified personnel.
- Comparison of evidence from independent sources.

Evidence must be protected from alteration. Each item should be labelled with its source, date, time, collector and storage location. Hash values should be calculated for digital evidence, and a chain-of-custody record should be maintained.

## Strongest evidence

System-generated logs and transaction records are generally the strongest evidence when they are complete, time-synchronized, protected against alteration and collected directly from the original system.

A useful strength order is:

1. Protected system, authentication and transaction logs.
2. Independently verified backup and security reports.
3. Asset lists and approved policies supported by observation.
4. Documents created during normal operations.
5. Employee interviews.

Interview statements alone are weaker because they may be incomplete or biased. They should be confirmed using logs, records or direct observation.

## Classification of identified findings

|Finding|Rating|Reason|
|---|---|---|
|No backups were performed|Critical|The bank may be unable to restore encrypted systems or recover customer and transaction data|
|Employees share accounts|Critical|Actions cannot be attributed to individuals, and unauthorized access or fraud may go undetected|
|Password is “Welcome123”|High|The password is predictable and easily compromised, creating a serious unauthorized-access risk|

If “Welcome123” is used for a privileged, CBS or widely shared account, it should also be classified as **Critical**.

---

# 3. Audit Report

## Executive summary

The audit identified serious weaknesses in XYZ Bank’s access control, backup management and information security practices. A weak password was in use, employees shared accounts, and required backups had not been performed.

These weaknesses significantly increased the likelihood and impact of the ransomware attack. Shared accounts and weak credentials could have allowed unauthorized access to customer information, while the absence of backups prevented timely restoration of encrypted systems.

The bank’s control environment is therefore assessed as **ineffective and high risk**. Immediate corrective action is required to protect customer data, restore services and meet regulatory obligations.

## Findings and recommendations

### Finding 1: No backups were performed  Critical

**Condition:** The bank could not provide evidence that regular backups had been completed.

**Risk:** Encrypted or destroyed systems may not be recoverable. The bank could permanently lose customer, account and transaction data.

**Recommendation:**

- Implement automated backups immediately.
- Follow the 3-2-1 principle: three copies, two storage types and one offline or off-site copy.
- Maintain immutable or write-protected backups.
- Separate backup credentials and systems from the production domain.
- Monitor every backup job and investigate failures.
- test restoration at defined intervals.
- Define recovery time and recovery point objectives.

### Finding 2: Employees share accounts  Critical

**Condition:** Multiple employees use the same user accounts.

**Risk:** The bank cannot identify who performed an activity. Shared accounts facilitate unauthorized access, fraud and concealment of malicious actions.

**Recommendation:**

- Assign a unique account to every employee.
- Disable shared and generic accounts unless technically unavoidable.
- Require management approval for exceptional service accounts.
- Use role-based access control and least privilege.
- Introduce multi-factor authentication.
- Review accounts and permissions regularly.
- Log and monitor all privileged activity.

### Finding 3: Weak password “Welcome123”  High

**Condition:** A predictable password was used on a bank system.

**Risk:** Attackers may guess or obtain the password and access customer or administrative systems.

**Recommendation:**

- Reset the password immediately.
- Force password changes for potentially exposed accounts.
- Block common and compromised passwords.
- Require long passphrases.
- Introduce multi-factor authentication.
- Apply account lockout and login-rate limiting.
- Store passwords using secure salted hashing.
- Monitor repeated login failures and unusual access.

## Conclusion

XYZ Bank did not maintain adequate preventive, detective or recovery controls. The ransomware attack exposed weaknesses that existed before the incident, particularly in identity management and backup operations.

Critical systems should not return to normal operation until compromised credentials have been reset, affected systems have been rebuilt or verified as clean, access has been restricted, and recovery arrangements have been tested. Management should prepare a formal remediation plan with accountable owners and deadlines. A follow-up audit should confirm that corrective actions are operating effectively.

---

# 4. Application Controls

The online transaction system must protect the accuracy, completeness, authorization and validity of every transaction.

## Input controls

Input controls ensure that information entered into the system is complete, valid and authorized.

### User ID validation

- Each user must have a unique user ID.
- The ID must exist and have an active status.
- The user must be authorized for the requested function.
- Dormant, terminated or locked accounts must be rejected.
- Customer and employee accounts must be separated.
- Sensitive functions must follow role-based access rules.

### Password validation

- Passwords must be checked using secure password hashes.
- Plain-text passwords must never be stored or logged.
- Common and compromised passwords must be blocked.
- Multi-factor authentication should be required.
- Repeated failures should trigger rate limiting or account lockout.
- Password reset must verify the user’s identity.
- Sessions should expire after inactivity.

### Other input controls

- Mandatory-field checks.
- Data-type and format checks.
- Account-number validation.
- Amount and transaction-limit checks.
- Sufficient-balance checks.
- Date and time validation.
- Beneficiary validation.
- Confirmation screen before submission.
- Maker-checker approval for high-value or sensitive transactions.

## Processing controls

Processing controls ensure that accepted transactions are processed completely, accurately and only once.

### Duplicate-submission control

The system should:

- Generate a unique transaction reference or idempotency key.
- Disable the submit button after the first valid submission.
- Reject repeated requests using the same reference.
- Check account, amount, beneficiary and time for likely duplicates.
- Process debit and credit entries as one atomic transaction.
- Roll back the entire transaction if any processing step fails.
- Clearly show whether a transaction succeeded, failed or is pending.
- Reconcile pending transactions with the payment network.

### Other processing controls

- Apply approved interest, fee and tax calculations.
- Enforce account and daily transaction limits.
- Maintain proper debit-credit balancing.
- Use sequence checks and control totals.
- Record all processing steps in an audit trail.
- Prevent users from changing completed transactions directly.
- Route reversals through an authorized process.
- Require secondary approval for exceptional transactions.

## Output controls

Output controls ensure that reports, receipts and statements are accurate, complete and provided only to authorized people.

### Transaction-report generation

Each report should include:

- Unique transaction reference.
- Transaction date and time.
- Masked account information.
- Transaction type.
- Amount and currency.
- Beneficiary details where applicable.
- Transaction status.
- User or channel that initiated the transaction.
- Authorizer details for maker-checker transactions.
- Reversal or failure reason, if applicable.

The system should also:

- Reconcile report totals with database and general-ledger totals.
- Restrict reports according to user roles.
- Encrypt reports during storage and transmission.
- Mask sensitive personal and account data.
- Prevent unauthorized editing.
- Record who viewed, generated, downloaded or printed a report.
- Apply approved report-retention periods.
- Require review of exception and failed-transaction reports.

---

# 5. Security and Disaster Recovery

## Scenario: Ransomware encrypts the server

The following controls should already exist before an attack occurs.

## Preventive security controls

- Multi-factor authentication.
- Strong, unique passwords.
- Removal of shared accounts.
- Least-privilege access.
- Privileged-access management.
- Endpoint detection and response.
- Regular patching and vulnerability management.
- Email filtering and attachment scanning.
- Network segmentation.
- Restricted remote access.
- Application allow-listing.
- Security-awareness and phishing training.
- Encryption of sensitive customer data.
- Secure configuration baselines.
- Third-party access controls.

## Detective controls

- Centralized and tamper-resistant logging.
- Continuous security monitoring.
- Alerts for unusual account activity.
- Alerts for mass file encryption.
- Antivirus and EDR alerts.
- Failed-login and privilege-escalation monitoring.
- File-integrity monitoring.
- Data-loss prevention.
- Regular security reviews and penetration testing.

## Backup and recovery controls

- Automated and monitored backups.
- Offline, off-site and immutable backup copies.
- Separate backup credentials.
- Multiple backup generations.
- Regular restoration tests.
- Documented recovery procedures.
- Recovery point objectives for acceptable data loss.
- Recovery time objectives for acceptable service downtime.
- A geographically separate disaster recovery site.
- Clean recovery images and essential software.
- Replicated critical data with protection against ransomware propagation.

## Business continuity arrangements

- Approved business continuity and disaster recovery plans.
- Defined incident-response team and contact list.
- Alternative communication arrangements.
- Manual procedures for critical banking services.
- Priority order for recovering systems.
- Periodic tabletop exercises and full recovery tests.
- Arrangements with critical technology vendors.
- Regulatory and customer communication procedures.

## Immediate response when ransomware is detected

1. Activate the incident-response and crisis-management teams.
2. Isolate infected servers and endpoints from the network.
3. Disable compromised accounts and remote-access channels.
4. Do not destroy or unnecessarily alter affected systems.
5. Preserve logs, memory images and disk evidence.
6. Determine the ransomware strain and initial entry point.
7. Identify affected systems, users and customer data.
8. Block malicious indicators across the environment.
9. Notify management, regulators, law enforcement and affected parties as required.
10. Rebuild systems from verified clean sources.
11. Restore data from tested offline or immutable backups.
12. Validate system and transaction integrity before reconnecting.
13. Increase monitoring after recovery.
14. conduct a post-incident review and update controls.

## Recovery priority

1. Identity, authentication and security-monitoring services.
2. Core Banking Solution and customer-account database.
3. Payment and transaction-processing services.
4. Internet and mobile banking.
5. ATM and branch-banking services.
6. Reporting and supporting administrative systems.

## Final security and DR assessment

XYZ Bank was not adequately prepared for ransomware because essential access and backup controls were absent or ineffective. The bank must implement layered security, tested offline backups, a functioning disaster recovery site and a regularly exercised incident-response plan. Recovery should be treated as a verified business capability rather than merely a written policy.   