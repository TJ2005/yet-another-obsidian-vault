---
Title: DFIR Lab 7
Status: Active
marker:
tags:
Date: 2026.04.25
Time: 00:00
---

# DFIR Lab 7
## Ann's Rendezvous Case

> [!info] Submission Details
>
> **Name:** Tejas Sahoo  
> **Roll Number:** K057  
> **Subject:** Digital Forensics and Incident Response  
> **Branch:** B.Tech. Cyber Security, Semester 6  
> **Experiment No.:** 7

> [!abstract] Aim
>
> To recover email messages from packet capture and analyze the same.

> [!tip] Title
>
> Ann's Rendezvous Case

## Objective
This lab examines SMTP traffic in a packet capture to recover communications, credentials, attachments, and location clues.

## Case Context
Investigators captured Ann Dercover's network activity and need the packet evidence analyzed for communications with a possible contact.

## Tools and Environment
- Wireshark
- SMTP filters
- Packet stream reconstruction
- Exported objects/files

## Procedure
1. Opened the evidence packet capture in Wireshark.
2. Filtered for SMTP and related email traffic.
3. Followed TCP streams to reconstruct message content.
4. Looked for aliases, credentials, attachments, and location indicators.

## Observations
- Email content can often be reconstructed from unencrypted SMTP traffic.
- Network packets may reveal both message content and supporting metadata such as addresses and hosts.

## Evidence

> [!example]- Page 3 Evidence
>
> ![[attachments/dfir/dfir-lab-07/lab-07-page-03-image-01.jpg]]
>
> ![[attachments/dfir/dfir-lab-07/lab-07-page-03-image-02.jpg]]
>
> ![[attachments/dfir/dfir-lab-07/lab-07-page-03-image-03.jpg]]
>
> ![[attachments/dfir/dfir-lab-07/lab-07-page-03-image-04.jpg]]
>
> ![[attachments/dfir/dfir-lab-07/lab-07-page-03-image-05.jpg]]

> [!example]- Page 4 Evidence
>
> ![[attachments/dfir/dfir-lab-07/lab-07-page-04-image-01.jpg]]
>
> ![[attachments/dfir/dfir-lab-07/lab-07-page-04-image-02.jpg]]

> [!example]- Page 5 Evidence
>
> ![[attachments/dfir/dfir-lab-07/lab-07-page-05-image-01.jpg]]

> [!example]- Page 6 Evidence
>
> ![[attachments/dfir/dfir-lab-07/lab-07-page-06-image-01.jpg]]

## Result
SMTP evidence from the packet capture was inspected and relevant case artifacts were recovered.

## Conclusion
The lab shows how packet analysis can turn raw network traffic into useful investigative evidence.
