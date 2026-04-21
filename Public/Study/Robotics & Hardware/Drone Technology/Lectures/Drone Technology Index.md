---
Title: "Drone Technology Index"
Status: Active
tags: drone-technology, index, btech, sem-5
Date: "2026.02.01"
Unit: index
---
# Drone Technology
### BTech Cyber Security — Semester 5 | 3 Credits | 30 Hours

> **Teaching Scheme**: 2 Lecture Hours + 2 Practical Hours per week
> **Assessment**: 50 marks internal (ICA) + 50 marks theory exam (3 hrs)

---

## Unit 1 — Introduction to UAV Systems (6 hrs)

**Syllabus Topics**: UAV definition, aviation history, UAV fundamentals and terminology, classes and missions, examples by size, drone parts (hardware/software/mechanical), ground controllers, military/industrial/commercial use cases.

| Note | Coverage |
|------|---------|
| [[Drone]] | UAV definition, 10 key components, 5 classification axes, applications, Indian regulations |
| [[Aerial Terminology in Drones]] | Thrust vs weight, Newton's laws, roll/pitch/yaw axes, all maneuvers, flight modes |

---

## Unit 2 — Drone System Design Flow (8 hrs)

**Syllabus Topics**: System design, mechanical design (propellers, X-frame), hardware block diagram, power architecture, linear/switching regulators, battery estimation and constraints.

| Note | Coverage |
|------|---------|
| [[Propellors & Motors]] | Propeller physics, diameter/pitch, CW/CCW, blade design, BLDC motors, KV rating, high KV vs low KV, selection guide |
| [[Thrust Dependencies]] | Full thrust equation, effect of KV/voltage/diameter/pitch/blades/material/altitude |
| [[Electronic Speed Controller]] | ESC function, PWM/DShot protocols, MOSFET commutation, 5 ESC types, BEC, BLHeli_32, calibration |
| [[Power Distribution in a drone]] | Power chain, PDB, voltage regulation, connectors, wire gauges, common issues |
| [[Drone Batteries]] | LiPo chemistry, S/P notation, C-rating, energy calculation, LiPo vs Li-Ion, safety rules |

---

## Unit 3 — Drone Hardware Devices (6 hrs)

**Syllabus Topics**: UAV sensors (accelerometers, rate gyros, pressure sensors, compass, GPS), communication (Wi-Fi, Bluetooth, 3G/4G, RF), imaging systems, flight controllers (MCU/MPU, FPGA).

| Note | Coverage |
|------|---------|
| [[Drone Technology Sensors]] | Accelerometer (ADXL335), gyroscope (Coriolis), magnetometer, barometer (BMP388), GPS trilateration, ultrasonic HC-SR04, optical flow, LiDAR |
| [[Flight Controller & Communication]] | Transmitter/receiver/protocols (PWM/SBUS/ELRS), FC tiers, PID control theory, ArduPilot/PX4/Betaflight, GPS navigation, telemetry |

---

## Unit 4 — Autonomous Control of Mini Quadrotor (10 hrs)

**Syllabus Topics**: Mini quadrotor introduction, experimental platform, embedded control system, sensor and control units, wireless camera + modem, controller design and modelling, drone security threats.

| Note | Coverage |
|------|---------|
| [[Flight Controller & Communication]] | PX4 5 functions, state estimation EKF, mission execution, MAVLink |
| *Autonomous Controller Design* | *(See lab notes — SITL simulation, Mission Planner)* |

> Unit 4 is covered practically through the ArduPilot SITL labs.

---

## Labs & Practical Work

| Lab | Topic | Status |
|-----|-------|--------|
| Drone Tech Lab 1 | Introduction to RDS Simulator; drone types and specs | Basic |
| [[Drone Tech Lab 2]] | Drone construction, types (quad/hexa/octo), UAV categorisation | K057 — Complete |
| Drone Tech Lab 3 | ArduPilot SITL — GPS failure simulation and EKF response | Complete |
| Drone Tech Lab 4 | Autonomous mission using Mission Planner | Complete |

---

## Quick Reference

### By Component

| Component | Note |
|-----------|------|
| Motors & Propellers | [[Propellors & Motors]] |
| Thrust Analysis | [[Thrust Dependencies]] |
| ESC (Speed Controller) | [[Electronic Speed Controller]] |
| Battery | [[Drone Batteries]] |
| Power Distribution | [[Power Distribution in a drone]] |
| Flight Controller | [[Flight Controller & Communication]] |
| Sensors | [[Drone Technology Sensors]] |
| Flight Physics | [[Aerial Terminology in Drones]] |
| Drone Overview | [[Drone]] |

### By Exam Topic

| Exam Topic | Where to Study |
|-----------|----------------|
| UAV definition & classes | [[Drone]] §1–3 |
| Drone flight physics | [[Aerial Terminology in Drones]] §2–5 |
| Trust equation & factors | [[Thrust Dependencies]] §1–3 |
| Motor KV rating | [[Propellors & Motors]] §3 |
| ESC working principle | [[Electronic Speed Controller]] §3 |
| ESC types (BEC, OPTO, BLHeli) | [[Electronic Speed Controller]] §5 |
| Battery C-rating | [[Drone Batteries]] §2.3 |
| Sensors & how they work | [[Drone Technology Sensors]] §2–6 |
| PID control | [[Flight Controller & Communication]] §4 |
| PX4 functions | [[Flight Controller & Communication]] §5.2 |
| Transmitter frequencies | [[Flight Controller & Communication]] §2.1 |

---
*Drone Technology — BTech Cyber Security Sem 5 | MPSTME*
