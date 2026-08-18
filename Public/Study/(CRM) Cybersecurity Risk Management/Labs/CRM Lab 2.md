---

Title: "CRM Lab 2"

Status:

marker:

tags:

Date: "2026.07.25"

Time: "10:27"

---
# CRM Lab 2

| Sr. No | Risk – Threat – Vulnerability                                   | Primary Domain Impacted                                                                                                                                                | Domain         | Impact | Likelihood                  | I   |
| ------ | --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------ | --------------------------- | --- |
| 1      | Unauthorized access from public Internet                        | Lan to Wan / Remote Access<br><br>Countermeasure : Make sure only authorized and try to avoid remote access gateways                                                   | Infrastructure | 5      | 4                           |     |
| 2      | User destroys data in application and deletes all files         | User Domain<br><br>Countermeasure:<br><br>Add an administration lock on files on applications and files that are sensitive / not supposed to be deleted.               | Information    | 3      | 3                           |     |
| 4      | VPN tunneling between remote computer and ingress/egress router | Remote Access / LAN to Wan<br><br>Make sure only known / Trusted gateways can connect and only after authentication.                                                   | Infrastructure | 3      | 2                           |     |
| 5      | Fire destroys primary data center                               | System Application Domain<br><br>Countermeasure :<br><br>Ensure fire safety and ensure backups                                                                         | Infrastructure | 3      | 2                           |     |
| 6      | Communication circuit outages                                   | Lan to Wan Domain<br><br>Countermeasure :<br><br>Failover connection and backup routes.                                                                                | Infrastructure | 3      | 3                           |     |
| 7      | Workstation OS has a known software vulnerability               | Workstation Domain<br><br>Countermasure :<br><br>Make sure latest security updates are installed; Make sure vulnerable software installation is not allowed.           | Application    | 4      | 4                           |     |
| 8      | Unauthorized access to organization owned Workstations          | User Domain<br><br>Countermeasure:<br><br>Ensure RBAC                                                                                                                  | Infrastructure | 5      | 3.5                         |     |
| 9      | Loss of production data                                         | Lan Domain<br><br>Countermeasure:<br><br>Timed Backups                                                                                                                 | Information    | 4      | 3                           |     |
| 10     | Denial of service attack on organization e-mail Server          | WAN Domain<br><br>Countermeasure:<br><br>Ensure rate limits;<br><br>Queuing legitimate requests;<br><br>Firewall                                                       | Information    | 4      | 3                           |     |
| 11     | Remote communications from home office                          | Remote Access Domain<br><br>Countermeasure:<br><br>RBAC and Key Rotation + 2FA must have for remote connections IF necessary at all                                    | Infrastructure | 2      | 2                           |     |
| 12     | LAN server OS has a known software vulnerability                | Lan Domain<br><br>Countermeasure :<br><br>Maintain the server and make sure there are latest updates.                                                                  | Application    | 3.5    | 4                           |     |
| 13     | User downloads an unknown email attachment                      | User Domain<br><br>Countermeasure:<br><br>User awareness programs and IDPS and Malware Detection for last layer security.                                              | People         | 4      | 4                           |     |
| 14     | Workstation browser has software vulnerability                  | Workstation Domain<br><br>Countermeasure:<br><br>Workstation Browser must be on latest version and from a verified source with checksum checks.                        | Application    | 3.5    | 5 Depends on Maintenance    |     |
| 15     | Service provider has a major network outage                     | Lan to Wan Domain<br><br>Countermeasure:<br><br>Backup service providers and ensure reliability on service providers                                                   | Application    | 3      | 3                           |     |
| 16     | Weak ingress/egress traffic filtering degrades performance      | Lan to Wan Domain<br><br>Countermeasure:<br><br>Configure firewalls and ACLs with proper ingress/egress filtering; deploy IDS/IPS and regularly review firewall rules. | Application    | 3      | 4<br>Depends on application |     |
|        |                                                                 |                                                                                                                                                                        |                |        |                             |     |
  
## C. Risk Impact Assessment Using C-I-A-P

**Rating scale:** H = High impact, M = Medium impact, L = Low impact, and N/A = no material direct impact.

### A. Unauthorised Access from the Public Internet

| Risk / Asset Area | C | I | A | P | Risk Impact | Mitigation and Management |
| --- | :---: | :---: | :---: | :---: | --- | --- |
| Information | H | H | M | H | An external attacker may view, copy, alter or delete confidential business and personal information. | Classify and encrypt sensitive information, apply least privilege, monitor data access, and maintain tested offline backups. |
| Application | H | H | H | M | Compromised accounts or exposed services may allow application takeover, malicious changes or service disruption. | Use MFA, secure authentication, timely patching, secure coding, WAF protection, vulnerability scanning and application logs. |
| Infrastructure | H | H | H | M | The attacker may enter through an exposed port, VPN, firewall or remote-access gateway and move laterally. | Deny access by default, close unused ports, segment networks, use firewalls and IDS/IPS, harden remote access, and review rules regularly. |
| People | H | M | M | H | Stolen credentials, phishing and social engineering may expose employees and customers to fraud or identity theft. | Conduct awareness training, enforce MFA and strong password policies, provide a simple incident-reporting channel, and rehearse response procedures. |

