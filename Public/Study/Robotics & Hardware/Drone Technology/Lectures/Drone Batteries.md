---
Title: "Drone Batteries"
Status: Active
tags: unit-2, batteries, LiPo, C-rating, energy, power
Date: "2025.10.06"
Unit: 2
---
# Drone Batteries

**Related Notes**: [[Drone Technology Index]] | [[Power Distribution in a drone]] | [[Electronic Speed Controller]] | [[Propellors & Motors]]

**Unit**: [[Drone Technology Index#Unit 2|Unit 2 — Drone System Design Flow]]

---

## 1. Overview

The battery is the **sole energy source** for a drone's motors, flight controller, and all electronics. Battery selection has a direct impact on:
- Flight time (endurance)
- Maximum thrust output
- Overall drone weight
- Safety risks

Nearly all modern drones use **Lithium Polymer (LiPo)** batteries because of their exceptional **energy density**, **power delivery capability**, and **lightweight** form factor.

---

## 2. LiPo Battery Fundamentals

### 2.1 Cell Voltage

A single LiPo cell operates between:
- **Fully charged**: 4.2 V
- **Nominal**: 3.7 V
- **Minimum safe**: 3.5 V (going lower causes permanent cell damage)

Multi-cell packs are denoted by their **S number** (cells in Series):

| Config | Cells | Nominal Voltage | Fully Charged |
|--------|-------|----------------|--------------|
| 1S | 1 | 3.7 V | 4.2 V |
| 2S | 2 | 7.4 V | 8.4 V |
| 3S | 3 | 11.1 V | 12.6 V |
| 4S | 4 | 14.8 V | 16.8 V |
| 6S | 6 | 22.2 V | 25.2 V |

Higher cell count = higher voltage = motor spins faster (higher RPM) = more thrust.

### 2.2 Capacity (mAh)

Capacity in **mAh (milliamp-hours)** is how much charge the battery holds.

$$E = V \times \frac{\text{mAh}}{1000} \quad (\text{Watt-hours, Wh})$$

Example: A **4S 5000 mAh** battery:
$$E = 14.8 \times \frac{5000}{1000} = 74 \text{ Wh}$$

Higher capacity = longer flight time, **but also heavier**.

### 2.3 C-Rating — The Discharge Rate

The **C-rating** defines how fast the battery can safely discharge relative to its capacity.

$$I_{\text{max}} = C \times \text{Capacity (Ah)}$$

Example: A **5000 mAh, 30C** battery:
$$I_{\text{max}} = 30 \times 5 = 150 \text{ A continuous}$$

| C-Rating | Safe Discharge Rate | Typical Application |
|----------|--------------------|--------------------|
| 15–25C | Moderate | Aerial photography, long endurance |
| 35–50C | High | General freestyle/FPV |
| 75–100C | Very High | Racing drones (short bursts) |

- **Higher C-rating** = battery can deliver power more rapidly without voltage sag
- Voltage sag under high load causes motors to lose power mid-flight — especially dangerous in racing
- ESCs and motors together determine the **peak current demand** → match C-rating accordingly

### 2.4 Parallel Cells (P Number)

Batteries can also have cells in **Parallel (P)** to increase capacity without increasing voltage:
- **4S2P**: 4 cells in series, 2 such packs in parallel → 14.8V, double the capacity
- Parallel packs are used for large payload drones needing long endurance

---

## 3. Battery Comparison — LiPo vs Alternatives

| Type | Energy Density | Max Discharge | Cycle Life | Weight | Best For |
|------|---------------|--------------|-----------|--------|---------|
| **LiPo** | High (~200 Wh/kg) | Very High (50–100C) | ~300 cycles | Light | Most drones |
| **Li-Ion (18650)** | Very High (~265 Wh/kg) | Low (5–10C) | ~500 cycles | Heavier per volume | Long-endurance |
| **LiHV (High Voltage)** | Slightly > LiPo | High | ~300 cycles | Same as LiPo | Performance builds |
| **NiMH** | Moderate | Moderate | ~1000 cycles | Heavy | Old RC tech |
| **NiCd** | Low | Moderate | High | Very Heavy | Obsolete |

> **Li-Ion** (e.g., Samsung 40T, Molicel P42A) is gaining ground in long-range drones because of superior energy density, even though it cannot discharge as rapidly.

---

## 4. Key Battery Specifications at a Glance

| Spec | Meaning | Higher = ? |
|------|---------|-----------|
| S (cell count) | Voltage level | More power, higher RPM |
| mAh (capacity) | Energy stored | Longer flight time (heavier) |
| C-rating | Max safe discharge rate | Better handling of current spikes |
| Weight | Physical mass | Heavier reduces flight time |
| Internal Resistance | Resistance within cells | Lower is better — less heat, less sag |

---

## 5. Flight Time Estimation

A rough estimate of flight time:

$$t_{\text{flight}} \approx \frac{\text{Capacity (mAh)} \times 0.8}{I_{\text{hover}} \times 1000} \times 60 \quad (\text{minutes})$$

where $I_{\text{hover}}$ is the current draw in amps during hover, and the 0.8 factor leaves 20% reserve.

Example: 5000 mAh battery, hover current 20 A:
$$t = \frac{5000 \times 0.8}{20 \times 1000} \times 60 = \frac{4000}{20000} \times 60 = 12 \text{ min}$$

---

## 6. LiPo Safety Rules

LiPo batteries can catch fire or explode if mishandled. These rules are **non-negotiable**:

| Rule | Why |
|------|-----|
| Never discharge below **3.5V per cell** | Causes permanent cell damage and capacity loss |
| Never overcharge above **4.2V per cell** (4.35V for LiHV) | Thermal runaway risk |
| Never charge at more than **1C** unless battery explicitly rated higher | Heat buildup |
| Always charge in a **LiPo-safe bag** or fireproof container | Containment if fire starts |
| Store at **3.8V per cell** (storage voltage) for long-term storage | Prevents degradation |
| Never charge a **puffed or damaged** battery | Cell integrity already compromised |
| Keep away from **heat, water, and sharp objects** | Self-explanatory |
| Never leave **unattended while charging** | Early thermal events can be stopped |

---

## 7. Battery Maintenance & Life

- Charge at **1C rate** for longest battery life
- Balance charge with a **balance charger** every 2–3 cycles to equalize cell voltages
- LiPos typically last **300–500 cycles** before significant capacity loss
- Capacity loss > 20% = time to replace
- Store batteries in a **cool, dry place** at storage voltage when not flying for > 1 week

---

## See Also
- [[Power Distribution in a drone]] — How battery power is routed
- [[Electronic Speed Controller]] — Current demands that define C-rating requirements
- [[Propellors & Motors]] — Motor KV determines voltage (cell count) needs
- [[Aerial Terminology in Drones]] — Thrust, weight, and endurance relationships

---
*Unit 2 — Drone System Design Flow | Drone Technology — BTech Sem 5*
