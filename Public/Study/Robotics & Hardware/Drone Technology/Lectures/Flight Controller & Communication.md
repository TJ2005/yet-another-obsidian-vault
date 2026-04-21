---
Title: "Flight Controller & Communication Systems"
Status: Active
tags: unit-3, flight-controller, transmitter, receiver, PWM, PX4, ArduPilot
Date: "2025.10.06"
Unit: 3
---
# Flight Controller & Communication Systems

**Related Notes**: [[Drone Technology Index]] | [[Drone]] | [[Electronic Speed Controller]] | [[Drone Technology Sensors]] | [[Power Distribution in a drone]]

**Unit**: [[Drone Technology Index#Unit 3|Unit 3 — Drone Hardware Devices]]

---

## 1. Overview

The **Flight Controller (FC)** is the brain of the drone. It:
- Reads all sensor data (gyro, accelerometer, barometer, GPS)
- Interprets pilot commands from the RC receiver
- Runs **stabilisation and control algorithms** (PID loops)
- Outputs motor speed commands to all 4 ESCs

Without the flight controller, a multirotor is physically **impossible to fly** — it is inherently unstable.

---

## 2. Transmitter & Receiver (RC Link)

### 2.1 Radio Transmitter (Tx)

The **transmitter** is the handheld controller the pilot uses. It converts stick positions and switch states into radio signals.

| Spec | Details |
|------|---------|
| Channels | Minimum 6 (throttle, yaw, pitch, roll + 2 aux); 16+ for advanced systems |
| Protocols | PPM, SBUS, CRSF (Crossfire), ELRS (ExpressLRS) |
| Frequency | Legacy: 27 MHz / 72 MHz; Modern: **2.4 GHz** standard, 900 MHz for long-range |

**Frequency evolution:**
| Frequency | Era | Characteristics |
|-----------|-----|----------------|
| 27 MHz | Early RC | Very long wavelength, interference-prone, only 1 drone at a time |
| 72 MHz | 1990s–2000s | Cleaner but still limited channels |
| **2.4 GHz** | 2000s–today | FHSS (Frequency Hopping), many drones simultaneously, good range |
| 900 MHz | 2020s (ELRS) | Long range (10+ km), penetrates obstacles better |

### 2.2 RC Receiver (Rx)

The **receiver** is mounted on the drone and decodes the transmitter's radio signal into channel data for the FC.

**Signal output types:**
- **PWM (Pulse Width Modulation)**: One wire per channel. 1000–2000 µs pulse. Old standard.
- **PPM (Pulse Position Modulation)**: Multiplexes all channels on a single wire sequentially.
- **SBUS**: Serial digital protocol (inverted UART), single wire, up to 16 channels, fast (14 ms frame).
- **CRSF (Crossfire Serial)**: TBS Crossfire protocol — low latency, telemetry, up to 5 km range.
- **ELRS**: Open-source, 250 Hz link rate, extremely low latency (<1 ms effective), long range.

### 2.3 Stick-to-Motor Signal Flow

```
Pilot moves stick
  → Transmitter encodes position as PWM/SBUS
  → Radio link to Receiver
  → Receiver sends channel data to Flight Controller
  → FC PID loop calculates needed motor speeds
  → FC sends PWM/DShot to each ESC
  → ESC adjusts motor RPM
  → Drone moves
```

---

## 3. Flight Controller Hardware

### 3.1 FC Tiers

| Tier | Examples | Processor | Features | Use Case |
|------|---------|-----------|---------|---------|
| **Basic** | KK2, Naze32, CC3D | 8-bit / early 32-bit | Basic stabilisation, limited sensors | Learning, budget builds |
| **Intermediate** | Betaflight F4/F7, SpeedyBee F405 | 32-bit ARM Cortex-M4/M7 | Blackbox logging, OSD, DShot, Betaflight | FPV racing, freestyle |
| **Advanced** | Pixhawk, CubeOrange, Holybro Durandal | 32-bit dual-core + FPU | GPS waypoints, full MAVLink, telemetry, redundancy | Professional, autonomous |

### 3.2 Key FC Sensors (On-board)

| Sensor | What it Measures | Used For |
|--------|-----------------|---------|
| **IMU (MPU6000/ICM42688)** | 3-axis acceleration + 3-axis angular rate | Core attitude estimation |
| **Barometer (BMP388/MS5611)** | Atmospheric pressure → altitude | AltHold mode, altitude hold |
| **Magnetometer (QMC5883L)** | Magnetic heading (compass) | Yaw reference for GPS modes |
| **GPS** | Latitude, longitude, altitude, speed | Loiter, waypoints, RTH |

---

## 4. PID Control System

The flight controller's most critical function is running **PID (Proportional-Integral-Derivative) control loops** to stabilise the drone.

### 4.1 What PID Does

The FC constantly compares the **desired attitude** (from pilot input) with the **actual attitude** (from IMU), calculates an **error**, and drives the motors to correct it.

$$\text{Output} = K_P \cdot e + K_I \cdot \int e \, dt + K_D \cdot \frac{de}{dt}$$

| Term | Effect | Too High | Too Low |
|------|--------|---------|---------|
| **P** (Proportional) | Correction proportional to error | Oscillation | Sluggish response |
| **I** (Integral) | Corrects accumulated steady-state error | Winding up / slow oscillation | Drift |
| **D** (Derivative) | Dampens rapid changes (prevents overshoot) | High-frequency vibration amplified | Overshoots |

Well-tuned PID = smooth, responsive, wobble-free flight.

### 4.2 PID Tuning Tools

- **Betaflight Configurator** (FPV drones): Auto-tune via Blackbox analysis
- **Mission Planner AutoTune** (ArduPilot): Automated PID tuning in flight
- **PX4 SysID**: System identification toolchain

---

## 5. Flight Controller Firmware

### 5.1 Popular Firmware Platforms

| Firmware | Hardware Targets | Primary Use |
|---------|-----------------|------------|
| **Betaflight** | Any F4/F7 FC | FPV racing & freestyle |
| **ArduPilot** | Pixhawk, CubeOrange, Matek H743 | Autonomous fixed/multi-rotor |
| **PX4** | Pixhawk family | Research, commercial autonomous drones |
| **iNav** | F4/F7 FCs | Fixed-wing + multirotor navigation |
| **Cleanflight** | Legacy | Outdated — replaced by Betaflight |

### 5.2 PX4 Flight Stack — 5 Core Functions

PX4 is widely used in academic and commercial settings. Its 5 principal functions:

1. **State Estimation** — Fuses sensor data (IMU, GPS, barometer, vision) using EKF2 (Extended Kalman Filter) to estimate position, velocity, and attitude
2. **Flight Control** — PID-based attitude and position controllers; translates setpoints into actuator commands
3. **Mission Execution** — Follows GPS waypoint missions; supports take-off, loiter, land, RTL behaviours
4. **Safety Management** — Failsafe triggers on RC loss, battery low, geofence breach
5. **Communication (MAVLink)** — Bidirectional protocol for telemetry, parameters, mission upload/download, GCS connection

### 5.3 ArduPilot Flight Modes

| Mode | GPS Needed | Description |
|------|-----------|-------------|
| Stabilize | No | FC levels the craft; pilot provides all inputs |
| AltHold | No | Barometer-locked altitude; pilot controls position |
| Loiter | Yes | GPS position + altitude hold; GPS required |
| Auto | Yes | Executes waypoint mission |
| RTL | Yes | Returns to launch point and lands |
| Land | No | Descends and lands at current position |
| Acro | No | Pure rate mode; no self-levelling |

---

## 6. GPS & Autonomous Navigation

### 6.1 How GPS Works on a Drone

The GPS receiver receives signals from ≥ 4 satellites. Using **trilateration** (time-of-arrival of signals), it calculates latitude, longitude, and altitude.

For a drone, GPS enables:
- **Position Hold (Loiter)**: Maintains a fixed coordinate in 3D
- **Waypoint Navigation**: Autonomous mission along GPS coordinates
- **Return to Home (RTH)**: Automatically returns on signal loss or battery alarm
- **Geofencing**: Prevents flight beyond a defined boundary

### 6.2 GPS Accuracy

| Technology | Accuracy |
|-----------|---------|
| Standard GPS (L1 only) | ±3–5 m |
| SBAS/WAAS corrected | ±1–3 m |
| RTK GPS (Real-Time Kinematic) | ±1–2 cm |

RTK GPS is used in professional survey drones where centimetre-level precision is needed.

---

## 7. Telemetry

Telemetry allows the **Ground Control Station (GCS)** to receive real-time flight data from the drone:

| Data Streamed | Use |
|--------------|-----|
| Attitude (roll/pitch/yaw) | Monitor stability |
| GPS position & altitude | Track drone location |
| Battery voltage & current | Monitor power health |
| Airspeed / groundspeed | Performance analysis |
| Mode & arming state | Safety monitoring |
| ESC temperatures | Prevent overheating |

Common telemetry hardware: **SiK radio 915/433 MHz**, **Wi-Fi MAVLink bridge**, **LTE cellular telemetry**.

---

## See Also
- [[Drone Technology Sensors]] — Detailed breakdown of individual sensors
- [[Electronic Speed Controller]] — How FC commands translate to ESC outputs
- [[Drone Batteries]] — Power system that the FC monitors
- [[Propellors & Motors]] — The actuators the FC ultimately controls
- [[Aerial Terminology in Drones]] — Flight modes and maneuver physics

---
*Unit 3 — Drone Hardware Devices | Drone Technology — BTech Sem 5*
