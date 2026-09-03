---
Title: "(HLACS) Lab 6"
Status: complete
tags: [semester-7, cybersecurity, HLACS, lab]
Date: "2026.09.03"
---

# (HLACS) Lab 6 — PCI DSS Standard

| | |
| --- | --- |
| **Academic Year** | 2026–27 |
| **Programme** | BTECH HLACS |
| **Year / Semester** | 4th / VII |
| **Name of Student** | Tejas |
| **Batch** | K2 |
| **Roll No** | K057 |
| **Date of experiment** | 03-Sep-26 |
| **Faculty** | |
| **Signature with Date** | |

## Aim

To study PCI DSS standard and apply it for given scenario.

## Learning Outcomes

- Describe PCI DSS standard requirements
- Apply the PCI DSS standard for the given scenario

## Theory

The Payment Card Industry Data Security Standard (PCI DSS) was developed to encourage and enhance cardholder data security and facilitate the broad adoption of consistent data security measures globally. PCI DSS provides a baseline of technical and operational requirements designed to protect account data. PCI DSS applies to all entities involved in payment card processing—including merchants, processors, acquirers, issuers, and service providers. PCI DSS also applies to all other entities that store, process or transmit cardholder data (CHD) and/or sensitive authentication data (SAD). The PCI Data Security Standard specifies twelve requirements for compliance, organized into six logically related groups called "control objectives":

| Control Objective | PCI DSS Requirements |
| --- | --- |
| **1. Build and Maintain a Secure Network and Systems** | 1. Install and maintain network security controls<br>2. Apply secure configurations to all system components |
| **2. Protect Cardholder Data** | 3. Protect stored cardholder data<br>4. Protect cardholder data with strong cryptography during transmission over open, public networks |
| **3. Maintain a Vulnerability Management Program** | 5. Protect all systems and networks from malicious software<br>6. Develop and maintain secure systems and software |
| **4. Implement Strong Access Control Measures** | 7. Restrict access to system components and cardholder data by business need-to-know<br>8. Identify users and authenticate access to system components<br>9. Restrict physical access to cardholder data |
| **5. Regularly Monitor and Test Networks** | 10. Log and monitor all access to system components and cardholder data<br>11. Test security of systems and networks regularly |
| **6. Maintain an Information Security Policy** | 12. Support information security with organizational policies and programs |

### Key Definitions

| Term | Definition |
| --- | --- |
| **CHD (Cardholder Data)** | Primary Account Number (PAN) + any of: cardholder name, expiration date, service code |
| **SAD (Sensitive Authentication Data)** | Full track data (magnetic stripe/EMV chip), CAV2/CVC2/CVV2/CID, PINs/PIN blocks |
| **CDE (Cardholder Data Environment)** | All systems, networks, and processes that store, process, or transmit CHD/SAD, plus any connected systems |
| **PAN** | 15–19 digit Primary Account Number — the card number |
| **Service Provider** | Entity that processes, transmits, or stores CHD on behalf of another entity |
| **P2PE** | Point-to-Point Encryption — validated solution encrypting CHD at point of interaction |
| **Compensating Control** | Alternative control meeting requirement intent when primary control cannot be implemented |

## Procedure

1. Visit <https://www.pcisecuritystandards.org/document_library> and download the PCI DSS standard
2. Form a group of 3–4 students
3. Read the standard and prepare a summary document
4. Solve the scenario below and create an action plan + filled SAQ
5. Upload summary document and scenario solution

## Scenario: Poshak Store — PCI DSS Compliance

**Background:** Jeet Shah owns 'Poshak', a readymade garment store in Borivali, Mumbai. The store has 10 employees. Jeet is tech-savvy and has adopted multiple technology solutions for better customer experience. One initiative: accepting credit/debit card and UPI payments. Annual card transactions: ~10,000. He wants to become PCI DSS compliant and has approached you (PCI DSS compliance expert).

### Your Task

As a PCI DSS compliance expert, help Jeet Shah achieve compliance. Provide:

#### A. Action Plan for Jeet Shah

