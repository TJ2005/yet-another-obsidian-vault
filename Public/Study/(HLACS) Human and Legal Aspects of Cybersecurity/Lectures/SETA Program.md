---
Title: "SETA Program"
Status:
tags: [hlacs, unit-1]
Date: "2026.08.24"
---

# SETA — Security Education, Training and Awareness

> [!INFO] Source: NIST SP 800-50
> Auditors and regulators recognise the need for security awareness training. SETA is the structured organisational response to the [[Humans in Cybersecurity|human element]].

![[p28_img_7.png]]

## The learning continuum

| Level | Seeks to | Example |
| --- | --- | --- |
| **Awareness** | Focus *attention* on security — recognise concerns and respond; change behaviour / reinforce good practice. **Not training** | Posters, briefings |
| **Training** | Teach *skills* to perform a specific function — for non-security specialists (management, developers, auditors) | Sysadmin security course — management/operational/technical controls |
| **Education** | Integrate all skills into a common body of knowledge + multidisciplinary study → produce security *professionals* | University degree program |

- Key divider: **training teaches skills; awareness focuses attention**

## Program lifecycle (NIST SP 800-50)

### 1. Design the program

#### Structuring models
1. **Model 1 — Centralised**: centralised policy, strategy, implementation
2. **Model 2 — Partially decentralised**: centralised policy + strategy, distributed implementation
3. **Model 3 — Fully decentralised**: centralised policy only; distributed strategy + implementation

##### Policy vs strategy vs implementation

| Layer | Meaning | Example |
| --- | --- | --- |
| **Policy** | The *mandate* — rules stating training **must** happen, who is responsible, minimum requirements; non-negotiable, org-wide | "All employees complete annual awareness; role-based training for admins" |
| **Strategy** | The *plan* — which audiences, content priorities, delivery methods, sequencing, budget, timelines; connects policy → action | "Year 1: phishing simulation for all staff; Year 2: role-specific courses for devs/finance" |
| **Implementation** | The *execution* — building and delivering: sessions, posters, LMS modules, attendance tracking | HR runs Friday workshops; IT deploys the phishing module |

- Policy = **why/what is required**
- Strategy = **the plan to achieve it**
- Implementation = **doing it today**

##### When does a firm need each model?

| Model | Firm profile | Why it fits | Trade-off |
| --- | --- | --- | --- |
| **1 — Centralised** | Small-to-medium, single location, one business line, homogeneous roles | Consistency + cost-efficiency beat local fit — identical content everywhere (200-person fintech office) | Efficient but rigid |
| **2 — Partially decentralised** | Mid-to-large, multiple sites, shared values + common baseline | HQ sets *what*, units decide *how* (national bank: trading floor vs branches vs IT) | Balance; needs coordination |
| **3 — Fully decentralised** | Large diverse conglomerate — many business lines, geographies, regulations | One strategy cannot fit hospital vs software vs overseas subsidiary; each unit plans under umbrella policy | Maximum relevance; risk of inconsistency |

> [!TIP] Exam logic
> - More diversity of roles/locations/regulations → **more decentralisation**
> - Smaller homogeneous firm → **more centralisation**

#### Needs assessment methods

- **Interviews** with all key groups and organisations
- **Organisational surveys**
- **Review of existing material** — current content, schedules, attendee lists
- **Training metrics analysis** — % of users completing sessions
- **Security plan review** — identify system owners and security representatives
- **Oversight findings** — audits, inspector general reviews
- **Event analysis** — DoS attacks, defacements, virus incidents indicating training gaps
- **Industry trend studies** — early-warning insight into emerging issues

#### Strategy & plan contents

- Existing **national/local policy** requiring the program
- **Scope** of the awareness and training program
- **Roles and responsibilities** — who designs, develops, implements, maintains
- **Goals** for each aspect
- **Target audiences**
- **Mandatory/optional courses** per audience
- **Learning objectives** and topics
- **Deployment methods**
- **Documentation, feedback, evidence of learning**
- **Evaluation and update cycle** per aspect
- Exposure **frequency** per audience

#### Establishing priorities

- Availability of **material/resources**
- Role and **organisational impact**
- State of **current compliance**
- Critical **project dependencies**

#### Setting the bar

- Decide the **complexity level** of material to develop
- Must be commensurate with the learner's **role**
- Two criteria: **position in organisation** + **security skills required** for that position

#### Funding options

- Percent of overall **training budget**
- Allocation **per user by role** — key security staff cost more than general users
- Percent of overall **IT budget**
- Explicit **dollar allocations by component**

### 2. Develop material

- Driving question 1: *"What behaviour do we want to reinforce?"* → awareness
- Driving question 2: *"What skill should the audience learn and apply?"* → training

### 3. Implement

- **Communicate the plan**
- Choose **delivery techniques** for awareness/training material

### 4. Post-implementation

- Monitor **compliance**
- **Evaluation and feedback**
- **Manage change**

## Why traditional programs fall short

- Logic flaw: exposing people to information ≠ adopting appropriate behaviour
- This is the **knowledge–intention–behaviour gap**

| Statement | Implication |
| --- | --- |
| "Just because I'm aware doesn't mean I care." | No caring → no effort or engagement |
| "Work against human nature and you will fail." | Humans avoid difficult, awkward, change-requiring actions |

## Your "why" determines your "what"

| Reason | Benefit | Effort |
| --- | --- | --- |
| Compliance | Limited | Low |
| Information dissemination | Limited | Low |
| **Behaviour shaping** | Transformational | High |
| **Culture shaping** | Transformational | High |

## Related

- [[ADDIE and ARCS Models]] ← instructional design behind SETA content
- [[Security Fatigue]] ← what over-training causes
- [[Decision Making in Cybersecurity]]
- [[HLACS Unit 1 Glossary]]