---

Title: "Network Mapping"

Status:

marker:

tags:

Date: "2026.02.24"

Time: "15:28"

---
### 1. Target Specification

This section defines **who** or **what** you are scanning. You can use hostnames, IP addresses, or CIDR ranges.

```bash
TARGET SPECIFICATION:
  Can pass hostnames, IP addresses, networks, etc.
  Ex: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254
  -iL <inputfilename>: Input from list of hosts/networks
  -iR <num hosts>: Choose random targets
  --exclude <host1[,host2][,host3],...>: Exclude hosts/networks
  --excludefile <exclude_file>: Exclude list from file

```

| Flag | Description |
| --- | --- |
| `-iL` | Read target list from a text file. |
| `-iR` | Select random targets (useful for internet research). |
| `--exclude` | Skip specific hosts or networks in a range. |
| `--excludefile` | Skip hosts listed in a specific file. |

---

### 2. Host Discovery

Commonly called "Ping Scanning," these options determine which hosts are "alive" before attempting a full port scan.

```bash
HOST DISCOVERY:
  -sL: List Scan - simply list targets to scan
  -sn: Ping Scan - disable port scan
  -Pn: Treat all hosts as online -- skip host discovery
  -PS/PA/PU/PY[portlist]: TCP SYN, TCP ACK, UDP or SCTP discovery to given ports
  -PE/PP/PM: ICMP echo, timestamp, and netmask request discovery probes
  -PO[protocol list]: IP Protocol Ping
  -n/-R: Never do DNS resolution/Always resolve [default: sometimes]
  --dns-servers <serv1[,serv2],...>: Specify custom DNS servers
  --system-dns: Use OS's DNS resolver
  --traceroute: Trace hop path to each host

```

| Flag | Description |
| --- | --- |
| `-sL` | List Scan: Just lists targets, sends no packets. |
| `-sn` | Ping Scan: Only checks if host is up; skips port scanning. |
| `-Pn` | No Ping: Forces Nmap to scan even if the host doesn't respond to pings. |
| `-PS/PA/PU` | Discovery via TCP SYN, ACK, or UDP probes. |
| `-PE/PP/PM` | Discovery via ICMP Echo, Timestamp, or Netmask requests. |
| `-n` / `-R` | Disable DNS resolution / Force DNS resolution. |
| `--traceroute` | Maps the network path to the target. |

---

### 3. Scan Techniques

These define the "style" of the scan, such as how the TCP handshake is handled.

```bash
SCAN TECHNIQUES:
  -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
  -sU: UDP Scan
  -sN/sF/sX: TCP Null, FIN, and Xmas scans
  --scanflags <flags>: Customize TCP scan flags
  -sI <zombie host[:probeport]>: Idle scan
  -sY/sZ: SCTP INIT/COOKIE-ECHO scans
  -sO: IP protocol scan
  -b <FTP relay host>: FTP bounce scan

```

| Flag | Description |
| --- | --- |
| `-sS` | **TCP SYN Scan**: The "stealth" scan (default for root users). |
| `-sT` | **TCP Connect Scan**: Full 3-way handshake (default for non-root). |
| `-sU` | **UDP Scan**: Scans for UDP services (DNS, DHCP, etc.). |
| `-sN/sF/sX` | **Null, FIN, and Xmas**: Specialized scans to bypass certain firewalls. |
| `-sI` | **Idle Scan**: Spoofs your IP using a "zombie" host. |
| `-sO` | **Protocol Scan**: Determines which IP protocols (TCP, ICMP, etc.) are supported. |

---

### 4. Port Specification and Scan Order

Options to narrow down which "doors" you check on a target.

```bash
PORT SPECIFICATION AND SCAN ORDER:
  -p <port ranges>: Only scan specified ports
    Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9
  --exclude-ports <port ranges>: Exclude the specified ports from scanning
  -F: Fast mode - Scan fewer ports than the default scan
  -r: Scan ports sequentially - don't randomize
  --top-ports <number>: Scan <number> most common ports
  --port-ratio <ratio>: Scan ports more common than <ratio>

```

