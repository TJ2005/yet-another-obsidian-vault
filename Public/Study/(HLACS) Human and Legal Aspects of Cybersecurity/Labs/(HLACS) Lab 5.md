---
Title: "(HLACS) Lab 5"
Status: complete
tags: [semester-7, cybersecurity, HLACS, lab]
Date: "2026.08.29"
---

# Experiment 5 — Cybersecurity Culture

> [!INFO]
> Solved lab — frameworks compared: **Georgiadou et al. (2020)** vs **KnowBe4 Security Culture Maturity Model (2023)**. Case study: 2022 Uber breach.

## Aim

To study cybersecurity culture and various frameworks.

## Learning Outcomes

- Define cybersecurity culture
- Explain the dimensions of cybersecurity culture
- Compare and contrast various CSC frameworks
- Analyse real-world breaches through the lens of human behaviour and cultural breakdowns

> Related notes: [[Cybersecurity Culture]] · [[Seven Dimensions of Security Culture]] · [[Culture Failure Scenarios]]

## Theory

- NIST: cyberspace = "global domain ... consisting of the interdependent network of information systems infrastructures including the Internet, telecommunications networks, computer systems, and embedded processors and controllers"
- **7,800** publicly disclosed breaches (2012–2017) → **half attributed to insider threats**
- Technical controls alone cannot satisfy cybersecurity requirements → **organisational means** required
- Untrained users become a **peril** for the organisation and themselves
- Fostering CSC → a **cyber-resilient environment**

## Framework comparison

### Framework 1 — Georgiadou et al. (2020)

- **Full title:** *A Cyber-Security Culture Framework for Assessing Organization Readiness* (JCIS)
- Authors: Anna Georgiadou, Spiros Mouzakitis, Kanaris Bounas, Dimitris Askounis (NTUA)
- **Objective:** assess and quantify the **current security readiness** of the workforce through a **domain-agnostic, multi-dimensional model**
- **Structure:** two levels × 10 dimensions × 52 domains × **500+ controls**
	- **Organisational level:** Assets, Continuity, Access and Trust, Operations, Defense
	- **Individual level:** Attitude, Awareness, Behaviour, Competency
- **Assessment:** staff questionnaires (CSCAT-style survey), simulations, serious games; each dimension scored → readiness level + tailored training recommendations
- **Strengths:** holistic (org + individual), scientifically quantified, benchmarkable, adapts to any sector (EPES)
- **Limitations:** resource-heavy (large control set), survey-based → self-report bias, academic focus

### Framework 2 — KnowBe4 Security Culture Maturity Model (2023)

