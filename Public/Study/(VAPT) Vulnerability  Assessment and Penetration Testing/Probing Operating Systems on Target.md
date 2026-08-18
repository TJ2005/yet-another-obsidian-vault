---

Title: "Probing Operating Systems on Target"

Status:

marker:

tags:

Date: "2026.02.03"

Time: "15:38"

---
## 1. OS Fingerprinting Methodologies

Fingerprinting is split into two main approaches: **Active** (sending probes) and **Passive** (silently watching traffic).

### **Active Fingerprinting**

* **Actual Use:** An attacker sends "malformed" or "out-of-spec" packets to the target and records the responses. They then compare these responses against a database of known OS signatures (like `nmap-os-db`).
* **Command:** `nmap -O <target_ip>`
* **Pros:** Highly accurate; can often determine specific service pack or kernel versions.
* **Cons:** Very "noisy"; easily detected by Intrusion Detection Systems (IDS).

### **Passive Fingerprinting**

* **Actual Use:** An attacker sniffs existing network traffic (using tools like `p0f` or Wireshark) and analyzes fields like TTL and Window Size from legitimate packets.
* **Attacker Strategy:** Used when the attacker wants to remain completely invisible and avoid triggering any alerts.
* **Pros:** Undetectable; doesn't send a single packet to the target.
* **Cons:** Less accurate; requires existing traffic to be flowing from the target.

---

## 2. Common OS Signatures (The "Clues")

Attackers look for specific values in packet headers to identify the OS.

| Field | Linux (Common) | Windows (Common) | Reason for Difference |
| --- | --- | --- | --- |
| **TTL (Time to Live)** | **64** | **128** | Different kernels set different default "hop" limits. |
| **Window Size** | **~5840** | **~8192 / 65535** | Memory allocation strategies for the TCP buffer vary by OS. |
| **DF (Don't Fragment)** | Often Set (1) | Often Set (1) | Most modern OSs set this to prevent packet splitting. |
| **TOS (Type of Service)** | **0x00** | **0x00** | Usually zero, but some legacy systems or specialized routers vary here. |

---

## 3. Advanced Detection Techniques

### **The "Nmap -O" Logic**

Nmap doesn't just look at TTL. It sends a sequence of **16 probes** (TCP, UDP, and ICMP) and checks:

1. **TCP ISN (Initial Sequence Number):** Is it truly random (Linux/modern Windows) or predictable (older OSs)?
2. **TCP Options:** The order and type of options (like SACK or Window Scaling) are highly specific to kernel versions.
3. **IP ID Generation:** Does the IP ID increment by 1 (Incremental), or is it random? (Windows often uses "Broken Increment" due to byte-ordering).

### **Banner Grabbing**

* **Use:** Connecting to a service (like Port 80 for HTTP or 22 for SSH) to see if it "blabs" its version info.
* **Command:** `curl -I <target_ip>` or `telnet <target_ip> 80`
* **Attacker Intent:** If a banner says `Server: Microsoft-IIS/10.0`, the attacker knows with 100% certainty it is Windows Server 2016/2019.

---

## 4. Difference Table: Active vs. Passive

| Feature | Active Fingerprinting (`nmap -O`) | Passive Fingerprinting (`p0f`) |
| --- | --- | --- |
| **Interaction** | Sends crafted packets to target. | Sniffs existing traffic. |
| **Stealth** | **Low** (Aggressive/Noisy). | **High** (Invisible). |
| **Accuracy** | High (determines kernel/patch level). | Moderate (guesses OS family). |
| **Requirement** | Target must be reachable/responsive. | Must have access to the traffic path. |
| **Best For** | Penetration Testing / VAPT. | Stealthy Reconnaissance / APTs. |

---

## 5. Defensive Measures (The "Hardening")

To protect your OS from being identified:

* **Modify TTL:** Change the default TTL value in the registry (Windows) or via `sysctl` (Linux) to "lie" about your OS.
* *Linux Command:* `sysctl -w net.ipv4.ip_default_ttl=128` (Makes Linux look like Windows).

* **Block ICMP:** Disable ICMP "Unreachable" and "Echo Request" messages at the firewall to break Nmap's OS probes.
* **Scrub Banners:** Configure web and mail servers to hide version numbers (e.g., set `ServerTokens Prod` in Apache).


# References


###### Information
- date: 2026.02.03
- time: 15:38