---
Title: DFIR Lab 4
Status: Active
marker:
tags:
Date: 2026.04.25
Time: 00:00
---
[]()
# DFIR Lab 4
## MBR and GPT Analysis

> [!info] Submission Details
>
> **Name:** Tejas Sahoo  
> **Roll Number:** K057  
> **Subject:** Digital Forensics and Incident Response  
> **Branch:** B.Tech. Cyber Security, Semester 6  
> **Experiment No.:** 4

> [!abstract] Aim
>
> To analyze Master Boot Record and GUID Partition Table structures.

> [!tip] Title
>
> MBR and GPT Analysis

## Objective
This experiment focuses on how disks describe partitions and boot information, which matters during forensic acquisition and recovery.

## Tools and Environment
- Disk Management
- Hex/disk inspection concepts
- MBR structure notes
- GPT structure notes

## Theory
MBR stores boot code, a small partition table, and a boot signature in the first sector of a disk.
GPT is the newer partitioning scheme used with UEFI systems and supports larger disks, more partitions, and redundant partition metadata.

## Procedure
1. Reviewed the layout of MBR and GPT partition structures.
2. Compared BIOS/MBR and UEFI/GPT boot approaches.
3. Analyzed partition metadata and disk layout evidence.
4. Captured screenshots showing the analysis workflow.

## Observations
- MBR is limited to four primary partitions unless extended partitions are used.
- GPT improves reliability by storing backup partition information and CRC checks.

## Evidence

> [!example]- Page 2 Evidence
>
> ![[attachments/dfir/dfir-lab-04/lab-04-page-02-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-04/lab-04-page-02-image-02.png]]
>
> ![[attachments/dfir/dfir-lab-04/lab-04-page-02-image-03.png]]

> [!example]- Page 3 Evidence
>
> ![[attachments/dfir/dfir-lab-04/lab-04-page-03-image-01.png]]

> [!example]- Page 4 Evidence
>
> ![[attachments/dfir/dfir-lab-04/lab-04-page-04-image-01.png]]

> [!example]- Page 5 Evidence
>
> ![[attachments/dfir/dfir-lab-04/lab-04-page-05-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-04/lab-04-page-05-image-02.png]]

> [!example]- Page 6 Evidence
>
> ![[attachments/dfir/dfir-lab-04/lab-04-page-06-image-01.png]]

> [!example]- Page 7 Evidence
>
> ![[attachments/dfir/dfir-lab-04/lab-04-page-07-image-01.png]]

> [!example]- Page 8 Evidence
>
> ![[attachments/dfir/dfir-lab-04/lab-04-page-08-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-04/lab-04-page-08-image-02.png]]
>
> ![[attachments/dfir/dfir-lab-04/lab-04-page-08-image-03.png]]
>
> ![[attachments/dfir/dfir-lab-04/lab-04-page-08-image-04.png]]
>
> ![[attachments/dfir/dfir-lab-04/lab-04-page-08-image-05.png]]
>
> ![[attachments/dfir/dfir-lab-04/lab-04-page-08-image-06.png]]

## Result
MBR and GPT disk structures were compared and analyzed from a forensic perspective.

## Conclusion
Understanding partition structures helps investigators interpret disk images, recover partitions, and explain boot-related evidence.
