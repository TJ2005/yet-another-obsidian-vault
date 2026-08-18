---

Title: "DIVF Lab 1"

Status:

marker:

tags:

Date: "2026.07.24"

Time: "12:27"

---
# Digital Image and Video Forensics – Practical 1

## Title

**Metadata Extraction from Image and Video Files**

## Objective

To extract and analyze metadata from digital image and video files in order to identify information such as device make, model, date and time of capture, GPS location, software used, video codec, duration, bitrate, frame rate, and audio codec. Such metadata can assist forensic investigators in determining the origin, authenticity, location, and technical characteristics of digital media evidence.

## Tools Required

* ExifTool version 13.59
* MediaInfo command-line utility
* Sample JPEG image
* Sample MOV video
* macOS Terminal

---

# Part A: Setup

## Installation and Preparation

ExifTool and MediaInfo were installed on the system. An image stored in the Apple Photos Library and a video recorded using an Apple iPhone 16 Pro were selected for metadata analysis.

The following files were examined:

1. `9C47F876-E195-4FB5-965C-6426C52DB3B2_1_105_c.jpeg`
2. `IMG_3738.MOV`

![[IMG-20260724124433494.png]]
---

# Part B: Performing the Practical

## 1. Image Metadata Extraction Using ExifTool

The following command was executed in Terminal:

```zsh
./exiftool /Users/tj/Pictures/Photos\ Library.photoslibrary/resources/derivatives/9/9C47F876-E195-4FB5-965C-6426C52DB3B2_1_105_c.jpeg
```

ExifTool successfully extracted the camera details, timestamps, GPS coordinates, exposure settings, lens information, software version, image resolution, and color profile.

## Important Image Metadata

| Metadata Field     | Extracted Value                                   |
| ------------------ | ------------------------------------------------- |
| File Name          | 9C47F876-E195-4FB5-965C-6426C52DB3B2_1_105_c.jpeg |
| File Type          | JPEG                                              |
| MIME Type          | image/jpeg                                        |
| File Size          | 385 kB                                            |
| Camera Make        | Apple                                             |
| Camera Model       | iPhone 16 Pro                                     |
| Software           | 26.1                                              |
| Date/Time Original | 2026-04-05 17:05:08.584 +05:30                    |
| Create Date        | 2026-04-05 17:05:08.584 +05:30                    |
| Modify Date        | 2026-04-05 18:18:04.218 +05:30                    |
| GPS Latitude       | 18° 55' 54.26" N                                  |
| GPS Longitude      | 72° 50' 2.35" E                                   |
| GPS Altitude       | 19.7 m above sea level                            |
| GPS Date/Time      | 2026-04-05 11:34:51 UTC                           |
| Exposure Time      | 1/110 second                                      |
| Aperture           | f/2.8                                             |
| ISO                | 160                                               |
| Flash              | Off, did not fire                                 |
| White Balance      | Auto                                              |
| Focal Length       | 15.7 mm                                           |
| 35 mm Equivalent   | 120 mm                                            |
| Lens Model         | iPhone 16 Pro back camera 15.66 mm f/2.8          |
| Image Dimensions   | 768 × 1024 pixels                                 |
| Megapixels         | 0.786 MP                                          |
| Color Profile      | Display P3                                        |
| Encoding           | Baseline DCT, Huffman coding                      |
| Chroma Subsampling | YCbCr 4:2:0                                       |
| Bits per Sample    | 8 bits                                            |

---

## 2. Video Metadata Extraction Using MediaInfo

The following command was executed in Terminal:

```zsh
/Users/tj/Documents/prog/mediainfo/build/mediainfo /Users/tj/Downloads/IMG_3738.MOV
```

MediaInfo successfully extracted the container format, video codec, duration, bitrate, frame rate, recording device, operating system, GPS location, audio codecs, HDR information, and embedded metadata tracks.

## General Video Metadata

