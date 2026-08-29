---

Title: "Video Processing and Analytics"

Status:

tags: [divf, unit-1]

Date: "2026.08.21"

---
# Video Processing and Analytics

> [!INFO] Scope
> How video degrades, how it is categorised, and the algorithm families used to analyse it.

## Technical issues in video recordings

- **Packet loss**
- **Bitrate fluctuations**
- **Frame freezing or skipping**
- **Synchronisation issues**

## Visual distortions and artefacts

![[s39_img_3.jpg]]

| Artefact | Cause |
| --- | --- |
| **Compression artefacts** (blockiness, blurring) | Lossy coding |
| **Noise** | Low-light or analog recordings |
| **Motion blur** | Movement during exposure |
| **Lens flare and reflections** | Optics |
| **Colour banding** | Insufficient bit depth / gradient compression |

## Video quality evaluation metrics

Objective and subjective measures of delivered quality (see [[DVIF Exam Glossary]]).

## Categories of digital videos

| Basis | Types |
| --- | --- |
| **Camera placement** | Fixed vs mobile viewpoints |
| **Mode of capture** | Continuous vs event-triggered recording |
| **Environmental conditions** | Indoor/outdoor, lighting, weather |

## Video analytics algorithms

| Family | Techniques |
| --- | --- |
| **Detection & recognition** | Object/person/face detection and recognition |
| **Tracking** | **Kalman filter, SORT, Deep SORT** — track objects across frames |
| **Scene understanding** | ![[s48_img_4.jpg]] **Action recognition** (walking, fighting); **anomaly detection** (unusual behaviour in surveillance) |
| **Post-processing** | ![[s50_img_5.jpg]] Refinement of analytic output |

## Related

- [[Image Processing Techniques]]
- [[Images and Videos as Legal Evidence]]
- [[DVIF Exam Glossary]]