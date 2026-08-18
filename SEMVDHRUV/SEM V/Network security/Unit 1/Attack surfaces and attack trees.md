## Attack Surfaces

- **Definition:** The total set of points where an attacker can try to enter, interact with, or extract data from a system.
- **Components:**
    - **Network Surface:** Open ports, protocols, exposed services.
    - **Software Surface:** Applications, APIs, libraries, input validation flaws.
    - **Human Surface:** Social engineering, phishing, insider threats.
    - **Physical Surface:** Devices, hardware interfaces, physical access points.
- **Goal of Defense:** Minimize the attack surface by reducing unnecessary exposure, hardening configurations, and monitoring entry points.

---

## Attack Trees

- **Definition:** A hierarchical model representing possible ways an attacker can achieve a goal.
- **Structure:**
    - **Root Node:** Attacker’s ultimate objective (e.g., steal data, gain root access).
    - **Branches:** Different strategies or sub‑goals leading to the root.
    - **Leaf Nodes:** Specific actions or exploits required.
- **Types of Nodes:**
    - **AND nodes:** All child conditions must be met.
    - **OR nodes:** Any child condition can achieve the goal.
- **Use Cases:**
    - Threat modeling.
    - Risk assessment.
    - Prioritizing defenses.

---

## Comparison

|Aspect|Attack Surface|Attack Tree|
|---|---|---|
|Focus|Entry points/exposure|Paths to achieve attacker’s goal|
|Representation|List or map of vulnerabilities|Hierarchical tree of attack strategies|
|Purpose|Identify and reduce exposure|Model attacker behavior and plan defenses|
|Defensive Action|Minimize, patch, monitor|Block critical paths, strengthen weak nodes|

---
