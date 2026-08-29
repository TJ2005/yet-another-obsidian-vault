---
Title: "CRM Lab 5 — OOCL India BIA"
Status: complete
tags: [semester-7, cybersecurity, CRM, lab]
Date: "2026.08.29"
---

# OOCL India — Business Impact Analysis (BIA)

|                         |           |
| ----------------------- | --------- |
| **Academic Year**       | 2026–27   |
| **Programme**           | BTECH-CRM |
| **Year / Semester**     | 4th / VII |
| **Name of Student**     | Tejas     |
| **Batch**               | K2        |
| **Roll No**             | K057      |
| **Date of experiment**  | 29-Aug-26 |
| **Faculty**             | Parth Ved |
| **Signature with Date** |           |

## Aim

Perform a Business Impact Analysis (BIA) for OOCL India's container shipping and logistics IT infrastructure.

## Learning Outcomes

- Define the goal and objective of a Business Impact Analysis (BIA)
- Identify where a BIA fits within a Business Continuity Plan (BCP)
- Identify mission-critical applications and access-to-data requirements for a shipping-line scenario
- Perform a BIA utilising a qualitative assessment approach
- Create a BIA executive summary report for management

## Solution

### Part 1 — Scenario and business functions

#### A. Organisation profile

| Field | Answer |
| --- | --- |
| **Organisation name** | OOCL India (Orient Overseas Container Line) |
| **What it provides** | Global container shipping / ocean freight & logistics (Indian arm of COSCO group) |
| **Headquarters** | Mumbai (India head office) |
| **Geographies served** | India-wide port terminals: Mumbai, Chennai, Delhi NCR, Kolkata, Mundra, plus global network via COSCO group |
| **Key datasets handled** | Container tracking data, Bill of Lading (BL), customs declarations (ICEGATE), vessel schedules, stowage plans, customer booking & payment data, reefer telemetry, terminal/yard move records |
| **Legal / contractual obligations** | DPDP Act / IT Act 2000 / Indian Customs Act / GST / SOLAS / IMO regulations / customer NDAs / carrier SLAs |
| **Risk appetite (one line)** | Zero tolerance for BL/customs data loss or integrity breach; very low appetite for booking/tracking outage beyond 2 h; low appetite for vessel/terminal disruption beyond 4 h; moderate appetite for internal reporting delays |

#### B. Business function register (validated against CIAP)

| # | Business function | Stakeholders / owners | Key datasets | C | I | A | P | CIAP notes |
| --: | --- | --- | --- | :-: | :-: | :-: | :-: | --- |
| 1 | Container booking & e-commerce (MyOOCL) | Commercial / Digital team | Booking requests, container allocations, pricing, customer PII | ✔ | ✔ | ✔ | ✔ | Revenue-critical; customer PII under DPDP |
| 2 | Container tracking & visibility API | Operations / Digital team | Container location, ETA, events, milestones | ✔ | ✔ | ✔ | ✘ | Real-time ops; high A; no direct PII |
| 3 | Customs clearance / ICEGATE gateway | Customs compliance team | Shipping bills, BE, BL, duty payments, cargo manifests | ✔ | ✔ | ✔ | ✘ | Legal mandate; zero data loss (RPO 0) |
| 4 | Vessel & fleet management | Vessel operations | Schedules, stowage plans, ballast, bunker, port rotations | ✔ | ✔ | ✔ | ✘ | Safety-of-navigation; SOLAS |
| 5 | Terminal / yard operations (CFS) | Terminal ops / Stevedores | Gate moves, yard slots, reefer monitoring, equipment status | ✔ | ✔ | ✔ | ✘ | Throughput-critical; port congestion risk |
| 6 | Finance & invoicing | Finance / Accounts | Invoices, payments, collections, GST returns, revenue recognition | ✔ | ✔ | ✔ | ✘ | Revenue integrity; statutory GST |
| 7 | Customer support & kiosk services | Customer service | Tickets, queries, documents, SLA tracking | ✔ | ✔ | ✔ | ✔ | Customer PII; SLA-bound |
| 8 | HR & payroll | HR | Employee records, payroll, attendance, KYC | ✔ | ✔ | ✔ | ✔ | DPDP sensitive; statutory deadlines |
| 9 | Marketing & reporting | Marketing / BI | Campaign data, analytics, market intelligence | ✔ | ✘ | ✘ | ✔ | Non-transactional; PII in leads |

### Part 2 — BIA worksheet

> [!NOTE] Qualitative impact scale
> - **Critical** = function cannot operate (or statutory/legal breach)
> - **High** = major disruption, quickly material loss
> - **Medium** = degraded but tolerable short-term
> - **Low** = minor inconvenience
> - **None** = no impact
> - **RTO** = maximum acceptable downtime