**Overall risk:** Critical because successful Internet-based access can affect every organisational domain.

### B. Denial-of-Service Attack on the Organisation E-mail Server

| Risk / Asset Area | C | I | A | P | Risk Impact | Mitigation and Management |
| --- | :---: | :---: | :---: | :---: | --- | --- |
| Information | L | L | H | L | Messages may be delayed, lost or inaccessible; confidentiality is normally not the attacker's primary target. | Queue messages, use redundant mail storage, back up mailboxes and verify message delivery after recovery. |
| Application | L | M | H | L | The mail service may become slow or unavailable, and overloaded processes may fail. | Apply rate limits, connection throttling, anti-spam controls, health monitoring and automatic service failover. |
| Infrastructure | L | M | H | L | Network bandwidth, DNS, gateways, load balancers and server resources may be exhausted. | Use upstream DDoS protection, redundant links, load balancing, traffic filtering, capacity planning and tested failover. |
| People | M | L | H | M | Employees cannot communicate, customers may not receive support, and attackers may exploit the outage for impersonation. | Maintain approved alternate communication channels, publish an outage procedure and warn users about outage-related phishing. |

**Overall risk:** High because e-mail is a critical communication service, even when confidentiality and integrity remain unaffected.

### C. Regulatory Compliance Obligations Were Not Adhered To

| Risk / Asset Area | C | I | A | P | Risk Impact | Mitigation and Management |
| --- | :---: | :---: | :---: | :---: | --- | --- |
| Information | H | H | M | H | Information may be collected, stored, shared or retained without a lawful basis or adequate protection. | Maintain a data inventory, classification and retention schedule; encrypt sensitive data; record consent and securely dispose of expired records. |
| Application | H | H | M | H | Applications may lack required access controls, audit trails, privacy notices or secure processing features. | Add compliance requirements to the SDLC, perform privacy/security reviews, retain audit logs and test controls before release. |
| Infrastructure | H | H | M | H | Weak configurations or unapproved storage locations may violate security, residency or retention requirements. | Use approved hardened platforms, configuration baselines, continuous compliance monitoring, encryption and controlled backup locations. |
| People | H | H | M | H | Staff may process personal or regulated information incorrectly, causing legal action, penalties and reputational damage. | Assign compliance ownership, train staff by role, require policy acknowledgement, conduct audits and apply a documented breach-response process. |

**Overall risk:** Critical because non-compliance can cause regulatory penalties, lawsuits, loss of trust and restrictions on business operations.

### D. Unauthorised Access by Users

| Risk / Asset Area | C | I | A | P | Risk Impact | Mitigation and Management |
| --- | :---: | :---: | :---: | :---: | --- | --- |
| Information | H | H | M | H | An employee, contractor or compromised account may access, copy, modify or delete information beyond an authorised role. | Apply RBAC and least privilege, perform periodic access reviews, use data-loss prevention, log sensitive actions and separate duties. |
| Application | H | H | H | M | Excessive privileges may allow users to change configurations, bypass workflows, commit fraud or stop services. | Enforce server-side authorisation, privileged-access management, MFA, approval workflows, session controls and application audit logs. |
| Infrastructure | H | H | H | M | Unauthorised administrative access may permit malware installation, security-control changes or lateral movement. | Restrict admin accounts, use separate privileged identities, segment networks, harden endpoints and monitor privileged commands. |
| People | H | H | M | H | Insider misuse or credential sharing can harm customers, employees and the organisation's reputation. | Conduct background checks where lawful, train users, prohibit account sharing, provide whistleblowing/reporting channels and promptly revoke leavers' access. |

**Overall risk:** Critical when privileged accounts are involved; otherwise High.

### E. Unprotected Storage/Retention and Outdated Devices/Workstations

| Risk / Asset Area | C | I | A | P | Risk Impact | Mitigation and Management |
| --- | :---: | :---: | :---: | :---: | --- | --- |
| Information | H | H | H | H | Unencrypted or over-retained data may be stolen, corrupted or made unavailable through malware or device loss. | Encrypt data at rest, classify it, minimise collection, enforce retention/deletion schedules and maintain protected, tested backups. |
| Application | H | H | H | M | Unsupported applications and operating systems may contain exploitable vulnerabilities or incompatible components. | Maintain an asset and software inventory, apply patches within defined SLAs, remove unsupported software and use application allow-listing. |
| Infrastructure | H | H | H | M | Legacy endpoints provide an easy entry point and may spread malware or ransomware across the network. | Replace end-of-life devices, use EDR, secure configurations, network segmentation, vulnerability scanning and quarantine for non-compliant endpoints. |
| People | H | M | M | H | Lost devices and weak storage practices expose users' personal data, while outdated systems make phishing and malware more successful. | Train users, enforce screen locks and device encryption, enable remote wipe, restrict local storage and provide a clear lost-device reporting process. |

