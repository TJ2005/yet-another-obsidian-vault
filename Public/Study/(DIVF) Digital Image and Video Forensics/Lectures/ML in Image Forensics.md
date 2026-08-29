---

Title: "ML in Image Forensics"

Status:

tags: [divf, unit-3]

Date: "2026.08.21"

---
# Machine Learning in Image Forensics

> [!INFO] Big picture
> ML has moved image forensics from manual inspection → automated detection. Traditional methods rely on hand-crafted features (noise, edges, metadata); ML/DL learns hidden manipulation patterns, detects sub-visible artifacts and scales to large investigations.

## Why forgery is easier now

| Enabler | Detail |
| --- | --- |
| **Traditional editing tools** | Photoshop, GIMP, CorelDraw — copy-paste (copy-move), splicing, retouching — little expertise needed |
| **AI-based image generators** | Text-to-image synthesis of photorealistic scenes |
| **Deepfake technology** | GANs + autoencoders — face swapping, lip-syncing, voice-video alignment |
| **Accessibility** | Free apps, mobile filters, online services — anyone can produce convincing fakes |

![[s159_img_28.png]]
*GPT-4o-class models can effortlessly create convincing fake passports and IDs.*

### Multi-factor identity verification — the necessary path forward

Instead of one forgeable piece of evidence, validate multiple independent factors simultaneously in a single session:

1. **User's device trust** — known/trusted device; passkeys cryptographically bind user to device
2. **Location & network context** — IP/GPS plausibility; flag VPN/proxy associated with fraud
3. **Advanced ID document validation** — remote forensic document analysis cross-referenced with trusted national databases (one factor, not the only factor)
4. **Simultaneous validation & orchestration** — spoofing one factor is feasible; faking trusted device + plausible location + passing document checks at once is significantly harder

![[s160_img_29.png]]

## Technique families

### 1. Supervised learning (classical)

- **Input:** handcrafted features — noise residuals, CFA inconsistencies, edge artifacts, DCT coefficients
- **Models:** SVM, k-NN, Random Forest, Logistic Regression → forged vs authentic
- **Applications:** copy-move detection, splicing detection, tampering localization

### 2. Deep learning

| Architecture | Forensic role |
| --- | --- |
| **CNNs** | Detect and localize manipulations |
| **RNNs / LSTMs** | Analyse video tampering over time |
| **Autoencoders** | Anomaly detection via reconstruction error |
| **GANs** | Both forgery *creation* and detection |

### 3. Noise and frequency domain analysis with ML

- **PRNU matching** — train models to match camera noise fingerprints against claimed source
- **DCT/DWT + ML classifiers** — transform to frequency domain; classify hidden inconsistencies invisible to the eye

### 4. Ensemble and hybrid models

Combine multiple detectors/models; fuse feature sets for robustness.

### 5. Transfer learning and pretrained models

Fine-tune networks pretrained on large vision datasets for forensic tasks with limited labelled data.

### 6. Adversarial learning (GAN-based forensics)

Adversarial training hardens detectors against evasion; GANs generate hard forgery examples.

### 7. Explainable AI (XAI)

- Models highlight **why** an image was predicted fake
- **Grad-CAM / SHAP** visualise suspicious regions (e.g., lighting mismatch)
- Critical for legal evidence transparency

### 8. Anomaly and outlier detection

- Works **without labelled data**
- Finds unusual noise/lighting/compression patterns
- Example: **One-Class SVM** flags an image whose statistical features deviate from genuine ones

## Applications

Legal & law enforcement · social media monitoring · deepfake detection · journalism & media verification · cybersecurity (steganography detection).

## Datasets

| Dataset | Content |
| --- | --- |
| **CASIA v1.0 / v2.0** | Spliced images |
| **Columbia Splicing Dataset** | Authentic vs tampered |
| **CoMoFoD** | Copy-move forgeries |
| **FaceForensics++** | Deepfake videos/images |
| **Wild Web Dataset** | Real-world tampered media |

## Challenges

- Increasing realism of GAN-based forgeries
- Adversarial attacks fool ML detectors
- Limited datasets for robust training
- **Generalization problem** — unseen manipulations may go undetected

## Future directions

Explainable AI for forensic transparency · multi-modal forensics (image + metadata + video) · federated learning across distributed sources without sharing sensitive data · AI–legal system collaboration.

## Related

- [[Forgery Detection Techniques]]
- [[Deepfake Detection]]
- [[DVIF Exam Glossary]]