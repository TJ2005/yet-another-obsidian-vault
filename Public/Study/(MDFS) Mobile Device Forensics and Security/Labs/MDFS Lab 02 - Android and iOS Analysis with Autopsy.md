---
Title: "MDFS Lab 02 - Android and iOS Analysis with Autopsy"
Status: Active
marker:
tags:
Date: 2026.04.23
Time: 01:21
---

# MDFS Lab 02 - Android and iOS Analysis with Autopsy

## Student Details
- Name: tejas kamal sahoo
- Roll no: k057

## Aim
Perform logical forensic analysis of Android and iOS datasets using Autopsy and relevant mobile analyzers.

## Learning Outcomes
- Create forensic cases and import logical mobile data correctly.
- Use Android and iOS analyzers to extract relevant artifacts.
- Validate evidence integrity using hash checks before analysis.
- Answer evidence-driven investigation questions from artifacts.
- Document findings in a repeatable and forensically sound format.

## Tools and Environment
- Autopsy
- aLEAPP modules (Android Analyzer and iOS Analyzer)
- 7-Zip for dataset extraction
- Hash verification utilities

## Procedure
1. Downloaded Android and iOS forensic datasets and verified cryptographic hashes.
2. Created separate Autopsy cases for Android and iOS analysis.
3. Imported logical files and enabled only required mobile ingest modules.
4. Examined extracted artifacts including calls, messages, web history, Bluetooth, GPS, and notifications.
5. Captured answers for flagged investigation prompts and recorded evidence screenshots.

## Key Findings
- Android most recently installed app identified as com.u360mobile.usna.
- Android web activity included http://yahoo.com/ at the queried timestamp.
- iOS paired device evidence indicated Eli's Apple Watch.
- iOS evidence included phone number +15415005105 in the requested area code.
- Signal code and Snapchat-related notification artifacts were recoverable from dataset evidence.

## Conclusion
Autopsy-based logical analysis successfully recovered cross-platform mobile artifacts and answered investigation questions from both Android and iOS evidence. The exercise reinforces forensic discipline: integrity checks, targeted ingest, artifact validation, and clear documentation.

## References
- https://resources.infosecinstitute.com/topic/android-forensic-logical-acquisition/
- http://sleuthkit.org/autopsy/docs/user-docs/4.18.0/aleapp_page.html

## Evidence Screenshots
Key screenshots are embedded below. Full extracted set is available in assets/mdfs_lab_02_android_and_ios_analysis_with_autopsy/

![[IMG-20260423202656227.jpg]]

![[IMG-20260423202656421.jpg]]

![[IMG-20260423202657299.jpg]]

![[IMG-20260427170152283.jpg]]

![[IMG-20260429201807249.jpg]]

![[IMG-20260429201807416.jpg]]

![[IMG-20260429201807901.jpg]]

![[IMG-20260429201808203.jpg]]

![[IMG-20260429201808278.jpg]]

![[IMG-20260429201808554.jpg]]
