---
Title: "CRM Lab 5"
Status: incomplete
tags: [semester-7, cybersecurity, CRM, lab]
Date: "2026.08.29"
---

# CRM Lab 5 — Develop a BCP & DRP Plan

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

Develop a detailed Business Continuity and Disaster Recovery (BCP & DRP) Plan per ISO 22301:2019 for an organisation of a chosen sector.

## Learning Outcomes

- Establish a BCP & DRP to control risks and recover as quickly as possible from any crisis
- Identify the various regulatory and compliance requirements w.r.t engaging with third parties
- Align the risk and impact using the concepts of Risk Management Frameworks

## Frameworks for reference

- ISO 27001:2022
- ISO 22301:2019
- ISO 27017:2015

## Procedure

- Develop a detailed Business Continuity and Disaster Recovery Plan per ISO 22301:2019.
- Pick up a use-case scenario with pre- and post-COVID BCP changes & implications in the IT infrastructure for an organisation of your chosen sector.
- Identify all the inherited and residual risks across Network, Infrastructure, Applications (Web & Mobile), Kiosk, Cloud, Physical & Environmental, which affect the overall BCP & DRP Plan.

## Use-case scenario

> [!INFO] OOCL India — global container liner shipping and logistics (Indian arm of OOCL, Orient Overseas Container Line, part of the COSCO Shipping group)

| Field                              | Answer                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Sector**                         | Global container shipping (ocean freight & logistics)                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Organisation name**              | OOCL India (Orient Overseas Container Line)                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Headquarters / geographies**     | India head office in Mumbai<br>Offices + terminal/CFS presence in Chennai, Delhi NCR, Kolkata, Mundra and major ports                                                                                                                                                                                                                                                                                                                                              |
| **Core IT infrastructure**         | Vessel & fleet systems<br>Container tracking<br>Booking/e-commerce platform (MyOOCL)<br>Mobile app (OOCL Lite)<br>EDI/API integrations (incl. Indian customs/ICEGATE)<br>Terminal / yard systems<br>Cloud-hosted web & mobile services<br>Customer-service kiosks<br>My OOCL Center<br>Booking Capacity and Rollover management<br>Internal Documentation platform<br>FreightSmart<br>SAP Ticket systems to manage shipments<br>Notification for vessel delays<br> |
| **Key business functions**         | International container shipping (FCL)<br>Inland transportation & CFS<br>Reefer cargo<br>Documentation (Bill of Lading)<br>Customs clearance support<br>Customer tracking portal                                                                                                                                                                                                                                                                                   |
| **Legal / compliance obligations** | DPDP Act / IT Act 2000<br>Indian customs & GST requirements<br>Global shipping-data regulations<br>Customer NDAs<br>Contractual SLAs with shippers, terminals and partners                                                                                                                                                                                                                                                                                         |

## Pre- and post-COVID BCP changes

| Aspect                              | Pre-COVID                                                                           | Post-COVID                                                                                                 | Implication on IT infrastructure                                               |
| ----------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Workforce model**                 | Office-centric at Mumbai/port offices<br>Staff issue BL, bookings, customer queries | Hybrid / remote-first<br>Many functions moved home-office<br>Added VPNs                                    | Secure remote access<br>Video conferencing<br>Cloud apps reliance              |
| **Access model**                    | In-office LAN<br>Limited VPN for senior staff                                       | VPN / Zero Trust extended to all staff<br>BYOD posture                                                     | VPN capacity<br>MFA<br>Endpoint hardening<br>Remote helpdesk                   |
| **Data centre / cloud posture**     | On-premise datacentres<br>Leased lines to ports/terminals                           | Accelerated cloud adoption<br>(booking portal, tracking, analytics)                                        | Hybrid footprint<br>Cloud DR<br>Vendor resilience<br>ISO 27017 controls        |
| **Business continuity triggers**    | Typhoons<br>Port closures<br>Vessel breakdowns<br>Strikes<br>Wars<br><br>           | Added: lockdowns<br>Staff illness clusters<br>Port-operational constraints<br>Information Security<br><br> | More scenario triggers<br>Digital-first continuity of booking/tracking         |
| **Third-party / vendor engagement** | Terminal operators<br>Feeder lines<br>Customs brokers<br>On-prem vendors            | Cloud vendors<br>Remote-managed services<br>Existing partners                                              | New inherited risks (cloud/remote vendors)<br>Compliance & SLA review required |

