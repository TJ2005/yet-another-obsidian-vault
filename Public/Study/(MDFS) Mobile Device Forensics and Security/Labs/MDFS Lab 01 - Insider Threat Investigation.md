---
Title: "MDFS Lab 01 - Insider Threat Investigation"
Status: Active
marker:
tags:
Date: 2026.04.23
Time: 01:21
---

# MDFS Lab 01 - Insider Threat Investigation


## Student Details
- Name: tejas kamal sahoo
- Roll no: k057

## Aim
Investigate a simulated insider threat case using password-manager, browser, and VPN logs to determine whether credential exfiltration occurred.

## Learning Outcomes
- Analyze password-manager audit logs for high-risk activity.
- Correlate browser artifacts with credential access events.
- Interpret VPN metadata (time, IP, geolocation) for attribution.
- Build a unified forensic timeline from multiple data sources.
- Produce a defensible incident conclusion.

## Tools and Environment
- keeper_audit_log.txt
- chrome_history.csv
- vpn_access.log
- Timeline correlation and report-writing workflow

## Procedure
1. Preserved the evidence set and validated that no source files were modified.
2. Analyzed password-manager logs to identify user, credential target, and access time.
3. Reviewed browser history for suspicious destinations after credential operations.
4. Reviewed VPN logs for session window and anomalous geolocation.
5. Correlated all timestamps into a single investigative timeline.
6. Assessed intent and risk based on sequence, proximity, and context of events.

## Key Findings
- User j.smith accessed Prod_DB_Credentials at 21:32:10 (outside normal office hours).
- Credential view and password copy actions were recorded in the same session.
- Pastebin access occurred shortly after credential copy, indicating potential exfiltration path.
- VPN session originated from Romania, inconsistent with expected operating location.
- Combined evidence strongly supports suspicious insider misuse and escalation requirement.

## Conclusion
The correlated logs establish a high-confidence insider-threat pattern: sensitive credential access, immediate copy action, suspicious external site access, and anomalous VPN origin. The event sequence is consistent with potential unauthorized disclosure of production credentials and should be escalated for containment and legal review.

## Evidence Screenshots
Key screenshots are embedded below. Full extracted set is available in assets/mdfs_lab_01_insider_threat_investigation/

![[IMG-20260423202656218.jpg]]

![[IMG-20260423202656346.jpg]]

![[IMG-20260423202656836.jpg]]

![[IMG-20260427170152265.jpg]]

![[IMG-20260423202657392.jpg]]
