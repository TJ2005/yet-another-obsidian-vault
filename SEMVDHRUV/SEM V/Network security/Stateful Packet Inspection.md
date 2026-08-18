# Stateful Packet Inspection

A sophisticated type of [[Packet Filtering Firewall]] that maintains context about active connections.

## How It Works
Keeps track of each connection between internal and external systems using a **state table**.

### State Table Contents
The state table includes:
- **Which:** Station has sent the packet
- **What:** Content of the packet  
- **When:** Time stamp

## Key Difference
Instead of checking an Access Control List (ACL), stateful inspection checks the history of receiving packets stored in the state table.

## Trade-offs

### Advantages
- Context-aware filtering
- Can detect packets that are part of legitimate connections
- More secure than [[Static Packet Filtering]] or [[Dynamic Packet Filtering]]
- Better at preventing certain types of attacks

### Disadvantages
- **Additional Compute Required:** Checking and maintaining the state table requires more processing power
- **Vulnerability:** Without proper checks, vulnerable to DOS (Denial of Service) attacks that can overwhelm the state table

## Generation
Part of Third Generation in [[Firewall Generations]].

## Related Concepts
- [[Packet Filtering Firewall]]
- [[DoS Attack]]
- [[TCP-IP Model]] - Connection tracking relies on understanding connection states

---
*