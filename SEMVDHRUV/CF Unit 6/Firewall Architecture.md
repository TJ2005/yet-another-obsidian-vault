# Firewall Architecture

The structure and configuration of [[Firewalls Overview|firewalls]] depends on several factors:
- Objectives
- Organization's ability
- Implementation requirements
- Budget

## Types of Architecture-Based Firewalls

1. [[Single Bastion Host]]
2. [[Screened Host Firewall]]
3. [[Screened Subnet Firewall]]
4. [[Dual Homed Firewall]]

Each architecture provides different levels of security and complexity, suitable for different organizational needs.

## Key Concepts
- **[[Bastion Host]]:** Any system/router/firewall exposed to the untrusted network
- **[[DMZ (Demilitarized Zone)]]:** Buffer zone between internal and external networks
- **Defense in Depth:** Multiple layers of security controls

## Architectural Considerations
- Single point of failure vs. redundancy
- Performance requirements
- Complexity of management
- Cost constraints
- Security requirements

## Related Topics
- [[Network Security Architecture]]
- [[NAT (Network Address Translation)]]
- [[PAT (Port Address Translation)]]
- [[Firewall Best Practices]]

---