- Authors: KnowBe4 Research (built on the **Seven Dimensions** — Roer's CLTRe research)
- **Objective:** industry's **first data-driven maturity model** for security culture — measure, benchmark and grow culture level by level
- **Structure:** seven dimensions (Attitude, Behaviours, Cognition, Communication, Compliance, Norms, Responsibilities) → aggregated via **Culture Maturity Indicators (CMIs)** → **five maturity levels**
	- **Level 1** Basic Compliance · **2** Security Awareness Foundation · **3** Programmatic Security Awareness & Behaviour · **4** Security Behaviour Management · **5** Sustainable Security Culture
- **CMIs:** training frequency/modules, phish-prone percentage, reported/clicked metrics, culture survey scores, SIEM/DLP behavioural data — each weighted and averaged
- **Output:** 0–100 culture score (<80 moderate, <60 poor-to-moderate) + S-curves show awareness → behaviour → culture gains per level
- **Strengths:** evidence-driven at massive scale, maturity roadmap, benchmarking against industries/regions, practical improvement cycles
- **Limitations:** vendor-centric data, commercial tooling, single-company dataset bias

### Comparison table (as per procedure)

| Comparison Attribute | Selected Framework 1 | Selected Framework 2 |
| --- | --- | --- |
| **Framework Name & Author** | Security Culture Framework — Georgiadou, Mouzakitis, Bounas, Askounis (2020) | Security Culture Maturity Model — KnowBe4 Research (2023) |
| **Primary Focus / Objective** | Quantify current **security readiness** of workforce (organisational + individual) | Benchmark **maturity level** and progress culture towards Level 5 |
| **Core Components / Pillars** | 2 levels × 10 dimensions × 52 domains × 500+ controls<br>Organisational: Assets, Continuity, Access & Trust, Operations, Defense<br>Individual: Attitude, Awareness, Behaviour, Competency | 7 dimensions (Roer)<br>Culture Maturity Indicators (CMIs)<br>5 maturity levels<br>0–100 culture score |
| **How it addresses Human Error / Social Engineering** | Measures attitude/awareness/behaviour per employee → detects weak human controls → tailors training (sims, serious games) | Phishing-resilience metrics (PPP, click/report rates) + training CMIs reveal social-engineering vulnerability and drive behaviour change |
| **Strengths & Limitations** | Strengths: holistic, scientific, domain-agnostic<br>Limitations: resource-heavy, self-report bias | Strengths: data-driven, benchmarkable, actionable roadmap<br>Limitations: vendor-centric dataset, commercial tooling |

## Review questions

### Q1. Explain the need for cybersecurity culture

- Half of all disclosed breaches (2012–2017) trace to **insider threats** — people, not systems
- Human factor is the **substantial element** — technical controls alone are insufficient
- Users who do not use cyberspace in a safe, conscientious, principled manner become a **peril**
- CSC makes security an **integral part of daily job, habits and conduct** → lowers human-flavoured risk
- A strong CSC delivers a **cyber-resilient environment** for the organisation
- Regulatory/audit recognition: culture underpins effective compliance (see [[SETA Program]])

### Q2. Define cybersecurity culture

- CSC refers to the **knowledge, beliefs, perceptions, attitudes, assumptions, norms and values** of people regarding cybersecurity
- And **how they manifest in people's behaviour** with information technologies
- It embeds security considerations into an employee's **job, habits and day-to-day conduct**

### Q3. Explain the seven dimensions of cybersecurity culture

| # | Dimension | Definition |
| :-: | --- | --- |
| 1 | **Attitude** | Feelings and beliefs toward security protocols and issues |
| 2 | **Behaviours** | Actions with direct/indirect impact on organisational security |
| 3 | **Cognition** | Understanding, knowledge and awareness of security issues |
| 4 | **Communication** | Quality of channels to discuss security and report incidents |
| 5 | **Compliance** | Knowledge of written policies and the extent they are followed |
| 6 | **Responsibilities** | Perceiving one's role as critical to sustaining/endangering security |
| 7 | **Norms** | Adherence to unwritten rules of conduct |

### Q4. How can you measure cybersecurity culture?

- **Surveys/questionnaires** per dimension — e.g., security culture survey scoring each dimension 0–100 (CLTRe-style)
- **Behavioural metrics** — phishing simulation results (phish-prone %, click/report rates), training completion, SIEM/DLP behaviour alerts
- **Maturity models** — KnowBe4 SCMM aggregates weighted CMIs into a maturity level (1–5) and 0–100 score
- **Scientific frameworks** — Georgiadou et al.: 500+ controls scored per dimension → readiness assessment, cross-tested via piloting and validation
- **Triangulation** — combine surveys + observed behaviour; single datapoints are unreliable ("awareness ≠ behaviour")

### Q5. 2022 Uber Social Engineering Breach case study

(a) Two cultural dimensions that failed

- **Behaviours** — the contractor performed an action (approving MFA) that directly endangered security despite the alert pattern being abnormal
- **Communication** — trusted an **unverified WhatsApp message** from a spoofed "IT Support" instead of using an official reporting channel; no norm of verifying through legitimate support
- (Also arguable: **Cognition** — failed to recognise the MFA spam signature; **Norms** — compliance with unusual requests was the norm, not challenge/reporting)

(b) Why did the contractor comply?

- **MFA fatigue** — dozens of late-night push notifications exhausted and desensitised the contractor ([[Security Fatigue]])
- **Authority spoofing** — WhatsApp sender appeared to be IT support → social proof/authority shortcut
- **Relief framing** — *"accept and the alerts will stop"* offered an easy way out of the annoyance
- **System 1 thinking** — tired, low-cost single tap; no cognitive space to methodically verify ([[Decision Making in Cybersecurity]])
- **No easy verification path** — the contractor had no quick, known channel to confirm the request → complied instead of [[HLACS Unit 2 Glossary|reporting]]

(c) Two cultural interventions (beyond technical MFA changes such as FIDO2)

- **Blame-free reporting culture** — reward and normalise reporting any unusual MFA/credential event; guarantee no reprisal; make reporting the default response to unsolicited IT requests (strengthens **Behaviours**, **Communication**, **Norms**)
- **Verification norms + awareness simulations** — establish and train the unwritten rule *"IT never requests actions via personal/unofficial channels"*; rehearse MFA-fatigue attacks in phishing simulations and spotlight the ● stop/take-a-beat-and-verify behaviour (strengthens **Cognition**, **Compliance**, **Norms**)
- Optional third: **security champions** visible in each team as the safe touchpoint for suspicious requests → reinforces shared responsibility.

## Conclusion

Cybersecurity is a human problem as much as a technical one. Frameworks such as Georgiadou et al. (2020) and the KnowBe4 SCMM show that culture can be decomposed, measured and deliberately improved across dimensions and maturity levels. The Uber breach demonstrates that even strong MFA fails when norms, communication and behaviour are weak — the remedy is a measurable, leadership-supported security culture that makes reporting and verification the instinctive human responses.