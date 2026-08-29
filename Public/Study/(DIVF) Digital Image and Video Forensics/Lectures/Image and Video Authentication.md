---

Title: "Image and Video Authentication"

Status:

tags: [divf, unit-2]

Date: "2026.08.21"

---
# Image and Video Authentication

> [!INFO] Unit 2
> Authentication answers two questions: *where did this media come from* (**source**) and *has it been altered* (**content**).

## Source vs content authentication

| Type | Question answered |
| --- | --- |
| **Source authentication** | Which device/software produced the file? |
| **Content authentication** | Has the media been modified since capture? |

## Verification techniques

### Hash value analysis

- Compute a cryptographic fingerprint — e.g., **SHA-256**
- Compare against a known-good reference hash
- Any single-bit change → completely different hash
- Tool: **HashCalc**

### Hex encoding

- Raw byte-level view of the file
- Reveals true format, hidden appended data, header anomalies

### Error Level Analysis (ELA)

- Re-compresses the image at a uniform quality; measures per-region error
- Originally-saved areas show similar error levels; re-edited regions stand out

### Hex editor analysis

- Tools: **HxD**, **Hex Fiend**
- Inspect headers/footers, metadata blocks, embedded thumbnails, trailing data after EOF markers

### Metadata consistency checks

- Tools: **ExifTool**, **MediaInfo**
- Cross-check creation/modification times, camera model, GPS, software tags against the claimed provenance — contradictions indicate tampering

## Case study: disputed footage

Typical forensic tasks on a disputed video/image:

1. Verify file integrity via hash comparison
2. Inspect hex structure for anomalies
3. Run ELA for localized edits
4. Audit metadata consistency
5. Assess enhancement history and chain of custody

**Limitations:** social-media re-encoding strips metadata; repeated compression destroys error-level cues; absence of evidence is not proof of authenticity.

## Related

- [[Images and Videos as Legal Evidence]]
- [[Image Forgery Types]]
- [[Forgery Detection Techniques]]
- [[DVIF Exam Glossary]]