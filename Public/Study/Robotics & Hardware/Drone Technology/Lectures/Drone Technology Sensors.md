---
Title: "Drone Technology Sensors"
Status: Active
tags: unit-3, sensors, IMU, accelerometer, gyroscope, GPS, barometer, ultrasonic, magnetometer
Date: "2025.10.06"
Unit: 3
---
# Drone Technology Sensors

**Related Notes**: [[Drone Technology Index]] | [[Flight Controller & Communication]] | [[Aerial Terminology in Drones]] | [[Drone]]

**Unit**: [[Drone Technology Index#Unit 3|Unit 3 — Drone Hardware Devices]]

---

## 1. Why Sensors Matter

Drones are inherently unstable — unlike a car or boat, a multirotor will tumble immediately if the flight controller stops making corrections. Sensors provide the **continuous stream of data** the FC uses to maintain stable, controllable flight.

The sensor suite enables:
- **Attitude estimation** — knowing the drone's orientation at all times
- **Altitude hold** — maintaining a fixed height
- **GPS navigation** — position hold, waypoints, RTH
- **Obstacle avoidance** — detecting nearby objects

---

## 2. Inertial Measurement Unit (IMU)

The IMU is the most critical sensor on any drone. It combines two complementary sensors:

### 2.1 Accelerometer

The **accelerometer** measures **linear acceleration** along all 3 axes (X, Y, Z) in units of g (gravitational force equivalent).

| Spec | Common Value |
|------|-------------|
| Sensor IC | ADXL335, MPU6050, ICM42688 |
| Measurement Range | ±2g to ±16g (configurable) |
| Sensitivity (ADXL335) | 300 mV/g |
| Axis | 3-axis |

**How it works:**
Inside the chip, a tiny proof mass is suspended by microscopic springs. Acceleration deflects the mass, and that deflection is measured as a voltage change by capacitive sensing.

**What accelerometers tell the FC:**
- Tilt angle relative to gravity (attitude at rest)
- Linear velocity changes
- Vibration level (used for motor health monitoring)

**Limitation**: In dynamic flight, accelerometers measure both gravity and motion — they cannot distinguish between "tilted" and "accelerating horizontally." That's why we pair with a gyroscope.

### 2.2 Gyroscope

The **gyroscope** measures **angular velocity** — how fast the drone is rotating around each axis — in degrees per second (°/s).

| Spec | Common Value |
|------|-------------|
| Sensor IC | MPU6050, MPU6500, ICM42688 |
| Measurement Range | ±250°/s to ±2000°/s |
| Axis | 3-axis (roll rate, pitch rate, yaw rate) |

**How it works (MEMS Gyroscope):**
Uses the **Coriolis effect** — a vibrating micro-structure is deflected when it rotates, and that deflection is detected as a voltage signal.

**What gyroscopes tell the FC:**
- Rate of rotation about each axis (used for PID D-term)
- Very fast response (>1 kHz sampling)
- Accurate for short times but **drifts** over time (integration error accumulates)

### 2.3 Sensor Fusion — Why Both Are Needed

| Sensor | Strength | Weakness |
|--------|----------|---------|
| Accelerometer | Accurate long-term tilt reference | Noisy during dynamic motion |
| Gyroscope | Fast, low-noise angular rate | Drifts over time |

The FC uses a **complementary filter** or **Extended Kalman Filter (EKF)** to fuse both:
- Gyroscope provides fast, short-term attitude changes
- Accelerometer corrects gyro drift over time

$$\hat{\theta}(t) = \alpha \cdot (\hat{\theta}_{t-1} + \omega \cdot \Delta t) + (1-\alpha) \cdot \theta_{\text{acc}}$$

where $\alpha \approx 0.98$ (high weighting on gyro, small accelerometer correction).

---

## 3. Magnetometer (Electronic Compass)

The **magnetometer** measures the Earth's magnetic field to determine the drone's **heading (yaw angle)** relative to magnetic north.

| Spec | Details |
|------|---------|
| Sensor IC | HMC5883L, QMC5883L, LIS3MDL |
| Axis | 3-axis |
| Output | Magnetic field strength in each axis (µT) |

$$ \text{Heading} = \arctan\left(\frac{B_y}{B_x}\right) $$

**Critical for**: GPS-dependent flight modes (Loiter, Auto, RTL) — the FC must know which way the drone is facing to translate "fly north" into motor commands.

**Interference warning**: Must be mounted **away from motors and power wires** (high current = magnetic field that confuses the magnetometer). Usually mounted on the GPS mast.

---

## 4. Barometer (Pressure Sensor)

The **barometer** measures atmospheric pressure to determine the drone's **altitude** above the launch point.

| Spec | Details |
|------|---------|
| Sensor IC | BMP388, BMP280, MS5611 |
| Altitude Resolution | BMP388: ±0.5 m |
| Measurement | Absolute pressure + temperature compensation |

**How it works:**
$$P = P_0 \cdot \left(1 - \frac{h}{44330}\right)^{5.255}$$

where $P_0 = 101{,}325$ Pa (sea-level pressure) and $h$ = altitude in metres.

The FC differentiates pressure measurements to estimate altitude change (climb/descent rate).

**Limitations**:
- Wind pressure changes can cause false readings
- Must be shielded from prop wash with foam pad
- Temperature changes affect accuracy

---

## 5. GPS Module

The **GPS module** provides absolute geographic position (latitude, longitude, altitude) and velocity.

### 5.1 How GPS Works on a Drone

GPS receivers detect microwave signals from multiple satellites. Each signal contains the satellite's position and precise timestamp. The receiver calculates its distance from each satellite using signal travel time:

$$d = c \cdot \Delta t$$

With distances from ≥ 4 satellites, the receiver solves 4 simultaneous equations for X, Y, Z, and clock offset — this is **trilateration**.

### 5.2 Specifications

| Parameter | Value |
|-----------|-------|
| Frequencies | L1 (1575.42 MHz), some with L1+L2 |
| Update Rate | 1–10 Hz (standard), 18 Hz+ (high-performance) |
| Cold Start Time | 30–60 seconds |
| Standard Accuracy | ±3–5 m horizontal |
| With RTK | ±1–2 cm |

### 5.3 GPS Modules Common in Drones

| Module | Features |
|--------|---------|
| **U-blox M8N** | Standard, 72-channel, 10 Hz, GLONASS+GPS |
| **U-blox F9P** | RTK capable, 1 cm accuracy, 25 Hz |
| **BN-880** | Budget, integrated compass |

### 5.4 What GPS Enables

| Function | Description |
|---------|-------------|
| Position Hold | Drone maintains exact GPS coordinate |
| Waypoint Navigation | Autonomous flight between GPS points |
| Return to Home (RTH) | Operator trigger or failsafe → fly home |
| Geofencing | Prevent flight outside defined boundary |
| Speed Measurement | Ground speed from Doppler shift |

---

## 6. Ultrasonic Sensor (HC-SR04)

The **ultrasonic sensor** measures distance to objects below the drone using sound waves.

| Spec | Details |
|------|---------|
| Module | HC-SR04 |
| Range | 2 cm – 4 m |
| Angle | 15° cone |
| Frequency | 40 kHz ultrasonic pulses |
| Accuracy | ±3 mm |

**How it works:**
1. Trigger pin sends 40 kHz ultrasonic burst
2. Burst reflects off surface below
3. Echo pin goes HIGH when pulse returns
4. Distance = (time × speed of sound) / 2

$$d = \frac{v \cdot t}{2} = \frac{340 \, \text{m/s} \times t}{2}$$

**Use in drones**: Low-altitude hold (landing assist, terrain following below ~3 m), obstacle detection.

**Limitations**: Only works on flat, non-absorptive surfaces; limited range; carpet and foam absorb sound poorly.

---

## 7. Optical Flow Sensor

The **optical flow sensor** is like a downward-facing optical mouse — it detects relative horizontal movement by analysing ground texture.

| Feature | Details |
|---------|---------|
| Method | Image processing (similar to computer mouse) |
| Pairs With | Ultrasonic (height) or LIDAR |
| Enables | Position hold **without GPS** (indoors) |
| Accuracy | Depends on altitude and surface texture |

Used in indoor drones where GPS is unavailable.

---

## 8. LiDAR (Light Detection and Ranging)

LiDAR uses **laser pulses** to measure precise distances (similar to ultrasonic but using light).

| Parameter | Value |
|-----------|-------|
| Range | 0.1 m – 100+ m (depending on module) |
| Accuracy | ±2 cm |
| Frequency | Up to 100 Hz |
| Weight | 50–300 g |

Used for: terrain following, precision altitude hold, 3D mapping.

---

## 9. Sensor Summary Table

| Sensor | Measures | For | Update Rate |
|--------|---------|-----|-------------|
| Accelerometer | Linear acceleration | Attitude, vibration | 1–8 kHz |
| Gyroscope | Angular velocity | Attitude rate, PID | 1–8 kHz |
| Magnetometer | Magnetic heading | Yaw reference for GPS modes | 50–100 Hz |
| Barometer | Atmospheric pressure | Altitude hold | 25–50 Hz |
| GPS | Position, velocity | Navigation, waypoints | 1–18 Hz |
| Ultrasonic | Distance below | Landing, low-alt hold | 40 Hz |
| Optical Flow | Ground-relative velocity | Indoor position hold | 30–120 Hz |
| LiDAR | Precise laser distance | Terrain following, mapping | 50–100 Hz |

---

## See Also
- [[Flight Controller & Communication]] — How sensors feed the FC's algorithms
- [[Aerial Terminology in Drones]] — How sensor data relates to flight physics
- [[Drone]] — Overview of all drone components including sensors
- [[Electronic Speed Controller]] — What sensor data ultimately controls

---
*Unit 3 — Drone Hardware Devices | Drone Technology — BTech Sem 5*
