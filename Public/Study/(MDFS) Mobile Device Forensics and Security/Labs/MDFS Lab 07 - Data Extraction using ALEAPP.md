---
Title: "MDFS Lab 07 - Data Extraction using ALEAPP"
Status: Active
marker:
tags:
Date: 2026.04.23
Time: 01:21
---

# MDFS Lab 07 - Data Extraction using ALEAPP

Source file: K057_TejasSahoo_MDSF LAB-7 - Data Extraction using ALEAPP.pdf

## Student Details
- Name: tejas kamal sahoo
- Roll no: k057

## Aim
Analyze an Android filesystem dataset using ALEAPP to recover communication, browsing, and network artifacts.

## Learning Outcomes
- Run ALEAPP on a logical Android dataset.
- Interpret artifacts across SMS, call logs, browser, WhatsApp, and Wi-Fi data.
- Correlate timestamps to reconstruct user activity timeline.
- Identify potentially suspicious indicators from multi-source evidence.

## Tools and Environment
- Python 3.x
- ALEAPP
- Android dataset containing telephony, browser, app, and Wi-Fi files

## Procedure
1. Prepared dataset and ALEAPP runtime environment.
2. Executed ALEAPP with input dataset and report output directory.
3. Opened generated HTML report and navigated artifact categories.
4. Extracted key fields from SMS, call logs, browser history, WhatsApp messages, and Wi-Fi profiles.
5. Correlated extracted timestamps to produce event narrative.

## Key Findings
- Recovered SMS conversations with multiple phone numbers and contextual message content.
- Call logs included outgoing, incoming, and missed events with durations.
- Browser history contained high-risk entry: http://darkwebmarket.onion.
- WhatsApp message entries confirmed parallel chat activity.
- Wi-Fi profile data showed Cafe_WiFi connection around 2024-03-12 19:22:01.

## Conclusion
ALEAPP enabled structured artifact recovery across multiple Android data domains. Cross-artifact correlation provided a coherent behavioral timeline and demonstrated how dataset-level extraction supports forensic reconstruction.

## Evidence Screenshots
Key screenshots are embedded below. Full extracted set is available in assets/mdfs_lab_07_data_extraction_using_aleapp/

![[IMG-20260423202656249.png]]

![[IMG-20260423202656688.png]]

![[IMG-20260423202657263.png]]

![[IMG-20260427170152276.png]]

![[IMG-20260429201807248.png]]

![[IMG-20260429201807326.png]]

![[IMG-20260429201807716.png]]

![[IMG-20260429201808128.png]]

![[IMG-20260429201807594.png]]

![[IMG-20260429201808138.png]]
