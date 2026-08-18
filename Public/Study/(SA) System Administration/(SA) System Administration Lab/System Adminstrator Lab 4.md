---

Title: "System Adminstrator Lab 4"

Status:

marker:

tags:

Date: "2026.02.05"

Time: "13:11"

---
# **Experiment 4: Linux Performance Monitoring Tools**

---
**Name:** Tejas Sahoo
**Roll Number:** K057

## **Aim**

To monitor the performance of a Linux system using various built-in and third-party utilities.

---

## **Learning Outcomes**

1. Execute various performance monitoring utilities.
2. Interpret the output of various commands.

---

## **Theory**

| Tool | Description |
|------|-------------|
| `top` | Dynamic real-time view of running processes; refreshes every 5 seconds, sorted by CPU usage. |
| `htop` | Enhanced interactive version of `top`; supports tree view of processes. |
| `iotop` | Monitors real-time Disk I/O per process; useful for identifying high disk read/write. |
| `vmstat` | Reports processes, memory, paging, block I/O, traps, and CPU activity. |
| `w` | Shows who is logged on and what they are doing. |
| `uptime` | Shows how long the system has been running, number of users, and load averages. |
| `free` | Displays total/used/free physical and swap memory, plus kernel buffers. |
| `iostat` | Reports CPU statistics and I/O stats for devices, partitions, and NFS. |
| `mpstat` | Displays per-processor activity; `mpstat -P ALL` shows average CPU utilization per core. |
| `iptraf-ng` | Interactive colorful IP LAN monitor; generates TCP, UDP, ICMP, Ethernet, and node statistics. |
| `tcpdump` | Captures and describes packets on a network interface matching a boolean expression. |
| `lsof` | Lists open files, network connections, and more. |
| `iftop` | Terminal-based bandwidth monitor; shows real-time bandwidth usage between two hosts. |

---

## **Procedure & Observations**

> Install any missing tool with: `sudo apt-get install <package_name>`

---

### **1. `top` — Real-time Process Viewer**

```bash
top
```

![[IMG-20260420174732616.png]]
---

### **2. `htop` — Interactive Process Viewer**

```bash
sudo apt-get install htop
htop
```
![[IMG-20260420174732639.png]]
---

### **3. `vmstat` — System Activity**

```bash
vmstat
```

```bash
vmstat 2
```
*(continuous monitoring, refreshes every 2 seconds — press `Ctrl+C` to stop)*

![[IMG-20260420174732683.png]]

---

### **4. `w` — Logged-in Users**

```bash
w
```
![[IMG-20260420174732719.png]]
---

### **5. `uptime` — System Uptime**

```bash
uptime
```
![[IMG-20260420174732783.png]]
---

### **6. `free` — Memory Usage**

```bash
free
free -h
```

![[IMG-20260420174732802.png]]
---

### **7. `iostat` — CPU & Disk I/O Stats**

```bash
sudo apt-get install sysstat
iostat
```

![[IMG-20260420174732822.png]]

---

### **8. `mpstat` — Multiprocessor Usage**

```bash
mpstat
mpstat -P ALL
```
![[IMG-20260420174732897.png]]
---

### **9. `iptraf-ng` — Real-time Network Statistics**

```bash
sudo apt-get install iptraf-ng
sudo iptraf-ng
```

![[IMG-20260420174732934.png]]
---

### **10. `tcpdump` — Packet Capture**

```bash
sudo tcpdump
```
![[IMG-20260420174732954.png]]
---

### **11. `lsof` — List Open Files**

```bash
lsof
```

![[IMG-20260420174733005.png]]
---

### **12. `iftop` — Network Bandwidth Monitor**

```bash
sudo apt-get install iftop
sudo iftop
```

![[IMG-20260420174733032.png]]

---

### **13. `ps -eo` — Custom Process Listing**

```bash
ps -eo pid,ni,comm
```

![[IMG-20260420174733082.png]]

---

### **14. `vmstat -f` — Forks Since Boot**

```bash
vmstat -f
```
![[IMG-20260420174733102.png]]
---

## **Additional Task — Linux Monitoring Script**

Script that collects top CPU/memory processes, disk I/O, network usage, and uptime:

```bash
#!/bin/bash
echo "===== SYSTEM MONITOR REPORT ====="
echo "Date: $(date)"
echo ""

echo "--- Uptime ---"
uptime

echo ""
echo "--- Top 5 CPU-using Processes ---"
ps -eo pid,comm,%cpu --sort=-%cpu | head -6

echo ""
echo "--- Top 5 Memory-using Processes ---"
ps -eo pid,comm,%mem --sort=-%mem | head -6

echo ""
echo "--- Disk I/O Usage ---"
iostat -d 1 1

echo ""
echo "--- Network Usage ---"
cat /proc/net/dev | awk 'NR>2 {print $1, "RX:", $2, "TX:", $10}'

echo ""
echo "--- Memory Summary ---"
free -h
```

Save as `monitor.sh`, then run:

```bash
chmod +x monitor.sh
./monitor.sh
```

---

## **Result**

![[IMG-20260420174733167.png]]
Performance monitoring tools were executed successfully. CPU, memory, disk I/O, and network statistics were observed using various Linux utilities.

---

## **Review Questions**

1. **Which processes in `top` have a nice value of -20? What does it indicate?**
   → Kernel threads and critical system services may have nice value `-20`, indicating **highest priority** — they are allowed to use CPU before all other processes.

2. **What is the nice value and PID of `systemd`?**
   → PID: `1`, Nice value: `0` (normal priority). Verify with:
   ```bash
   ps -eo pid,ni,comm | grep systemd
   ```

3. **What is the nice value and PID of `iscsid`?**
   → PID varies by system; Nice value is typically `0`. Verify with:
   ```bash
   ps -eo pid,ni,comm | grep iscsid
   ```

4. **Comment on your observation for Q2 and Q3.**
   → Both `systemd` and `iscsid` have nice value `0` (normal priority). Although `systemd` is critical, it doesn't need `-20` priority because Linux dynamically manages scheduling to maintain stability.

5. **Which command displays number of forks since boot?**
   → `vmstat -f`

6. **Explore any three system monitoring tools not in the list.**
   - **`glances`** — All-in-one monitor showing CPU, memory, disk, and network in one screen.
   - **`atop`** — Records system performance over time for past behavior analysis.
   - **`dstat`** — Combines `vmstat`, `iostat`, and `netstat` into one tool.

7. **Explore any three network monitoring tools not in the list.**
   - **`nload`** — Real-time incoming/outgoing network traffic display.
   - **`bmon`** — Bandwidth monitor with per-interface network statistics.
   - **`netstat`** — Displays connections, routing tables, and interface statistics.

---

## **Conclusion**

This lab provided hands-on experience with Linux performance monitoring tools and helped understand real-time analysis of CPU, memory, disk, and network usage. It enhanced practical knowledge of system administration and automated monitoring using shell scripting.

---

## **See Also**

- [[System Adminstrator Lab 5]] — `lsof` can confirm Apache is listening on port 80; `tcpdump` can capture live HTTP traffic from the web server; `iftop`/`iptraf-ng` monitor bandwidth to/from the Apache server
- [[System Adminstrator Lab 6]] — `tcpdump` monitors the exact traffic that iptables rules filter; `iptraf-ng` and `iftop` show traffic iptables can block or allow; `netstat` shows connections controlled by iptables rules

---

# References


###### Information
- date: 2026.02.05
- time: 13:11
