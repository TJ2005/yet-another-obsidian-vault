---

Title: "Protocol to Avoid getting Caught"

Status:

marker:

tags:

Date: "2026.02.03"

Time: "15:19"

---


## 1. Primary Network Scan List

These are the core scanning techniques used by Nmap and other network mappers. They are categorized by their "noise" level and how they interact with the TCP stack.

| Scan Category | Specific Scan Types |
| --- | --- |
| **Connection-Oriented** | TCP Connect Scan (`-sT`) |
| **Half-Open / Stealth** | SYN Stealth Scan (`-sS`) |
| **Stateless / Spec Scans** | NULL (`-sN`), FIN (`-sF`), XMAS (`-sX`) |
| **Mapping / Discovery** | ACK Scan (`-sA`), UDP Scan (`-sU`), ICMP Scan (`-PE`, `-sn`) |
| **Advanced / Blind** | Idle (Zombie) Scan (`-sI`) |

---

## 2. Scan Analysis: Use, Commands, and Attacker Intent

### **TCP Connect Scan**

* **Mechanism:** Completes the full 3-way handshake (SYN → SYN/ACK → ACK).
* **Attacker Use:** Used when the attacker lacks "raw packet" privileges (non-root access) or wants to confirm a service is fully functional and accepting connections.
* **Command:** `nmap -sT <target>`
* **Pros:** Highly reliable; works on any networking stack.
* **Cons:** **High Noise.** Every connection is logged by the application (e.g., an Apache log entry).

### **SYN Stealth Scan (Half-Open)**

* **Mechanism:** Sends SYN; receives SYN/ACK; sends **RST** instead of the final ACK.
* **Attacker Use:** The "bread and butter" of reconnaissance. It gathers port info without establishing a full session.
* **Command:** `nmap -sS <target>`
* **Pros:** Faster than Connect scans; avoids some application-level logging.
* **Cons:** Requires root/admin privileges; easily flagged by modern IDS/IPS systems.

### **The "RFC 793" Scans (NULL, FIN, XMAS)**

* **Mechanism:** These send packets with unusual flag combinations. According to RFC 793, a closed port *must* respond with **RST**, while an open port *should* ignore the "garbage" packet.
* **Attacker Use:** Bypassing older, non-stateful firewalls that only look for the SYN flag to block new connections.
* **Commands:**
* **NULL:** `nmap -sN <target>` (No flags set)
* **FIN:** `nmap -sF <target>` (Finish flag only)
* **XMAS:** `nmap -sX <target>` (FIN, PSH, URG flags)


* **Pros:** Extremely stealthy against specific systems.
* **Cons:** Ineffective against modern Windows systems (they respond with RST for open and closed ports); often results in "Open|Filtered" results.

### **ACK Scan (Firewall Mapping)**

* **Mechanism:** Sends only the ACK flag.
* **Attacker Use:** This isn't for finding open ports; it's for **mapping firewall rules**.
* **Command:** `nmap -sA <target>`
* **Pros:** Determines if a firewall is "Stateful" (drops the ACK) or "Stateless" (sends an RST).
* **Cons:** Provides zero information about whether a port is actually open or closed.

### **Idle (Zombie) Scan**

* **Mechanism:** Spoofs the IP of a "Zombie" device. The attacker monitors the Zombie's IP ID increment to see if the Target responded to the Zombie.
* **Attacker Use:** Total anonymity. The Target sees the Zombie's IP, not the attacker's.
* **Command:** `nmap -sI <zombie_ip> <target_ip>`
* **Pros:** The "Ghost" scan; almost impossible to trace back to the attacker.
* **Cons:** Extremely slow; requires a "Zombie" host with a predictable IP ID increment.

---

## 3. Comparison & Reference Table

This table helps you quickly differentiate based on your defensive study goals.

| Scan Type | Visibility (Noise) | Target OS Suitability | Primary Goal |
| --- | --- | --- | --- |
| **TCP Connect** | **Very High** | Universal | Port Discovery / Service Confirmation |
| **SYN Scan** | **Medium** | Universal | Rapid Reconnaissance |
| **UDP Scan** | **Medium** | Universal | Finding DNS, SNMP, DHCP services |
| **XMAS / NULL** | **Low** | Mostly *NIX (Linux/BSD) | Firewall Evasion |
| **ACK Scan** | **Low** | Universal | Mapping Firewall Policy |
| **Idle Scan** | **Zero** | Requires specific Zombie | Maximum Stealth / Anonymity |

---

## 4. Glossary of Terms

* **RST (Reset):** A packet sent to immediately kill a connection. Defensively, it's the "I'm not here" or "Go away" signal.
* **IP ID:** A serial number in the IP header. If it increases predictably (e.g., +1 for every packet), it can be exploited by an Idle Scan.
* **Stateful Inspection:** A firewall feature that remembers the state of a connection. It won't allow an **ACK** through unless it previously saw a **SYN**.
* **RFC 793:** The "Law of the Land" for TCP. Many stealth scans rely on the fact that older systems follow this law literally, while modern ones (like Windows) have customized their behavior.
* **Filtered:** The port is behind a firewall, and Nmap cannot tell if it is open or closed because the firewall dropped the packet silently.

---


# References



###### Information
- date: 2026.02.03
- time: 15:19