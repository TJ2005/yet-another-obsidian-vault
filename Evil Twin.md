---

Title: "Evil Twin"

Status:

marker:

tags:

Date: "2026.04.30"

Time: "12:35"

---
## Evil Twin Attack

---

## Definition

> “An evil twin is a rogue Wi-Fi access point that mimics a legitimate network to trick users into connecting.”

* It looks like a **real Wi-Fi network**
* Uses the **same SSID (network name)** as a trusted network
* Created with **malicious intent** 

---

## What is actually happening

### Normal Wi-Fi behavior

* Devices automatically connect to:

  * Known networks
  * Strongest signal available

* Wi-Fi discovery works using:

  * **Beacons** (AP announcing itself)
  * **Probe requests/responses** (device searching for networks)

---

### Evil twin exploitation

> “Wi-Fi does not verify the identity of access points before connection.”

* Attacker creates a **fake access point**
* Broadcasts same SSID as real network
* Places it **closer to victim** → stronger signal

Device behavior:

* Sees two networks with same name
* Chooses the **stronger signal (attacker’s AP)**

---

## Step-by-step attack flow

1. Attacker scans for a legitimate network (e.g., café Wi-Fi)
2. Identifies SSID using tools
3. Creates **software-based fake access point**
4. Victim device auto-connects (no suspicion)
5. Attacker now sits **between user and internet (MITM)**

> Similar to a man-in-the-middle attack in wired networks 

---

## Why this works

### Weakness in Wi-Fi design

* Access points are **not required to prove identity**
* Management packets can be **forged easily**
* Encryption (WEP/WPA/WPA2):

  * Happens **after connection**
  * Cannot stop connecting to fake AP 

---

## What attacker can do

* Capture:

  * Login credentials
  * Emails
  * Session cookies
* Perform:

  * Phishing attacks
  * Traffic interception
  * Session hijacking

---

## Real-world examples

* Fake café Wi-Fi stealing login details
* Airport/railway Wi-Fi clones
* Campus Wi-Fi impersonation
* Fake hotspot mimicking saved networks 

---

## Key concept

> “The attack doesn’t break encryption — it tricks you into connecting to the wrong network.”

---

## Countermeasures

### User-side protection

* Disable **auto-connect**
* Verify correct network before connecting
* Use **VPN on public Wi-Fi**
* Check **HTTPS (padlock)** before entering credentials
* Avoid sensitive activity on public Wi-Fi 

---

### Device/OS-level protection

* Enable **MAC address randomization**
* Remove unused saved networks
* Use built-in security warnings (OS alerts)

---

## Simple analogy

> Real Wi-Fi = official bank branch
> Evil twin = fake branch with same name outside

You enter the fake one → they collect everything you give

---

## Quick Summary

* Evil twin = fake Wi-Fi impersonating real network
* Exploits **automatic connection behavior**
* Leads to **man-in-the-middle attacks**
* Prevention = **verification + cautious usage**

  

# References


###### Information
- date: 2026.04.30
- time: 12:35