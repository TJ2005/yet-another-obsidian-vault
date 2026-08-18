---
Title: "CRM Lab 3"
Status: complete
tags: [semester-7, cybersecurity, CRM, lab]
Date: "2026.08.08"
---

# CRM Lab 3 — IT Risk Management Plan

## Aim

To review risks across the domains of a typical IT infrastructure and progressively develop an IT risk management plan for a technology company based in India and operating across multiple geographies.

## Procedure

1. Review the identified risks, threats, and vulnerabilities categorised according to the domains of a typical IT infrastructure. Refer to [[CRM Lab 1]] and the retained register in [[CRM Lab 2]].
2. For every infrastructure domain, review the risks using five stages:
   - Risk planning
   - Risk identification
   - Risk assessment
   - Risk mitigation
   - Risk monitoring
3. Assess a technology company based in India and operating across multiple geographies.
4. Prepare a comprehensive IT risk management plan table of contents encompassing the five major risk areas identified during the assessment.
5. Evaluate Annualised Rate of Occurrence (ARO), Single Loss Expectancy (SLE), and Annualised Loss Expectancy (ALE) as part of risk management planning.

## Part 1 and Part 2 — Domain-wise Risk Review

The following risks and infrastructure domains are reviewed from the earlier exercises in [[CRM Lab 1]] and [[CRM Lab 2]] using the five stages of risk management.

| No. | Risk, threat, or vulnerability                                         | IT infrastructure domain   | Risk planning                                                                                                                              | Risk identification                     | Risk assessment                                                         | Risk mitigation     | Risk monitoring                           |
| --: | ---------------------------------------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------- | ----------------------------------------------------------------------- | ------------------- | ----------------------------------------- |
|   1 | Unauthorised access from the public Internet                           | LAN-to-WAN / Remote Access | Scope: Devices / Infrastructure<br><br>Protect:<br>- Thin-client devices<br>- Remote-access computers<br>- Remotely accessed resources | Threats<br>- Mismanaged access controls | Likelihood: Medium, depending on configuration<br><br>Impact:<br>High | Configuration checks | SIEM logs for unrecognised login attempts |
|   2 | A user destroys application data and deletes files                     | User                       | Scope: Information<br><br>Protect:<br>- Files<br>- Data<br>- Databases                                                                      | Threats<br>- Mismanaged file access controls | Likelihood: High<br><br>Impact:<br>Medium                                | Lock important files | Access-log management                     |
|   3 | VPN tunnelling between a remote computer and the ingress/egress router | Remote Access / LAN-to-WAN | Scope: Devices / Network infrastructure<br><br>Protect:<br>- Sensitive computers<br>- Network infrastructure                              | Threats<br>- Remote connection to sensitive computers | Likelihood: Low if properly configured<br><br>Impact:<br>High             | Proper configuration of remote connections | Remote-connection and VPN logs            |
|   4 | Fire destroys the primary data centre                                  | System/Application         | Scope: Physical infrastructure<br><br>Protect:<br>- Buildings<br>- Infrastructure                                                         | Threats<br>- Destruction of important physical infrastructure | Likelihood: Low if regulations are followed<br><br>Impact:<br>High without backups; Medium with backups | Follow fire-safety regulations and maintain backups | Fire and environmental sensors            |
|   5 | Communication circuit outage                                           | LAN-to-WAN                 | Scope: Network<br><br>Protect:<br>- Connectivity<br>- Service continuity                                                                    | Threats<br>- Circuit or service-provider failure | Likelihood: Medium, depending on provider reliability<br><br>Impact:<br>High if no failover connection is available | Maintain redundant links and tested failover routes | Circuit availability and failover logs   |
|   6 | A workstation operating system has a known vulnerability               | Workstation                | Scope: Computer / Network if the computer is exposed<br><br>Protect:<br>- Device                                                            | Threats<br>- Remote code execution (RCE) | Likelihood: Depends on exposure and patch status<br><br>Impact:<br>High, depending on the workstation's use case | Keep the workstation up to date | Antivirus logs and unknown-process monitoring |
|   7 | Unauthorised access to organisation-owned workstations                 | User / Workstation         | Scope: Computer devices / Role access<br><br>Protect:<br>- Devices                                                                          | Threats<br>- RCE<br>- Backdoors | Likelihood: Depends on access controls<br><br>Impact:<br>Medium            | RBAC management     | Monitor stale roles                       |
|   8 | Loss of production data                                                | LAN                        | Scope: Data<br><br>Protect:<br>- Information                                                                                                | Threats<br>- Information loss | Likelihood: Depends on access and backup controls<br><br>Impact:<br>Medium with backups; High without backups | Maintain isolated backups | Monitor backup status and restoration-test results |
|   9 | Denial-of-service attack on the organisation's email server            | WAN / System/Application   | Scope: Network and applications<br><br>Protect:<br>- Business continuity                                                                   | Threats<br>- Loss of availability and business continuity | Likelihood: Depends on network protection<br><br>Impact:<br>High           | Use rate limiting, service redundancy, and backup communication channels | Monitor network, server, and email-service status |
|  10 | Insecure remote communications from a home office                      | Remote Access              | Scope: Devices<br><br>Protect:<br>- Devices                                                                                                 | Threats<br>- RCE | Likelihood: Depends on remote-access restrictions<br><br>Impact:<br>High   | Access controls and restrictions | Monitor account usage and restrictions    |
|  11 | A LAN server operating system has a known vulnerability                | LAN / System/Application   | Scope: Server infrastructure<br><br>Protect:<br>- Applications running on the server                                                        | Threats<br>- Bugs in the server operating system | Likelihood: Depends on server version and patch status<br><br>Impact:<br>Medium | Keep the server up to date | Monitor software versions                 |
|  12 | A user downloads an unknown email attachment                           | User                       | Scope: User email / Device<br><br>Protect:<br>- User data                                                                                   | Threats<br>- Information loss | Likelihood: Depends on user awareness<br><br>Impact:<br>Medium             | Awareness and training-needs-analysis (TNA) programmes | Conduct and monitor phishing drills       |
|  13 | A workstation browser has a known software vulnerability               | Workstation                | Scope: Workstation / Browser<br><br>Protect:<br>- Device<br>- Applications running on the workstation                                      | Threats<br>- Browser bugs<br>- RCE | Likelihood: Depends on browser version and patch status<br><br>Impact:<br>Medium | Keep the browser and workstation up to date | Monitor browser versions and security logs |
|  14 | A service provider suffers a major network outage                      | WAN / LAN-to-WAN           | Scope: Network and applications<br><br>Protect:<br>- Business continuity                                                                   | Threats<br>- Loss of availability and business continuity | Likelihood: Depends on service-provider reliability<br><br>Impact:<br>High | Maintain backup networks and service providers | Monitor network and provider status       |
|  15 | Weak ingress/egress traffic filtering degrades performance             | LAN-to-WAN                 | Scope: Network<br><br>Protect:<br>- Network performance<br>- Ingress and egress connections                                                 | Threats<br>- Weak filtering<br>- Unauthorised or harmful traffic | Likelihood: Depends on filter configuration<br><br>Impact:<br>Medium       | Improve ingress and egress filtering | Monitor packet and firewall logs          |