## BCP / DRP Plan (per ISO 22301:2019)

### 1. Business continuity policy and scope

- **Policy statement:** OOCL India maintains cyber-resilient continuity of its booking, tracking, customs-clearance and vessel-operations platforms. Any cyber event (ransomware, credential theft, cloud outage, supply-chain compromise) must be contained within MAO, with customer-facing services restored per RTO/RPO. Policy covers all IT/OT assets, cloud tenants, third-party integrations and physical port terminals.
- **Scope (functions / sites / systems in scope):** MyOOCL booking portal (web/mobile), OOCL Lite app, container-tracking API, EDI/ICEGATE customs gateway, vessel & fleet management, terminal/CFS yard systems, cloud infrastructure (IaaS/SaaS), customer-service kiosks, VPN/Zero-Trust remote access. Sites: Mumbai HO, Chennai, Delhi NCR, Kolkata, Mundra offices and associated port terminals.
- **BCP objectives (RTO / RPO):**

| Function | RTO | RPO | Rationale |
| --- | --- | --- | --- |
| Booking & tracking (MyOOCL / API) | 1 h | 15 min | Customer-facing revenue; SLA; container visibility |
| Customs/ICEGATE gateway | 2 h | 0 | Legal mandate; Bill of Lading integrity; zero data loss |
| Vessel/fleet systems | 1 h | 5 min | Safety of navigation; stowage plan currency |
| Terminal/yard systems | 2 h | 30 min | Gate throughput; yard move tracking |
| Finance & invoicing | 4 h | 1 h | Revenue recognition; GST compliance; from [[CRM Lab 5 — OOCL India BIA]] |
| Internal HR / payroll | 12 h | 24 h | Employee services; statutory payroll deadlines |
| Customer support / kiosk | 4 h | 1 h | SLA-bound ticket resolution; portal access |
| Marketing & reporting | 24 h | 24 h | Non-transactional; analytics refresh window |

### 2. Risk register (inherited and residual)

| # | Risk | Domain | Likelihood | Impact | Inherited risk | Residual risk | Control / treatment |
| --: | --- | --- | --- | --- | --- | --- | --- |
| 1 | Ransomware on booking/tracking platform (phishing → lateral move) | Applications (Web & Mobile) | High | Critical | Cloud provider shared responsibility (IaaS patching) | Medium | Immutable backups, network segmentation, EDR, phishing sims, 1 h RTO tested |
| 2 | API key / EDI credential compromise (MyOOCL / ICEGATE) | Applications (Web & Mobile) | Medium | Critical | Vendor API gateway defaults (rate limits, scopes) | Low | Key vault with rotation, short-lived tokens, mTLS, audit logs, anomaly alerts |
| 3 | Cloud misconfiguration (public S3 / security group) exposing container PII | Cloud | Medium | High | CSP shared responsibility (control plane) | Low | IaC policy-as-code (OPA), CSPM, drift detection, monthly pen-test |
| 4 | Supply-chain / vendor compromise (terminal OS, feeder-line portal) | Cloud / Infrastructure | Low | High | Vendor security posture (outside OOCL control) | Medium | Vendor risk tiering, contractual SLAs, ISO 27017 attestations, continuous monitoring |
| 5 | Insider threat (privileged admin exfiltrates shipment data) | Infrastructure / Applications | Low | Critical | None (internal) | Low | PAM with session recording, least-privilege, DLP on egress, UEBA |
| 6 | DDoS on public booking API / tracking portal | Network / Applications | Medium | High | CDN / WAF provider capacity (inherited) | Low | Always-on DDoS mitigation, rate-limiting, geo-blocking, capacity reserve |
| 7 | VPN / Zero-Trust bypass (MFA fatigue, token theft) | Network | Medium | High | IdP / MFA vendor resilience | Low | Phishing-resistant MFA (FIDO2), conditional access, token binding, SIM-swap protection |
| 8 | Physical terminal kiosk compromise (USB drop, tampered firmware) | Kiosk / Physical | Low | Medium | Terminal operator maintenance | Low | Kiosk hardening (kiosk mode, signed firmware, USB disable), daily integrity check |
| 9 | Cloud region outage (primary DR region unavailable) | Cloud | Low | Critical | CSP SLA (inherited) | Medium | Multi-region active-active for booking/tracking, automated failover tested quarterly |
| 10 | Data integrity attack on Bill-of-Lading / customs records | Applications / Physical | Low | Critical | None | Low | WORM storage, cryptographic signing of BL, hash verification on ingest, audit trail |

