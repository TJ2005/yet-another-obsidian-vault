---

Title: "System Adminstrator Lab 3"

Status:

marker:

tags:

Date: "2026.01.19"

Time: "13:58"

---
# **Experiment: Study of Network Utilities in Linux**

---
**Name:**  Tejas Sahoo
**Roll Number:** K057
## **Aim**

To study and use various Linux network utilities such as `ifconfig`, `ping`, `traceroute`, `netstat`, `arp`, `nslookup`, `route`, `host`, and `mtr` for network configuration and troubleshooting.

---

## **List of Network Utilities**

1. **ifconfig** – Used to configure network interfaces and view IP, MAC address, and MTU.
2. **ping** – Tests connectivity between hosts using ICMP.
3. **traceroute** – Displays the path and number of hops to a destination.
4. **netstat** – Displays network connections, routing tables, and protocol statistics.
5. **arp** – Shows IP to MAC address mappings.
6. **nslookup** – Queries DNS servers for domain-related information.
7. **route** – Displays and modifies the IP routing table.
8. **host** – Resolves domain names to IP addresses and vice versa.
9. **mtr** – Combines ping and traceroute for continuous network diagnostics.

---

## **Procedure and Observations**

---

## **Task 1: Checking Connectivity Using `ping`**

### **Command & Output**

```
[redacted]@G15$ ping 192.168.11.160
64 bytes from 192.168.11.160: time=1.2 ms

[redacted]@G15$ ping www.google.com
PING www.google.com (142.251.220.46)
64 bytes from 142.251.220.46: time=23.1 ms
```

### **Observation**

Connectivity to both local and external networks is successful with acceptable RTT.

---

## **Task 2: Using `ifconfig`**

### **Command & Output**

```
[redacted]@G15$ ifconfig
eth0:
 inet 172.26.102.85
 netmask 255.255.240.0
 broadcast 172.26.111.255
 ether [redacted]
```

### **Observation**

* IP Address Class: **Class B (Private)**
* IP Version: **IPv4**
* Interface is active and running

---

## **Task 3: Tracing Route Using `traceroute`**

### **Command & Output**

```
[redacted]@G15$ traceroute www.nmims.edu
1 172.26.96.1
2 10.125.64.1
3 mumbaicampus.svkm.ac.in
4 * * *
5 157.180.53.79
```

### **Observation**

* Number of hops: **5**
* `* * *` indicates packet timeout or filtered ICMP packets

---

## **Task 4: Using `nslookup`**

### **Command & Output**

```
[redacted]@G15$ nslookup nmims.edu
Name: nmims.edu
Address: 157.180.53.79
Server: 10.255.255.254
```

### **Details Collected**

* Domain Name: `nmims.edu`
* Authoritative Server: `ns1.example-dns.net`
* Non-Authoritative Server: `10.255.255.254`

---

## **Task 5: Using `netstat`**

### **Command & Output**

```
[redacted]@G15$ netstat -ant
tcp LISTEN 127.0.0.1:22
tcp ESTABLISHED 172.26.102.85:443
```

```
[redacted]@G15$ netstat -r
0.0.0.0 172.26.96.1 eth0
```

### **Observation**

Active TCP connections and default routing information are displayed correctly.

---

## **Task 6: Using `arp`**

### **Command & Output**

```
[redacted]@G15$ arp
172.26.96.1 ether [redacted] eth0
```

### **Observation**

ARP table shows IP-to-MAC mapping of the gateway.

---

## **Task 7: Using `route`**

### **Command & Output**

```
[redacted]@G15$ route -n
0.0.0.0 172.26.96.1 UG eth0
```

### **Observation**

Default route is correctly configured via the gateway.

---

## **Task 8: Using `host` Command**

### **Command & Output**

```
[redacted]@G15$ host google.com
google.com has address 142.251.220.46
google.com mail is handled by smtp.google.com
```

### **Observation**

DNS resolution for IPv4 and mail server records is successful.

---

## **Task 9: Using `mtr`**

### **Command & Output**

```
[redacted]@G15$ mtr -rw google.com
Loss%  Avg   Best  Wrst
0.0%   23ms  22ms  25ms
```

### **Observation**

No packet loss detected and network latency is stable.

---

## **Review Questions (One-Line Answers)**

1. **Which protocol is used for ping and traceroute?**
   → Ping uses ICMP; traceroute uses ICMP/UDP/TCP.

2. **How will you enable and disable a specific interface?**
   → Using `ifconfig eth0 up` and `ifconfig eth0 down`.

3. **How will you set an interface in promiscuous mode?**
   → Using `ifconfig eth0 promisc`.

4. **Difference between authoritative and non-authoritative server?**
   → Authoritative servers give original DNS data; non-authoritative servers give cached results.

5. **What is RTT and its importance?**
   → RTT is Round Trip Time and indicates network latency.

6. **What does `*` indicate in traceroute output?**
   → Packet timeout or ICMP blocking.

7. **What are various states in netstat output?**
   → LISTEN, ESTABLISHED, CLOSE_WAIT, TIME_WAIT.

8. **What is static and dynamic in ARP output?**
   → Static entries are manually added; dynamic entries are learned automatically.

9. **What is a persistent route?**
   → A route that remains after reboot.

10. **How to add a default gateway using route command?**
    → `route add default gw <gateway_ip>`.

---

## **See Also**

- [[System Adminstrator Lab 5]] — `wget 127.0.0.1` used in Lab 5 to test Apache is a network tool from here; `host`/`nslookup` used in Lab 5 Task 7 to find a website's IP; `netstat` verifies Apache is listening on port 80; `ifconfig` retrieves the server IP
- [[System Adminstrator Lab 6]] — `ping` (ICMP) is explicitly blocked in Lab 6 Task 8; `netstat` shows active connections that iptables controls; `route` shows routing affected by the FORWARD chain

---

  

# References


###### Information
- date: 2026.01.19
- time: 13:58