| Metadata Field     | Extracted Value                  |
| ------------------ | -------------------------------- |
| File Name          | IMG_3738.MOV                     |
| Complete Path      | /Users/tj/Downloads/IMG_3738.MOV |
| Container Format   | MPEG-4                           |
| Format Profile     | QuickTime                        |
| File Size          | 21.0 MiB                         |
| Duration           | 6.590 seconds                    |
| Overall Bitrate    | 26.8 Mb/s                        |
| Bitrate Mode       | Variable                         |
| Overall Frame Rate | 59.940 FPS                       |
| Recorded Date      | 2026-07-24 12:39:07 +05:30       |
| Encoded Date       | 2026-07-24 07:09:07 UTC          |
| Tagged Date        | 2026-07-24 07:09:14 UTC          |
| Recorded Location  | 19.1080° N, 72.8375° E           |
| Recorded Altitude  | 10.986 m                         |
| Location Accuracy  | Approximately 19.73 m            |
| Writing Library    | Apple QuickTime                  |
| Operating System   | Apple iOS 26.5                   |
| Recording Hardware | Apple iPhone 16 Pro              |

---

## Video Stream Metadata

| Metadata Field           | Extracted Value              |
| ------------------------ | ---------------------------- |
| Video Codec              | HEVC                         |
| Codec Description        | High Efficiency Video Coding |
| Codec ID                 | hvc1                         |
| Codec Profile            | Main 10@L4.1@Main            |
| HDR Format               | Dolby Vision Profile 8.4     |
| HLG Compatibility        | Yes                          |
| Video Duration           | 6.590 seconds                |
| Video Bitrate            | 26.1 Mb/s                    |
| Resolution               | 1920 × 1080 pixels           |
| Aspect Ratio             | 16:9                         |
| Rotation                 | 90°                          |
| Frame Rate Mode          | Variable                     |
| Average Frame Rate       | 59.940 FPS                   |
| Minimum Frame Rate       | 54.545 FPS                   |
| Maximum Frame Rate       | 60.000 FPS                   |
| Color Space              | YUV                          |
| Chroma Subsampling       | 4:2:0                        |
| Bit Depth                | 10 bits                      |
| Color Primaries          | BT.2020                      |
| Transfer Characteristics | HLG                          |
| Ambient Illumination     | 314 lux                      |
| White Point              | D65                          |
| Stream Size              | 20.5 MiB                     |

---

## Audio Stream Metadata

The video contained two separate audio streams.

### Audio Stream 1

| Metadata Field    | Extracted Value                     |
| ----------------- | ----------------------------------- |
| Audio Codec       | AAC LC                              |
| Codec Description | Advanced Audio Codec Low Complexity |
| Codec ID          | mp4a-40-2                           |
| Duration          | 6.590 seconds                       |
| Bitrate           | 157 kb/s                            |
| Channels          | 2                                   |
| Channel Layout    | Left and Right                      |
| Sampling Rate     | 48.0 kHz                            |
| Compression       | Lossy                               |
| Stream Size       | 126 KiB                             |

### Audio Stream 2

| Metadata Field    | Extracted Value              |
| ----------------- | ---------------------------- |
| Audio Codec       | APAC                         |
| Codec Description | Apple Positional Audio Codec |
| Duration          | 6.590 seconds                |
| Bitrate           | 401 kb/s                     |
| Channels          | 4                            |
| Sampling Rate     | 48.0 kHz                     |
| Compression       | Lossy                        |
| Stream Size       | 323 KiB                      |
| Metadata Type     | Cinematic audio              |

---

# Part C: Observation Table

| File Name                                         | Make/Model          | Date and Time              | GPS Information                                | Codec                    | Duration       | Bitrate                            |
| ------------------------------------------------- | ------------------- | -------------------------- | ---------------------------------------------- | ------------------------ | -------------- | ---------------------------------- |
| 9C47F876-E195-4FB5-965C-6426C52DB3B2_1_105_c.jpeg | Apple iPhone 16 Pro | 2026-04-05 17:05:08 +05:30 | 18°55'54.26" N, 72°50'2.35" E; altitude 19.7 m | JPEG                     | Not applicable | Not applicable                     |
| IMG_3738.MOV                                      | Apple iPhone 16 Pro | 2026-07-24 12:39:07 +05:30 | 19.1080° N, 72.8375° E; altitude 10.986 m      | HEVC/H.265, Dolby Vision | 6.590 seconds  | 26.1 Mb/s video; 26.8 Mb/s overall |