### 3. Business impact analysis summary (MAO / RTO / RPO)

| # | Business function | Maximum Acceptable Outage (MAO) | RTO | RPO | Impact classification |
| --: | --- | --- | --- | --- | --- |
| 1 | Container booking & e-commerce (MyOOCL) | 2 h | 1 h | 15 min | Critical |
| 2 | Container tracking & customer API | 2 h | 1 h | 15 min | Critical |
| 3 | Customs clearance / ICEGATE gateway | 4 h | 2 h | 0 | Critical |
| 4 | Vessel & fleet management | 3 h | 1 h | 5 min | Critical |
| 5 | Terminal / yard operations (CFS) | 4 h | 2 h | 30 min | Critical |
| 6 | Finance & invoicing | 8 h | 4 h | 1 h | Critical |
| 7 | Customer support / kiosk services | 8 h | 4 h | 1 h | Major |
| 8 | HR & payroll | 24 h | 12 h | 24 h | Major |
| 9 | Marketing / reporting | 48 h | 24 h | 24 h | Minor |

> [!NOTE] RTO/RPO values aligned with [[CRM Lab 5 — OOCL India BIA]] BIA for OOCL India container shipping platform.

### 4. Recovery plan and strategy

- **Recovery objectives:** Restore customer-facing booking, tracking and customs gateway within 1–2 h (RTO). Preserve zero data loss for customs/BL records (RPO 0). Contain lateral movement within 30 min of detection.
- **Recovery strategy (alternate site / cloud DR / backup):**
  - **Active-active multi-region** for MyOOCL, tracking API, ICEGATE gateway (primary: Mumbai region, DR: Chennai region) — automated health-check failover < 5 min
  - **Immutable backup vault** (daily snapshots, 30-day retention, cross-region copy) for vessel, finance, BL datasets — point-in-time restore to meet RPO
  - **Cold standby** for terminal/yard systems (rebuild from IaC within 2 h) — lower criticality
  - **Vendor failover** for EDI/ICEGATE: secondary customs broker API pre-contracted
- **Recovery teams & roles (RACI):**
  - **CISO / CTO (Accountable)** — invoke DR, executive comms
  - **Security Operations Lead (Responsible)** — containment, forensics, eradication
  - **Platform Engineering Lead (Responsible)** — infra rebuild, failover execution
  - **Application Owners (Consulted)** — data validation, business sign-off
  - **Legal / Compliance (Informed)** — regulator notification (CERT-In, DPDP), customer comms
  - **Vendor Managers (Consulted)** — third-party SLAs, cloud support tickets
- **RTO/RPO vs strategy mapping:**
  - Critical (RTO ≤ 2 h): active-active cloud failover + immutable backups
  - Major (RTO ≤ 12 h): warm standby + IaC rebuild + backup restore
  - Minor (RTO ≤ 48 h): cold rebuild from GitOps

### 5. Recovery procedures (playbook)

