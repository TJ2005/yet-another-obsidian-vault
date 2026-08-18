---

Title: "(ISA) Lab 4"

Status:

marker:

tags:

Date: "2026.08.10"

Time: "18:34"

---
# (ISA) Lab 4

# Experiment No. 4 — Business Continuity and Disaster Recovery Audit

## Aim

To study **Business Continuity (BC)** and its audit.

## Title

**Case Study Analysis for Business Continuity and Disaster Recovery**

---

# Part A — Business Continuity and Disaster Recovery

## Business Continuity

Business Continuity (BC) focuses on maintaining critical business operations during and after a disruption.

A Business Continuity Plan (BCP) defines:

* Critical business activities
* Alternative working arrangements
* Communication procedures
* Manual workarounds
* Responsibilities during disruption
* Recovery priorities

The main objective is to **minimise operational downtime and maintain essential services**.

## Disaster Recovery

Disaster Recovery (DR) focuses mainly on restoring:

* IT systems
* Applications
* Infrastructure
* Networks
* Data
* Technology services

The main objective is to **restore normal IT operations within an acceptable time after a disruption**.

## Business Continuity vs Disaster Recovery

| Business Continuity                                | Disaster Recovery                         |
| -------------------------------------------------- | ----------------------------------------- |
| Keeps critical operations running                  | Restores failed IT services               |
| Broader organisational scope                       | Mainly technology-focused                 |
| Includes people, processes, facilities and vendors | Includes systems, infrastructure and data |
| Focuses on continuity during disruption            | Focuses on recovery after disruption      |
| Uses alternate procedures and workarounds          | Uses backups, failover and restoration    |

Both BCP and DR should be **documented, tested, reviewed and regularly updated**.

---

# Part B — ABC Multispeciality Hospital Case Study

ABC Multispeciality Hospital is a **500-bed, 24×7 hospital**.

Its Hospital Management System (HMS) supports:

* Patient registration
* Electronic Health Records (EHR)
* Emergency services
* Laboratory
* Radiology
* Pharmacy
* Billing
* Discharge

The objective of the audit is to determine whether the hospital's existing BCP and DR arrangements can maintain critical hospital services during a major HMS disruption.

---

# Background Concepts

| Concept         | Meaning / Audit Focus                                                   |
| --------------- | ----------------------------------------------------------------------- |
| **BIA**         | Identifies critical activities and their dependencies                   |
| **RTO**         | Maximum acceptable time to restore a service                            |
| **RPO**         | Maximum acceptable amount of data loss                                  |
| **BCP**         | Defines how critical operations continue during disruption              |
| **DR**          | Defines how IT systems, applications and data are restored              |
| **Testing**     | Demonstrates whether BCP/DR arrangements actually work                  |
| **Maintenance** | Ensures plans remain updated after organisational or technology changes |

---

# Task 1 — Review the BIA

## BIA Audit Worksheet

| Audit Check                                | Yes / No / Partial | Evidence / Observation                                                                                                  |
| ------------------------------------------ | ------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| Critical services identified               | Yes                | Emergency/EHR, Pharmacy, Laboratory and Billing are identified and prioritised by criticality.                          |
| RTO defined for critical services          | Yes                | RTO values are defined for all listed services.                                                                         |
| RPO defined for critical services          | Yes                | RPO values are defined for all listed services.                                                                         |
| People dependencies identified             | No                 | Exhibit A does not identify required staff, roles or personnel dependencies.                                            |
| Technology dependencies identified         | No                 | Specific systems, servers, networks, databases and other technology dependencies are not documented in the BIA extract. |
| Premises dependencies identified           | No                 | No alternate site, facility or premises dependency is identified.                                                       |
| Third-party/vendor dependencies identified | No                 | Vendor dependencies are not included in Exhibit A.                                                                      |
| Manual workarounds documented              | No                 | Exhibit A contains no documented manual workaround procedures.                                                          |
| Single points of failure identified        | No                 | No single points of failure are identified in the BIA extract.                                                          |

## Audit Conclusion

The hospital **cannot demonstrate that the BIA is complete enough to fully support continuity planning**.