## Part 3 — Multi-geography Technology Company Assessment

### Company profile

For this assessment, the organisation is **Sahyadri ERP Technologies Pvt. Ltd.**, an Indian technology company providing a cloud-based enterprise resource planning platform to customers in multiple geographies.

| Question | Working answer |
| --- | --- |
| What technology product or service does the company provide? | A multi-tenant, cloud-based ERP platform. It provides HR, employee attendance, leave requests and approvals, administrative workflows, reporting, and other business-management functions through a web application. |
| Where is its headquarters in India? | Pune, Maharashtra, India. |
| In which other geographies does it operate? | India, the European Union, the United Kingdom, North America, and Southeast Asia. Customers and remote employees access the platform across these regions. |
| What information does it process? | Employee identities and roles, attendance and leave records, organisational information, workflow approvals, business records, authentication and access logs, and operational monitoring data. Some records may contain personal or sensitive business information. |
| What are its critical applications and infrastructure? | The ERP web application, authentication and role-based access system, tenant-isolated PostgreSQL database, workflow engine, background job workers, application servers, network and remote-access infrastructure, monitoring services, backups, and recovery systems. |
| Which employees, customers, vendors, and cloud/service providers are involved? | Customer employees and administrators, the company's developers, support staff and system administrators, business management, cloud and database providers, network providers, software vendors, auditors, and other authorised third parties. |
| Which legal, contractual, privacy, and security obligations may apply? | Indian data-protection and cybersecurity requirements, customer contracts and service-level agreements, applicable overseas privacy requirements, breach-notification duties, data-retention requirements, access-control obligations, and recognised security practices such as NIST CSF and ISO/IEC 27001. Privacy-management practices may also be mapped to ISO/IEC 27701. |
| What are the company's risk appetite and impact criteria? | Very low appetite for unauthorised cross-customer data access, privacy breaches, fraudulent or incorrect authoritative ERP actions, and unrecoverable data loss. Low appetite for prolonged service outages. Limited and formally approved risk may be accepted for minor, reversible issues that do not expose sensitive information or interrupt critical customer operations. Impact is evaluated using confidentiality, integrity, availability, privacy, financial loss, legal consequences, customer disruption, and reputational harm. |

### Five major risk areas

These categories consolidate the domain risks reviewed in Parts 1–2 and will form the core of the risk management plan in Part 4.

