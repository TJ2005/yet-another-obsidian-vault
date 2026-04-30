---
Title: DFIR Lab 3
Status: Active
marker:
tags:
Date: 2026.04.25
Time: 00:00
---

# DFIR Lab 3
## Registry Analysis

> [!info] Submission Details
>
> **Name:** Tejas Sahoo  
> **Roll Number:** K057  
> **Subject:** Digital Forensics and Incident Response  
> **Branch:** B.Tech. Cyber Security, Semester 6  
> **Experiment No.:** 3

> [!abstract] Aim
>
> To analyze the registry of a Windows system.

> [!tip] Title
>
> Registry Analysis

## Objective
This lab studies the Windows Registry as a forensic artifact source for system configuration, user activity, installed software, and persistence clues.

## Tools and Environment
- Windows Registry Editor
- Command Prompt
- Registry hives
- Windows forensic artifact notes

## Theory
The Windows Registry is a hierarchical database that stores operating system, hardware, application, and user configuration data.
Registry hives such as HKLM, HKCU, HKCR, HKU, and HKCC can reveal installed programs, recent activity, user preferences, and system-level settings.

## Procedure
1. Opened Registry Editor using the `regedit` command.
2. Explored major registry hives and noted their purpose.
3. Inspected selected keys and values relevant to Windows activity.
4. Captured evidence screenshots while navigating the registry structure.

## Observations
- Registry values can connect activity to a user profile or machine-wide configuration.
- Registry analysis is useful, but careless modification can affect the system, so investigation should be read-only wherever possible.

## Evidence

> [!example]- Page 6 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-06-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-06-image-02.jpg]]

> [!example]- Page 7 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-07-image-01.jpg]]
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-07-image-02.jpg]]

> [!example]- Page 8 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-08-image-01.jpg]]
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-08-image-02.jpg]]

> [!example]- Page 9 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-09-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-09-image-02.png]]

> [!example]- Page 10 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-10-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-10-image-02.png]]

> [!example]- Page 11 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-11-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-11-image-02.png]]

> [!example]- Page 12 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-12-image-01.png]]

> [!example]- Page 13 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-13-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-13-image-02.jpg]]

> [!example]- Page 14 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-14-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-14-image-02.png]]

> [!example]- Page 15 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-15-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-15-image-02.png]]

> [!example]- Page 16 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-16-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-16-image-02.png]]

> [!example]- Page 17 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-17-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-17-image-02.png]]

> [!example]- Page 18 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-18-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-18-image-02.png]]

> [!example]- Page 19 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-19-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-19-image-02.png]]

> [!example]- Page 20 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-20-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-20-image-02.png]]

> [!example]- Page 21 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-21-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-21-image-02.png]]

> [!example]- Page 22 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-22-image-01.png]]

> [!example]- Page 23 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-23-image-01.png]]

> [!example]- Page 24 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-24-image-01.png]]

> [!example]- Page 25 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-25-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-25-image-02.png]]

> [!example]- Page 26 Evidence
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-26-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-03/lab-03-page-26-image-02.png]]

## Result
Windows Registry structure and forensic relevance were analyzed through practical navigation.

## Conclusion
The Registry is an important source of DFIR evidence because it records configuration and user activity that may support incident timelines.
