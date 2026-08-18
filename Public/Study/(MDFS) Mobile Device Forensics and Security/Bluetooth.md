---

Title: "Bluetooth"

Status:

marker:

tags:

Date: "2026.04.30"

Time: "12:36"

---
# Bluetooth

## Definition

> “Bluetooth is a short-range wireless communication technology used to connect devices.”

* Type: **Wireless Personal Area Network (WPAN)**
* Range: typically **~10 meters** (can extend up to 100 m with amplifiers)
* Frequency band: **2.4 GHz ISM band**
* Supports:

  * Data transfer
  * Voice communication 

---

## How Bluetooth actually works

* Uses **frequency hopping (FHSS)**:

  * Switches frequencies rapidly to avoid interference
  * ~1600 hops per second across multiple channels

* Devices form small networks:

  * One device acts as **master**
  * Others act as **slaves**
  * This network is called a **piconet**

---

## Bluetooth Architecture

### Piconet

> “A small network of Bluetooth devices connected in an ad hoc manner.”

* 1 master + up to 7 active slaves
* Master controls communication and hopping pattern
* Devices synchronize with master

---

### Scatternet

* Multiple piconets connected together

* A device can:
  * Be master in one piconet
  * Be slave in another

* Enables **larger communication networks**

---

## Bluetooth 5.4

> “Bluetooth 5.4 focuses on large-scale, low-power, and secure device communication.”

### Key features

* **Periodic Advertising with Responses (PAwR)**
  * Enables communication with **hundreds/thousands of devices**
  * Useful for IoT (sensors, automation)

* **Encrypted Advertising Data**
  * Broadcast data can be encrypted
  * Improves privacy

* **LE GATT Security Levels**
  * Devices can check **security requirements before connecting**

* **Improved range and speed**
  * Better performance in industrial and smart environments

* **Enhanced security**
  * Stronger protection against unauthorized access

* **Channel selection algorithm**
  * Chooses best channel → more reliable communication

* **Link loss mitigation**
  * Reduces connection drops 

---

## Bluetooth Classic vs Bluetooth Low Energy (BLE)

> “Bluetooth has two main variants designed for different purposes.”

### Bluetooth Classic (BR/EDR)

* Designed for:
  * Continuous data streaming
  * Audio (headphones, speakers)

* Characteristics:
  * Higher power consumption
  * Uses **79 channels**
  * Stable point-to-point communication

---

### Bluetooth Low Energy (BLE)

* Designed for:
  * Low power devices
  * IoT, wearables, sensors

* Characteristics:
  * Very low power usage
  * Uses **40 channels**
  * Supports:
    * Broadcast
    * Mesh networks
    * Device positioning

---

## Key Differences

| Aspect            | Bluetooth Classic      | BLE             |
| ----------------- | ---------------------- | --------------- |
| Power consumption | High                   | Very low        |
| Use case          | Audio, continuous data | Sensors, IoT    |
| Channels          | 79                     | 40              |
| Communication     | Point-to-point         | Broadcast, mesh |
| Battery life      | Lower                  | Much higher     |



---

## Security Basics in Bluetooth

* **Authentication** → verifies device identity
* **Confidentiality** → prevents eavesdropping
* **Authorization** → controls access to services

---

## Simple understanding

> Bluetooth Classic = like a phone call (continuous connection)
> BLE = like sending small messages occasionally (energy efficient)

---

## Quick Summary

* Bluetooth = short-range wireless communication
* Uses **frequency hopping** to avoid interference
* Forms networks like **piconet/scatternet**
* Bluetooth 5.4 improves **IoT scalability, security, and efficiency**
* Classic vs BLE = **performance vs power efficiency trade-off**

  

# References


###### Information
- date: 2026.04.30
- time: 12:36