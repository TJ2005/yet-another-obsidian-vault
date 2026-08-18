---
Title: "Thrust Dependencies"
Status: Active
tags: unit-2, thrust, KV-rating, propeller, physics, motor
Date: "2025.10.06"
Unit: 2
---
# Thrust Dependencies

**Related Notes**: [[Drone Technology Index]] | [[Propellors & Motors]] | [[Aerial Terminology in Drones]] | [[Electronic Speed Controller]] | [[Drone Batteries]]

**Unit**: [[Drone Technology Index#Unit 2|Unit 2 — Drone System Design Flow]]

---

## 1. The Fundamental Thrust Equation

Propeller thrust is described by actuator disk theory:

$$T = C_T \cdot \rho \cdot n^2 \cdot D^4$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $T$ | Thrust | Newtons (N) |
| $C_T$ | Thrust coefficient (blade geometry factor) | dimensionless |
| $\rho$ | Air density | kg/m³ |
| $n$ | Propeller rotational speed | rev/s |
| $D$ | Propeller diameter | m |

**Critical insight**: The $n^2$ term means doubling RPM **quadruples** thrust. The $D^4$ term means small diameter increases create **enormous** thrust gains.

---

## 2. KV Rating — Motor Speed from Voltage

$$\text{RPM} = KV \times V$$

The motor KV rating defines how fast the motor spins per volt applied.

**Example:**
- 2200 KV motor + 11.1V (3S LiPo) = **24,420 RPM**
- 1000 KV motor + 14.8V (4S LiPo) = **14,800 RPM**

Since $n$ (revolutions/sec) = RPM / 60:
$$T \propto n^2 = \left(\frac{KV \times V}{60}\right)^2 \propto (KV \times V)^2$$

So: **doubling KV or doubling voltage** each quadruples thrust (everything else equal).

---

## 3. All Factors That Affect Thrust

### 3.1 KV Rating

| KV | RPM (at 11.1V) | Thrust Character | Prop Size |
|----|---------------|-----------------|---------|
| 500 KV | 5,550 | Very high torque, very low speed | 14–18″ |
| 1000 KV | 11,100 | High torque, low speed | 10–13″ |
| 2200 KV | 24,420 | Balanced | 5–7″ |
| 3000 KV | 33,300 | High speed, low torque | 3–5″ |

Higher KV → more RPM → more thrust up to the point where drag from small props limits gains.

### 3.2 Supply Voltage

$T \propto V^2$ (since $\text{RPM} \propto V$ and $T \propto \text{RPM}^2$)

Going from 3S (11.1V) to 4S (14.8V) with the same motor:
$$\frac{T_{4S}}{T_{3S}} = \left(\frac{14.8}{11.1}\right)^2 \approx 1.78$$ → **78% more thrust**

### 3.3 Propeller Diameter

$T \propto D^4$

| Diameter Change | Thrust Change |
|----------------|--------------|
| +1″ (e.g., 9″→10″) | ≈ +16% |
| +2″ (e.g., 9″→11″) | ≈ +38% |
| Double (9″→18″) | 16× thrust |

This is why large drones use enormous propellers — dramatically more efficient thrust with smaller RPM.

### 3.4 Propeller Pitch

$T \propto P$ (approximately linear for small pitch changes)

Increasing pitch from 4.5″→5″: ≈ **+8.3% thrust** but with increased current draw.

| Pitch | Thrust | Speed | Current |
|-------|--------|-------|---------|
| Low (e.g., 3″) | Lower | Lower | Lower |
| High (e.g., 5″) | Higher | Higher | Higher |

### 3.5 Number of Blades

| Blades | Thrust Effect | Efficiency | Use Case |
|--------|-------------|-----------|---------|
| 2-blade | Baseline | High | Racing, fixed-wing |
| 3-blade | +10–15% thrust | Moderate | General purpose |
| 4-blade | +20–25% thrust | Lower | Smooth/quiet, payload |

More blades increase thrust but each additional blade overlaps the wake of the previous, reducing efficiency.

### 3.6 Blade Material

| Material | Flexibility | Efficiency | Impact |
|----------|-----------|-----------|-------|
| Plastic/Nylon | Flexible — twist reduces effective pitch | Moderate | Survives crashes |
| Carbon Fiber | Rigid — maintains geometry | High | Shatters on hard impacts |
| Wood | Semi-rigid | Good | Smooth but rare |

Stiffer blades maintain their designed pitch under load → more consistent, predictable thrust.

### 3.7 Air Density ($\rho$)

$T \propto \rho$

Air density decreases with altitude and temperature:
- Sea level (15°C): $\rho = 1.225$ kg/m³
- 2000 m altitude: $\rho \approx 1.006$ kg/m³ (−18% thrust)
- 4000 m altitude: $\rho \approx 0.819$ kg/m³ (−33% thrust)

Drones operated at high altitude need larger props or higher voltage to compensate.

---

## 4. Practical Design Rules

| Goal | Action |
|------|--------|
| More hover thrust | Larger diameter prop + lower KV motor |
| More top speed | Higher KV + higher pitch prop |
| Longer flight time | Larger diameter + low pitch + efficient low-KV motor |
| More agility | Higher KV + 3-blade prop for better response |
| Higher payload | Large prop + very low KV + high voltage battery |

---

## 5. Efficiency — Thrust per Watt

The best measure of propulsion efficiency is **thrust per watt** (g/W):

$$\eta_{\text{prop}} = \frac{T \text{ (g)}}{P \text{ (W)}}$$

- Low KV + large prop: typically **8–12 g/W**
- High KV + small prop: typically **3–6 g/W**

For maximum endurance, maximise thrust-per-watt, which consistently points toward large props + low KV motors.

---

## See Also
- [[Propellors & Motors]] — Detailed motor and propeller specifications
- [[Aerial Terminology in Drones]] — How thrust relates to flight maneuvers
- [[Drone Batteries]] — Voltage that directly affects RPM and thrust
- [[Electronic Speed Controller]] — Controls motor RPM to modulate thrust

---
*Unit 2 — Drone System Design Flow | Drone Technology — BTech Sem 5*
