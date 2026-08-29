---

Title: "Forgery Detection Techniques"

Status:

tags: [divf, unit-3]

Date: "2026.08.21"

---
# Forgery Detection Techniques

> [!INFO] Unit 3
> Three families of forgery detection: **active** (embedded data), **passive/blind** (content-only analysis) and **hybrid** (fusion). Plus the per-artifact toolbox used before them.

## Artifact-level techniques

| Technique | Detects |
| --- | --- |
| **Metadata analysis** | Editing-software traces, timestamp inconsistencies |
| **Error Level Analysis (ELA)** | Regions saved at different compression error levels |
| **Clone detection** | Duplicated regions — block-based matching; keypoint methods (**SIFT, SURF, ORB**) with rotation/scaling invariance |
| **Noise & sensor analysis** | **PRNU** fingerprint mismatches between regions/devices |
| **Lighting & shadow analysis** | Physically impossible light directions/intensities |
| **Frequency domain analysis** | Periodic interpolation/resampling artifacts (Fourier, Radon) |
| **Deep learning detection** | CNNs, autoencoders, GAN-discriminators trained on FaceForensics++, CASIA, NIST Nimble |

### Tools

- **Izitru** — verifies whether a JPEG was saved by the original camera
- **JPEGsnoop** — compression signature and quantization-table inspection
- **Forensically** — clone detection, ELA, metadata analysis in one web tool; quick forensic analysis for non-technical users

> [!TIP] Deepfakes
> Deepfake-specific detection (blink, lip-sync, temporal coherence) has its own note → [[Deepfake Detection]]

## 1. Active detection techniques

Methods relying on information **embedded at creation time**, verified later.

- **Digital watermarking** — invisible/visible marks embedded in image data, verifiable without altering appearance
- **Digital signatures** — cryptographic proof of integrity and source authenticity

| Advantages | Limitations |
| --- | --- |
| High reliability if watermark/signature intact | Requires pre-processing before distribution |
| Direct proof of authenticity | Not applicable to legacy images without embedded data |

### Digital watermarking

A secret mark concealed in the host multimedia creates the watermarked image, communicated through a physical transmission channel.

![[s132_img_22.png]]
*Embedding → transmission → detection pipeline.*

#### Attacks on watermarks

| Type | Attack | Mechanism |
| --- | --- | --- |
| **Unintentional** | Compression | JPEG/JPEG2000 discard less-important components carrying the mark |
| | Filtering | Attenuates high-frequency components where watermarks live |
| | Volumetric transformations | Histogram spreading/equalization, gamma — brightness remapping degrades the mark |
| | Noise | Masks watermark signal, disturbs detection |
| | Geometric transformations | Translation/rotation/scaling/cropping/**StirMark** — mark survives but becomes undetectable (desynchronization) |
| **Intentional** | Cryptographic attack | Exhaustive key search against watermark algorithms — computationally expensive, rare |
| | Protocol attack | Creates ownership ambiguity — invertible operations (subtract then claim ownership), copy attacks (transplant a watermark between documents) |

Modern schemes use **deep learning-based watermarking** for robustness against these attacks.

## 2. Passive (blind) detection techniques

No prior embedded information — analyse content itself for manipulation-induced anomalies.

| Analysis | What it checks |
| --- | --- |
| **Pixel-level** | Noise inconsistencies, residual noise, unusual edge artifacts, local colour/texture variations |
| **Format-based** | Double JPEG compression, blocking effects |
| **Physical-based** | Lighting, shadows, reflections inconsistent with scene physics |
| **Camera-based** | **PRNU** sensor-noise pattern tampering |

| Advantages | Limitations |
| --- | --- |
| Works on any image/video without prior knowledge | Sensitive to image quality and compression |
| Effective across wide manipulation range | False positives on complex images |

### Pixel-level details

Tampered regions show local noise statistics incompatible with a single camera processing chain. Residual noise after demosaicing + JPEG compression is *correlated*, creating medium-sized noise spots that differ across splice boundaries.

### Format-based details

![[s145_img_23.png]]
*Lossy JPEG compression — block structure.*

![[s146_img_24.png]]
*Dataset samples: (a) original, (b) median-filtered, (c) JPEG-compressed, (d) AWGN-added, (e) mean-filtered.*

### Physical-based details

![[s147_img_25.png]]
*Shadow direction vs claimed light source.*

### Camera-based details

**PRNU analysis** identifies the source device by extracting its unique fingerprint — subtle manufacturing imperfections of the sensor — and checking consistency across the whole image.

![[s148_img_26.png]]

## 3. Hybrid detection techniques

- Combine active + passive elements
- Use embedded information when available, supplemented by passive analysis
- Employ ML/AI to fuse multiple feature sets → increased robustness

## Related

- [[Image Forgery Types]]
- [[ML in Image Forensics]]
- [[Deepfake Detection]]
- [[DVIF Exam Glossary]]