---

Title: "Deepfake Detection"

Status:

tags: [divf, unit-4]

Date: "2026.08.21"

---
# Deepfake Detection

> [!INFO] Unit 4
> **Deepfakes** are AI-generated synthetic media — realistic fake faces/videos produced with GANs and autoencoders. Detection focuses on **biological and temporal inconsistencies**.

## Risks

- **Fake news and information** — synthetic media presented as authentic reporting
- **Political agenda**
	- Fabricating events and statements — politicians shown saying/doing things they never did → rumours, discrediting, public unrest
	- Influencing election outcomes — strategic release before debunking; low-quality **cheapfakes** (manipulated but not AI-generated) serve the same purpose
	- Personalizing disinformation — targeted campaigns per voter demographic
	- Driving polarization — algorithms amplify emotionally charged deepfakes, reinforcing beliefs and dividing society
	- Inciting violence and unrest — fabricated inflammatory statements trigger real-world harm

### Mechanisms of incitement

- Fabricated evidence of world leaders burning religious texts or advocating violence → riots, targeted attacks
- Deployment just before elections → voter confusion, manipulated sentiment
- Extremist recruitment — legitimising grievances with fabricated proof of conspiracies/government wrongdoing

### Recent examples

| Year | Case |
| --- | --- |
| 2025 | India-Pakistan conflict — AI video of Pakistan PM Shehbaz Sharif falsely conceding defeat |
| 2024 | US election — deepfaked audio of VP Kamala Harris (poaching accusation video) |
| 2024 | New Hampshire primary — robocall with deepfaked Biden audio urging voters to stay home |
| 2024 | Indian elections — BJP used AI-generated Manoj Tiwari videos criticising opponents in multiple languages |

## Creation

Powered by **GANs and autoencoders**: an encoder maps faces to a shared latent space; decoders swap identities frame-by-frame; lip-sync and voice-video alignment models complete the illusion.

## Detection approaches

Principle — exploit what synthesis still gets wrong:

| Technique | Signal |
| --- | --- |
| **Facial landmark tracking** | Unnatural movements |
| **Blink detection** | Deepfakes often miss blinking |
| **Lip-sync analysis** | Audio-video mismatch |
| **Temporal coherence** | Frame-to-frame inconsistency |

### Image techniques
Artifact-level cues — blending boundaries, colour mismatch, frequency-domain fingerprints of generated content.

### Video techniques
Temporal analysis across frames — flickering identity, unstable landmarks, inconsistent head pose dynamics.

### ML approaches
CNN/GAN-discriminator classifiers on face crops; temporal models (RNN/LSTM) over landmark sequences; trained on benchmark corpora.

### Tools
Microsoft Video Authenticator · Deepware Scanner · FaceForensics++ models.

## Datasets

**FaceForensics++** (deepfake videos/images) is the standard benchmark; see [[ML in Image Forensics]] for the full dataset table.

## Future

Multi-modal detection (visual + audio + metadata), provenance standards (C2PA-style content credentials), continuous arms-race adaptation as generation quality improves.

## Case studies

Covered in lecture — political deepfakes above are the primary case material.

## Related

- [[ML in Image Forensics]]
- [[Forgery Detection Techniques]]
- [[DVIF Exam Glossary]]