---
Title: DFIR Lab 9
Status: Active
marker:
tags:
Date: 2026.04.25
Time: 00:00
---

# DFIR Lab 9
## Data Leak Case - Part 2

> [!info] Submission Details
>
> **Name:** Tejas Sahoo  
> **Roll Number:** K057  
> **Subject:** Digital Forensics and Incident Response  
> **Branch:** B.Tech. Cyber Security, Semester 6  
> **Experiment No.:** 9

> [!abstract] Aim
>
> To analyze a data leak case using forensic artifacts.

> [!tip] Title
>
> Data Leak Case - Part 2

## Objective
This lab continues the data leak investigation by using Autopsy and artifact review to connect user behavior with possible confidential data movement.

## Case Context
A company employee is suspected of leaking sensitive technology data through cloud storage and removable media.

## Tools and Environment
- Autopsy
- Forensic image
- File metadata review
- Timeline analysis
- USB/CD artifact review

## Procedure
1. Loaded the provided evidence into Autopsy.
2. Reviewed user activity, file access, and removable-media indicators.
3. Searched for confidential files, transfer traces, and communication artifacts.
4. Captured evidence supporting the investigation questions.

## Observations
- Data leak cases require timeline correlation across files, devices, and communications.
- Removable media and cloud artifacts can show intent, access, and possible exfiltration paths.

## Evidence

> [!example]- Page 2 Evidence
>
> ![[attachments/dfir/dfir-lab-09/lab-09-page-02-image-01.jpg]]
>
> ![[attachments/dfir/dfir-lab-09/lab-09-page-02-image-02.jpg]]
>
> ![[attachments/dfir/dfir-lab-09/lab-09-page-02-image-03.jpg]]
>
> ![[attachments/dfir/dfir-lab-09/lab-09-page-02-image-04.jpg]]

> [!example]- Page 3 Evidence
>
> ![[attachments/dfir/dfir-lab-09/lab-09-page-03-image-01.jpg]]
>
> ![[attachments/dfir/dfir-lab-09/lab-09-page-03-image-02.jpg]]

> [!example]- Page 4 Evidence
>
> ![[attachments/dfir/dfir-lab-09/lab-09-page-04-image-01.jpg]]
>
> ![[attachments/dfir/dfir-lab-09/lab-09-page-04-image-02.jpg]]
>
> ![[attachments/dfir/dfir-lab-09/lab-09-page-04-image-03.jpg]]

> [!example]- Page 5 Evidence
>
> ![[attachments/dfir/dfir-lab-09/lab-09-page-05-image-01.jpg]]
>
> ![[attachments/dfir/dfir-lab-09/lab-09-page-05-image-02.png]]
>
> ![[attachments/dfir/dfir-lab-09/lab-09-page-05-image-03.jpg]]

> [!example]- Page 6 Evidence
>
> ![[attachments/dfir/dfir-lab-09/lab-09-page-06-image-01.jpg]]
>
> ![[attachments/dfir/dfir-lab-09/lab-09-page-06-image-02.jpg]]

> [!example]- Page 7 Evidence
>
> ![[attachments/dfir/dfir-lab-09/lab-09-page-07-image-01.jpg]]

> [!example]- Page 8 Evidence
>
> ![[attachments/dfir/dfir-lab-09/lab-09-page-08-image-01.jpg]]

## Result
Part 2 of the data leak case was analyzed and the relevant forensic artifacts were documented.

## Conclusion
The experiment highlights the importance of correlating multiple artifacts before making claims about insider data leakage.
