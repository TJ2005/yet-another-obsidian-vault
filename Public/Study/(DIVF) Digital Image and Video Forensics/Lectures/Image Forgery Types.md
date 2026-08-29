---

Title: "Image Forgery Types"

Status:

tags: [divf, unit-3]

Date: "2026.08.21"

---
# Image Forgery Types

> [!INFO] Unit 3
> **Image forgery** = any modification of an image intended to deceive. Six canonical families, each leaving characteristic traces.

## 1. Splicing forgery

- **Definition:** combining parts from two or more images into a single composite
- **Purpose:** create realistic composites or misleading visuals
- **Detection:**
	- Noise pattern inconsistencies
	- Lighting and shadow mismatch analysis
	- Colour filter array (**CFA**) pattern irregularities
	- Edge and boundary artifact detection

### Light and shadow analysis
Objects pasted from another photo carry their original light direction/intensity — inconsistent shadow angles expose the splice.

### Edge and boundary detection
![[s115_img_20.png]]
Splice boundaries often show abrupt transitions or halo-like artifacts.

## 2. Cloning (copy-move) forgery

- **Definition:** copying a region *within the same image* and pasting it elsewhere
- **Purpose:** hide unwanted objects or duplicate elements
- **Detection:**
	- **Block-based matching** — find duplicated blocks
	- **Keypoint-based methods** — SIFT/SURF feature detectors
	- Rotation- and scaling-invariant detection

## 3. Object removal forgery

- **Definition:** erasing objects/persons via cloning or **inpainting**
- **Purpose:** conceal information or unwanted elements
- **Detection:**
	- Texture and noise inconsistencies in filled regions
	- Unnatural smoothness or irregularities
	- Machine-learning detection of inpainting artifacts

## 4. Upscale, crop and resampling forgery

| Operation | Trace left |
| --- | --- |
| **Upscaling** | Interpolation artifacts from enlargement |
| **Cropping** | Removed context; possibly hidden details |
| **Resampling** | Geometric transforms (rotation, scaling, skewing) with interpolation |

- **Detection:** periodic interpolation artifacts; statistical pixel-correlation analysis; frequency-domain analysis (**Fourier, Radon transforms**)

## 5. Frame-based tampering in videos

- **Definition:** manipulating individual frames — insertion, deletion, replacement
- **Detection:** temporal consistency analysis; optical flow / motion vector analysis; frame duplication detection via feature matching or hashing

![[s125_img_21.jpg]]

Frames not tampered with undergo compression twice; manipulated frames are compressed *again* after forgery. Three frame classes result:
1. **Pristine frame**
2. **Double-compressed frame without tampering**
3. **Tampered frame**

## 6. Recompression and transcoding detection

- **Definition:** repeated saving or format conversion that can mask manipulation
- **Why it matters:** tampering usually involves resaving → multiple compression generations
- **Detection:**
	- Double JPEG compression detection via **quantization tables**
	- Compression signature analysis
	- Bitstream analysis for video transcoding
- **Indicators:** blocking artifacts, inconsistent compression noise

Merging videos leaves spikes in the **interframe difference** signal (average difference between adjacent frames plotted against frame index); interpolation of frames can repair them.

## Related

- [[Forgery Detection Techniques]]
- [[Digital Image Manipulation Methods]]
- [[ML in Image Forensics]]
- [[DVIF Exam Glossary]]