---

Title: "DVIF Exam Glossary"

Status:

tags: [divf, unit-1, unit-2, unit-3, unit-4]

Date: "2026.08.21"

---
# DVIF Exam Glossary

> [!ABSTRACT] How to use
> Fixed, objective definitions for exam answers. Grouped by unit; each entry is self-contained.

## Unit 1 — Evidence & fundamentals

| Term | Definition |
| --- | --- |
| **Admissibility** | Whether evidence may be accepted in court — determined by relevance, authenticity and absence of undue prejudice |
| **Relevance** | The evidence must prove or disprove a fact at issue in the case |
| **Authenticity** | The evidence must be shown to be what it claims to be — unmanipulated and correctly attributed |
| **Chain of custody** | Documented record of evidence handling from collection to courtroom, proving integrity |
| **Forensic imaging** | Creating a bit-for-bit copy so analysis never alters the original |
| **Locard's Exchange Principle** | Every interaction with a system leaves a trace linking actor to action/device |
| **Hash value** | Fixed-length fingerprint of a file (e.g., SHA-256); any change alters it — used to verify integrity |
| **Metadata** | Data about the file — timestamps, camera settings, software used — analysed for consistency |
| **Steganography** | Hiding data inside media; detection is a forensic analysis technique |
| **Semantic segmentation** | Assigns a class label to every pixel; all pixels of one class treated identically |
| **Instance segmentation** | Additionally distinguishes individual objects of the same class |
| **Panoptic segmentation** | Combines semantic + instance — class labels AND individual object boundaries |
| **Histogram equalization** | Redistributes pixel intensities for a uniform histogram — improves global contrast |
| **Lossy compression** | Permanently discards information (JPEG); smaller files, unrecoverable quality loss |
| **Lossless compression** | Original perfectly reconstructable (PNG) |
| **Image synthesis** | Computational generation/modification of images — e.g., texture synthesis, GAN generation |
| **Feature extraction** | Transforming raw pixels into compact descriptors (edges, corners, histograms) preserving discriminative info |
| **Image restoration** | Objective, model-driven recovery of degraded images (deblurring, denoising) — vs subjective enhancement |
| **Morphological processing** | Structure-modifying operations using structuring elements: erosion, dilation, opening, closing |

## Unit 2 — Processing & analytics

| Term | Definition |
| --- | --- |
| **Packet loss** | Data units lost in transit — causes corruption/freezing in streamed video |
| **Bitrate fluctuation** | Variable data rate causing uneven video quality |
| **Motion blur** | Smearing from subject/camera movement during exposure |
| **Colour banding** | Visible steps in gradients due to insufficient bit depth |
| **Kalman filter** | Recursive estimator predicting object state (position/velocity) for tracking |
| **SORT / Deep SORT** | Online tracking algorithms; Deep SORT adds deep-appearance descriptors to reduce ID switches |
| **Action recognition** | Classifying activities (walking, fighting) in video sequences |
| **Anomaly detection** | Flagging unusual behaviour/patterns deviating from learned normality |
| **Source authentication** | Verifying which device produced the media |
| **Content authentication** | Verifying the media has not been altered since creation |
| **Hex encoding/editor analysis** | Inspecting raw bytes (HxD, Hex Fiend) for hidden headers, appended data, format anomalies |
| **Error Level Analysis (ELA)** | Highlights regions re-saved at different compression error levels — tampered areas stand out |

## Unit 3 — Manipulation & forgery

