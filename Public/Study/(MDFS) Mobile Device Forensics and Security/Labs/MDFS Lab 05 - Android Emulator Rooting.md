---
Title: "MDFS Lab 05 - Android Emulator Rooting"
Status: Active
marker:
tags:
Date: 2026.04.23
Time: 01:21
---

# MDFS Lab 05 - Android Emulator Rooting

Source file: K057_Tejas_Sahoo_MDSF LAB-5 - Android Emulator Rooting.pdf

## Student Details
- Name: tejas kamal sahoo
- Roll no: k057

## Aim
Set up Android emulators for security testing and demonstrate the difference between normal-user and rooted execution contexts.

## Learning Outcomes
- Create Android Virtual Devices (AVDs) for forensic/security experiments.
- Configure emulator storage and connectivity settings.
- Use ADB to validate device communication.
- Obtain and verify root shell access in controlled environments.

## Tools and Environment
- Android Studio
- Android Emulator (Google Play and non-Play system images)
- ADB
- Qute Terminal Emulator

## Procedure
1. Installed Android Studio and created baseline emulator configurations.
2. Built Google Play-enabled AVD for standard user-mode behavior.
3. Built separate x86/non-Play image for root-capable testing workflow.
4. Connected via ADB and validated device visibility.
5. Opened shell with adb shell and executed su to confirm root context.
6. Collected command outputs (for example uname/ps) as operational evidence.

## Key Findings
- ADB connectivity confirmed stable emulator-device communication.
- Root access was successfully obtained only in appropriate emulator configuration.
- System-level visibility increased in root shell compared with user mode.
- The setup is suitable for controlled malware/forensic lab validation.

## Conclusion
The exercise clearly separated standard Android runtime behavior from rooted forensic testing behavior. Controlled emulator rooting provides a repeatable environment for security research and artifact extraction without modifying physical devices.

## Evidence Screenshots
Key screenshots are embedded below. Full extracted set is available in assets/mdfs_lab_05_android_emulator_rooting/

![[IMG-20260423202656249.png]]

![[IMG-20260423202656555.jpg]]

![[IMG-20260423202656688.png]]

![[IMG-20260423202657263.png]]

![[IMG-20260423202657576.png]]

![[IMG-20260427170152276.png]]

![[IMG-20260429201807248.png]]

![[IMG-20260429201807326.png]]

![[IMG-20260429201807594.png]]

![[IMG-20260423202659396.jpg]]

![[IMG-20260423202659410.jpg]]

![[IMG-20260429201808138.png]]
