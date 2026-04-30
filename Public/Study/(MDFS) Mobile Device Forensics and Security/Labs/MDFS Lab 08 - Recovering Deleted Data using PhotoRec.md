---
Title: "MDFS Lab 08 - Recovering Deleted Data using PhotoRec"
Status: Active
marker:
tags:
Date: 2026.04.23
Time: 01:21
---

# MDFS Lab 08 - Recovering Deleted Data using PhotoRec

Source file: K057_Tejas_Sahoo_MDSF LAB-8 - Recovering Deleted Data using PhotoRec.docx

## Student Details
- Name: tejas kamal sahoo
- Roll no: k057

## Aim
Recover deleted files from forensic disk images using PhotoRec and evaluate limitations of file-carving workflows.

## Learning Outcomes
- Understand file-carving based recovery in digital forensics.
- Configure PhotoRec for selective and broader file-type recovery.
- Compare simple and complex recovery scopes.
- Evaluate recovery quality and structural limitations.

## Tools and Environment
- PhotoRec
- disk.flag.img / android_sdcard.img style forensic image
- Forensic workstation environment

## Procedure
1. Executed simple recovery with restricted file-type options.
2. Executed complex recovery with expanded file signature set.
3. Collected outputs from recup_dir folders and categorized recovered types.
4. Reviewed recovered artifacts for potentially relevant textual indicators.
5. Compared output completeness between simple and complex runs.

## Key Findings
- Deleted multimedia and document artifacts were recoverable from image data.
- Complex configuration recovered wider file-type diversity than simple mode.
- Recovered outputs lacked original filename/folder structure due to carving process.
- Result quality depends strongly on overwrite state and filesystem behavior.

## Conclusion
PhotoRec-based carving successfully recovered deleted evidence candidates from disk images. The lab highlights both the strength of signature-based recovery and the practical limitation of metadata loss during reconstruction.

## Evidence Screenshots
Key screenshots are embedded below. Full extracted set is available in assets/mdfs_lab_08_recovering_deleted_data_using_photorec/

![[IMG-20260423202656254.png]]

![[IMG-20260423202656805.png]]

![[IMG-20260423202657368.png]]

![[IMG-20260427170152274.png]]

![[IMG-20260429201807241.png]]

![[IMG-20260429201807320.png]]

![[IMG-20260429201807663.png]]

![[IMG-20260429201808070.png]]

![[IMG-20260429201808389.png]]