Although critical services, RTOs and RPOs are identified, important dependencies involving people, technology, premises and third-party vendors are missing. Manual workarounds and single points of failure are also not identified.

**Audit Query:** Obtain the complete BIA and supporting dependency analysis to determine whether these areas are documented elsewhere.

---

# Task 2 — Test RTO Achievement

| Service         | Target RTO | Actual Recovery | Pass / Fail | Audit Comment                                          |
| --------------- | ---------: | --------------: | ----------- | ------------------------------------------------------ |
| Emergency / EHR |     15 min |          42 min | **Fail**    | Recovery exceeded RTO by 27 minutes.                   |
| Pharmacy        |     30 min |          65 min | **Fail**    | Recovery exceeded RTO by 35 minutes.                   |
| Laboratory      |     60 min |          80 min | **Fail**    | Recovery exceeded RTO by 20 minutes.                   |
| Billing         |    4 hours |     3 hr 10 min | **Pass**    | Recovery completed 50 minutes within the approved RTO. |

## Conclusion

Three of the four tested services failed to meet their defined RTO.

Most importantly, **Emergency/EHR and Pharmacy**, both classified as critical, failed their recovery objectives.

---

# Task 3 — Test RPO Achievement

### Given

* Required RPO = **5 minutes**
* HMS failure = **10:00 AM**
* Latest recoverable data = **9:20 AM**

### Calculation

**Actual Data Loss = Failure Time − Latest Recoverable Data**

**10:00 AM − 9:20 AM = 40 minutes**

| Required RPO | Failure Time | Latest Recoverable Data | Actual Data Loss | Pass / Fail |
| -----------: | ------------ | ----------------------- | ---------------: | ----------- |
|        5 min | 10:00 AM     | 9:20 AM                 |       **40 min** | **Fail**    |

## Audit Conclusion

The Emergency/EHR RPO was **not achieved**.

The approved RPO allows only **5 minutes of data loss**, while the exercise demonstrated **40 minutes of data loss**.

This creates a significant risk of loss of recent patient records, clinical updates and other critical information.

---

# Task 4 — Evaluate BCP Controls

| Control / Evidence           | Control Type           | Design Adequate? | Operating Effectively? | Reason                                                                                     |
| ---------------------------- | ---------------------- | ---------------- | ---------------------- | ------------------------------------------------------------------------------------------ |
| BCP staff training           | Preventive / Proactive | Yes              | No                     | Training is appropriate, but coverage is poor in Pharmacy and Laboratory.                  |
| BIA with RTO/RPO             | Preventive / Proactive | Partial          | Partial                | Recovery objectives exist, but major dependencies are not demonstrated in the BIA extract. |
| DR exercise                  | Detective              | Yes              | Yes                    | Exercise successfully identified recovery weaknesses and RTO failures.                     |
| Tabletop exercise            | Detective              | Yes              | Yes                    | Exercise identified problems with manual procedures, escalation and failover.              |
| Database backup              | Recovery               | Partial          | No                     | Backups exist, but the latest recoverable data was 40 minutes old against a 5-minute RPO.  |
| Database failover            | Recovery / Corrective  | Yes              | No                     | Failover mechanism exists but failed on the first attempt.                                 |
| Manual patient registration  | Corrective / Recovery  | Yes              | No                     | Nursing staff were unsure how to perform the procedure.                                    |
| Offline medication list      | Recovery               | Yes              | No                     | Pharmacy staff could not access the list during the exercise.                              |
| Emergency escalation process | Corrective             | Yes              | No                     | Escalation took 22 minutes, delaying incident response.                                    |
| Corrective-action tracking   | Corrective             | No               | No                     | No formal post-exercise corrective-action tracker was created.                             |

## Control Evaluation Conclusion

The hospital has several continuity and recovery controls, but many are **not operating effectively**.

The major weaknesses relate to:

* Recovery performance
* Backup effectiveness
* Staff preparedness
* Failover
* Manual workarounds
* Escalation
* Corrective-action tracking

---

# Task 5 — Identify Audit Findings