| Phase | Activity | Description | Timeline | Resources Needed |
| --- | --- | --- | --- | --- |
| **1. Scoping** | Define CHD/SAD scope | Identify all CHD (PAN, expiry, name) and SAD (none stored) in Poshak's environment. Document CDE boundaries. | Week 1 | Merchant interview, network diagram, terminal inventory |
| | Map transaction flow | Trace card data from POS terminal → acquirer → payment gateway. Identify all touchpoints. | Week 1 | Terminal config, gateway docs, network capture |
| | Inventory assets | List all systems in CDE: POS terminals (2), POS server, router/firewall, Wi-Fi AP, backup PC. | Week 1 | Asset management tool, physical walkthrough |
| | Classify merchant level | 10,000 transactions/year → **Level 4 merchant** (SAQ eligible, no ROC required). | Week 1 | Transaction volume report from acquirer |
| **2. Gap Analysis** | SAQ C requirements review | Compare current state against each SAQ C requirement (20 questions across 12 reqs). | Week 2 | SAQ C v4.0.1, evidence collection |
| | Technical vulnerability scan | Run internal/external ASV scan on CDE segment. Identify open ports, weak configs, missing patches. | Week 2 | ASV scanner (Qualys/Tenable), network access |
| | Policy & procedure gap | Review existing docs: no security policy, no incident response, no risk assessment, no vendor management. | Week 2 | Document review, staff interviews |
| | Physical security assessment | Check terminal physical security, server room access, media disposal, visitor logs. | Week 2 | Site walkthrough, photo evidence |
| | Staff awareness check | Interview 10 employees on security practices, phishing, password handling, incident reporting. | Week 2 | Questionnaire, 15-min interviews |
| **3. Remediation** | Network segmentation | Configure firewall: isolate CDE (POS terminals, server) from guest Wi-Fi, admin PC, CCTV. Block internet from CDE except acquirer/gateway IPs. | Week 3–4 | Firewall (FortiGate/Ubiquiti), VLAN-capable switch |
| | Secure configurations | Harden POS server (disable unused services, change defaults, patch OS), terminal config (disable USB, restrict admin). | Week 3 | CIS benchmarks, vendor hardening guides |
| | Encryption & key management | Ensure TLS 1.2+ for terminal→gateway; implement key rotation policy; no CHD stored on POS server. | Week 3 | Gateway TLS cert, key management SOP |
| | Access control & MFA | Unique IDs for 10 staff; MFA for POS server admin (Duo/Google Authenticator); role-based access (cashier vs manager). | Week 3–4 | MFA solution, AD/local accounts |
| | Anti-malware & patching | Deploy endpoint protection (Defender/EDR) on POS server; auto-patch schedule; USB blocking. | Week 3 | EDR license, WSUS/intune |
| | Logging & monitoring | Enable audit logs on POS server, firewall, terminal OS; forward to SIEM/log aggregator; 1-year retention. | Week 4 | Syslog forwarder, log storage (100 GB) |
| | Physical security | Lock POS server in cabinet; terminal cable locks; visitor log; media shredder for receipts. | Week 3 | Cabinet, locks, shredder, visitor book |
| | Policy development | Write: Information Security Policy, Incident Response Plan, Risk Assessment Procedure, Vendor Management, Acceptable Use, Password Policy. | Week 4 | Policy templates, legal review |
| | Staff training | 1-hour session: phishing, password hygiene, incident reporting, clean desk, terminal tamper checks. | Week 4 | Training slides, attendance register |
| **4. Validation** | Internal validation | Complete SAQ C honestly; document evidence for each "Yes"; remediate any "No/Partial" before submission. | Week 5 | SAQ C v4.0.1, evidence folder |
| | ASV scan (external) | Quarterly external vulnerability scan by PCI-approved ASV; resolve Critical/High findings. | Week 5 | ASV vendor (Qualys/Trustwave) |
| | Attestation of Compliance (AOC) | Sign AOC for SAQ C; submit to acquirer/bank along with SAQ. | Week 5 | AOC template from acquirer |
| **5. Ongoing Compliance** | Quarterly ASV scans | External scan every 90 days; after any significant change (new terminal, firewall rule, OS upgrade). | Quarterly | ASV contract |
| | Annual SAQ renewal | Re-assess, update SAQ, re-submit AOC annually before expiry. | Annually | Updated evidence |
| | Semi-annual risk assessment | Update risk register; review threat landscape; validate controls. | Semi-annually | Risk register template |
| | Annual penetration test | Internal pen test (or after major change); fix findings within 30 days. | Annually | Internal tester / 3rd party |
| | Log review (daily/weekly) | Automated alerts for failed logins, config changes, AV hits; weekly manual review summary. | Daily/Weekly | SIEM/log alerts |
| | Staff refresher training | 30-min refresher every 6 months; phishing simulation quarterly. | Semi-annually | Training material |
| | Vendor monitoring | Annual review of gateway/acquirer PCI compliance; maintain vendor risk register. | Annually | Vendor attestations |

---

#### B. Self-Assessment Questionnaire (SAQ) Selection

