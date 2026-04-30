---

Title: "Mobile Communication challenges & Specifications"

Status:

marker:

tags:

Date: "2026.04.27"

Time: "17:21"

---
# 1.2 Mobile Communication challenges & Specifications

> [!abstract] What This Note Covers
> - Delay + energy constraints in mobile networks
> - Wireless channel challenges (noise, shared medium, mobility, QoS diversity)
> - Where constraints show up across the protocol stack
> - Spectrum/performance snapshots + technology enhancements

> [!seealso] Related Notes
> - [[Wireless System Distributed Control and Spectrum#1.4.4 Frequency Characteristics]]
> - [[Wireless Networks MultiPlexing in Dimensions#1.5.1 Concept]]
> - [[Nodular Wireless Networks#1.3.2 Energy Constraints and Their Impact]]
> - [[Cellular coverage maps and handoff#1.6.4 Frequency Reuse]]

> [!info] Quick Facts
> - Wireless channels are shared and capacity-limited, so QoS becomes a first-class constraint.

## 1.2.1 Constraints in Mobile Networks

### 1.2.1.1 Hard Delay Constraints

* Strict latency requirements
* Must deliver data within fixed time
* Example: voice, real-time video

### 1.2.1.2 Hard Energy Constraints

* Devices run on battery
* Limited power → impacts transmission, processing

---

## 1.2.2 Wireless Network Challenges

* Wireless channels are:

  * Noisy
  * Capacity-limited
  * Shared (broadcast medium)

* Dynamic behavior:

  * User movement
  * Changing traffic
  * Variable network conditions

* Applications are heterogeneous:

  * Different QoS requirements
  * Some need strict delay/energy guarantees

---



## 1.2.3 Energy and Delay Constraints Across Protocol Stack

Energy and delay constraints affect all layers:

* **Physical Layer:**
  * Power control, modulation, coding

* **Link Layer:**
  * Error control, retransmissions, scheduling

* **Network Layer:**
  * Routing decisions based on energy and latency

* **Transport Layer:**
  * Congestion control adapted for wireless

* **Application Layer:**
  * Adaptive QoS, compression, data prioritization

→ Key idea:
**Design is no longer isolated per layer — constraints propagate across the entire stack**

---

## 1.2.4 Spectrum / Performance Data (from slides)

### 1.2.4.1 Current Systems

* **5G Cellular:** ~20 Gbps
* **Wi-Fi 6 (802.11ax):** up to ~9.6 Gbps (2.4/5 GHz)

### 1.2.4.2 Next Generation

* **6G Cellular:** ~1 Tbps
* **Wi-Fi 7 (802.11be):**

  * Multi-gigabit speeds
  * Lower latency
  * ~4× faster than Wi-Fi 6

---

## 1.2.5 Technology Enhancements

### 1.2.5.1 Hardware

* Improved batteries
* Better processors and circuits

### 1.2.5.2 Link Layer

* Advanced antennas
* Modulation and coding
* DSP techniques
* Bandwidth optimization

### 1.2.5.3 Network Layer

* Dynamic resource allocation
* Mobility management

### 1.2.5.4 Application Layer

* Soft and adaptive QoS

---

## 1.2.6 Traffic Characteristics (from screenshot)

| Type  | Delay      | Packet Loss | BER  | Data Rate  | Traffic    |
| ----- | ---------- | ----------- | ---- | ---------- | ---------- |
| Voice | <100 ms    | <1%         | 10⁻³ | 8–32 Kbps  | Continuous |
| Data  | Not strict | 0           | 10⁻⁶ | 1–100 Mbps | Bursty     |
| Video | <100 ms    | <1%         | 10⁻⁶ | 1–20 Mbps  | Continuous |

---

## 1.2.7 Key Takeaway

* Different applications require **different network designs**
* “One-size-fits-all protocols do not work”
* Wireless systems must adapt to:

  * Delay constraints
  * Energy limits
  * Dynamic environments

  
## 1.2.8 Ad Hoc Networks — Keywords Table

| Category    | Keywords                                                                       |
| ----------- | ------------------------------------------------------------------------------ |
| Definition  | Infrastructure-less; No base station; Peer-to-peer; Node = router              |
| Properties  | Dynamic topology; Self-configuring; Multi-hop                                  |
| Capacity    | Unknown; Variable; Depends on nodes, mobility, interference                    |
| Design      | No fixed strategy; Transmission = dynamic; Access = dynamic; Routing = dynamic |
| Routing     | Frequent route changes; On-demand discovery; Multi-hop paths                   |
| Cross-layer | Layer interdependence; PHY ↔ MAC ↔ Network; Optimization required              |
| Energy      | Battery limited; Power-sensitive; Lifetime constraint                          |
| Tradeoffs   | Power vs battery; Delay vs hops; Throughput vs energy                          |
| Core Idea   | Flexible; Unpredictable; Resource-constrained                                  |
# References


###### Information
- date: 2026.04.27
- time: 17:21
