---
Title: "Culture Failure Scenarios"
Status:
tags: [hlacs, unit-2]
Date: "2026.08.24"
---

# Culture Failure Scenarios

> [!INFO] Why these matter
> Three breach stories showing weak [[Cybersecurity Culture]] beating strong controls — each maps to missing dimensions from [[Seven Dimensions of Security Culture]].

## Scenario 1 — The "Production Emergency" Short-Cut (GitLab / CI-CD)

- Fast-growing startup racing a major feature before a funding round
- Security tools in the **CI/CD pipeline added 20 minutes** per deployment build
- Developers regularly **bypassed static-analysis checks** using administrative override keys
- Attacker compromised an engineer's **GitHub personal access token** with persistent admin access
- Malicious code pushed and ran **unnoticed for three weeks**

## Scenario 2 — The Push-Fatigue Trap (Uber 2022)

- Attacker bought an Uber contractor's stolen password on the **Dark Web**
- Access protected by **MFA** — password alone useless
- Attack: **dozens of MFA push notifications** sent late at night (**MFA fatigue**)
- Attacker posed as Uber IT on WhatsApp: *"the alerts will stop if you just tap Accept"*
- Exhausted contractor tapped **Accept** → full internal admin control

## Scenario 3 — The VIP Exemption (The Executive Phish)

- CEO found MFA and password updates **annoying during business trips**
- Ordered IT to put his account on an **MFA Exemption List**
- Six months later: **spear-phishing campaign** compromised his password
- Attackers reached **high-value IP and finance channels** — no secondary authentication ever triggered
- **Privilege + exemption = single point of failure**

## Dimension mapping (exam angle)

| Scenario | Broken dimension(s) |
| --- | --- |
| CI/CD short-cut | **Norms** (bypass became normal)<br>**Behaviours**<br>**Compliance** |
| Uber push-fatigue | **Cognition** (didn't recognise attack pattern)<br>**Attitude** (convenience over caution) |
| VIP exemption | **Responsibilities** (leadership exempts itself)<br>**Compliance**<br>**Norms** |

## Related

- [[Cybersecurity Culture]]
- [[Seven Dimensions of Security Culture]]
- [[Security Fatigue]] ← Unit 1 concept visible in Scenario 2
- [[Heuristics and Biases]] ← optimism bias in Scenario 3
- [[HLACS Unit 2 Glossary]]