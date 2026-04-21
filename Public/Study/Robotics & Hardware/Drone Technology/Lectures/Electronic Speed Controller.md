---
Title: "Electronic Speed Controller (ESC)"
Status: Active
tags: unit-2, ESC, BLDC, PWM, MOSFET, BEC, motor-control
Date: "2025.10.06"
Unit: 2
---
# Electronic Speed Controller (ESC)

**Related Notes**: [[Drone Technology Index]] | [[Propellors & Motors]] | [[Drone Batteries]] | [[Power Distribution in a drone]] | [[Flight Controller & Communication]]

**Unit**: [[Drone Technology Index#Unit 2|Unit 2 — Drone System Design Flow]]

---

## 1. What is an ESC?

An **Electronic Speed Controller (ESC)** is an electronic circuit that controls and regulates the rotational **speed and direction** of a brushless motor by converting DC power from the battery into the precisely-timed **3-phase AC signals** that brushless motors require.

Without an ESC, you could not run a brushless motor — they physically cannot run on raw DC power.

---

## 2. Why ESCs are Necessary

| Motor Type | Power Needed | Can Run on Raw DC? |
|-----------|-------------|-------------------|
| Brushed DC | DC current | Yes — brushes do the commutation |
| Brushless DC (BLDC) | 3-phase AC (sequenced) | No — requires electronic commutation |

A BLDC motor has **3 stator coils** (phases) that must be energised in a precise rotating sequence to create a spinning magnetic field. The ESC generates this sequence electronically.

---

## 3. How an ESC Works

### 3.1 Signal Input

The **flight controller** sends a **PWM (Pulse Width Modulation)** signal to the ESC:
- Standard PWM: 1000–2000 µs pulse width at 50–490 Hz
- 1000 µs = minimum throttle (motor off / idle)
- 2000 µs = maximum throttle (full speed)
- Modern protocols: **OneShot125**, **Multishot**, **DShot300/600** — faster, digital

### 3.2 Signal Processing (MOSFETs)

The ESC contains **6 MOSFETs** (3 high-side + 3 low-side) arranged in a 3-phase H-bridge. The microcontroller in the ESC switches these MOSFETs in the correct sequence to simulate rotating 3-phase AC.

```
Battery DC → ESC Microcontroller → MOSFET switching (6-step commutation) → 3-phase AC → Motor
```

### 3.3 Commutation Detection

To know which phase to energise next, the ESC detects rotor position using:
- **BEMF (Back-Electromotive Force)**: the motor's own generated voltage on the passive winding tells you rotor position — used in sensorless ESCs
- **Hall Effect Sensors**: physical sensors in the motor — used in sensored (smoother start) ESCs

### 3.4 Motor Speed Control

Higher throttle signal → ESC increases the frequency and duty cycle of MOSFET switching → motor spins faster.

---

## 4. Key ESC Parameters

### 4.1 Current Rating (Amps)

The most critical specification. The ESC must handle the **peak current the motor draws**.

$$I_{\text{ESC}} \geq 1.2 \times I_{\text{motor\_max}}$$

Use a **20% safety margin** to prevent thermal shutdown. Never run an ESC at its rated limit continuously.

| Drone Class | Motor Max Current | Recommended ESC |
|------------|-----------------|----------------|
| Micro FPV | ~10 A | 15–20 A ESC |
| 5″ Freestyle | ~35 A | 40–45 A ESC |
| 7″ Long Range | ~40 A | 50 A ESC |
| Heavy-Lift Hex | ~60 A | 75–80 A ESC |

### 4.2 Voltage Rating (Cell Count)

The ESC voltage rating must match the LiPo cell count:

| LiPo Config | Nominal Voltage | Fully Charged |
|------------|----------------|--------------|
| 3S | 11.1 V | 12.6 V |
| 4S | 14.8 V | 16.8 V |
| 6S | 22.2 V | 25.2 V |

> Using a 4S battery with a 3S-rated ESC will instantly **destroy the ESC**.

### 4.3 Weight

ESC weight matters in small drones. A heavy ESC eats into payload capacity.

| Weight Class | Typical ESC Current | Drone Application |
|------------|--------------------|--------------------|
| Micro (< 5 g) | 5–15 A | Micro FPV |
| Light (5–15 g) | 20–35 A | 5″ racing |
| Medium (15–40 g) | 40–60 A | 7″ / photography |
| Heavy (> 40 g) | 80 A+ | Industrial UAVs |

---

## 5. Types of ESCs

### 5.1 Brushed ESC

- Controls older brushed DC motors via direct voltage modulation
- Simple PWM switching — no commutation sequencing needed
- Low efficiency, large size for same power
- Found only in very cheap toy drones today

### 5.2 Standard Brushless (Sensorless) ESC

- Most common type for drones
- Uses BEMF for commutation — works well at medium-to-high RPM
- May stutter on very slow starts (poor at extremely low throttle)
- Sufficient for most FPV, photography, and general drones

### 5.3 Sensored Brushless ESC

- Uses Hall effect sensors in the motor for precise commutation at any speed
- Smooth, no-stutter startup even from standstill
- Typically used in cars and industrial applications — less common in drones

### 5.4 OPTO ESC (Optically Isolated)

- Uses an **optocoupler** to electrically isolate the signal circuit from the power circuit
- Eliminates high-frequency electrical noise from reaching the flight controller
- **Does NOT have an internal BEC** — requires external 5V supply for FC/receiver
- Used in large, high-voltage systems (6S+ industrial drones) where noise suppression is critical

### 5.5 BEC ESC (Battery Eliminator Circuit)

- Contains an internal voltage regulator producing **5V or 6V** output
- Powers the flight controller and receiver directly from the main battery
- Eliminates the need for a separate power module
- Limited to **2–3 A output** — fine for small drones, insufficient for large FCs with many peripherals

### 5.6 BLHeli_32 High-Performance ESC

- Runs **BLHeli_32 firmware** on a 32-bit ARM microcontroller
- Supports digital protocols: **DShot150/300/600/1200** — near-zero latency, no calibration needed
- Features: active braking, bi-directional DSHOT (for RPM telemetry), RPM filtering for FC
- Programmable via BLHeliSuite32 software
- Higher cost but dramatically better performance for FPV racing and cinematic work

---

## 6. BEC — Battery Eliminator Circuit

| Feature | Linear BEC | Switching BEC (SBEC) |
|---------|-----------|---------------------|
| Efficiency | ~50% | ~90% |
| Noise | None | Some RF noise |
| Heat | High | Low |
| Cost | Cheap | Moderate |
| Use | Small drones | Larger systems |

A BEC allows you to power the flight controller and receiver from the main flight battery, eliminating a separate battery — hence "eliminator."

---

## 7. ESC Firmware & Signal Protocols

| Protocol | Type | Latency | Calibration |
|----------|------|---------|-------------|
| Standard PWM | Analog | ~20 ms | Yes |
| OneShot125 | Analog | ~2.5 ms | Yes |
| Multishot | Analog | ~0.5 ms | Yes |
| DShot150 | Digital | <1 ms | No |
| DShot300/600 | Digital | <0.5 ms | No |

**DShot** is now the preferred protocol for modern builds as it's digital (no noise), requires no calibration, and supports **bidirectional telemetry** (ESC sends RPM data back to FC).

### Popular ESC Firmware

| Firmware | Key Features | Compatible With |
|---------|-------------|-----------------|
| **BLHeli_S** | Lightweight, 8-bit, DShot | Budget brushless ESCs |
| **BLHeli_32** | 32-bit, full-featured, telemetry | Performance ESCs |
| **SimonK** | Oldest, basic throttle response | Legacy ESCs |
| **AM32** | Open-source 32-bit alternative | Modern open-hardware ESCs |

---

## 8. ESC Calibration (Standard PWM)

For analog PWM ESCs, you must calibrate throttle range before first use:

1. Turn on transmitter — set throttle stick to **maximum**
2. Connect LiPo battery to ESC
3. Disconnect and reconnect the battery (with throttle still at max)
4. Wait for calibration-mode **beep tones**
5. When tones stop, **lower throttle to minimum**
6. ESC stores max and min throttle values, emits confirmation beeps
7. Power cycle drone before flight

> Digital protocols (DShot) do not require this calibration.

---

## 9. Power Distribution Board (PDB)

The **PDB** distributes power from the battery to all 4 ESCs and the flight controller. In modern builds it is often integrated into the FC stack.

**Functions:**
1. Centralized battery connection point — one XT60 solder pad feeds all ESCs
2. Voltage regulation — provides 12V and 5V rails for camera/VTX/FC
3. Simplifies wiring — eliminates parallel battery lead splitters
4. Maintains equal voltage to all motors for balanced thrust

---

## 10. ESC Selection Summary

| Factor | Rule |
|--------|------|
| **Current** | ESC rating ≥ 1.2 × max motor current |
| **Voltage** | Must match LiPo cell count |
| **Firmware** | BLHeli_32 + DShot for best performance |
| **BEC** | Only if no separate power module; check current capacity |
| **Weight** | Lighter the better — especially for small frames |
| **FC Compatibility** | Verify protocol support (DShot vs PWM) |

---

## See Also
- [[Propellors & Motors]] — Motor KV, type, and sizing
- [[Drone Batteries]] — How cell count and C-rating affect ESC selection
- [[Power Distribution in a drone]] — How ESCs connect in the power chain
- [[Flight Controller & Communication]] — FC sends commands to ESCs

---
*Unit 2 — Drone System Design Flow | Drone Technology — BTech Sem 5*