| Incident type | Detection | Response | Recovery | Restoration & verification |
| --- | --- | --- | --- | --- |
| **Ransomware on booking/tracking platform** | EDR alert + anomalous file encryption + SIEM correlation | Isolate affected VPC/subnet; revoke compromised creds; engage IR retainer | Failover to DR region (active-active); restore DB from immutable snapshot (RPO 15 min) | Smoke-test booking flow; verify tracking API integrity; customer comms; lessons-learned |
| **API key / EDI credential compromise** | Anomalous geo/IP + rate spike on MyOOCL / ICEGATE keys | Revoke keys in vault; rotate emergency keys; notify customs broker | Re-issue keys to legitimate consumers; validate EDI transaction flow | Audit last 48 h transactions; confirm no fraudulent BL issued; update key-rotation policy |
| **Cloud misconfiguration (public bucket / SG)** | CSPM drift alert / external researcher report | Immediate remediate (private ACL, SG restrict); quarantine exposed data | Verify no data exfiltration via CloudTrail / VPC flow logs | Re-scan entire tenant; update IaC guardrails; post-mortem |
| **Supply-chain / vendor compromise** | Vendor security advisory / threat intel feed | Assess blast radius (which OOCL systems consume vendor API); isolate integration | Switch to secondary vendor API; deploy compensating controls (WAF rules) | Joint incident review; contractual penalty / SLA enforcement; vendor re-tiering |
| **Insider threat (privileged admin data exfil)** | UEBA alert (bulk download, odd hours) + DLP trigger | Suspend account; PAM session review; forensic image workstation | Reset all privileged creds; rotate service accounts; verify no persistence | Legal hold; DPDP breach assessment; access-recertification campaign |
| **DDoS on public booking API** | CDN/WAF volumetric alert + latency spike | Auto-mitigation (rate-limit, geo-block, challenge) engages; scale origin | Monitor mitigation effectiveness; engage L3/L7 scrubbing if needed | Confirm legitimate traffic restored; tune WAF rules; capacity planning |
| **VPN / Zero-Trust bypass (MFA fatigue, token theft)** | Impossible travel / token replay / MFA prompt flood alerts | Revoke session; enforce step-up FIDO2; quarantine device | Conditional access policy refresh; re-enroll authenticator | Review IdP logs for lateral access; user security coaching; phishing sim |
| **Physical terminal kiosk compromise** | Tamper alert / unexpected process / USB device log | Disable kiosk network port; collect forensic image | Re-image from signed golden image; verify firmware signature | Physical inspection; update kiosk hardening checklist; rotate local certs |
| **Cloud region outage** | CSP status page + health-check failures | Automated failover to DR region (pre-tested) | Validate DR region capacity; redirect DNS / API gateway | Run full booking/tracking regression; confirm RTO met; CSP credit claim |
| **Data integrity attack on BL / customs records** | Hash mismatch on ingest / auditor finding | Quarantine affected records; revert to last known-good WORM snapshot | Re-process legitimate transactions from source systems | Cryptographic verification of all BLs; customs reconciliation; legal sign-off |

### 6. Communication, testing and maintenance

- **Communication plan (internal / external / regulators):**
  - **Internal:** Slack/Teams #bcp-war-room (auto-created on DR invoke); 15-min sitrep cadence; executive summary hourly
  - **Customers:** Status page (status.oocl.com) + email/SMS for active bookings; SLA breach notices per contract
  - **Regulators:** CERT-In within 6 h (cyber incident); DPDP breach notification within 72 h; customs authority for ICEGATE disruption
  - **Vendors:** Cloud support tickets (P1); terminal operator liaison; customs broker escalation
- **Testing & exercising (frequency / type):**
  - **Quarterly:** Tabletop for ransomware + cloud-region failover (CISO, SecOps, Platform, Legal)
  - **Monthly:** Automated DR failover test (non-prod) for MyOOCL + tracking API; verify RTO < 1 h
  - **Semi-annual:** Red-team / purple-team exercise targeting API keys, VPN, supply-chain
  - **Annual:** Full BCP/DRP review + ISO 22301 internal audit; update risk register, MAO, contacts
- **Review & maintenance cycle:**
  - **Monthly:** Risk register refresh (new threats, vendor changes); MAO/RTO validation
  - **Quarterly:** Playbook walkthrough with application owners; update runbooks
  - **Post-incident:** Mandatory retrospective within 5 business days; update controls, runbooks
  - **Annual:** Policy re-approval by board; ISO 22301 surveillance audit alignment
- **Third-party / vendor compliance requirements (ISO 27017 / contractual):**
  - Cloud providers: ISO 27001 + ISO 27017 certified; contractual RTO/RPO; right-to-audit; data-residency India
  - Terminal operators: Cyber hygiene questionnaire; incident-notification SLA 1 h; patching cadence
  - Customs brokers / EDI gateways: mTLS mandatory; API versioning policy; DR test participation
  - SaaS vendors (IdP, monitoring, ticketing): SOC 2 Type II; data-processing addendum (DPDP)

## Inherited and residual risks across domains