| # | Business function | Stakeholders | Datasets | Supporting IT systems / applications / resources | Impact | RTO |
| --: | --- | --- | --- | --- | --- | --- |
| 1 | Container booking & e-commerce (MyOOCL) | Commercial / Digital | Booking, pricing, customer PII | MyOOCL web portal, OOCL Lite mobile app, API gateway, PostgreSQL, Redis cache, payment gateway | Critical | 1 h |
| 2 | Container tracking & visibility API | Operations / Digital | Container location, ETA, events | Tracking microservice, Kafka event stream, Elasticsearch, PostgreSQL, CDN | Critical | 1 h |
| 3 | Customs clearance / ICEGATE gateway | Customs compliance | Shipping bills, BE, BL, duty payments | EDI/ICEGATE adapter, message queue, WORM storage, digital signature service | Critical | 2 h |
| 4 | Vessel & fleet management | Vessel operations | Schedules, stowage, ballast, rotations | Fleet management system, AIS feed, weather API, PostgreSQL, GIS | Critical | 1 h |
| 5 | Terminal / yard operations (CFS) | Terminal ops | Gate moves, yard slots, reefer data | TOS (Terminal Operating System), IoT gate readers, reefer controllers, PLC/SCADA | Critical | 2 h |
| 6 | Finance & invoicing | Finance | Invoices, payments, GST | ERP (SAP/Oracle), invoice generator, bank gateway, GSTN portal | Critical | 4 h |
| 7 | Customer support & kiosk services | Customer service | Tickets, documents, SLA data | ServiceNow/Zendesk, kiosk thin clients, document store, telephony | Major | 4 h |
| 8 | HR & payroll | HR | Employee, payroll, KYC | HRMS, payroll engine, bank portal, document vault | Major | 12 h |
| 9 | Marketing & reporting | Marketing / BI | Campaigns, leads, analytics | BI platform (Tableau/PowerBI), data warehouse, CRM (Salesforce) | Minor | 24 h |

### Part 3 — Executive summary (four paragraphs)

**1. Goals and purpose of the BIA.** OOCL India conducted this Business Impact Analysis to quantify the impact of IT disruptions on its container shipping and logistics operations across Indian port terminals. The exercise identifies mission-critical functions — booking (MyOOCL), tracking, customs/ICEGATE, vessel management, terminal operations, and finance — their data dependencies, and the maximum tolerable downtime (MAO) so that recovery investment targets the services whose loss directly threatens revenue, regulatory compliance, and shipper trust. Every dataset is validated against CIA + Privacy (CIAP) objectives before any recovery target is set.

**2. Crown Jewels summary and assessment.** The organisation's crown jewels concentrate in transactional, legal and safety-critical data: Bill of Lading and customs declarations (zero data-loss mandate), container booking and payment records (revenue + DPDP), vessel stowage and navigation data (SOLAS safety), and terminal gate/yard move records (port throughput). Exposure of these assets is assessed as **Critical** — their confidentiality, integrity and availability requirements are all confirmed under CIAP. Customer PII in booking and support channels adds high privacy weight under the DPDP Act. Together these assets attract the highest confidentiality and integrity ratings in the register, and their loss would be financially, legally and reputationally material.

**3. Prioritisation — critical, major and minor.** Three classifications emerge from the qualitative impact values. **Critical** functions — Booking, Tracking, Customs/ICEGATE, Vessel/Fleet, Terminal/Yard, Finance — cannot sustain more than 1–4 hours of downtime and are protected first. **Major** functions — Customer Support/Kiosk, HR/Payroll — tolerate 4–12 hours and form the second recovery wave. **Minor** functions — Marketing/Reporting — tolerate up to 24–48 hours and are recovered last. This ordering ensures constrained recovery resources target the highest-impact, shortest-RTO functions first.

**4. Impacted IT systems and applications vs recovery time objectives.** Every critical function depends on a shared cloud-native core — the MyOOCL booking stack, tracking event pipeline, EDI/ICEGATE adapter, fleet management system, terminal operating system (TOS), and the ERP/finance backbone — hosted in a multi-region cloud (primary Mumbai, DR Chennai) with immutable cross-region backups. Because the core serves multiple critical functions, its recovery defines the floor for every RTO: the booking/tracking/API layer and ICEGATE gateway must failover within **1–2 hours** (active-active), the TOS and fleet systems within **2 hours** (warm standby + IaC rebuild), and the ERP/finance within **4 hours** (backup restore). Meeting these RTOs requires a tiered recovery runbook, automated health-check failover, and isolated, tested backups aligned with the stated risk appetite.

## Questions

### Q1. How do risk management and risk assessment connect to a business impact analysis for an IT infrastructure?

