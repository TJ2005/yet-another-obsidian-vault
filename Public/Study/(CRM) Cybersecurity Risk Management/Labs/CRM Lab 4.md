---
Title: "CRM Lab 4"
Status: complete
tags: [semester-7, cybersecurity, CRM, lab]
Date: "2026.08.22"
---

# CRM Lab 4 — Business Impact Analysis for a Mock IT Infrastructure

|                         |           |
| ----------------------- | --------- |
| **Academic Year**       | 2026–27   |
| **Programme**           | BTECH CRM |
| **Year / Semester**     | 4th / VII |
| **Name of Student**     | Tejas     |
| **Batch**               | K2        |
| **Roll No**             | K057      |
| **Date of experiment**  | 22-Aug-26 |
| **Faculty**             | Parth Ved |
| **Signature with Date** |           |

## Aim

Perform a Business Impact Analysis (BIA) for a mock IT infrastructure.

## Learning Outcomes

- Define the goal and objective of a Business Impact Analysis (BIA)
- Identify where a Business Impact Analysis (BIA) fits within a Business Continuity Plan (BCP)
- Identify mission-critical applications and access-to-data requirements for a given scenario
- Perform a Business Impact Analysis (BIA) utilising a qualitative assessment approach
- Create a Business Impact Analysis executive summary report for management

## Procedure

1. For an IT service organisation, conduct a BIA assessment by assigning a qualitative business impact value.
2. Identify the various business functions and respective stakeholders, and validate the datasets against CIAP.
3. Identify the IT systems, applications, and resources that are involved as part of those business functions and can be impacted.
4. Assess the recovery time objectives needed for the IT systems, applications, and resources.
5. For each identified dataset, evaluate the risk on the basis of the various objectives of BIA against: Low, Medium, High, Critical, or None.
6. Craft a four-paragraph executive summary according to the following outline:
   - **a.** Goals and purpose of the BIA — unique to your scenario
   - **b.** Summary of Crown Jewels for the identified business functions and assessment
   - **c.** Prioritisations — critical, major, and minor classifications
   - **d.** IT systems and applications impacted — to support the defined recovery time objectives

## Solution

### Part 1 — Scenario and business functions

#### A. Organisation profile

| Field | Answer |
| --- | --- |
| **Organisation name** | Sahyadri ERP Technologies |
| **What it provides** | ERP services — focused on freight-forwarding companies |
| **Headquarters** | Belapur |
| **Geographies served** | India |
| **Key datasets handled** | Customer data, vendor data, process information, sensitive documents (Bill of Lading, LR) |
| **Legal / contractual obligations** | DPDP Act · IT Act 2000 · GST requirements · NDAs from customers |
| **Risk appetite (one line)** | Very low appetite for confidentiality/privacy breaches and tampering of financial records (integrity); low appetite for outages beyond defined RTOs; moderate appetite only for brief, non-critical degradation (e.g., delayed reports) with no data exposure |

#### B. Business function register (validated against CIAP)