---

# Analysis of Image Metadata

The image was created using an Apple iPhone 16 Pro. The metadata identifies the precise camera model, lens, exposure settings, timestamp, GPS coordinates, and operating-system software version.

The original capture time was recorded as 5 April 2026 at 17:05:08 with the Indian Standard Time offset of +05:30. The GPS timestamp was recorded in UTC as 11:34:51, which corresponds closely with the local capture time after applying the +05:30 offset.

The metadata also shows that the image was modified at 18:18:04, approximately one hour and thirteen minutes after the original capture time. This does not necessarily prove intentional image manipulation. The modification may have resulted from processing, editing, exporting, synchronization, or the creation of a derivative file by the Apple Photos application.

The image was located inside the following directory:

```text
Photos Library.photoslibrary/resources/derivatives/
```

The term `derivatives` indicates that the analyzed JPEG may not be the original full-resolution camera file. It may be a reduced-size preview, thumbnail, edited version, or processed copy generated by Apple Photos.

This interpretation is further supported by the image dimensions of only 768 × 1024 pixels and a resolution of approximately 0.786 megapixels, which is significantly lower than the normal native resolution of an iPhone 16 Pro photograph.

Therefore, although the metadata identifies the original capture device and location, the analyzed file should be treated as a derived copy rather than conclusively assumed to be the original camera file.

---

# Analysis of Video Metadata

The video was recorded using an Apple iPhone 16 Pro running iOS 26.5. The recording date was 24 July 2026 at 12:39:07 Indian Standard Time.

The encoded time was stored as 07:09:07 UTC. When the +05:30 time-zone offset is applied, this corresponds exactly to 12:39:07 IST. Therefore, the local recording time and UTC encoded time are consistent.

The video was stored in the QuickTime MOV container and encoded using HEVC, also known as H.265. The video used the Main 10 profile, indicating 10-bit video encoding.

The video also contained Dolby Vision Profile 8.4 metadata and was compatible with Hybrid Log-Gamma. Its BT.2020 color primaries indicate that the video used a wide-color-gamut HDR format.

The average frame rate was 59.940 FPS. However, the minimum and maximum frame rates ranged from 54.545 FPS to 60 FPS. This confirms that the video used a variable frame rate rather than maintaining a perfectly constant frame rate.

A rotation value of 90 degrees was stored in the metadata. This indicates that the video was recorded in a portrait orientation while its underlying encoded frame dimensions remained 1920 × 1080 pixels. Compatible video players use the rotation metadata to display the video correctly.

The video contained two audio streams:

1. A standard stereo AAC LC stream.
2. A four-channel Apple Positional Audio Codec stream.

The second stream appears to support Apple's spatial or cinematic audio processing.

The file also contained several timed metadata tracks, including:

* Video orientation
* Cinematic audio
* Detected-face information
* Face bounds
* Face roll and yaw angles
* Live Photo information
* Scene illumination
* Segment identifiers

This demonstrates that modern smartphone videos can contain significantly more information than ordinary audio and video streams.

---

# Interesting and Unusual Findings

## 1. Precise GPS Information

Both the image and video contained embedded GPS coordinates. This can help investigators determine where the media was captured.

The image location was:

```text
18°55'54.26" N, 72°50'2.35" E
```

The video location was:

```text
19.1080° N, 72.8375° E
```

The video metadata also recorded an approximate horizontal location accuracy of 19.73 metres.

## 2. Image May Be a Derived Copy

The image was stored in the Apple Photos `derivatives` directory and had a relatively low resolution of 768 × 1024 pixels. This suggests it was likely a generated preview or processed copy rather than the original full-resolution image.

## 3. Difference Between Original and Modified Time

The image's modification timestamp occurred approximately one hour and thirteen minutes after its original capture time. This may indicate editing, processing, export, synchronization, or generation of a derivative file.

