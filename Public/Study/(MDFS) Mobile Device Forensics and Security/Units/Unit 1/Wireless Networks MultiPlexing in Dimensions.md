---
Title: Wireless Networks MultiPlexing in Dimensions
Status: Active
marker:
  - "[[(MDFS) Mobile Device Forensics and Security index]]"
tags:
  - BTech
Date: 2026.04.27
Time: 18:55
---
# 1.5 Multiplexing in Wireless Systems

> [!abstract] What This Note Covers
> - Multiplexing as channel sharing across frequency/time/space/code
> - FDM, TDM, CDM, SDM with quick pros/cons

> [!seealso] Related Notes
> - [[Cellular coverage maps and handoff#1.6.4 Frequency Reuse]]
> - [[3G Network#1.9.1.3 Core Technologies]]
> - [[Mobile Communication challenges & Specifications#1.2.4 Spectrum / Performance Data (from slides)]]

> [!info] Quick Facts
> - "Code" as a dimension is the conceptual bridge to CDMA-style systems.

---

## 1.5.1 Concept

* Multiplexing = **sharing a single communication channel among multiple users/signals**
* Goal:

  * Efficient use of **limited spectrum**
  * Allow **simultaneous communication**

---

## 1.5.2 Dimensions Available

### 1.5.2.1 Frequency

* Different users → different frequency bands
* Used in **FDM**

---

### 1.5.2.2 Time

* Same frequency shared over time
* Users transmit in **time slots**
* One user at a time
* Used in **TDM**

---

### 1.5.2.3 Space

* Signals separated based on **physical location**
* Signal strength decreases with distance
* Depends on **transmit power**

---

### 1.5.2.4 Code

* Same time + frequency
* Different users → unique codes
* Used in **CDM**

---

## 1.5.3 Frequency Division Multiplexing (FDM)

![[IMG-20260429201746697.png]]

### 1.5.3.1 Concept

* Spectrum split into **multiple frequency bands**
* Each user gets a dedicated frequency
* All users transmit **simultaneously**

### 1.5.3.2 Advantages

* Works for analog and digital signals
* Parallel transmission

### 1.5.3.3 Disadvantages

* Low flexibility
* Bandwidth wastage

---

## 1.5.4 Time Division Multiplexing (TDM)

![[IMG-20260429201746720.png]]
	
### 1.5.4.1 Concept

* Entire frequency used by one user at a time
* Time divided into **equal slots**
* Users transmit sequentially

### 1.5.4.2 Advantages

* Simple
* Flexible

### 1.5.4.3 Disadvantages

* Synchronization required
* Implementation complexity

---

## 1.5.5 Code Division Multiplexing (CDM)

![[IMG-20260429201746821.png]]

### 1.5.5.1 Concept

* All users share **same time and frequency**
* Each user assigned a **unique code**
* Uses orthogonal/chip sequences (+1, −1)

### 1.5.5.2 Advantages

* High efficiency
* Less interference

### 1.5.5.3 Disadvantages

* Complex
* Lower data rates

---

## 1.5.6 Space Division Multiplexing (SDM)

### 1.5.6.1 Concept

* Combines **frequency + time + spatial separation**
* Different users transmit:

  * At different locations
  * Using specific frequency and time

### 1.5.6.2 Advantages

* High data rate
* Efficient use of spectrum

### 1.5.6.3 Disadvantages

* Interference issues
* Signal loss over distance

---

## 1.5.7 Core Understanding

* Multiplexing = **divide resources across users**
* Dimensions:

  * Frequency
  * Time
  * Space
  * Code

→ Different techniques = different ways to **avoid interference and maximize capacity**

  

# References


###### Information
- date: 2026.04.27
- time: 18:55
