---
Title: "MDFS Lab 06 - Logical Data Extraction using Andriller"
Status: Active
marker:
tags:
Date: 2026.04.23
Time: 01:21
---

# MDFS Lab 06 - Logical Data Extraction using Andriller

Source file: K057_MDSF LAB-6 - Logical Data Extraction using Andriller.pdf

## Student Details
- Name: tejas kamal sahoo
- Roll no: k057

## Aim
Perform logical acquisition from an Android emulator using Andriller and analyze extracted communication artifacts.

## Learning Outcomes
- Prepare emulator evidence state for forensic extraction.
- Enable debug and ADB-based connectivity for acquisition.
- Run full logical extraction workflow in Andriller.
- Interpret extracted SMS, call, and contact artifacts.

## Tools and Environment
- Andriller (Free Version)
- Android Studio Emulator
- ADB
- HTML/CSV report export

## Procedure
1. Launched emulator and verified seeded test artifacts.
2. Enabled Developer Options and USB debugging in emulator.
3. Validated ADB connectivity using adb devices.
4. Executed Andriller full analysis and selected report output format.
5. Reviewed generated report artifacts and mapped key database sources.

## Key Findings
- SMS artifacts recovered from mmssms.db.
- Call log artifacts recovered from calllog.db.
- Contact artifacts recovered from contacts2.db.
- Device metadata extracted and preserved in report output.

## Conclusion
Logical extraction with Andriller produced consistent communication and metadata evidence from the emulator environment. The workflow demonstrates a practical and repeatable acquisition process suitable for introductory mobile forensic investigations.

## Evidence Screenshots
Key screenshots are embedded below. Full extracted set is available in assets/mdfs_lab_06_logical_data_extraction_using_andriller/

![[IMG-20260423202656249.png]]

![[IMG-20260423202656688.png]]

![[IMG-20260423202657263.png]]

![[IMG-20260427170152265.jpg]]

![[IMG-20260429201807232.png]]

![[IMG-20260429201807313.png]]

![[IMG-20260427170152276.png]]

![[IMG-20260429201807248.png]]

![[IMG-20260429201807594.png]]

![[IMG-20260429201808014.png]]