## 4. Accurate UTC and Local-Time Conversion

The video recorded time was 12:39:07 +05:30, while the encoded UTC time was 07:09:07. These values are consistent after applying the Indian Standard Time offset.

## 5. Variable Frame Rate

Although the reported average frame rate was 59.940 FPS, the actual frame rate varied between approximately 54.545 FPS and 60 FPS. Variable frame rates are common in smartphone videos but may affect frame-by-frame forensic timing analysis.

## 6. Dolby Vision and HDR Metadata

The video used 10-bit HEVC encoding with Dolby Vision Profile 8.4, HLG transfer characteristics, BT.2020 color primaries, and wide-color-gamut information.

Forensic tools and video players that do not properly support HDR may display such footage with incorrect brightness or colors.

## 7. Multiple Audio Streams

The video contained standard AAC stereo audio and a separate four-channel Apple Positional Audio Codec stream. The second stream appears to store spatial or cinematic audio information.

## 8. Face-Detection Metadata

The video contained metadata keys related to:

* Detected faces
* Face identifiers
* Face boundaries
* Face roll angles
* Face yaw angles

This means information produced by on-device computer-vision processing may remain embedded in the video even though it is not immediately visible during normal playback.

## 9. Live Photo and Scene Information

The file contained Live Photo metadata and scene-illumination data. The ambient illumination was recorded as 314 lux with a D65 chromaticity reference.

## 10. Different Software Versions

The image reported software version 26.1, while the video reported iOS 26.5. This indicates that the two files were created at different times or under different operating-system versions.

---

# Forensic Importance of Metadata

Metadata can help forensic investigators:

* Identify the device used to capture media.
* Determine the date and time of creation.
* Recover geographical coordinates.
* Compare local timestamps with UTC timestamps.
* Detect possible editing or processing.
* Determine whether a file is original or derivative.
* Identify video and audio codecs.
* Understand frame-rate behaviour.
* Locate additional hidden metadata streams.
* Correlate media with other digital evidence.
* Establish an investigative timeline.

However, metadata alone should not be treated as absolute proof because it can be altered, deleted, copied, or fabricated. Metadata findings should be validated using file hashes, filesystem timestamps, source-device examination, visual analysis, and other forensic evidence.

---

# Expected Outcome

The practical provided an understanding of the metadata stored inside digital image and video files.

ExifTool was used to extract image metadata including camera make, model, timestamp, GPS coordinates, lens information, exposure settings, software version, and image dimensions.

MediaInfo was used to extract video metadata including the recording device, location, HEVC codec, Dolby Vision profile, duration, bitrate, resolution, frame rate, audio codecs, and embedded timed metadata.

The practical demonstrated how metadata can be used to identify the possible source, location, time, processing history, and technical characteristics of digital media evidence.

---

# Result

Metadata extraction from the selected image and video files was successfully performed using ExifTool and MediaInfo.

The image was identified as being captured using an Apple iPhone 16 Pro and contained timestamps, GPS coordinates, exposure information, lens details, software information, and image properties.

The video was also recorded using an Apple iPhone 16 Pro and contained HEVC video, Dolby Vision HDR, variable frame-rate information, two audio streams, GPS coordinates, face-detection metadata, cinematic-audio information, Live Photo metadata, and scene-illumination information.

The practical demonstrated that image and video files may preserve extensive forensic information beyond their visible and audible content.

---

# Conclusion

The experiment successfully demonstrated the extraction and forensic analysis of metadata from an image and a video.

The findings showed that metadata can reveal the capture device, recording time, geographical location, camera settings, operating-system version, codec information, frame rate, HDR format, audio configuration, and evidence of file processing.

The image appeared to be a derivative generated by Apple Photos rather than the original full-resolution file. The video contained advanced smartphone metadata, including face-detection, Live Photo, cinematic-audio, scene-illumination, and positional-audio information.

Therefore, metadata analysis is a valuable preliminary step in digital image and video forensic investigations. Nevertheless, investigators must verify metadata using additional forensic techniques because metadata can be changed or removed.

---
