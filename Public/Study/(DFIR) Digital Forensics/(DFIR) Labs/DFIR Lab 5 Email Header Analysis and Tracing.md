---
Title: DFIR Lab 5
Status: Active
marker:
tags:
Date: 2026.04.25
Time: 00:00
---

# DFIR Lab 5
## Email Header Analysis and Tracing

> [!info] Submission Details
>
> **Name:** Tejas Sahoo  
> **Roll Number:** K057  
> **Subject:** Digital Forensics and Incident Response  
> **Branch:** B.Tech. Cyber Security, Semester 6  
> **Experiment No.:** 5

> [!abstract] Aim
>
> To analyze an email header and trace it to the source.

> [!tip] Title
>
> Email Header Analysis and Tracing

## Objective
This lab studies email metadata so suspicious messages can be traced, authenticated, and evaluated for spoofing or phishing indicators.

## Tools and Environment
- Email header viewer
- MXToolbox-style header analyzer
- IP lookup tools
- WHOIS/DNS references

## Theory
Email headers contain routing metadata added by mail servers as a message travels from sender to recipient.
Fields such as Received, From, Return-Path, Message-ID, SPF, DKIM, and DMARC help assess origin and authenticity.

## Procedure
1. Collected the full email header from the sample message.
2. Inspected sender, recipient, date, subject, return path, and received lines.
3. Traced the routing path using server and IP information.
4. Checked for mismatches that may indicate spoofing or phishing.

## Observations
- The visible From address alone is not reliable evidence of sender identity.
- Received lines and authentication results provide stronger clues about the actual message path.

## Evidence

> [!example]- Page 4 Evidence
>
> ![[attachments/dfir/dfir-lab-05/lab-05-page-04-image-01.png]]

> [!example]- Page 5 Evidence
>
> ![[attachments/dfir/dfir-lab-05/lab-05-page-05-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-05/lab-05-page-05-image-02.png]]

> [!example]- Page 6 Evidence
>
> ![[attachments/dfir/dfir-lab-05/lab-05-page-06-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-05/lab-05-page-06-image-02.png]]

> [!example]- Page 8 Evidence
>
> ![[attachments/dfir/dfir-lab-05/lab-05-page-08-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-05/lab-05-page-08-image-02.png]]

> [!example]- Page 10 Evidence
>
> ![[attachments/dfir/dfir-lab-05/lab-05-page-10-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-05/lab-05-page-10-image-02.png]]

> [!example]- Page 11 Evidence
>
> ![[attachments/dfir/dfir-lab-05/lab-05-page-11-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-05/lab-05-page-11-image-02.png]]
>
> ![[attachments/dfir/dfir-lab-05/lab-05-page-11-image-03.png]]

> [!example]- Page 12 Evidence
>
> ![[attachments/dfir/dfir-lab-05/lab-05-page-12-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-05/lab-05-page-12-image-02.png]]

> [!example]- Page 13 Evidence
>
> ![[attachments/dfir/dfir-lab-05/lab-05-page-13-image-01.png]]
>
> ![[attachments/dfir/dfir-lab-05/lab-05-page-13-image-02.png]]

## Result
The email header was analyzed and the message path was traced using metadata fields.

## Conclusion
Email header analysis is a practical DFIR technique for validating message origin and identifying phishing indicators.
