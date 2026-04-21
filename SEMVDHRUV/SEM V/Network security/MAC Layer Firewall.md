# MAC Layer Firewall

A [[Firewall Processing Modes|firewall processing mode]] that filters traffic based on hardware addresses.

## Method
Filters based on:
- MAC ID (Media Access Control address)
- NIC ID (Network Interface Card identifier)

## Technical Details
- **Installed On:** Specific Host Computer
- **Functions On:** Media Access Control sublayer of Data Link Layer (Layer 2 in [[OSI Model]])

## How It Works
- Examines the hardware address of network devices
- Compares MAC addresses against allowed/denied lists
- Blocks or allows traffic based on the device's physical network adapter

## Common Use Cases
- Used commonly to deny some devices access to LAN
- Restricting access to specific network features
- Device-level access control on local networks
- Guest network management

## Advantages
- Simple device identification
- Works at low network layer
- Can prevent unauthorized device connections

## Limitations
- **MAC Spoofing:** Attackers can change their MAC address to bypass filters
- **Limited to Local Network:** Only effective within the same broadcast domain
- **Not Scalable:** Difficult to manage in large networks
- **No Content Inspection:** Cannot analyze packet contents

## Comparison
- Operates at lower layer than [[Packet Filtering Firewall]] (Layer 2 vs Layer 3)
- More device-focused than [[Application Layer Proxy Firewall]]
- Simpler but less flexible than other firewall types

## Related Concepts
- [[OSI Model#Data Link Layer|Data Link Layer]]
- [[Network Access Control (NAC)]]

---