| No. | Audit Observation                                                           | Risk / Impact                                                                                            | Evidence Ref. | Priority   |
| --: | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------- | ---------- |
|   1 | Critical services failed to meet defined RTOs.                              | Delayed access to EHR, pharmacy and laboratory services may affect patient care and hospital operations. | A, B          | **High**   |
|   2 | Emergency/EHR actual data loss was 40 minutes against a 5-minute RPO.       | Recent patient and clinical data may be unavailable after disruption.                                    | A, C          | **High**   |
|   3 | BCP has not been formally reviewed since January 2024.                      | Continuity procedures may no longer represent the hospital's current environment.                        | D             | **High**   |
|   4 | Pharmacy and Laboratory have low BCP training coverage.                     | Staff may be unable to execute continuity procedures during an actual emergency.                         | E, F          | **High**   |
|   5 | Database failover failed on the first attempt.                              | Critical systems may not recover within required recovery times.                                         | F             | **High**   |
|   6 | Emergency contact escalation took 22 minutes and includes former employees. | Incident response and decision-making may be delayed.                                                    | D, F          | **High**   |
|   7 | No formal corrective-action tracker was created after the exercise.         | Identified weaknesses may remain unresolved and recur during future incidents.                           | F             | **Medium** |
|   8 | New vendor and cloud laboratory application are absent from the BCP.        | Recovery planning may fail to account for current external and technology dependencies.                  | D             | **High**   |

---

# Task 6 — Develop Professional Audit Findings

## Finding 1 — Critical Services Failed RTO

| Element                                | Student Response                                                                                                                                                                                  |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Criteria**                           | Critical services should be recoverable within their approved RTOs.                                                                                                                               |
| **Condition**                          | Emergency/EHR recovered in 42 minutes against a 15-minute RTO, Pharmacy in 65 minutes against 30 minutes, and Laboratory in 80 minutes against 60 minutes.                                        |
| **Cause**                              | Recovery arrangements are not sufficiently effective to achieve the approved recovery targets. Further root-cause evidence should be obtained to determine the specific technical/process causes. |
| **Consequence / Risk**                 | Extended unavailability of critical clinical systems may delay patient treatment, medication processing and laboratory services.                                                                  |
| **Corrective Action / Recommendation** | Review recovery architecture and procedures, identify causes of recovery delays, remediate weaknesses and perform another DR exercise to verify RTO achievement.                                  |
| **Priority**                           | **High** — Critical clinical services failed their approved recovery objectives.                                                                                                                  |

---

## Finding 2 — Emergency/EHR RPO Failure

| Element                                | Student Response                                                                                                                                                        |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Criteria**                           | Emergency/EHR has an approved RPO of 5 minutes.                                                                                                                         |
| **Condition**                          | At the 10:00 AM failure, the latest recoverable data was from 9:20 AM, resulting in 40 minutes of data loss.                                                            |
| **Cause**                              | The 30-minute backup frequency and demonstrated recoverability do not support the approved 5-minute RPO.                                                                |
| **Consequence / Risk**                 | Recent patient records and clinical transactions may be lost, affecting patient care and data integrity.                                                                |
| **Corrective Action / Recommendation** | Implement a recovery mechanism capable of meeting the 5-minute RPO, such as more frequent replication or equivalent technology, and verify it through recovery testing. |
| **Priority**                           | **High** — The demonstrated data loss is significantly above the approved tolerance for a critical clinical service.                                                    |

---

## Finding 3 — BCP Documentation Is Outdated

| Element                                | Student Response                                                                                                                                                                                    |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Criteria**                           | BCP documentation should be periodically reviewed and updated following organisational, personnel, vendor and technology changes.                                                                   |
| **Condition**                          | The BCP was last formally reviewed in January 2024. Two emergency contacts have left, a critical vendor has changed, and a cloud laboratory application introduced in 2025 is absent from the plan. |
| **Cause**                              | An effective periodic BCP maintenance and update process has not been demonstrated.                                                                                                                 |
| **Consequence / Risk**                 | During an incident, staff may contact incorrect personnel or follow recovery procedures that do not cover current vendors and systems.                                                              |
| **Corrective Action / Recommendation** | Immediately review and update the BCP and establish a formal periodic review process triggered by major personnel, vendor, system and organisational changes.                                       |
| **Priority**                           | **High** — Multiple material changes are missing from the current BCP.                                                                                                                              |

