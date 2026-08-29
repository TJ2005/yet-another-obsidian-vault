---

Title: "Digital Image Manipulation Methods"

Status:

tags: [divf, unit-2]

Date: "2026.08.21"

---
# Digital Image Manipulation Methods

> [!INFO] Scope
> The toolbox used both by editors (legitimately) and forgers (maliciously). Forensic detection works by spotting the *residues* these operations leave behind.

## Basic processing

- **Cropping & resizing**
- **Colour correction**
- **Noise reduction**
- **Sharpening / blurring**

## Geometric transformations

| Transformation | Effect |
| --- | --- |
| **Translation** | Shifts every point by a fixed offset |
| **Rotation** | Rotates around a centre point |
| **Scaling** | Enlarges or shrinks (interpolation involved) |
| **Shearing** | Slants the image along an axis |
| **Affine** | Combination preserving parallelism (translation + rotation + scale + shear) |
| **Perspective** | Non-linear remapping simulating viewpoint change — parallel lines converge |

![[s72_img_10.jpg]]
![[s73_img_11.jpg]]
![[s74_img_12.jpg]]

Applications: ![[s76_img_13.jpg]] ![[s78_img_14.jpg]]

## Filtering

Convolution kernels that modify frequency content — smoothing (low-pass), sharpening (high-pass), edge-enhancing filters.

## Morphological operations

Structure-modifying ops using structuring elements:

| Operation | Effect |
| --- | --- |
| **Erosion** | Shrinks bright regions — removes small noise |
| **Dilation** | Expands bright regions — fills gaps |
| **Opening** | Erosion → dilation — removes small objects |
| **Closing** | Dilation → erosion — closes small holes |

## Enhancement & restoration

- **Enhancement** — subjective quality improvement
- **Restoration** — objective recovery using degradation models
	- **Deblurring** — inverse/adaptive filtering
	- **Inpainting** — filling missing/damaged regions from surrounding context

## Segmentation & registration

- **Segmentation** — partition into meaningful regions (see [[Image Processing Techniques]])
- **Registration** — aligning two or more images of the same scene into a common coordinate system

## Compression

Lossy (JPEG) vs lossless (PNG) encoding — see [[Image Processing Techniques]].

## Advanced techniques

![[s88_img_15.jpg]]

| Technique | Purpose |
| --- | --- |
| **Style transfer** | Re-render an image in the style of another |
| **Super-resolution** | Reconstruct high-resolution detail from low-res input |
| **GANs** | Generate photorealistic synthetic imagery |
| **Augmented reality (AR)** | Overlay synthetic content onto real scenes |
| **Face / object recognition** | Identify entities within imagery |

![[s89_img_16.jpg]] ![[s90_img_17.jpg]] ![[s92_img_18.jpg]]

## Related

- [[Image Forgery Types]]
- [[Forgery Detection Techniques]]
- [[DVIF Exam Glossary]]