| Term | Definition |
| --- | --- |
| **Splicing** | Combining parts of two or more images into one composite |
| **Copy-move (cloning) forgery** | Pasting a region copied within the same image to hide/duplicate content |
| **Object removal / inpainting** | Erasing objects by filling from surrounding context |
| **Resampling** | Geometric transformation (rotation/scaling/skew) with interpolation — leaves periodic artifacts |
| **CFA (Colour Filter Array)** | Sensor colour-sampling pattern; spliced regions break its regularity |
| **Demosaicing** | Reconstructing full colour from CFA samples; creates correlated residual noise |
| **Frame insertion/deletion/replacement** | Frame-level video tampering types |
| **Pristine frame** | Untouched original frame |
| **Double-compressed frame** | Frame compressed twice without tampering |
| **Tampered frame** | Frame compressed again after forgery — third compression generation |
| **Interframe difference** | Average difference between adjacent frames vs frame index; merging spikes reveal edits |
| **Double JPEG compression detection** | Quantization-table analysis revealing two compression generations |
| **Optical flow** | Per-pixel motion field between frames; abrupt breaks expose frame tampering |
| **Affine transformation** | Translation+rotation+scaling+shear combination preserving parallel lines |
| **Perspective transformation** | Non-linear remapping simulating viewpoint change; parallel lines converge |
| **Erosion / dilation** | Shrink / expand bright regions using a structuring element |
| **Opening / closing** | Erosion→dilation (removes small objects) / dilation→erosion (fills holes) |
| **Image registration** | Aligning multiple images of a scene into one coordinate system |
| **Style transfer** | Re-rendering an image in another image's artistic style |
| **Super-resolution** | Recovering high-resolution detail from low-resolution input |
| **GAN (Generative Adversarial Network)** | Generator vs discriminator duel producing photorealistic synthetic media |
| **Autoencoder** | Encoder-decoder network; reconstruction error used for anomaly detection and face swapping |
| **PRNU (Photo Response Non-Uniformity)** | Unique sensor fingerprint from manufacturing imperfections — links media to source device |
| **Digital watermarking** | Concealing a secret mark in host media for later authenticity verification |
| **StirMark attack** | Benchmark geometric attack desynchronising watermarks without removing them |
| **Protocol attack** | Watermark attack exploiting scheme design to create ownership ambiguity (invertibility, copy attacks) |
| **Cryptographic attack** | Exhaustive key search against watermark security — expensive, rare |
| **Active detection** | Verifies embedded data (watermarks/signatures) present since creation |
| **Passive (blind) detection** | Analyses content alone for manipulation-induced inconsistencies |
| **Hybrid detection** | Fuses active + passive cues, often via ML, for robustness |
| **SVM / k-NN / Random Forest** | Classical classifiers on handcrafted forensic features (noise residuals, DCT) |
| **CNN** | Convolutional network detecting/localizing manipulations in images |
| **RNN / LSTM** | Sequence models analysing temporal video tampering |
| **XAI (Explainable AI)** | Methods (Grad-CAM, SHAP) showing *why* a model flagged an image — needed for legal transparency |
| **Grad-CAM / SHAP** | Visualisation techniques highlighting regions/features driving a model's decision |
| **One-Class SVM** | Unsupervised outlier detector flagging statistical deviation from genuine-image distribution |
| **Transfer learning** | Fine-tuning pretrained networks on small forensic datasets |
| **Federated learning** | Training across distributed data sources without sharing sensitive data |
| **CASIA v1/v2** | Benchmark dataset of spliced images |
| **CoMoFoD** | Copy-move forgery benchmark dataset |
| **FaceForensics++** | Deepfake video/image benchmark dataset |
| **Columbia Splicing Dataset** | Authentic-vs-tampered splicing benchmark |
| **Wild Web Dataset** | Real-world tampered media collection |

## Unit 4 — Deepfakes

| Term | Definition |
| --- | --- |
| **Deepfake** | AI-generated synthetic media (faces/video/audio) created with GANs and autoencoders |
| **Cheapfake** | Manipulated media made *without* AI — simple edits, speed changes, miscaptioning |
| **Blink detection** | Exploits deepfakes' failure to reproduce natural blinking |
| **Lip-sync analysis** | Detects audio-video mismatch in synthetic speech |
| **Temporal coherence** | Frame-to-frame consistency check — synthesis flickers over time |
| **Facial landmark tracking** | Monitors facial point trajectories for unnatural movement |
| **Microsoft Video Authenticator** | Tool scoring per-frame manipulation confidence in videos |
| **Deepware Scanner** | Online scanner for deepfake video detection |

## Related

- [[Images and Videos as Legal Evidence]] · [[Image Processing Techniques]] · [[Video Processing and Analytics]]
- [[Image and Video Authentication]] · [[Digital Image Manipulation Methods]] · [[Image Forgery Types]]
- [[Forgery Detection Techniques]] · [[ML in Image Forensics]] · [[Deepfake Detection]]