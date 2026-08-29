---

Title: "Image Processing Techniques"

Status:

tags: [divf, unit-1]

Date: "2026.08.21"

---
# Image Processing Techniques

> [!INFO] Scope
> The seven core technique families of digital image processing — enhancement, segmentation, compression, synthesis, feature extraction, restoration and morphological processing.

## 1. Image enhancement

Improving quality/appearance — correcting defects or making an image visually appealing.

| Technique | What it does |
| --- | --- |
| **Contrast adjustment** | Enhances difference between light and dark areas; *contrast stretching* spans pixel intensities across the full histogram range |
| **Histogram equalization** | Transforms intensity values so the output histogram is evenly distributed — improves global contrast; useful when background and foreground are both bright or both dark |
| **Noise reduction** | Removes random brightness/colour variations; methods: median filtering, Gaussian smoothing, bilateral filtering — smooth while preserving detail |

## 2. Image segmentation

Assigns a label to every pixel so pixels sharing visual characteristics (intensity, colour, texture) form coherent regions — unlike edge detection, which only finds boundaries.

| Technique | Mechanism |
| --- | --- |
| **Thresholding** | Binary split: pixels above threshold → white, below → black |
| **Edge detection** | Finds high intensity-gradient areas — Sobel, Canny, Prewitt operators |
| **Region-based** | Region growing (adjacent pixels grouped by similar properties); watershed segmentation (image as topographic map) |

### The three modern segmentation types

| Type | Behaviour | Example |
| --- | --- | --- |
| **Semantic segmentation** | Class label to every pixel by shared characteristics; all pixels of one class treated identically | All trees labelled "tree", regardless of count |
| **Instance segmentation** | Extends semantic — distinguishes individual objects of the same class | Each cat is a separate entity despite all being "cats" |
| **Panoptic segmentation** | Combines both — class labels **and** individual object boundaries | Traffic scene: labels pedestrians/cars AND outlines each person/car |

- [What is semantic segmentation?](https://www.geeksforgeeks.org/computer-vision/what-is-semantic-segmentation/)

## 3. Image compression

Reducing file size by eliminating redundant or less significant information while preserving acceptable visual quality.

| Type | Behaviour | Example |
| --- | --- | --- |
| **Lossy** | Permanently eliminates information (esp. redundant data) — smaller size, some quality loss | JPEG |
| **Lossless** | No quality loss — original perfectly reconstructable | PNG |

## 4. Image synthesis

Generating new images or modifying existing ones computationally rather than by capture — used for data augmentation, simulation, algorithm testing and ML training where real data is limited.

- **Texture synthesis** — generates large natural-looking textures from small samples (graphics, game design)
- **Image generation** — creates images from scratch or based on existing ones via **GANs** (realistic faces, artistic images)

## 5. Feature extraction

Transforming raw pixel data into compact, meaningful descriptors capturing shape, texture, colour or spatial structure — reduces dimensionality while preserving discriminative information.

- **Low-level features** — edges, corners, keypoints, colour histograms, texture descriptors
- **Feature descriptors** — numerical quantification (gradient/frequency-based) for comparison and learning
- **Task enablement** — foundation for object detection, classification, tracking, recognition

## 6. Image restoration

Recovering an image degraded by noise, blur, motion or distortion using mathematical/statistical models of the degradation. Unlike enhancement (**subjective, visual**), restoration is **objective and model-driven** — estimating the original image as accurately as possible.

- **Noise removal** — Gaussian/impulse noise from acquisition or transmission
- **Deblurring** — inverse or adaptive filtering against motion blur, defocus, atmospheric effects
- **Model-based approach** — known/estimated degradation models → reproducible results

## 7. Morphological processing

Operations that modify the geometric structure of objects using predefined shapes (**structuring elements**) — mainly binary and grayscale images.

| Operation pair | Effect |
| --- | --- |
| **Erosion / dilation** | Shrink or expand object regions — remove noise or fill gaps |
| **Opening / closing** | Compound ops — smooth contours, eliminate small objects, close narrow breaks |
| **Shape analysis** | Boundary extraction, skeletonisation, region refinement |

## Related

- [[Video Processing and Analytics]]
- [[Digital Image Manipulation Methods]]
- [[DVIF Exam Glossary]]