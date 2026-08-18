# Single Bastion Host

A simple [[Firewall Architecture]] with a single protection device on the network perimeter.

## Definition
Any system, router, or firewall that is exposed to the untrusted network can be called a **bastion host** (also known as **Sacrificial Host**).

## Implementation
Uses:
- **[[NAT (Network Address Translation)|NAT]]:** Network Address Translation
- **[[PAT (Port Address Translation)|PAT]]:** Port Address Translation

## Characteristics
- Single protection device on the network perimeter
- Commonly used in residential and SOHO (Small Office Home Office) environments
- Simplest firewall architecture

## Dual Homed Host Variant
A **dual homed host** is a [[Bastion Host]] with two network interfaces:
- One interface connected to internal network
- One interface connected to external network
- Acts as gateway between the two networks

## Advantages
- Simple to configure and maintain
- Cost-effective
- Suitable for small environments
- Low complexity

## Limitations
- **Lacks Defense in Depth:** Single point of failure
- **Complicated ACL Implementation:** All rules must be on single device
- **No Redundancy:** If compromised, entire network is exposed
- **Limited Scalability:** Not suitable for large organizations

## Use Cases
- Home networks
- Small office networks
- Development/testing environments
- Low-risk environments

## Comparison
- Simpler than [[Screened Host Firewall]]
- Less secure than [[Screened Subnet Firewall]]
- Single layer vs. multiple layers of protection

## Related Concepts
- [[Bastion Host]]
- [[Firewall Architecture]]
- [[Access Control List (ACL)]]

---
