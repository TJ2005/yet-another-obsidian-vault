---

Title: "DIVF Lab 2"

Status:

marker:

tags:

Date: "2026.08.19"

---
# Digital Image and Video Forensics – Practical 2

## Title

Image Tamper Detection using FotoForensics and Ghiro

## Objective

To detect image tampering and analyze forensic evidence using Error Level Analysis (ELA), metadata inspection, and automated forensic analysis. This practical introduces students to two commonly used image forensics tools: FotoForensics (online) and Ghiro (offline).

## Tools Required

- FotoForensics (https://fotoforensics.com/)
- Ghiro (https://getghiro.org/)
- Sample tampered and original images (spliced, copy-pasted, cropped, edited)

---

# Part A: Using FotoForensics (Online Tool)

1. Visit https://fotoforensics.com
2. Click Upload File and select a tampered image file.

![[Lab 2/attachments/img_1.png]]

3. After the image loads, observe the Error Level Analysis (ELA).
4. Note anomalies such as inconsistent compression, bright outlines, or patchy blocks.

![[Lab 2/attachments/img_2.png]]

5. Scroll down and examine metadata fields:
   - Camera make/model
   - Timestamp
   - Software used

![[Lab 2/attachments/img_3.png]]

6. Repeat with an original image and compare results.

![[Lab 2/attachments/img_4.png]]

![[Lab 2/attachments/img_5.png]]

7. Take a screenshot of the ELA and metadata analysis for submission.

---

# Part B: Using Ghiro (Offline Tool)

1. Open Ghiro Web Interface https://getghiro.org/

![[Lab 2/attachments/img_6.png]]

2. Log in with your credentials (admin or user)
3. Create a New Case (e.g., "Tamper Test 01")

![[Lab 2/attachments/img_7.png]]

4. Upload image files (original and tampered versions)

![[Lab 2/attachments/img_8.png]]

5. Let Ghiro automatically analyze them.
6. View results for each image:
   - EXIF Metadata
   - Signature analysis
   - Tampering clues (edited using software, thumbnail mismatch, etc.)
   - Hash values (MD5, SHA1, SHA256)

![[Lab 2/attachments/img_9.png]]

![[Lab 2/attachments/img_10.png]] ![[Lab 2/attachments/img_11.png]] ![[Lab 2/attachments/img_12.png]]

![[Lab 2/attachments/img_13.png]]

![[Lab 2/attachments/img_14.png]]

Tampered image

![[Lab 2/attachments/img_15.png]]

![[Lab 2/attachments/img_16.png]]

![[Lab 2/attachments/img_17.png]]

![[Lab 2/attachments/img_18.png]]

![[Lab 2/attachments/img_19.png]]

![[Lab 2/attachments/img_20.png]]

7. Export or screenshot the forensic report for submission.

Attached as html exports from Ghiro along with submission

---

# Expected Outcome

- Students will be able to visually interpret ELA results.
- Learn how to correlate metadata and file structure changes with potential manipulation.
- Understand how tools like Ghiro automate and validate image forensic investigations.

# Submission

- Submit at least one screenshot from FotoForensics showing ELA result.
- Submit at least one screenshot/report from Ghiro analysis.
- Complete the Observation Table for a minimum of 3 images.
- Mention any interesting findings (e.g., edited image software, GPS tampering).

# Note

This practical builds on foundational skills in media forensics. Being able to detect tampering is essential in digital evidence authentication for law enforcement, journalism, and cybercrime investigations.

## Attached Reports

- [[Lab 2/GHIRO-original-html-report.htm|GHIRO-original-html-report.htm]]
- [[Lab 2/GHIRO-tampered-html-report.htm|GHIRO-tampered-html-report.htm]]