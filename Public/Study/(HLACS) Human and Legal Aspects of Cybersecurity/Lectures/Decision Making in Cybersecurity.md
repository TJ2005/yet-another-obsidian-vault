---
Title: "Decision Making in Cybersecurity"
Status:
tags: [hlacs, unit-1]
Date: "2026.08.24"
---

# Decision Making in Cybersecurity

Two lenses: **how individuals think** (System 1 vs 2) and **how organisations decide** (event-based vs risk-based).

## System 1 vs System 2 thinking

| | System 1 | System 2 |
| --- | --- | --- |
| Speed | Fast | Slow |
| Nature | Emotional, intuitive | Methodical, logical, deliberate |
| Basis | **Heuristics** (mental shortcuts) — ~95% of our thinking | Analysis |

Classic demos: bat-and-ball ($1.10 total, bat costs $1 more → intuitive wrong answer $0.10), optical illusions ("pick the longest line").

### Security implications of System 1
- People build **security habits** with System 1 thinking (password behaviour)
- Attackers **weaponise heuristic thinking** — e.g., phishing URL `secure.bobibanking.verifyacctsite.com` looks right to a fast glance

## Event-based vs Risk-based decision making

| Feature | Event-Based (reactive) | Risk-Based (RBCRM, proactive) |
| --- | --- | --- |
| Approach | Reactive / tactical | Proactive / strategic |
| Focus | Alerts, logs, attacks, signatures | Asset criticality, threat context, business impact |
| Trigger | Thresholds & detection rules (5 failed logins, unknown IP, signature match) | Likelihood × impact vs cost of mitigation |
| Primary goal | Quick containment/mitigation | Prioritise resources for most valuable assets |
| Metric | MTTD / MTTR | Expected financial loss, risk-reduction ROI |
| Pros | Fast velocity, clear cause-effect, automatable (**SOAR playbooks**) | Eliminates alert fatigue, aligns with executive goals, budget to high-impact areas |
| Cons | Alert fatigue, blind to novel/zero-day, equal urgency regardless of asset value | Complex asset mapping, hard to quantify real-time, may miss low-likelihood/high-impact **black swans** if data outdated |
| Best used for | SOC operations, incident response, SIEM | Budgeting, vulnerability management, governance |

Two complexity sources risk-based must overcome:

- **Uncertainty concerning cyber incidents**
- **Delays in complex systems**

### The modern hybrid standard

Don't choose — use **risk context to filter and prioritise event responses**.

> Patch release for critical vulnerability (event) → instead of patching all 10,000 servers immediately, patch the **50 internet-facing servers holding sensitive customer data** first (risk-based prioritisation).

## Related

- [[Humans in Cybersecurity]] ← cognitive basis of decisions
- [[Heuristics and Biases]] ← cognitive basis of decisions
- [[Security Fatigue]]
- [[SETA Program]]
- [[HLACS Unit 1 Glossary]]