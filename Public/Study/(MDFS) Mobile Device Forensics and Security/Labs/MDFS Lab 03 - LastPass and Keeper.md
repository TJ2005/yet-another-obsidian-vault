---
Title: "MDFS Lab 03 - LastPass and Keeper"
Status: Active
marker:
tags:
Date: 2026.04.23
Time: 01:21
---
# MDFS Lab 03 - LastPass and Keeper

Source file: K057_MDSF_Lab03.pdf

## Student Details
- Name: tejas kamal sahoo
- Roll no: k057

## Aim
Examine how password-manager data can appear in process memory during runtime using LastPass and Keeper workflows.

## Learning Outcomes
- Identify target browser-extension processes for memory inspection.
- Perform live-memory search using correct Unicode encoding settings.
- Correlate process-level artifacts with credential handling behavior.
- Explain runtime-memory exposure risks in application security.

## Tools and Environment
- LastPass browser extension
- Keeper browser extension
- Process Explorer
- HxD memory viewer

## Procedure
1. Configured LastPass test data and identified extension process IDs in Process Explorer.
2. Opened target process memory in HxD and searched for known test credential strings in UTF-16 LE.
3. Configured Keeper test record and identified associated Firefox process via extension indicators.
4. Repeated UTF-16 memory search to locate defined test marker values.
5. Documented recovered in-memory indicators and interpreted security implications.

## Key Findings
- Credential-related strings were discoverable in extension process memory during active sessions.
- Process selection accuracy (extension-specific PID) was essential for successful recovery.
- UTF-16 LE search configuration was required for expected hits in memory.
- Keeper workflow exposed marker sequence (43 00 43 00) in runtime memory context.

## Conclusion
The lab demonstrates that secure storage alone is insufficient if sensitive values are exposed in runtime memory. Memory-focused analysis should be included in application security validation, especially for password-management and browser-extension ecosystems.

## References
- https://www.mdsec.co.uk/2022/10/analysing-lastpass-part-1/

## Evidence Screenshots
Key screenshots are embedded below. Full extracted set is available in assets/mdfs_lab_03_lastpass_and_keeper/

![[IMG-20260423202656249.png]]

![[IMG-20260423202656489.png]]

![[IMG-20260423202656949.png]]

![[IMG-20260423202657500.png]]

![[IMG-20260429201807230.png]]

![[IMG-20260429201807311.png]]

![[IMG-20260429201807487.jpg]]

![[IMG-20260423202656688.png]]

![[IMG-20260423202657263.png]]

![[IMG-20260423202657576.png]]

![[IMG-20260429201807232.png]]

![[IMG-20260429201807313.png]]