**Selected SAQ: SAQ C**

**Justification:**

| Factor | Poshak Reality | SAQ C Fit |
| --- | --- | --- |
| **Transaction channel** | Card-present (POS terminal in-store) | ✅ SAQ C = card-present, IP-connected payment application |
| **Annual transactions** | ~10,000 | ✅ Level 4 merchant (<20k Visa/MC, <1M total) |
| **CHD storage** | **None** — Jeet does not store PAN, expiry, or SAD post-authorization | ✅ SAQ C requires no electronic CHD storage |
| **SAD storage** | **Never** — Terminal does not retain track data, CVV, PIN | ✅ Mandatory for all SAQs |
| **Payment terminal** | IP-connected POS (Ethernet/Wi-Fi) to payment gateway/acquirer | ✅ SAQ C = IP-connected payment application |
| **P2PE** | Not confirmed — assume standard IP terminal (non-P2PE) | ❌ If P2PE validated → SAQ B-IP; otherwise SAQ C |
| **E-commerce** | No — UPI only, no card-not-present | ✅ SAQ C excludes e-comm |
| **Network segmentation** | Single store, can isolate POS segment | ✅ SAQ C requires isolated payment network |

> **Note:** If Jeet confirms the POS terminal uses a **PCI-listed P2PE solution**, downgrade to **SAQ B-IP** (simpler, fewer requirements). If CHD is stored electronically (e.g., POS server logs PAN), must use **SAQ D** (full 12 requirements).

---

#### C. Filled Self-Assessment Questionnaire (SAQ C v4.0.1)

> **Instructions:** For each requirement, mark **Yes** (fully implemented with evidence), **No** (not implemented), **Partial** (partially implemented), or **N/A** (not applicable per SAQ C scope). SAQ C includes 20 questions across Requirements 1, 2, 3, 4, 6, 8, 9, 10, 11, 12.

| Req | SAQ C Question (Abbreviated) | In Place? | Evidence / Notes | Remediation Needed |
| --- | --- | --- | --- | --- |
| **1.1** | Are network security controls (firewalls) installed between CDE and untrusted networks? | Partial | Basic router firewall; no segmentation VLAN | Configure VLANs, deny CDE→internet except acquirer IPs |
| **1.2** | Are secure configurations applied to all system components (POS server, terminals, firewall)? | No | Default configs on POS server, terminal USB enabled | Apply CIS benchmarks; disable unused services/ports |
| **2.1** | Is stored CHD protected (rendered unreadable)? | **Yes (N/A)** | No CHD stored electronically; receipts truncated | Maintain — verify no PAN in logs/DB |
| **2.2** | Is SAD never stored after authorization? | **Yes** | Terminal does not retain track/CVV/PIN | Confirm via terminal vendor letter |
| **3.1** | Is CHD transmitted over open networks encrypted with strong cryptography (TLS 1.2+)? | Partial | Gateway uses TLS; verify terminal→gateway encryption | Validate TLS 1.2+; disable SSL/early TLS |
| **3.2** | Is PAN masked on displays/receipts (max first 6/last 4)? | Yes | Receipts show only last 4 digits | Verify terminal config |
| **4.1** | Is anti-malware deployed on all CDE systems, updated, and scanned? | No | POS server has no AV; terminals unmanaged | Deploy EDR on server; vendor AV on terminals |
| **4.2** | Are systems/software developed securely (patches, change control)? | Partial | Ad-hoc patching; no change control | Monthly patch schedule; change approval log |
| **5.1** | Are unique IDs assigned to all users with CDE access? | Partial | Shared "cashier" login on POS; manager has own | Create 10 individual accounts; disable shared |
| **5.2** | Is MFA implemented for all non-console admin access to CDE? | No | POS server admin via RDP with password only | Enable MFA (Duo/TOTP) for admin accounts |
| **5.3** | Is physical access to CDE systems restricted and monitored? | Partial | Server in back office (unlocked); terminals on counter | Lock server cabinet; terminal cable locks; visitor log |
| **6.1** | Are audit logs enabled for all CDE access and retained 1 year? | No | POS server logging minimal; firewall logs 7 days | Enable Windows/terminal audit; syslog to 1-year retention |
| **6.2** | Are logs reviewed daily (automated) and anomalies investigated? | No | No log review process | Deploy log alerts; weekly manual review |
| **7.1** | Are quarterly internal/external vulnerability scans performed? | No | Never scanned | Contract ASV; schedule quarterly |
| **7.2** | Is penetration testing performed annually and after changes? | No | Never tested | Annual internal pen test; after firewall/OS changes |
| **8.1** | Is there a formal information security policy covering all 12 requirements? | No | No policy documents exist | Write policy (12 reqs); annual review; communicate |
| **8.2** | Is risk assessment performed annually and after changes? | No | Never done | Conduct initial risk assessment; semi-annual updates |
| **8.3** | Is incident response plan documented, tested, and includes card-brand notification? | No | No IR plan | Write IR plan; tabletop test; 24-hr card-brand notify |