---

# Task 7 — COBIT 2019 Mapping

> **Note:** Exact DSS04 practice/sub-practice identifiers should be taken from the COBIT 2019 material provided in class, as required by the lab.

| Audit Finding                        | COBIT Objective            | Relevant Practice / Area               | Control Gap                                                               | Recommendation                                                         |
| ------------------------------------ | -------------------------- | -------------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Critical services failed RTO         | DSS04 — Managed Continuity | Continuity response / recovery testing | Recovery capability does not meet defined RTO                             | Improve recovery arrangements and retest against approved RTOs.        |
| Emergency/EHR failed RPO             | DSS04 — Managed Continuity | Backup and recovery arrangements       | Current recoverability cannot achieve 5-minute RPO                        | Improve backup/replication and validate recovery capability.           |
| BCP documentation outdated           | DSS04 — Managed Continuity | Continuity plan maintenance            | BCP does not reflect current personnel, vendor and technology environment | Establish periodic and change-triggered BCP reviews.                   |
| Staff unable to perform workarounds  | DSS04 — Managed Continuity | Training / continuity exercises        | Staff are not adequately prepared to execute alternate procedures         | Increase BCP training and conduct regular exercises.                   |
| Exercise issues not formally tracked | DSS04 — Managed Continuity | Exercise review and improvement        | No corrective-action tracking mechanism                                   | Create a formal issue owner, target date and closure-tracking process. |

---

# Task 8 — Overall Audit Opinion

| Assurance Opinion                             | Select One            | Justification                                                                                                                                                     |
| --------------------------------------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Substantial / Reasonable / **Limited** / None | **Limited Assurance** | Important BCP/DR controls exist, but significant weaknesses prevent strong assurance that critical hospital services can be maintained and recovered as required. |

## Justification

**Limited Assurance** is appropriate because:

1. **Three services failed their RTO**, including Emergency/EHR and Pharmacy.
2. Emergency/EHR demonstrated **40 minutes of data loss against a 5-minute RPO**.
3. The BCP has not been formally reviewed since **January 2024** and contains outdated contacts, vendor information and technology dependencies.
4. Staff demonstrated weaknesses in manual procedures and offline medication access.
5. Database failover failed on its first attempt.
6. No formal corrective-action tracker was created after testing.

The hospital has established continuity arrangements, so **No Assurance** would be too strong. However, the significant operating weaknesses mean that Reasonable or Substantial Assurance cannot currently be supported.

---

# Final Question

## Does the existence of a documented BCP provide sufficient assurance that the hospital can maintain critical services during disruption?

**No.**

A documented BCP only demonstrates that continuity procedures have been formally defined. Effective assurance requires evidence that those procedures are **current, understood, tested and capable of meeting approved recovery objectives**.

The case demonstrates that documentation alone is insufficient because:

* Emergency/EHR recovered in **42 minutes against a 15-minute RTO**.
* Pharmacy recovered in **65 minutes against a 30-minute RTO**.
* Emergency/EHR experienced **40 minutes of recoverable data loss against a 5-minute RPO**.
* Staff were unsure about manual procedures.
* Pharmacy staff could not access the offline medication list.
* Database failover failed on its first attempt.
* The BCP contains outdated contacts and dependencies.
* No formal corrective-action tracker was created after the exercise.

Therefore, the hospital must demonstrate through **regular testing, staff training, recovery exercises, BCP maintenance and corrective-action tracking** that its continuity arrangements work in practice.

---

# Overall Conclusion

The hospital has established BCP and DR arrangements, but the audit identifies significant weaknesses in their effectiveness.

The most important issues are:

* Failure to achieve critical RTOs
* Failure to achieve the Emergency/EHR RPO
* Outdated BCP documentation
* Inadequate staff preparedness
* Failover failure
* Weak emergency escalation
* Missing corrective-action tracking

Therefore, the hospital currently receives an overall **Limited Assurance** opinion for its ability to maintain and recover critical services during a major HMS disruption.

  

# References


###### Information
- date: 2026.08.10
- time: 18:34