| Major risk area                                        | ERP context                                                                                                                                                                                 | Related reviewed risks        |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| 1. Identity, access, and tenant isolation              | Incorrect roles, stale permissions, compromised accounts, or failed tenant isolation may permit unauthorised access to another user or organisation's records.                              | Risks 1, 2, 7, and 10         |
| 2. Information protection, privacy, and recovery       | Employee and business data may be exposed, altered, deleted, over-retained, or become unrecoverable if access, storage, backup, and recovery controls fail.                                 | Risks 2, 4, 8, and 12         |
| 3. Application, workflow, and server integrity         | Vulnerable applications, browsers, operating systems, or workflow processing may enable RCE, incorrect approvals, duplicated actions, or unauthorised changes to authoritative ERP records. | Risks 6, 7, 11, and 13        |
| 4. Infrastructure availability and business continuity | Network failures, denial-of-service attacks, data-centre incidents, or failed background services may prevent customers from accessing essential ERP operations.                            | Risks 4, 5, 9, and 14         |
| 5. Network, third-party, and multi-geography exposure  | Remote access, weak traffic filtering, service-provider dependency, and operations across jurisdictions increase network, vendor, contractual, and compliance risk.                         | Risks 1, 3, 5, 10, 14, and 15 |

## Part 4 — Annotated IT Risk Management Plan Table of Contents

The following table of contents structures the proposed IT risk management plan around the five major risk areas identified in Part 3.

1. **Introduction and Scope**
   1. Purpose of the risk management plan
   2. Scope of the ERP platform
   3. Organisational and geographical context
   4. Risk appetite and impact criteria
   5. Roles, risk owners, reporting, and escalation

2. **Risk Management Methodology**
   1. Risk planning
   2. Risk identification
   3. Risk assessment
   4. Risk mitigation
   5. Risk monitoring and review

3. **Identity, Access, and Tenant-Isolation Management**
   1. PostgreSQL tenant-isolation strategy
   2. Row-Level Security and tenant-scoped database access
   3. Role-Based Access Control and least privilege
   4. Authentication and privileged-access management
   5. Tenant-context validation and access logging
   6. Periodic review of roles, policies, and cross-tenant access attempts

   The ERP will use PostgreSQL isolation controls so that one customer cannot access another customer's records. Tenant context will be applied to database operations, supported by Row-Level Security policies, restricted database roles, server-side authorisation, and logged access attempts. Isolation controls will be tested regularly rather than relying only on application-interface restrictions.

4. **Information Protection, Privacy, and Recovery Management**
   1. Information classification and ownership
   2. Applicable privacy and security obligations
   3. Encryption of data at rest and in transit
   4. Key and secret management
   5. Retention and secure deletion
   6. Backup, restoration, and recovery testing
   7. Privacy incidents and breach reporting

   The company will follow applicable privacy, contractual, and cybersecurity requirements. Sensitive ERP information will be protected using modern encryption in transit and at rest, controlled key management, access restrictions, retention rules, and isolated backups. The effectiveness of backups will be confirmed through scheduled restoration tests.

5. **Application, Workflow, and Server-Integrity Management**
   1. Separation of the database, application runtime, and workflow execution
   2. Application and API security
   3. Serverless workflow-function permissions
   4. Input validation and secure workflow execution
   5. Patch and vulnerability management
   6. Workflow idempotency, audit evidence, and authoritative business actions
   7. Runtime, error, and security monitoring

   Jobs will be separated according to responsibility. The database service will store authoritative records, the application runtime will handle user and API requests, and isolated serverless functions will execute workflow jobs. Each component will receive only the network access, credentials, and permissions it requires. This separation reduces the effect of a compromised component and prevents workflow failures from directly corrupting authoritative ERP records.

6. **Infrastructure Availability and Business-Continuity Management**
   1. Critical-service and dependency inventory
   2. Redundant application and storage infrastructure
   3. Isolated backup locations
   4. Recovery Point Objective and Recovery Time Objective
   5. Backup and recovery runbooks
   6. Restoration exercises and evidence
   7. Disaster recovery and continuity testing

   The company will maintain isolated backups because the cost of redundant storage is lower than the potential loss caused by unrecoverable ERP data. Backup copies will not share the same failure boundary or unrestricted credentials as production. Documented recovery runbooks will define the backup schedule, responsible owner, restoration sequence, recovery targets, escalation steps, and evidence required to prove that restoration succeeded.