| Flag | Description |
| --- | --- |
| `-p` | Specify ports (e.g., `-p80`, `-p1-1024`, or `-p U:53,T:80`). |
| `--exclude-ports` | Prevents Nmap from scanning specific ports. |
| `-F` | Fast: Scans only the top 100 ports (vs the default 1,000). |
| `-r` | Linear scan: Does not randomize the port order. |
| `--top-ports` | Scans the most common "X" number of ports. |

---

### 5. Service/OS/Script Detection

The "intelligence" layer—identifying software versions, OS types, and running automated scripts.

```bash
SERVICE/VERSION DETECTION:
  -sV: Probe open ports to determine service/version info
  --version-intensity <level>: Set from 0 (light) to 9 (try all probes)
  
SCRIPT SCAN:
  -sC: equivalent to --script=default
  --script=<Lua scripts>: comma separated list of scripts
  
OS DETECTION:
  -O: Enable OS detection
  --osscan-limit: Limit OS detection to promising targets

```

| Flag | Description |
| --- | --- |
| `-sV` | Service Detection: Tries to find version numbers of apps. |
| `-sC` | Default Scripts: Runs a safe set of Nmap Scripting Engine (NSE) scripts. |
| `--script` | Run specific Lua scripts for vulnerability/info gathering. |
| `-O` | OS Fingerprinting: Guesses the Operating System. |

---

### 6. Timing and Performance

Adjusts how fast or slow Nmap sends packets.

```bash
TIMING AND PERFORMANCE:
  -T<0-5>: Set timing template (higher is faster)
  --min-rate <number>: Send packets no slower than <number> per second
  --max-rate <number>: Send packets no faster than <number> per second

```

| Flag | Description |
| --- | --- |
| `-T0 to -T5` | Speed templates: 0 (Paranoid/Slow) to 5 (Insane/Fast). |
| `--max-retries` | Limits the number of times a probe is resent. |
| `--host-timeout` | Abandon a slow host after a set duration. |

---

### 7. Firewall/IDS Evasion

Tricks to hide the scan from network defenses.

```bash
FIREWALL/IDS EVASION AND SPOOFING:
  -f; --mtu <val>: fragment packets (optionally w/given MTU)
  -D <decoy1,decoy2[,ME],...>: Cloak a scan with decoys
  -S <IP_Address>: Spoof source address
  -e <iface>: Use specified interface
  --spoof-mac <mac address/prefix/vendor name>: Spoof your MAC address

```

| Flag | Description |
| --- | --- |
| `-f` | Fragment: Breaks packets into pieces to bypass simple firewalls. |
| `-D` | Decoy: Mixes your IP with others to hide the source. |
| `-S` | Spoof: Makes the scan look like it’s coming from another IP. |
| `--spoof-mac` | Changes your hardware address (MAC). |

---

### 8. Output

How you save your results.

```bash
OUTPUT:
  -oN/-oX/-oS/-oG <file>: Output in normal, XML, s|<rIpt kIddi3, and Grepable format
  -oA <basename>: Output in the three major formats at once
  -v: Increase verbosity level
  --reason: Display the reason a port is in a particular state

```

| Flag | Description |
| --- | --- |
| `-oN` | Standard readable text output. |
| `-oX` | XML: Best for automation and reporting tools. |
| `-oG` | Grepable: Easy to search via command line. |
| `-oA` | "All": Saves in Normal, XML, and Grepable formats at once. |
| `-v / -vv` | Increases the amount of info shown during the scan. |

---

### 9. Miscellaneous & Examples

```bash
MISC:
  -6: Enable IPv6 scanning
  -A: Enable OS detection, version detection, script scanning, and traceroute
  -V: Print version number

```

| Flag | Description |
| --- | --- |
| `-6` | Enables IPv6 support. |
| `-A` | **Aggressive mode**: Combines `-O`, `-sV`, `-sC`, and `--traceroute`. |

**Would you like me to help you craft a specific Nmap command for a task you're working on right now?**