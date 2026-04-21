---
Title: "Drone Tech Lab 3"
Status: 
marker: 
tags: 
Date: "2025.09.22"
Time: "16:26"
---
# Lab Report: ArduPilot Flight Mode Simulation
Date: September 22, 2025

### 1. Aimd
To simulate and analyze the behavior of a drone under different flight modes and conditions within the ArduPilot software-in-the-loop (SITL) environment. Specifically, this report documents the simulation of a GPS failure and its effect on the vehicle's state.
### 2. Pre-requisites
- Basic understanding of Unmanned Aerial Vehicles (UAVs) and their core components.
- Familiarity with the ArduPilot flight stack and the Mission Planner (or a similar MAVLink-based) ground control station.
- MAVProxy installed and configured for SITL simulation.
### 3. Simulation and Analysis
The simulation was conducted using MAVProxy to interact with the ArduPilot SITL instance. The primary goal was to observe the system's response to a simulated GPS signal loss.

#### 3.1. Initial State and Parameter Check
The simulation was initiated, and the vehicle's parameters were accessed through the MAVProxy command line. The focus was on the SIM_GPS_DISABLE parameter, which is used in SITL to emulate the loss of the GPS signal. A value of 0 indicates the GPS is functioning, while 1 indicates it is disabled. The initial check confirmed the GPS was active.

This image shows a list of flight parameters in the terminal. The command param show sim_gps_disable is used to verify the initial state of the simulated GPS, which is enabled (0.000000).
#### 3.2. Simulating GPS Failure
To simulate a GPS failure, the SIM_GPS_DISABLE parameter was changed from 0 to 1. This action instructs the simulator to stop sending GPS data to the flight controller software. Subsequently, the parameter was set back to 0 to simulate the recovery of the GPS signal.

This image demonstrates the process of inducing a GPS failure. The command param set sim_gps_disable 1 disables the GPS, and param set sim_gps_disable 0 re-enables it, allowing for the analysis of the drone's response to both signal loss and recovery.
#### 3.3. System Response in MAVProxy Console
The MAVProxy console provides a real-time feed of the vehicle's status. During the simulation, several key events and warnings were observed, indicating how the flight controller's Extended Kalman Filter (EKF) was handling the loss of sensor data.

This console view captures the drone's state during the test. Key takeaways include:
- Mode: The drone is in STABILIZE mode, which does not require GPS to fly.
- Status: The vehicle is ARMED.
- GPS: The GPS: OK6 (10) status indicates a good GPS lock before the failure simulation.
- Warnings:
- Flight battery warning: Indicates the simulated battery is low.
- APM: EKF3 lane switch 1: The EKF, which fuses sensor data to estimate the drone's state (position, velocity, etc.), has switched to a different "lane" or core, likely in response to sensor inconsistency.
- APM: EKF variance: Indicates a high level of uncertainty in the EKF's state estimate.
- APM: EKF3 IMU1 stopped aiding: The system has stopped using one of the IMUs to aid its position estimate, a direct consequence of the GPS data becoming unavailable.
- APM: EKF3 IMU0 is using GPS: This message would appear upon the recovery of the GPS signal, showing the EKF re-integrating the GPS data into its calculations.

## Images for Reference
![[IMG-20260420174736646.png]]![[IMG-20260420174736669.png]]![[IMG-20260420174736688.png]]![[IMG-20260420174736708.png]]![[IMG-20260420174736728.png]]
# References


###### Information
- date: 2025.09.22
- time: 16:26