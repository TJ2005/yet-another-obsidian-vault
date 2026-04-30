---
Title: Nodular Wireless Networks
Status: Active
marker:
  - "[[(MDFS) Mobile Device Forensics and Security index]]"
tags:
  - BTech
Date: 2026.04.27
Time: 18:19
---
# 1.3 Nodular Wireless Networks

> [!abstract] What This Note Covers
> - Sensor network characteristics (sink, low per-node rate, correlated data, cooperation)
> - Energy constraints and the delay vs energy tradeoff
> - System-level design implications when battery is the bottleneck

> [!seealso] Related Notes
> - [[Mobile Communication challenges & Specifications#1.2.1.2 Hard Energy Constraints]]
> - [[Wireless System Distributed Control and Spectrum#1.4.1 Distributed Control over Wireless Links]]
> - [[Wireless Networks MultiPlexing in Dimensions#1.5.2 Dimensions Available]]

> [!info] Quick Facts
> - In dense sensor deployments, correlated data is a feature: it enables aggregation/compression.

## 1.3.1 Sensor Networks — Study Notes (Absorption Style)

### 1.3.1.1 Basic Characteristics

- **Nodes powered by non-rechargeable batteries**  
    Each sensor node has limited energy → cannot be replaced or recharged → network lifetime depends on energy usage.
    
- **Data flows to a centralized location (sink)**  
    Sensors collect data → forward it (multi-hop) → reaches base station for processing.
    
- **Low per-node data rate, but large scale**  
    Each node sends small data → but total nodes can be very high (~100,000) → aggregate traffic becomes significant.
    
- **Data highly correlated (time + space)**  
    Nearby sensors measure similar values → redundancy present → enables compression and aggregation.
    
- **Nodes cooperate**  
    Nodes:
    
    - Forward data
        
    - Aggregate/compress data
        
    - Assist in transmission/reception  
        → Network acts as a **collaborative system**
        

---

## 1.3.2 Energy Constraints and Their Impact

- **Each node can send only finite bits**  
    Energy budget limits total communication → must be used efficiently.
    
- **Transmit energy ↓ when bit time ↑**  
    Slower transmission → less power per bit → saves energy.
    
- **Circuit energy ↑ with bit time**  
    Longer transmission duration → circuits stay active longer → more energy consumed.
    
- **Delay vs Energy Tradeoff**
    
    - Slow transmission → saves power but increases delay
        
    - Fast transmission → reduces delay but consumes more power
        

---

## 1.3.3 Energy Components in Short-Range Networks

Must consider:

- Transmit energy
    
- Circuit energy
    
- Processing energy
    

→ Total energy ≠ just transmission

---

## 1.3.4 Design Implications

- **Sophisticated techniques ≠ always energy-efficient**  
    Complex algorithms → more computation → higher energy usage.
    
- **Sleep modes save energy**  
    Nodes turn off when idle → conserve power  
    But:
    
    - Harder synchronization
        
    - Increased communication delay
        

---

## 1.3.5 System-Level Impact

Energy constraint affects entire network design:

- **Bit allocation optimization**  
    Decide:
    
    - Which node sends how much data
        
    - When and how often
        
- **Tradeoffs**
    
    - Delay vs Throughput
        
    - Throughput vs Energy
        
    - Energy vs Network lifetime
        
- **Node cooperation optimization**
    
    - Efficient routing
        
    - Data aggregation
        
    - Load balancing across nodes
        

---

## 1.3.6 Core Understanding

- Energy is the **primary constraint**
    
- Every design choice = **tradeoff between energy, delay, and performance**
    
- Network must be:
    
    - Energy-aware
        
    - Cooperative
        
    - Optimized across all layers
  
  

# References


###### Information
- date: 2026.04.27
- time: 18:19
