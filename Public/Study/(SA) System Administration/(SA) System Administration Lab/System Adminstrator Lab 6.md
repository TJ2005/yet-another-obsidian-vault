---

Title: "System Adminstrator Lab 8"

Status:

marker:

tags:

Date: "2026.02.23"

Time: "13:11"

---
# **Experiment 6: IPTables Firewall Configuration**

---
**Name:** Tejas Sahoo
**Roll Number:** K057

## **Aim**

To configure and manage firewall rules using `iptables` on a Linux system.

---

## **Learning Outcomes**

1. Understand the need for a firewall in a computer network.
2. Configure and manage `iptables` rules on a Linux system.

---

## **Theory**

`iptables` is a powerful Linux command-line firewall utility that controls incoming and outgoing network traffic based on defined rules.

- Uses **policy chains** to allow or block traffic.
- Rules are checked **sequentially** — first match wins.
- If no rule matches, the **default policy** is applied.
- Pre-installed on most Linux distributions.

### **Types of Chains**

| Chain | Purpose |
|-------|---------|
| `INPUT` | Controls incoming traffic to the system (e.g. SSH requests) |
| `FORWARD` | Used when the system acts as a router and forwards packets |
| `OUTPUT` | Controls outgoing traffic from the system |

> ⚠️ **Safety Note:** Always allow required services (e.g. SSH) **before** setting default policy to DROP — otherwise you will lose remote access.

---

## **Procedure & Observations**

---

### **Task 1: Display Current Rules**

```bash
sudo iptables -L
```

![[IMG-20260420174733338.png]]
---

### **Task 2: Change Default Policy to DROP**

```bash
sudo iptables --policy INPUT DROP
sudo iptables --policy OUTPUT DROP
sudo iptables --policy FORWARD DROP
```

---

### **Task 3: Block a Specific IP Address**

```bash
sudo iptables -A INPUT -s 10.10.10.10 -j DROP
```

---

### **Task 4: Block an Entire Subnet**

```bash
sudo iptables -A INPUT -s 10.10.1.0/24 -j DROP
```

---

### **Task 5: Block a Specific Service (FTP)**

```bash
sudo iptables -A INPUT -p tcp --dport ftp -s 10.10.10.10 -j DROP
```

---

### **Task 6: Allow SSH (Two-way)**

```bash
sudo iptables -A INPUT -i eth0 -p tcp --dport ssh -j ACCEPT
sudo iptables -A OUTPUT -o eth0 -p tcp --sport ssh -j ACCEPT
```

---

### **Task 7: Block Access to a Website**

Find the IP:
```bash
host -t A www.nmims.edu
```

Block the IP:
```bash
sudo iptables -A OUTPUT -p tcp -d 157.180.53.79 -j DROP
```

---

### **Task 8: Insert Rule at a Specific Line (Block ICMP)**

```bash
sudo iptables -I INPUT 2 -p icmp -s 10.10.1.0/24 -j DROP
```

---

### **Task 9: Save Rules**

```bash
sudo /sbin/iptables-save
```

---

### **Task 10: Delete a Specific Rule**

View rules with line numbers:
```bash
sudo iptables -L INPUT -n --line-numbers
```

Delete rule at line 4:
```bash
sudo iptables -D INPUT 4
```

---

### **Task 11: Flush All Rules**

```bash
sudo iptables -F
```

---

## Output
![[IMG-20260420174733433.png]]
## **Review Questions**

1. **Why is a packet filtering firewall required?**
   → A packet filtering firewall controls network access by inspecting packet headers (source/destination IP, port, protocol) and blocking unauthorized traffic, protecting the system from attacks, unauthorized access, and malicious connections.

2. **Explain the working of `iptables` in detail.**
   → `iptables` processes network packets through three chains: INPUT (incoming), OUTPUT (outgoing), and FORWARD (routed packets). Each chain contains ordered rules — when a packet arrives, `iptables` checks each rule sequentially. The first matching rule's target (`ACCEPT`, `DROP`, `REJECT`) is applied. If no rule matches, the chain's default policy is used.

3. **What is the difference between `DROP` and `REJECT`?**
   → `DROP` silently discards the packet — the sender gets no response and times out. `REJECT` discards the packet but sends an ICMP error back to the sender notifying them the connection was refused. `DROP` is stealthier; `REJECT` is more informative for debugging.

---

## **Conclusion**

`iptables` firewall rules were successfully configured on Linux. Incoming and outgoing traffic was controlled using INPUT, OUTPUT, and FORWARD chains. Rules were applied to block specific IPs, subnets, services, and websites, and were saved and managed using line-number based deletion and flush commands.

---

## **See Also**

- [[System Adminstrator Lab 3]] — `ping` (ICMP) blocked in Task 8 uses the same protocol covered in Lab 3; `host`/`nslookup` find the IPs targeted in Task 7; `netstat` shows connections iptables controls; `route` informs the FORWARD chain
- [[System Adminstrator Lab 4]] — `tcpdump`, `iptraf-ng`, and `iftop` from Lab 4 are used to verify whether iptables rules are working by observing if blocked traffic disappears
- [[System Adminstrator Lab 5]] — Apache (Lab 5) listens on port 80; if default policy is DROP, `iptables -A INPUT -p tcp --dport 80 -j ACCEPT` must be added for the web server to function

---

# References


###### Information
- date: 2026.02.23
- time: 13:11