| Domain | Inherited risks | Residual risks | Impact on BCP & DRP plan |
| --- | --- | --- | --- |
| **Network** | ISP / submarine-cable outage; CDN/WAF provider capacity limits; IdP/MFA vendor availability | DDoS mitigation bypass; VPN split-tunnel leakage | Multi-ISP + diverse paths; always-on scrubbing; Zero-Trust with device posture; DR region in separate network zone |
| **Infrastructure** | Hypervisor / host OS vulns (CSP responsibility); hardware supply-chain implants | Container escape; host-level persistence | Hardened node images; runtime security (Falco); node rotation; attestation |
| **Applications (Web & Mobile)** | Framework / library supply-chain (Log4j-style); third-party JS on booking portal | Code injection via compromised dependency; client-side skimming | SBOM + SCA in CI/CD; CSP + SRI for third-party JS; WAF virtual patching |
| **Kiosk** | Terminal operator firmware supply-chain; physical access at port | Malicious firmware; USB drop; skimming hardware | Signed firmware verification; kiosk mode lock-down; USB disable; daily integrity attestation |
| **Cloud** | CSP control-plane outage; shared-tenancy side-channels; IAM misconfig defaults | Region outage; data residency violation; privilege escalation via inherited roles | Multi-region active-active; customer-managed keys (CMK); CSPM guardrails; least-privilege IAM |
| **Physical & Environmental** | Port closure (cyclone, strike); power loss at Mumbai HO; fiber cut to terminal | Generator failure; HVAC failure in server room | Dual power feeds + UPS + generator; geo-diverse DR; remote-work continuity (tested post-COVID) |

## Deliverable — 3-pager report outline

- **Page 1 — Executive summary + scenario + BCP goals:**
  - OOCL India (global container liner, COSCO group) — Mumbai HO, port terminals across India
  - Cyber-resilient continuity for booking (MyOOCL), tracking, customs/ICEGATE, vessel ops
  - BCP scope: all web/mobile apps, cloud infra, EDI gateways, terminal kiosks, VPN/Zero-Trust
  - Goals: contain any cyber event within MAO; restore Critical services ≤2 h (RTO); zero data loss for customs/BL (RPO 0); meet DPDP, CERT-In, customs regulatory timelines

- **Page 2 — Risk, MAO, recovery plan and strategy:**
  - Top 10 cyber risks (ransomware, API key compromise, cloud misconfig, supply-chain, insider, DDoS, MFA fatigue, kiosk tampering, region outage, BL integrity) with inherited/residual split
  - MAO/RTO/RPO table (9 functions, Critical/Major/Minor tiers) aligned with [[CRM Lab 5 — OOCL India BIA]] BIA
  - Recovery strategy: active-active multi-region for Critical APIs; immutable cross-region backups for RPO; cold standby for yard systems; vendor failover for customs broker
  - RACI: CISO/CTO accountable; SecOps + Platform Engineering responsible; Legal/Compliance informed for CERT-In/DPDP; Vendor Managers consulted

- **Page 3 — Detailed DRP procedures + inherited/residual risk analysis + conclusion:**
  - 10-scenario playbook (Detection → Response → Recovery → Verification) for each cyber event
  - Domain risk matrix (Network, Infra, Apps, Kiosk, Cloud, Physical) — inherited vs residual with controls
  - Testing cadence: quarterly tabletop (ransomware + failover), monthly automated DR test, semi-annual red-team, annual ISO 22301 audit
  - Conclusion: OOCL India's cyber-BCP achieves regulatory compliance and customer trust through active-active cloud architecture, immutable backups, Zero-Trust access, and continuous testing — residual risk reduced to Low for all Critical functions

## Conclusion

OOCL India's Business Continuity and Disaster Recovery Plan, developed per ISO 22301:2019, demonstrates that cyber-resilient continuity for a global container liner requires treating cyber events as primary disruption scenarios — not afterthoughts. The plan aligns Maximum Acceptable Outage, RTO and RPO directly to the BIA from [[CRM Lab 5 — OOCL India BIA]], ensuring that customer-facing booking, tracking and customs-clearance services meet a 1–2 hour RTO with near-zero RPO. Key architectural decisions — active-active multi-region cloud deployment, immutable backup vaults, Zero-Trust network access, and supply-chain risk tiering under ISO 27017 — reduce residual risk to Low across all Critical functions. The inherited/residual risk matrix makes third-party dependencies visible and controllable. Quarterly tabletop exercises, monthly automated failover tests, and annual ISO 22301 audits create a living plan that evolves with the threat landscape. This BCP/DRP satisfies CERT-In 6-hour reporting, DPDP 72-hour breach notification, and customs/ICEGATE continuity mandates, while protecting the crown jewels: Bill of Lading integrity, container visibility, and shipper trust.

## References

- [[CRM Lab 5 — OOCL India BIA]] — Business Impact Analysis (inputs: functions, RTO/RPO, crown jewels)
- [[CRM Lab 4]] — ERP Studios BIA (comparison baseline)
- [[CRM Lab 3]] — risk management plan and quantitative risk evaluation
- [[CRM Lab 2]] — risk assessment with the NIST Cybersecurity Framework