> **SAQ C Completion Status:** 3/20 **Yes**, 2 **N/A**, 5 **Partial**, 10 **No** → Significant remediation required before submission.

---

#### D. Key Compliance Deliverables for Poshak

| Deliverable | Description | Status |
| --- | --- | --- |
| **Network diagram (CHD flow)** | VLAN diagram: POS terminals → isolated CDE VLAN → firewall → gateway/acquirer. No direct internet from CDE. | Pending (Week 3) |
| **Data flow diagram** | Card dip → terminal encrypts → TLS to gateway → acquirer. No CHD stored. SAD never retained. | Pending (Week 1) |
| **Asset inventory (CHD systems)** | 2× POS terminals (IP), 1× POS server (Windows), 1× firewall, 1× switch, 1× Wi-Fi AP (guest only). | Done (Week 1) |
| **Risk assessment report** | Identified: malware on POS, credential theft, network sniffing, physical tampering, vendor risk. Risk ratings + treatment. | Pending (Week 4) |
| **Policies & procedures document** | InfoSec Policy, IR Plan, Risk Assessment Proc, Vendor Mgmt, Acceptable Use, Password Policy, Change Control, Backup/Recovery. | Pending (Week 4) |
| **Employee training records** | 10 staff × 1-hr initial + attendance; phishing sim results; semi-annual refresher log. | Pending (Week 4) |
| **Vulnerability scan reports** | ASV external scan (quarterly); internal scan (monthly). Critical/High = 0 before submission. | Pending (Week 5) |
| **Penetration test report** | Annual internal pen test; scope = CDE segment. Findings tracked to closure. | Pending (Annual) |
| **Attestation of Compliance (AOC)** | SAQ C + AOC signed by Jeet (owner); submitted to acquirer bank. | Pending (Week 5) |

---

## Questions

### 1. SAQ Selection: Which SAQ applies to Poshak and why?

**Answer:** **SAQ C** applies.

**Reasoning:**
- **Card-present only** — All 10,000 transactions are in-store via POS terminal (no e-commerce)
- **IP-connected payment application** — Terminal communicates over IP (Ethernet/Wi-Fi) to payment gateway
- **No CHD storage** — Jeet does not store PAN, expiry, or SAD electronically post-authorization
- **Level 4 merchant** — <20,000 Visa/MC transactions/year qualifies for SAQ
- **No P2PE confirmed** — If terminal uses PCI-listed P2PE, could use SAQ B-IP (simpler). Without P2PE validation, SAQ C is correct.
- **UPI irrelevant** — UPI does not involve CHD/SAD; outside PCI DSS scope.

---

### 2. Scope Reduction: What strategies can Jeet use to reduce PCI DSS scope?

| Strategy | How It Works | Poshak Applicability |
| --- | --- | --- |
| **P2PE (Point-to-Point Encryption)** | Validated solution encrypts CHD at terminal; merchant never sees clear PAN. Removes POS server/network from CDE. | **High impact** — If terminal supports P2PE, switch to SAQ B-IP (12→9 questions). Cost: terminal upgrade + P2PE validation. |
| **Tokenization** | Gateway returns token instead of PAN; merchant stores only token. Eliminates CHD storage risk. | **Medium** — Requires gateway support; reduces SAQ C scope if CHD stored. |
| **Outsource payment processing** | Use payment service provider (PSP) with hosted payment page/iframe; merchant never touches CHD. | **Not applicable** — Card-present requires physical terminal. |
| **Network segmentation** | Isolate CDE via firewall/VLAN; only required systems in scope. Reduces systems needing controls. | **Essential** — Already in action plan. Low cost (VLAN + firewall rules). |
| **Eliminate CHD storage** | Configure POS/server to not log PAN; truncate receipts; purge databases. | **Already done** — Verify no PAN in logs, DB, backups. |
| **Use validated P2PE terminal + SAQ B-IP** | Reduces requirements from 20 (SAQ C) to ~13 (SAQ B-IP). | **Best ROI** — If budget allows terminal upgrade. |

---

