---

Title: "System Adminstrator Lab 7"

Status:

marker:

tags:

Date: "2026.04.18"

Time: "20:28"

---
# **Experiment 8: Implementation of Security Policy**

---
**Name:** Tejas Sahoo
**Roll Number:** K057

## **Aim**

To implement security policies for hardening the security posture of a Linux system.

---

## **Learning Outcomes**

1. Explain the need for a secure Linux system.
2. Implement simple but effective host security policies.

---

## **Theory**

Security in system administration should be integrated into day-to-day operations, not treated as a one-time setup task. A strong security posture combines preventive controls and response planning.

A secure system should:
- Reduce the attack surface through strict access control and service hardening.
- Detect abnormal or malicious activity through logging and audit tools.
- Prepare for incidents with clear procedures for recovery and containment.

Threats may come from external attackers (random scanning, targeted attacks) as well as internal users (misconfiguration, privilege misuse, or malicious behavior). Security policy must address both categories.

---

## **Procedure & Observations**

### **Task 1: Configure Automatic Security Updates**

Two common approaches can be used.

**Method 1: GNOME Update Manager**
1. Open `System -> Administration -> Update Manager -> Settings`.
2. In `Updates`, choose `Install security updates without confirmation`.

**Method 2: unattended-upgrades package**

```bash
sudo apt-get update
sudo apt-get install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

![[IMG-20260420174736838.png]]

**Observation:** Automatic security patching was enabled to reduce vulnerability exposure window.

---

### **Task 2: Harden Host Firewall with UFW**

Check firewall status:

```bash
sudo ufw status verbose
```

![[IMG-20260420174736903.png]]

Allow DNS traffic on port 53 (TCP/UDP):

```bash
sudo ufw allow 53
```

![[IMG-20260420174736936.png]]

Allow and deny FTP service as policy test:

```bash
sudo ufw allow ftp
sudo ufw deny ftp
sudo ufw status
```

![[IMG-20260420174736982.png]]

Enable firewall logging:

```bash
sudo ufw logging on
```

![[IMG-20260420174737013.png]]

Disable ping replies by editing `/etc/ufw/before.rules` and changing echo-request handling from `ACCEPT` to `DROP` (or commenting it out), then reload UFW:

```bash
sudo ufw reload
```

![[IMG-20260420174737052.png]]

**Observation:** UFW policy was validated, logging enabled, and ICMP echo reply handling restricted as part of hardening.

---

### **Task 3: Protect `su` by Limiting Access to Admin Group**

Create admin group and add administrative user:

```bash
sudo groupadd admin
sudo usermod -a -G admin <admin_username>
```

Restrict `/bin/su` using statoverride:

```bash
sudo dpkg-statoverride --update --add root admin 4750 /bin/su
```

Verify:

```bash
ls -l /bin/su
getent group admin
```

![[IMG-20260420174737097.png]]
![[IMG-20260420174737146.png]]
![[IMG-20260420174737169.png]]

**Observation:** Privilege escalation via `su` was restricted to users in `admin` group only.

---

### **Task 4: Harden Network Stack Using `sysctl`**

Edit `/etc/sysctl.conf` and add or un-comment the following:

```conf
# IP spoofing protection
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1

# Ignore ICMP broadcast requests
net.ipv4.icmp_echo_ignore_broadcasts = 1

# Disable source packet routing
net.ipv4.conf.all.accept_source_route = 0
net.ipv6.conf.all.accept_source_route = 0
net.ipv4.conf.default.accept_source_route = 0
net.ipv6.conf.default.accept_source_route = 0

# Ignore send redirects
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.default.send_redirects = 0

# Block SYN attacks
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_max_syn_backlog = 2048
net.ipv4.tcp_synack_retries = 2
net.ipv4.tcp_syn_retries = 5

# Log martian packets
net.ipv4.conf.all.log_martians = 1
net.ipv4.icmp_ignore_bogus_error_responses = 1

# Ignore ICMP redirects
net.ipv4.conf.all.accept_redirects = 0
net.ipv6.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
net.ipv6.conf.default.accept_redirects = 0

# Ignore directed pings
net.ipv4.icmp_echo_ignore_all = 1
```

Reload kernel parameters:

```bash
sudo sysctl -p
```

![[IMG-20260420174737195.png]]
![[IMG-20260420174737218.png]]

**Observation:** Kernel-level networking safeguards were applied successfully.

---

### **Task 5: Audit System Security Using Tiger**

Install Tiger:

```bash
sudo apt-get install tiger
```

![[IMG-20260420174737237.png]]

Run audit:

```bash
sudo tiger
```

Tiger output location:

```bash
ls /var/log/tiger
```

![[IMG-20260420174737260.png]]

View security report:

```bash
sudo less /var/log/tiger/security.report.*
```

![[IMG-20260420174737465.png]]
![[IMG-20260420174737492.png]]
![[IMG-20260420174737513.png]]

**Observation:** Tiger generated audit reports that help identify misconfigurations and security weaknesses.

---

## **Result**

Linux host security hardening was implemented through automated updates, firewall policy enforcement, privilege control for `su`, network kernel hardening with `sysctl`, and system audit using Tiger.

---

## **Review Questions**

1. **Write a note on `sysctl`.**  
   `sysctl` is a Linux interface used to view and modify kernel parameters at runtime. These parameters control behavior of networking, memory, filesystem, and process management. Temporary changes can be made using `sysctl -w`, while persistent changes are stored in `/etc/sysctl.conf` (or files under `/etc/sysctl.d/`) and applied with `sysctl -p`. In security hardening, `sysctl` is commonly used to disable risky network behaviors, enable spoofing protection, and improve resilience against attacks.

2. **List some best practices for firewall settings.**  
   Use a default-deny policy for inbound traffic; allow only required ports and protocols; restrict administrative services (SSH/RDP) by source IP where possible; disable unused services and open ports; enable firewall logging and periodically review logs; separate rules by service and document each rule purpose; validate rules after every change; avoid broad `allow any` rules; and maintain rule backups/version history for rollback.

3. **Explain SYN attack.**  
   A SYN attack (SYN flood) is a denial-of-service attack that abuses the TCP three-way handshake. The attacker sends a large number of SYN packets, often with spoofed source addresses. The server allocates resources and replies with SYN-ACK, but the final ACK never arrives. This fills the backlog of half-open connections, preventing legitimate users from establishing sessions. Mitigations include SYN cookies (`net.ipv4.tcp_syncookies=1`), rate limiting, tuning backlog parameters, and upstream filtering.

---

## **Conclusion**

The experiment demonstrated practical Linux hardening by combining host firewall policy, controlled privilege escalation, kernel network protections, automatic updates, and security auditing. Together, these controls significantly reduce attack surface and improve system resilience.

---

## **See Also**

- [[System Adminstrator Lab 2]] - user/group management and permissions used in `su` restriction.
- [[System Adminstrator Lab 3]] - networking fundamentals relevant to firewall and ICMP behavior.
- [[System Adminstrator Lab 4]] - monitoring tools useful for validating hardening impact.
- [[System Adminstrator Lab 6]] - packet filtering concepts related to UFW/iptables policy design.

---

# References

- Ubuntu documentation: UFW and `sysctl` hardening guidelines.
- Tiger Linux security audit documentation.

###### Information
- date: 2026.04.18
- time: 20:28