| # | Business function | Stakeholders / owners | Key datasets | C | I | A | P | CIAP notes |
| --: | --- | --- | --- | :-: | :-: | :-: | :-: | --- |
| 1 | Workflow Automation | Administrator | Workflow process information | ✔ | ✔ | ✔ | ✘ | Leakage exposes customer workflow strategy; needs access control |
| 2 | Process Maturity Flows | Business Relation Manager | Company strategy | ✔ | ✔ | ✘ | ✘ | Confidential, rarely time-critical |
| 3 | HR Module | HR Manager (customer) | Employee information, KYE | ✔ | ✔ | ✔ | ✔ | Personal data — DPDP sensitive, high C+P |
| 4 | Payroll Management | HR Manager / Account admin | Salary information | ✔ | ✔ | ✔ | ✔ | Highly sensitive + monthly statutory deadlines — needs availability |
| 5 | Truck Fleet Management | Operational Manager (customer) | Truck routes and strategies | ✔ | ✔ | ✔ | ✘ | Live ops data — high A |
| 6 | Shipment Manager | Operational Manager | Shipment information of customer (sensitive) | ✔ | ✔ | ✔ | ✘ | Core logistics data — highest C+A |
| 7 | Documentation Management | Documentation personnel | Documents like BL, LR | ✔ | ✔ | ✔ | ✘ | Official carriers' documents — custody + integrity critical |
| 8 | Shipment API Layer | Internal Administrator | Line API / sensitive keys | ✔ | ✔ | ✔ | ✘ | Hardcoded/rotated keys — extreme C concern |
| 9 | Invoicing Manager | CA / Accountant (customer) | Key payment information | ✔ | ✔ | ✔ | ✘ | Revenue + financial integrity |
| 10 | Marketing Report Management | Marketing Lead (customer) | Customer data | ✔ | ✘ | ✘ | ✔ | Marketing copy — lower criticality |
| 11 | Customer Resource Management | Marketing Lead (customer) | Customer data | ✔ | ✔ | ✔ | ✔ | CRM master data — P per DPDP |
| 12 | Customer Support | Customer Support Lead | Internal customer data | ✔ | ✔ | ✔ | ✘ | Support tickets — needs availability |

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
| 1 | Workflow Automation | Administrator | Workflow process info | ERP web app · workflow engine · job queue · PostgreSQL DB | High | 2 h |
| 2 | Process Maturity Flows | Business Relation Manager | Company strategy | Reporting/BI module · document store | Medium | 24 h |
| 3 | HR Module | HR Manager | Employee info, KYE | ERP HR module · identity & access (RBAC) · DB | High | 12 h |
| 4 | Payroll Management | HR Manager / Account admin | Salary info | ERP payroll module · auth service · DB · backups | Critical | 4 h |
| 5 | Truck Fleet Management | Operational Manager | Routes & strategies | Fleet tracking module · realtime feeds · API gateway | Critical | 1 h |
| 6 | Shipment Manager | Operational Manager | Shipment info | Shipment module · PostgreSQL · notification service | Critical | 1 h |
| 7 | Documentation Management | Documentation personnel | BL, LR docs | Document/edocument store · scan & e-sign tools | Critical | 2 h |
| 8 | Shipment API Layer | Internal Administrator | Line API / keys | API gateway · key vault · integration adapters | Critical | 1 h |
| 9 | Invoicing Manager | CA / Accountant | Payment info | Invoicing module · finance DB · tax (GST) integration | Critical | 4 h |
| 10 | Marketing Report Management | Marketing Lead | Customer data | Reporting/BI module · customer DB (marketing copy) | Low | 48 h |
| 11 | Customer Resource Management | Marketing Lead | Customer data | CRM module · customer DB · support tools | Medium | 12 h |
| 12 | Customer Support | Customer Support Lead | Internal customer data | Support portal · ticketing · knowledge base | Medium | 4 h |

> [!TIP] Priorities derived
> **Critical (impact):** Payroll, Fleet, Shipment, Documentation, API Layer, Invoicing — keep RTOs ≤ 4 h (most ≤ 1–2 h).
> **Major:** Workflow Automation, HR Module, CRM, Customer Support — RTO 4–12 h.
> **Minor:** Process Maturity Flows, Marketing Reports — RTO 24–48 h, disruption tolerable.

### Part 3 — Executive summary

**1. Goals and purpose of the BIA.** Sahyadri ERP Technologies conducted this Business Impact Analysis to determine how a disruption to its freight-forwarding ERP platform affects each customer business function, and to define the recovery priorities that will underpin its Business Continuity and Disaster Recovery planning. The exercise identifies mission-critical functions, their data dependencies and the maximum tolerable downtime, so that recovery investment is directed at the functions whose loss damages revenue, customers or regulatory standing. The BIA validates every dataset against the CIA + Privacy (CIAP) objectives before any recovery target is set.

**2. Crown Jewels summary and assessment.** The organisation's crown jewels concentrate in transactional and financial data: shipment and fleet information, carrier documents (Bill of Lading, LR), payment and salary records, and the API keys that tie the platform to carrier line integrations. Exposure of these assets is assessed as **Critical** — their confidentiality, integrity and availability requirements are all confirmed under CIAP. Employee KYE and salary data additionally carry high privacy weight under the DPDP Act. Together these assets attract the highest confidentiality and integrity ratings in the register, and their loss would be both financially and legally material.

**3. Prioritisations — critical, major and minor.** Three classifications emerge from the qualitative impact values. **Critical** functions — Payroll, Fleet, Shipment, Documentation, Shipment API Layer and Invoicing — cannot sustain more than 1–4 hours of downtime and are protected first. **Major** functions — Workflow Automation, HR Module, CRM and Customer Support — tolerate 4–12 hours and form the second recovery wave. **Minor** functions — Process Maturity Flows and Marketing Reporting — tolerate up to 48 hours and are recovered last. This ordering ensures constrained recovery resources target the highest-impact, shortest-RTO functions first.

**4. Impacted IT systems and applications vs recovery time objectives.** Every critical and major function depends on the same shared core — the ERP web application, authentication/RBAC service, PostgreSQL database, workflow engine and background job queue, the API gateway and key vault, document store and backup/recovery infrastructure. Because the core serves multiple functions, its recovery defines the floor for every RTO: the platform core and PostgreSQL database are required within **1 hour** (enabling Fleet, Shipment and API Layer RTOs), the document store and invoicing/finance datasets within **2–4 hours**, and subsidiary modules (HR, CRM, support) within **4–12 hours**. Meeting these RTOs requires a tiered recovery runbook and isolated, tested backups aligned with the stated risk appetite.

