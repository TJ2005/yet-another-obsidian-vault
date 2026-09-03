---
Title: "CRM Lab 6"
Status: incomplete
tags: [semester-7, cybersecurity, CRM, lab]
Date: "2026.09.03"
---

# CRM Lab 6 — PCI DSS Standard

| | |
| --- | --- |
| **Academic Year** | 2026–27 |
| **Programme** | BTECH CRM |
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

## Procedure

> [!NOTE] Steps to complete
> 1. Visit <https://www.pcisecuritystandards.org/document_library> and download the PCI DSS standard
> 2. Form a group of 3–4 students
> 3. Read the standard and prepare a summary document
> 4. Solve the scenario below and create an action plan + filled SAQ
> 5. Upload summary document and scenario solution

## Scenario: Poshak Store — PCI DSS Compliance

> **Background:** Jeet Shah owns 'Poshak', a readymade garment store in Borivali, Mumbai. The store has 10 employees. Jeet is tech-savvy and has adopted multiple technology solutions for better customer experience. One initiative: accepting credit/debit card and UPI payments. Annual card transactions: ~10,000. He wants to become PCI DSS compliant and has approached you (PCI DSS compliance expert).

### Your Task

As a PCI DSS compliance expert, help Jeet Shah achieve compliance. Provide:

#### A. Action Plan for Jeet Shah

| Phase | Activity | Description | Timeline | Resources Needed |
| --- | --- | --- | --- | --- |
| 1. Scoping | | | | |
| 2. Gap Analysis | | | | |
| 3. Remediation | | | | |
| 4. Validation | | | | |
| 5. Ongoing Compliance | | | | |

#### B. Self-Assessment Questionnaire (SAQ) Selection

> [!TODO] Determine which SAQ applies
> - SAQ A / A-EP / B / B-IP / C / C-VT / D / P2PE-HW
> - Justify selection based on Poshak's payment environment

**Selected SAQ:** 

**Justification:** 

#### C. Filled Self-Assessment Questionnaire (SAQ)

> [!NOTE] Fill the relevant SAQ sections based on Poshak's environment

| Requirement | PCI DSS Requirement | In Place? (Yes/No/Partial) | Evidence / Notes | Remediation Needed |
| --- | --- | --- | --- | --- |
| **1.1** | Network security controls (firewalls) | | | |
| **1.2** | Secure configurations | | | |
| **2.1** | Protect stored cardholder data | | | |
| **2.2** | No SAD storage post-authorization | | | |
| **3.1** | Cryptography for CHD transmission | | | |
| **3.2** | PAN masking | | | |
| **4.1** | Anti-malware on all systems | | | |
| **4.2** | Secure systems/software development | | | |
| **5.1** | Unique IDs for each user | | | |
| **5.2** | MFA for all non-console access | | | |
| **5.3** | Physical access controls | | | |
| **6.1** | Audit logs for all access | | | |
| **6.2** | Log review & retention | | | |
| **7.1** | Vulnerability scans (quarterly) | | | |
| **7.2** | Penetration testing (annual) | | | |
| **8.1** | Information security policy | | | |
| **8.2** | Risk assessment process | | | |
| **8.3** | Incident response plan | | | |

> Expand the table above with all 12 requirements and their sub-requirements as per the selected SAQ.

#### D. Key Compliance Deliverables for Poshak

| Deliverable | Description | Status |
| --- | --- | --- |
| Network diagram (CHD flow) | | |
| Data flow diagram | | |
| Asset inventory (systems handling CHD) | | |
| Risk assessment report | | |
| Policies & procedures document | | |
| Employee training records | | |
| Vulnerability scan reports | | |
| Penetration test report | | |
| Attestation of Compliance (AOC) | | |

## Questions

1. **SAQ Selection:** Which SAQ applies to Poshak and why? Consider: card-present vs card-not-present, payment terminal type, whether CHD is stored/processed/transmitted.
2. **Scope Reduction:** What strategies can Jeet use to reduce PCI DSS scope? (e.g., P2PE, tokenization, outsourcing payment processing)
3. **Compensating Controls:** If a requirement cannot be met, what compensating controls might be acceptable? Give examples.
4. **Annual Validation:** What ongoing activities must Jeet perform annually to maintain compliance?
5. **UPI Consideration:** Does UPI acceptance affect PCI DSS scope? Explain.

## References

- [PCI Security Standards Council — Document Library](https://www.pcisecuritystandards.org/document_library)
- [PCI DSS v4.0 Quick Reference Guide](https://www.pcisecuritystandards.org/document_library)
- [Sprinto — PCI Compliance for Small Businesses](https://sprinto.com/blog/pci-compliance-for-small-businesses/)
- [PCI DSS SAQ Instructions & Guidelines](https://www.pcisecuritystandards.org/saq-instructions)