
# **Antivirus Software Strategies**

**Prevention**
Block infection routes using software policies, restricted privileges, scanning downloads, and email filtering.

**Detection**
Identify malware using signatures, heuristics, anomaly detection, and behavior analysis.

**Identification**
Determine the specific virus variant present on the system.

**Removal**
Clean or quarantine infected files and restore their original state.

Antivirus solutions focus on:
— Virus signatures
— Suspicious storage patterns
— Execution behavior
— File and network transmission patterns

---

# **Prevention of Virus Infections**

* Use software from trusted vendors only.
* Test new software in isolated environments.
* Open attachments only when validated.
* Maintain system images for recovery.
* Keep clean backups of system executables.
* Run antivirus software regularly and keep definitions updated.

---

# **Truths and Misconceptions about Viruses**

* Viruses are not restricted to Windows—any OS can host them.
* Hidden or read-only files can still be modified by viruses.
* Viruses can appear in any type of file, not only executables.
* Viruses spread via multiple channels, not just disks or email.
* Viruses cannot survive a cold boot (complete power-off).
* Viruses cannot infect physical hardware.
* Viruses can be malicious, benign, or even beneficial in rare cases.

---

# **Worms**

A worm replicates across networked systems without attaching itself to a host program. It spreads automatically using vulnerabilities or open connections.

Propagation categories include:
— Internet scanning worms
— Email worms
— Peer-to-peer worms
— Web worms
— Mobile worms

Worms typically do not require user interaction beyond initial exposure.

---

# **Other Malicious Programs**

**Logic Bomb**
Hidden code triggered by a condition such as a date, event, or input.

**Time Bomb**
Triggers its payload when a specific time occurs.

**Rabbit**
Replicates infinitely, consuming system resources.

**Trojan Horse**
Appears to perform a useful function but secretly performs malicious actions using the host’s privileges.

**Backdoor / Trapdoor**
Hidden mechanism that bypasses normal authentication or checks.

**Auto-rooter**
Tools used by attackers to automatically exploit new machines.

**Rootkit**
Collection of tools used post-intrusion to hide presence, maintain access, and manipulate the OS.

---

# **Targeted Malicious Code**

**Trapdoor**
Undocumented entry in software for hidden access.

**Salami Attack**
Steals small amounts (e.g., rounding fractions of cents) that accumulate into large theft.

**Privilege Escalation**
Gaining higher privileges than granted.

**Keyloggers**
Capture keystrokes for credential theft.

**Mobile Code**
Executable code delivered by browsers or scripts (JavaScript, Java, ActiveX).

**Covert Channels**
Unauthorized channels that leak information.
Types:
— Storage: Uses presence/absence of objects in storage (e.g., creating/deleting files).
— Timing: Uses differences in execution time to convey information.

---

# **Controls Against Program Threats**

**Modularity**
Design components so each unit is independent and inspectable.

**Encapsulation**
Limit interfaces to reduce ways data can leak.

**Information Hiding**
Restrict internal details so they cannot affect unrelated components.

---

# **Additional Controls**

**Peer Reviews**
Independent checking for logic errors, malicious insertions, or vulnerabilities.

**Hazard Analysis**
Formal techniques to identify hazardous states.

**Testing Types**
Unit, integration, functional, performance, acceptance, installation, and regression testing.

**Good Design Practices**
Fault tolerance, consistent error handling, recorded design rationale.

**Prediction**
Assess risk of vulnerabilities during design.

**Static Analysis**
Tools that examine code structure for flaws without executing it.

**Configuration Management**
Control changes, versions, and patches.

**Analysis of Mistakes**
Review past faults to avoid repeated vulnerabilities.

**Program Correctness Proofs**
Mathematically prove absence of security flaws.

---

# **Operating System Controls**

**Trusted Software**
Software developed under strict engineering, security, and auditing requirements.

**Functional Correctness**
Confidence the software performs as intended.

**Integrity Enforcement**
Ensures data consistency and prevents corruption.

**Limited Privilege**
Runs with the least privileges necessary.

**Mutual Suspicion**
Each program assumes others may be untrusted.

**Confinement**
Restricts what resources a program can access (sandboxing).

**Access Log**
Records which users or programs accessed resources, with timestamps.

---

# **Administrative Controls**

**Development Standards**
Rules for coding, design, documentation, and project management.

**Testing Standards**
Procedures for rigorous testing.

**Configuration Standards**
Clear guidelines for version control and release management.

**Security Audits**
Independent evaluation of the system’s security posture.

**Separation of Duties**
No single individual controls all sensitive steps; reduces insider threat.

---