## Questions

### Q1. How do risk management and risk assessment connect to a business impact analysis for an IT infrastructure?

- **BIA is the foundation** of risk-driven continuity — it identifies the functions, assets and recovery targets that risk assessment then works with
- **Risk assessment** evaluates threats and vulnerabilities against those assets (likelihood × impact) — it needs **what is valuable** from the BIA
- **Risk management** then decides how to treat the exposure (mitigate/transfer/accept) — using BIA outputs such as RTO/RPO and asset criticality to justify **control spend and priorities**
- BIA contributes the **impact half** of risk; likelihood comes from threat/vulnerability analysis
- Together they close the cycle — see [[CRM Lab 2]] (NIST CSF assessment) and [[CRM Lab 3]] (risk management plan): BIA sets target recovery, risk assessment finds what could break it, risk management funds the fixes

### Q2. What are the organisation's critical crown jewels, and how will it mitigate those?

- **Crown jewels:** shipment & fleet data, carrier documents (BL/LR), payment records, salary data, API/line keys, employee privacy data (KYE)
- **Mitigations:**
	- **Encryption at rest and in transit** for sensitive datasets
	- **RBAC + least privilege** — only owners/stewards reach financial and document data
	- **MFA + privileged-access controls** for administrators and API key holders
	- **API key vaulting and rotation** — remove hardcoded/standing keys (Shipment API Layer)
	- **Data minimisation & segregation** — marketing/CRM copies kept separate from transactional master data
	- **Isolated, tested backups** and tiered recovery runbooks matching the RTOs
	- **DPDP/IT Act/GST compliance controls** — retention, consent, breach notification
	- **Monitoring & alerting** on financial and documentation modules to catch tampering early

### Q3. Detailed analysis of the BIA sheet with CIAP, considering all areas and objectives

**Dataset risk ratings (BIA objectives: Low / Medium / High / Critical / None):**

| Dataset | CIAP highlights | Overall risk |
| --- | --- | --- |
| Shipment information | Confidentiality + availability critical (customer trust) | **Critical** |
| Truck routes & strategies | Confidential, live availability | **Critical** |
| BL / LR documents | Integrity + custody (official documents) | **Critical** |
| Line API / sensitive keys | Compromise = platform-wide exposure | **Critical** |
| Payment information | Integrity (revenue) + privacy | **Critical** |
| Salary information | Privacy (DPDP) + monthly availability | **Critical** |
| Employee info / KYE | Privacy-weighted | **High** |
| Workflow process information | Competitive sensitivity | **High** |
| Company strategy | Confidential, low availability need | **High** |
| Customer data (CRM) | Privacy under DPDP | **High** |
| Internal customer data (support) | Availability for SLA | **Medium** |
| Customer data (marketing copy) | Privacy but non-transactional | **Medium** |

**Horizontal read (objective-wise):**

- **Confidentiality:** strongest for API keys, shipments, salary, strategy — enforced via RBAC, encryption, NDAs
- **Integrity:** highest for BL/LR documents, payments and invoice records — enforced via access controls, audit trails, validation in invoicing
- **Availability:** binding constraint — the shared core (app + DB + gateway) must recover within 1 hour to satisfy Fleet/Shipment/API RTOs
- **Privacy:** salary, KYE and customer data carry DPDP obligations — require consent, minimisation, retention controls
- **RTO clustering:** three recovery tiers (≤2 h critical, 4–12 h major, ≥24 h minor) let the organisation sequence restoration and size DR infrastructure

## Conclusion

The BIA shows that Sahyadri ERP Technologies' freight platform is disproportionately dependent on a shared transaction core serving six critical functions with RTOs of 1–4 hours. Confidentiality and integrity risks concentrate in documentation, financial and integration assets, while availability risk is driven by the core platform floor. Because recovery resources are limited and the risk appetite for privacy or integrity losses is very low, the organisation must implement tiered, tested recovery runbooks, isolated backups, and strict access controls around its crown jewels before a disruption materialises. Documented and routinely exercised, this BIA enables management to invest where impact is greatest and to keep business functions within their defined recovery objectives.

## References

- [[CRM Lab 1]] — infrastructure-domain risk identification
- [[CRM Lab 2]] — risk assessment with the NIST Cybersecurity Framework
- [[CRM Lab 3]] — IT risk management plan and quantitative risk evaluation