- BIA is the foundation of risk-driven continuity — it identifies the functions, assets and recovery targets that risk assessment then works with
- Risk assessment evaluates threats and vulnerabilities against those assets (likelihood × impact) — it needs **what is valuable** from the BIA
- Risk management then decides how to treat the exposure (mitigate/transfer/accept) — using BIA outputs such as RTO/RPO and asset criticality to justify control spend and priorities
- BIA contributes the **impact half** of risk; likelihood comes from threat/vulnerability analysis
- Together they close the cycle — see [[CRM Lab 2]] (NIST CSF assessment) and [[CRM Lab 3]] (risk management plan): BIA sets target recovery, risk assessment finds what could break it, risk management funds the fixes

### Q2. What are the organisation's critical crown jewels, and how will it mitigate those?

- **Crown jewels:** Bill of Lading & customs declarations, container booking & payment data, vessel stowage & navigation data, terminal gate/yard move records, customer PII
- **Mitigations:**
  - Encryption at rest and in transit for all crown-jewel datasets
  - WORM storage + cryptographic signing for BL/customs records (RPO 0)
  - RBAC + least privilege — only data owners/stewards reach financial, BL and navigation data
  - MFA + privileged-access controls (PAM) for administrators and API key holders
  - API key vaulting with rotation — eliminate standing keys for ICEGATE, MyOOCL, partner EDI
  - Data minimisation & segregation — marketing/analytics copies kept separate from transactional master data
  - Isolated, tested backups and tiered recovery runbooks matching the RTOs
  - DPDP/Customs/GST/SOLAS compliance controls — retention, consent, breach notification, safety reporting
  - Monitoring & alerting on financial, customs and navigation modules to catch tampering early

### Q3. Detailed analysis of the BIA sheet with CIAP, considering all areas and objectives

**Dataset risk ratings (BIA objectives: Low / Medium / High / Critical / None):**

| Dataset | CIAP highlights | Overall risk |
| --- | --- | --- |
| Bill of Lading / customs declarations | Confidentiality + Integrity + Availability + Privacy (legal mandate) | **Critical** |
| Container booking & payment data | Confidentiality + Integrity + Availability + Privacy (DPDP) | **Critical** |
| Vessel stowage / navigation / schedules | Integrity + Availability (SOLAS safety) | **Critical** |
| Container tracking events / location | Integrity + Availability (real-time ops) | **Critical** |
| Terminal gate / yard moves / reefer | Integrity + Availability (port throughput) | **Critical** |
| Finance / invoicing / GST records | Integrity + Availability (statutory) | **Critical** |
| Customer PII (booking, support) | Confidentiality + Privacy (DPDP) | **Critical** |
| HR / payroll / KYE | Confidentiality + Privacy + Availability (monthly) | **High** |
| Marketing leads / analytics | Confidentiality + Privacy (DPDP) | **Medium** |

**Horizontal read (objective-wise):**

- **Confidentiality:** strongest for BL/customs, booking payments, customer PII, HR — enforced via RBAC, encryption, NDAs, DPDP consent
- **Integrity:** highest for BL/customs (cryptographic signing), vessel stowage (safety), finance (audit trail), terminal moves — enforced via access controls, WORM, hash verification, validation rules
- **Availability:** binding constraint — the shared cloud core (booking, tracking, ICEGATE, fleet, TOS) must failover within 1–2 h to satisfy Critical RTOs
- **Privacy:** booking, support, HR, marketing carry DPDP obligations — require consent, minimisation, retention controls, breach notification
- **RTO clustering:** three recovery tiers (≤2 h critical, 4–12 h major, ≥24 h minor) let the organisation sequence restoration and size DR infrastructure

## Conclusion

The BIA shows that OOCL India's container shipping platform is disproportionately dependent on a shared cloud-native core serving six Critical functions with RTOs of 1–4 hours. Confidentiality and integrity risks concentrate in legal (BL/customs), financial (booking/payments), safety (vessel stowage) and operational (tracking/terminal) data, while availability risk is driven by the multi-function cloud core. Because recovery resources are limited and the risk appetite for data-loss or safety incidents is zero, the organisation must implement active-active multi-region failover for Critical APIs, immutable WORM backups for zero-RPO datasets, strict Zero-Trust access controls, and supply-chain risk tiering under ISO 27017. Documented and routinely exercised through quarterly tabletops, monthly automated failover tests, and annual ISO 22301 audits, this BIA enables management to invest where impact is greatest and to keep shipping operations within their defined recovery objectives — protecting shipper trust, regulatory standing, and crew safety.

## References

- [[CRM Lab 4]] — ERP Studios BIA (comparison baseline)
- [[CRM Lab 3]] — risk management plan and quantitative risk evaluation
- [[CRM Lab 2]] — risk assessment with the NIST Cybersecurity Framework
- [[CRM Lab 5]] — OOCL India BCP & DRP Plan (uses this BIA)