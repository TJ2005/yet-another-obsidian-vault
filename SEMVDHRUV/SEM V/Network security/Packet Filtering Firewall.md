# Packet Filtering Firewall

A firewall processing mode that examines packet header information to make filtering decisions.

## Method
Examines the header information of a packet including:
- Source IP address
- Destination IP address
- Protocol type

## Technical Details
- **Installed on:** TCP/IP based Network
- **Functions on:** 
  - Network Layer (OSI Model)
  - IP Layer (TCP/IP Model)

## Types of Packet Filtering Firewalls

### 1. Static Packet Filtering
- Requires rules to be developed and installed with the firewall
- Any changes require human intervention
- Common and easy to setup
- Static allow entire set of one type of packets to enter in response to authorized requests
- **Limitation:** Inflexible, cannot adapt to new threats

### 2. Dynamic Packet Filtering
- Can react to new emerging situations
- Updates and creates rules to deal with events automatically
- Example: Drops all packets from a particular address when many are malformed
- Allows only particular packets along with particular source-destination pairs
- **Advantage:** Adaptive security posture

### 3. Stateful Packet Inspection
- Keeps track of each connection between internal and external systems
- Uses a **state table** for tracking
- State table includes:
  - **Which:** Station has sent the packet
  - **What:** Content of the packet
  - **When:** Time stamp
- Instead of checking an ACL checks history of receiving packets
- **Trade-off:** Additional compute required to check the state table
- **Vulnerability:** Without proper checks vulnerable to DOS attacks

## Related Concepts
- [[Firewall Processing Modes]]
- [[Application Layer Proxy Firewall]]
- [[MAC Layer Firewall]]

---