7. **Network, Third-Party, and Multi-Geography Risk Management**
   1. Regional load balancing and service redundancy
   2. Regional database replication and controlled failover
   3. Data-residency and cross-border processing review
   4. SaaS and service-provider risk assessment
   5. Email, SMS, communications, and module dependencies
   6. Provider Service-Level Agreements and outage procedures
   7. Third-party exit and substitution plans
   8. Regional backup and recovery runbooks

   Regional load balancers and authorised database replicas will support availability across operating geographies. Replication will be designed around applicable data-residency, privacy, encryption, and access requirements. SaaS partners—including email, SMS, communications, and future module providers—will be assessed for security, availability, contractual protection, incident notification, recovery capability, and concentration risk. Continuity plans will record alternative providers or manual procedures for critical outsourced services.

8. **Quantitative Risk Evaluation**
   1. Asset Value and Exposure Factor
   2. Single Loss Expectancy
   3. Annualised Rate of Occurrence
   4. Annualised Loss Expectancy
   5. Control-cost comparison

9. **Risk Monitoring, Reporting, and Review**
   1. Key Risk Indicators
   2. Security and operational logs
   3. Control testing and review frequency
   4. Incident escalation
   5. Management reporting

10. **References and Appendices**
    1. Risk register
    2. Risk assessment matrix
    3. Risk treatment plan
    4. Backup and recovery runbooks
    5. Third-party assessment register

## Part 5 — Quantitative Risk Concepts

### Scenario: Loss or unavailability of ERP invoice records

Sahyadri ERP Technologies stores approximately 50,000 customer invoice records with an average recorded value of ₹20,000. Their combined face value is therefore ₹100 crore. However, the full face value is not treated as the Asset Value because an outage does not automatically destroy every underlying customer transaction. For risk estimation, the company assigns an operational Asset Value of ₹1 crore to the invoice dataset and its supporting service. This represents restoration work, downtime, invoice verification and re-creation, delayed collections, customer support, contractual consequences, and incident handling.

The following planning assumptions are used for this quantitative assessment.

| Concept | Meaning | Planning value |
| --- | --- | ---: |
| Invoice records | Number of invoice records affected | 50,000 |
| Average recorded invoice value | Average face value recorded per invoice | ₹20,000 |
| Total recorded invoice face value | 50,000 × ₹20,000 | ₹100,00,00,000 |
| Asset Value (AV) | Estimated operational value exposed by loss or prolonged unavailability | ₹1,00,00,000 |
| Exposure Factor (EF) | Estimated percentage of the Asset Value lost in one incident | 25% |
| Single Loss Expectancy (SLE) | Expected financial loss from one incident: **SLE = AV × EF** | ₹25,00,000 |
| Annualised Rate of Occurrence (ARO) | Estimated frequency of a major incident: once every five years | 0.20 |
| Annualised Loss Expectancy (ALE) | Expected annual financial loss: **ALE = SLE × ARO** | ₹5,00,000 per year |

### Calculation

> **SLE = AV × EF**  
> SLE = ₹1,00,00,000 × 25% = **₹25,00,000 per incident**

> **ALE = SLE × ARO**  
> ALE = ₹25,00,000 × 0.20 = **₹5,00,000 per year**

### Effect of the proposed controls

Assume that isolated backups, tested recovery runbooks, regional redundancy, access controls, and monitoring reduce the Exposure Factor from 25% to 10% and the ARO from 0.20 to 0.10.

| Residual-risk concept | Calculation | Result |
| --- | --- | ---: |
| Residual SLE | ₹1,00,00,000 × 10% | ₹10,00,000 |
| Residual ALE | ₹10,00,000 × 0.10 | ₹1,00,000 per year |
| Estimated annual risk reduction | ₹5,00,000 − ₹1,00,000 | ₹4,00,000 per year |

If the complete control programme costs less than ₹4,00,000 annually, the quantitative estimate supports its financial justification. The decision must still consider privacy, contractual duties, customer trust, and business continuity because these consequences are not always fully represented by ALE.

## References

1. [[CRM Lab 1]] — earlier infrastructure-domain risk identification exercise.
2. [[CRM Lab 2]] — earlier risk assessment and application of the NIST Cybersecurity Framework.
3. National Institute of Standards and Technology, [The NIST Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20), 2024.
4. International Organization for Standardization, [ISO/IEC 27001:2022 — Information security management systems](https://www.iso.org/standard/27001).
5. International Organization for Standardization, [ISO/IEC 27701:2025 — Privacy information management systems](https://www.iso.org/standard/27701).

## Conclusion

Having a planned approach for risks that may potentially arise creates a strong and proactive security posture. By identifying possible threats in advance, assessing their likelihood and impact, defining suitable mitigation measures, and continuously monitoring the relevant controls, an organisation can respond systematically instead of reacting only after an incident occurs. This preparation also clarifies responsibilities, supports business continuity, protects information and infrastructure, and helps management direct resources towards the most significant risks. Although every risk cannot be completely eliminated, a documented and regularly reviewed risk management plan enables the organisation to reduce uncertainty and maintain risk at an informed and acceptable level.