### 3. Compensating Controls: If a requirement cannot be met, what compensating controls might be acceptable?

| Requirement | Constraint | Acceptable Compensating Control | Validation Criteria |
| --- | --- | --- | --- |
| **Req 5.2 (MFA for admin)** | Legacy POS server OS (Windows 7) doesn't support modern MFA | **Physical token + PIN** for admin access; console-only admin (no remote); enhanced logging + alerting on admin login | 1) Meets intent (strong auth)<br>2) Risk analysis documented<br>3) No additional risk introduced<br>4) QSA/ISA sign-off |
| **Req 1.2 (Secure configs)** | Vendor-locked terminal OS prevents hardening | **Network-level controls**: CDE isolated; terminal only talks to gateway IP; IDS/IPS on CDE segment; terminal tamper alerts | Same 4 criteria + terminal vendor attestation |
| **Req 6.1 (Audit logs)** | Terminal OS cannot forward logs | **Network-based logging**: Firewall logs all CDE traffic; gateway logs all transactions; manual weekly terminal log review | Logs cover all required events; review documented |
| **Req 11.2 (Pen test)** | Budget constraints for 3rd party | **Internal pen test by trained staff** + annual 3rd party every 2 years; documented methodology | Qualified internal tester; methodology = industry standard |

> **Rule:** Compensating controls require **documented risk analysis**, **QSA/ISA approval**, and **annual re-validation**.

---

### 4. Annual Validation: What ongoing activities must Jeet perform annually to maintain compliance?

| Activity | Frequency | Owner | Evidence |
| --- | --- | --- | --- |
| **SAQ C re-assessment** | Annually (before AOC expiry) | Jeet / Consultant | Completed SAQ + evidence folder |
| **Attestation of Compliance (AOC)** | Annually | Jeet (owner) | Signed AOC submitted to acquirer |
| **External ASV scan** | Quarterly (4×/year) | ASV Vendor | Scan report + remediation proof |
| **Internal vulnerability scan** | Monthly | IT / Consultant | Scan report |
| **Penetration test** | Annually + after significant change | Internal/3rd party | Pen test report + closure log |
| **Risk assessment update** | Semi-annually | Jeet / Consultant | Updated risk register |
| **Information Security Policy review** | Annually | Jeet | Policy v2.0 with change log |
| **Incident Response Plan test** | Annually (tabletop) | Jeet + Staff | Exercise minutes + lessons learned |
| **Staff security training** | Semi-annually + quarterly phishing | Jeet / HR | Attendance + simulation results |
| **Vendor compliance review** | Annually | Jeet | Vendor AOCs/attestations on file |
| **Physical security audit** | Annually | Jeet | Checklist + photos |
| **Firewall rule review** | Semi-annually | IT | Rule audit log |

---

### 5. UPI Consideration: Does UPI acceptance affect PCI DSS scope?

**Answer: No.**

**Explanation:**
- **UPI (Unified Payments Interface)** is an Indian real-time payment system regulated by **NPCI (National Payments Corporation of India)**, not by card brands (Visa/MC/Amex).
- **PCI DSS scope** covers **cardholder data (CHD)** from **payment cards** (credit/debit/prepaid) bearing card-brand logos.
- **UPI transactions** use **virtual payment addresses (VPAs)**, bank account credentials, and UPI PIN — **no PAN, track data, CVV, or card expiry**.
- **No CHD/SAD involved** → UPI acceptance **does not expand** CDE or trigger additional PCI DSS requirements.
- **However:** If Jeet's POS terminal accepts **both cards and UPI** on the same device, the **card-present channel** still requires PCI DSS compliance. The terminal itself remains in scope for card transactions.
- **Best practice:** Ensure UPI and card payment flows are logically separated in terminal software; UPI PIN entry not logged; no cross-contamination of logs.

---

## References

- [PCI Security Standards Council — Document Library](https://www.pcisecuritystandards.org/document_library)
- [PCI DSS v4.0 Quick Reference Guide](https://www.pcisecuritystandards.org/document_library)
- [PCI DSS v4.0.1 Summary of Changes](https://www.pcisecuritystandards.org/document_library)
- [Sprinto — PCI Compliance for Small Businesses](https://sprinto.com/blog/pci-compliance-for-small-businesses/)
- [PCI DSS SAQ Instructions & Guidelines](https://www.pcisecuritystandards.org/saq-instructions)
- [PCI SSC — SAQ C v4.0.1](https://www.pcisecuritystandards.org/saq-instructions)
- [NPCI — UPI Guidelines](https://www.npci.org.in/upi-ecosystem)