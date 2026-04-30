---
Title: Cellular coverage maps and handoff
Status: Active
marker:
  - "[[(MDFS) Mobile Device Forensics and Security index]]"
tags:
  - BTech
Date: 2026.04.27
Time: 19:37
---
# 1.6 Cellular coverage maps and handoff

> [!abstract] What This Note Covers
> - Why we need cells: scaling, capacity, and interference constraints
> - Cellular concept: base stations, cell sizing, and idealized hexagonal models
> - Frequency reuse and how it increases capacity
> - Operational notes + capacity improvement techniques

> [!seealso] Related Notes
> - [[Wireless Networks MultiPlexing in Dimensions#1.5.2.1 Frequency]]
> - [[Wireless System Distributed Control and Spectrum#1.4.5 Frequency Allocation]]
> - [[3G Network#1.9.1.1 Introduction]]
> - [[4G Network#1.9.2.1 4G — Fourth Generation Mobile Networks]]
> - [[5G Network#1.9.3.1 Introduction]]

> [!info] Quick Facts
> - Frequency reuse is the core scaling trick: reuse spectrum in spatially separated cells.

## 1.6.1 Cellular Systems — Cells, Frequency Reuse and Capacity

---

## 1.6.2 Need for Cells

### 1.6.2.1 Naive Approach

* Single base station
* High transmit power
* Covers entire region
* Inverse Square Law there to limit us

### 1.6.2.2 Problems

* Does not scale
* Limited capacity
* High interference
* High power requirement

---

## 1.6.3 Cellular Concept (SDM)

* Region divided into **cells**
* Each cell has a **base station**
* Each cell uses a subset of frequencies

### 1.6.3.1 Key Points

* Cell size ∝ transmit power
* Cell shape irregular (due to obstacles)
* Hexagon used (ideal model):

  * Equal distance to neighbors
  * Easier handoff planning

![[IMG-20260429201746689.png]]
---

## 1.6.4 Frequency Reuse

* Same frequencies reused in **spatially separated cells**
* Improves capacity

### 1.6.4.1 Concepts

* Co-channel cells → same frequency
* Co-channel interference possible
* Distance maintained to reduce interference

![[IMG-20260429201746750.png]]'
---

## 1.6.5 System Operation

* Each cell: **10–50 frequencies** (depends on traffic)
* Base station power controlled
* Frequencies reused in distant cells

---

## 1.6.6 Advantages of Cellular System

### 1.6.6.1 Higher Capacity

* Limited spectrum reused
* SDM + TDM used
* More users supported

---

### 1.6.6.2 Accommodates More Users

* TDM within cell
* Smaller cells → more users

**Why smaller cells help:**

* More reuse of frequencies
* Less users per cell

---

### 1.6.6.3 Lower Power Requirement

* Smaller distance to base station
* Mobile devices use less power
* Saves battery

---

### 1.6.6.4 Robustness

* No single point of failure
* Multiple base stations
* If one cell fails → others still work

---

## 1.6.7 Disadvantages

### 1.6.7.1 High Infrastructure Cost

* More cells → more base stations
* If cell size reduced by factor F → base stations increase by F²

---

### 1.6.7.2 Complexity

* User location tracking
* Handoff management
* Base station interconnection

---

### 1.6.7.3 Frequency Planning

* Careful allocation needed
* Avoid interference between cells
* Cell size and shape decisions

---

### 1.6.7.4 Sectoring Complexity

* Cells divided into sectors
* Requires directional antennas

---

## 1.6.8 Capacity Improvement Techniques

### 1.6.8.1 Adding Channels

* Reserve channels used when needed

---

### 1.6.8.2 Frequency Borrowing

* Congested cell borrows frequency from neighbor

---

### 1.6.8.3 Cell Splitting

* Large cell → multiple smaller cells
* Example:

  * 6.5–13 km → reduced to ~1.5 km

---

### 1.6.8.4 Sectoring

* Cell divided into wedge-shaped sectors
* Reduces interference
* Improves capacity

---

## 1.6.9 Core Understanding

* Cellular system = **SDM + frequency reuse**

* Tradeoff:

  * Smaller cells → higher capacity
  * But → higher cost and complexity

* Design goal:

  * Maximize capacity
  * Minimize interference
  * Maintain efficient handoff and control

  

# References


###### Information
- date: 2026.04.27
- time: 19:37