**Overall risk:** Critical where sensitive data or unsupported Internet-connected devices are involved.

## Questions

### 1. Why is it important to address each identified threat or vulnerability from the C-I-A-P perspective?

The C-I-A-P perspective prevents the organisation from looking at risk through only one lens:

- **Confidentiality** asks whether information can be disclosed to an unauthorised person.
- **Integrity** asks whether information, systems or decisions can be changed without permission.
- **Availability** asks whether authorised users can access information and services when required.
- **Privacy** asks whether personal information is collected, used, retained and shared lawfully and fairly.

A single incident can affect these objectives differently. For example, a denial-of-service attack mainly affects availability, while unauthorised access may affect all four. Assessing each objective helps the organisation select suitable controls, estimate business consequences, avoid overlooking privacy obligations and decide which risks require immediate treatment.

### 2. How can a risk-management framework help assess the impact on information assets?

The standard considered is the **NIST Cybersecurity Framework (CSF) 2.0**. It can be applied as follows:

1. Use **ID.AM (Asset Management)** to identify information assets, owners, locations, classifications and dependencies.
2. Use **ID.RA (Risk Assessment)** to identify threats and vulnerabilities, estimate likelihood and impact, and record inherent risk.
3. Create a **Current Profile** showing existing controls and a **Target Profile** showing the required outcomes. The gap becomes the remediation plan.
4. Use **PR.AA (Identity Management, Authentication and Access Control)** to control who may access the information.
5. Use **PR.DS (Data Security)**, especially:
   - **PR.DS-01** for protecting the confidentiality, integrity and availability of data at rest;
   - **PR.DS-02** for data in transit;
   - **PR.DS-10** for data in use; and
   - **PR.DS-11** for creating, protecting, maintaining and testing backups.
6. Use **DE.CM (Continuous Monitoring)** to detect control failures and **RS.MA (Incident Management)** to manage incidents.
7. Reassess residual risk after controls are implemented and obtain formal acceptance where it remains above the organisation's risk appetite.

NIST CSF 2.0 provides common outcomes and terminology rather than prescribing one fixed technical solution. This allows the organisation to assess information risk consistently while choosing controls appropriate to its size, sector and obligations.

### 3. How should an identified threat be communicated, and how should remediation be prioritised?

The end-user message should be short, specific and actionable. It should state what was identified, who may be affected, what users must do, what they must avoid, where they can report suspicious activity and when the next update will be provided. Technical details that could help an attacker should be restricted to the incident team. Communication may use e-mail, the internal portal, security banners, manager briefings and emergency channels, depending on urgency.

Each risk should be recorded with an owner, affected asset, threat, vulnerability, existing controls, likelihood, impact, treatment, due date and status. Remediation should then be prioritised using:

> **Risk score = Likelihood × Impact**

The organisation should also consider data sensitivity, Internet exposure, active exploitation, number of users affected, legal deadlines, safety implications, business criticality and ease of attack. Critical risks with active exploitation or high-value information should be addressed first. Quick risk-reduction measures may be applied immediately, followed by a permanent corrective action. Remaining risk must be accepted by the authorised risk owner, not informally ignored.

### 4. Difference between effectiveness and efficiency in risk management

| Effectiveness | Efficiency |
| --- | --- |
| Measures whether a control achieves the intended security outcome. | Measures the resources used to achieve that outcome. |
| Focuses on doing the correct security work. | Focuses on doing the work with minimum avoidable cost, time and effort. |
| Example: MFA prevents unauthorised logins. | Example: MFA is deployed using automated enrolment and risk-based prompts that reduce support calls. |
| Typical measures include incident reduction, blocked attacks, detection coverage and residual risk. | Typical measures include cost per protected user, analyst time, alert-processing time and system overhead. |

A control can be efficient but ineffective, such as a cheap firewall rule that does not block the real attack path. It can also be effective but inefficient, such as manually reviewing every low-risk login. Good risk management first ensures that controls are effective and then improves their efficiency without weakening protection.

## Conclusion

This assessment shows that cybersecurity risks affect technology, information and people together. Unauthorised access, non-compliance, service disruption and obsolete systems can damage confidentiality, integrity, availability and privacy in different ways. The organisation should therefore identify assets, evaluate likelihood and business impact, apply layered controls, communicate clearly and continuously monitor residual risk. Using NIST CSF 2.0 provides a repeatable method to prioritise treatment and connect technical safeguards with business and regulatory needs. Risk cannot always be eliminated, but it can be reduced to an acceptable and formally approved level.

# References

1. [NIST Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20), NIST CSWP 29, 2024.
2. [NIST CSF 2.0 Reference Tool](https://csrc.nist.gov/projects/cybersecurity-framework/filters), including the CSF Core, subcategories and implementation examples.


###### Information
- date: 2026.07.25
- time: 10:27
