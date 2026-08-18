---

Title: "(HLACS) Lab 2"

Status:

marker:

tags:

Date: "2026.08.06"

Time: "09:19"

---
# Experiment 2: Cognitive Bias & Phishing Susceptibility Analysis

**Aim:** To investigate how social engineering attacks exploit
dual-process cognitive theories (System 1 vs. System 2 thinking) and
specific psychological heuristics, and to quantitatively evaluate
empirical behavioral data to determine which cognitive biases result in
the highest operational failure rates.

**Learning Outcomes:**

After completion of this experiment, student should be able to

1.  Deconstruct Social Engineering Mechanics
2.  Formulate Targeted Phishing Indicators
3.  Execute Behavioral Data Analytics
4.  Differentiate Cognitive Paths
5.  Recommend Evidence-Based Controls

**Theory:**

#### Dual-Process Theory (System 1 vs. System 2)

Modern cognitive psychology (pioneered by Daniel Kahneman and Amos
Tversky) models human decision-making via two distinct mechanisms:

- **System 1 (Fast Thinking):** Operates automatically, fast, with
  little or no effort, and no sense of voluntary control. It relies
  heavily on emotional reactions, habits, and cognitive shortcuts
  (heuristics).

- **System 2 (Slow Thinking):** Allocates attention to the effortful
  mental operations that demand it, including complex computations,
  critical thinking, and objective analysis.

Phishing attacks are specifically engineered to force targets into
**System 1 mode**. By introducing urgency, fear, greed, or stress, the
threat actor overloads the target's working memory, preventing the
transition to System 2 thinking where technical discrepancies (like
spoofed URLs or mismatched sender domains) would otherwise be noticed.

#### Psychological Heuristics Weaponized in Social Engineering

Robert Cialdini identified core principles of persuasion that threat
actors commonly abuse:

1.  **Authority:** Individuals possess an ingrained deference to
    authority figures or compliance mandates. Phishing emails mimicking
    C-level executives, legal entities, or network administrators
    exploit this bias to compel instant obedience.

2.  **Scarcity:** Human beings assign higher value to opportunities that
    are perceived as scarce or time-limited. Triggers involving brief
    execution windows (e.g., *"Account will terminate in 2 hours"*)
    generate artificial panic, causing victims to bypass validation
    procedures.

3.  **Commitment & Consistency:** People prefer to follow through with
    behaviors that align with prior statements, organizational policies,
    or accepted routines. Phishing campaigns that mimic standard
    internal workflows (e.g., standard HR annual policy acknowledgments)
    leverage this comfort zone.

**Procedure:**

**Task 1:**

Using an open-source phishing simulation framework (e.g., GoPhish) or a
mock markdown/HTML builder, construct three distinct email templates:

- **Template A (Authority Focus):** Target the Tech department using a
  critical infrastructure mandate.

**<u>Format</u>**

> **Subject**: Critical Infrastructure Security Update Required
>
> Hello,
>
> To support the ongoing critical infrastructure upgrades, the
> technology department has to deploy updated security controls across
> all employee workstations.
>
> Your account is required to confirm the update and adhere with the
> compliance policies.
>
> Please complete the confirmation using the link below
>
> \[[Confirm Security Update](https://www.phishing.com/)\]
>
> **Deadline: Today, 4:00 PM**
>
> Employees who do not complete the confirmation may experience
> temporary interruptions while access is reviewed.
>
> Regards,
>
> Technology Operations

- **Template B (Scarcity Focus):** Target the Finance department using a
  time-sensitive financial or administrative deadline.

**<u>Format</u>**

> **Subject**: FINAL REMINDER: Finance Portal Submission Deadline Today
>
> Dear Finance Team,
>
> This is a final reminder that all Finance personnel are required to
> complete the mandatory reconciliation confirmation before today's
> processing deadline.
>
> According to our records, your confirmation has not yet been received.
>
> Please complete the verification using the portal below **before 4:00
> PM** today to avoid delays in upcoming financial processing.
>
> **\[[Complete Finance Confirmation](https://www.phishing.com/)\]**
>
> Employees who miss the submission deadline may experience temporary
> delays in accessing finance-related services until their records have
> been verified.
>
> If you have already completed this process, please disregard this
> message.
>
> Thank you,
>
> Finance Operations

- **Template C (Commitment Focus):** Target the HR department or general
  employees leveraging a routine compliance standard.

**<u>Format</u>**

> **Subject:** Annual Policy Acknowledgement Required
>
> Hello,
>
> As part of our annual compliance program, all employees are required
> to acknowledge the latest updates to the Corporate Information
> Security and Acceptable Use Policy.
>
> Since you have successfully completed previous compliance
> requirements, only a brief acknowledgement is needed this year.
>
> Please review and acknowledge the updated policy below.
>
> **\[[Acknowledge Policy Update](https://www.phishing.com/)\]**
>
> Estimated completion time: **Under 2 minutes**
>
> Thank you for helping us maintain a secure and compliant workplace.
>
> Human Resources & Compliance

Document the explicit behavioral indicators and psychological
manipulation hooks utilized in each design.

**Task 2: AFTER REVIEW QUESTIONS**

1.  Load the provided dataset (phishing_behavioral_analysis_dataset.csv)
    into a Python development environment (Jupyter Notebook or an IDE).

2.  **Data Ingestion & Cleaning:** Use pandas to inspect the structure,
    account for baseline dimensions, and compute global performance
    benchmarks.

3.  **Statistical Aggregation:**

    1.  Calculate the **Click-Through Rate (CTR)** across different
        psychological_bias categories:


4.  Calculate the **Data Submission Rate** per template category.

5.  Cross-tabulate susceptibility by checking the correlation between
    department and psychological_bias.


4.  **Temporal Modeling:** Plot a distribution graph (histogram or
    kernel density estimate) of the time_to_click_sec variable segmented
    by cognitive bias to map the velocity of System 1 reactions.

5.  **Reporting:** Document structural vulnerabilities discovered in the
    dataset and provide empirical evidence detailing which group is most
    vulnerable to which bias.

**Review questions:**

1.  Based on your temporal distribution analysis of time_to_click_sec,
    what is the statistical relationship between highly urgent triggers
    (e.g., Scarcity/Authority) and response times compared to baseline
    informational templates? How does this validate Dual-Process Theory?

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 11%" />
<col style="width: 14%" />
<col style="width: 16%" />
<col style="width: 13%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Bias</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>n</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Mean</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Median</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Max</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>% of clicks ≤ 30 s</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Authority</p>
</blockquote></td>
<td><blockquote>
<p>37</p>
</blockquote></td>
<td><blockquote>
<p>17.2 s</p>
</blockquote></td>
<td><blockquote>
<p>12 s</p>
</blockquote></td>
<td><blockquote>
<p>58 s</p>
</blockquote></td>
<td><blockquote>
<p><strong>86.5 %</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Scarcity</p>
</blockquote></td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>17.5 s</p>
</blockquote></td>
<td><blockquote>
<p>15 s</p>
</blockquote></td>
<td><blockquote>
<p>44 s</p>
</blockquote></td>
<td><blockquote>
<p><strong>81.8 %</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Commitment (baseline/informational)</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>164.4 s</p>
</blockquote></td>
<td><blockquote>
<p>99 s</p>
</blockquote></td>
<td><blockquote>
<p>560 s</p>
</blockquote></td>
<td><blockquote>
<p><strong>0.0 %</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Authority and Scarcity produce a single sharp KDE spike at ~10–15 s.
> The Commitment/informational template (HR_POLICY_UPDATE) produces a
> broad, flat curve centred near 100 s with **not one** click under 30
> seconds.
>
> **How it validates Dual-Process Theory.** Dual-Process Theory
> distinguishes **System 1** (fast, automatic, reflexive, emotional)
> from **System 2** (slow, deliberate, analytical).
>
> \- Urgent triggers (Authority/Scarcity) fire responses inside the
> **reflexive System-1 window** — the click completes *before*
> deliberation can engage. Urgency short-circuits reasoning.
>
> \- The informational Commitment template elicited slow, deliberate
> responses (median 99 s) that are characteristic of **System-2
> processing**. Yet those users still clicked — meaning this is a
> **System-2 failure** (a considered-but-wrong decision), a
> fundamentally different vulnerability.
>
> The two clean, separated distributions are direct empirical evidence
> for two distinct cognitive processing modes, exactly as the theory
> predicts.

2.  The Tech department typically possesses higher baseline technical
    literacy regarding indicators like domain naming and certificate
    verification. Why might a highly targeted *Authority-based* trigger
    (such as an administrative infrastructure mandate) still achieve a
    high failure rate within this specialized demographic?

> Tech is the **most resilient** department overall — it resisted
> Scarcity (41.2 % CTR, the lowest non-Commitment cell). Yet the
> \`TECH_MANDATORY_PATCH\` (Authority) template produced the
> **campaign's single highest CTR at 61.3 %**.
>
> Reasons:
>
> 1\. **The lure was written in the target's own professional
> vocabulary.** A "mandatory infrastructure patch" is a routine,
> expected, legitimate-sounding request to a technical audience. It
> doesn't trip the domain/certificate scrutiny that Tech applies to
> *obviously* suspicious mail, because it never looks suspicious in the
> first place.
>
> 2\. **Authority exploits process compliance, not gullibility.**
> Responding to an infrastructure/admin mandate is a professional
> reflex, not a knowledge gap. Technical literacy tells you *how to
> verify a domain*; it does not tell you to pause on an email that
> matches your normal workflow.
>
> 3\. **Context-appropriate framing bypasses vigilance.** Vigilance is
> applied selectively. When the request fits the recipient's expected
> duties, the technical checks are never invoked.
>
> “*Technical fluency is not protection when the lure is phrased in the
> target's own professional vocabulary."* Tech's resilience is
> **domain-specific**, so Tech must **not** be exempted from Authority
> testing.

3.  If the cross-tabulation data reveals that the Finance department has
    a significantly higher vulnerability to *Scarcity* triggers than the
    HR department, how should an enterprise tailor its administrative
    and security awareness strategies to address this specific finding
    instead of utilizing a generic, organization-wide baseline program?

> The data shows department vulnerability is not uniform — it is a
> property of the **department × bias pairing** (χ² for department
> alone: p = 0.633, i.e. department by itself explains nothing). Finance
> is the *most* click-prone department for Scarcity (69.2 % CTR, highest
> in the matrix) but only average on Authority (50.0 %). "Finance is
> bought, not commanded."
>
> A generic org-wide program wastes effort and misses the actual attack
> surface. Instead:
>
> 1\. **Segment training by the group's specific weakness.** Give
> **Finance** simulations built on **incentive/scarcity framing**
> ("bonus expiring", "raffle", limited-time offers) -not
> executive-impersonation drills that they already resist.
>
> 2\. **Give HR the opposite treatment** — HR × Authority was the
> fastest, most lethal cell (45.5 % compromise, 10.5 s median). HR needs
> **Authority-themed re-training with verify-out-of-band drills**.
>
> 3\. **Use role/function-based risk profiles** rather than a single
> baseline. Map each department to its dominant bias and rotate the
> simulation themes accordingly.
>
> 4\. **Measure per-pairing, not per-department**, so the program keeps
> targeting the real vulnerability rather than a blended average that
> hides it.
>
> Net effect: finite security-awareness budget is spent on each group's
> *actual* soft spot instead of being diluted across a one-size-fits-all
> baseline.

4.  Technical controls (like secure email gateways, SPF/DKIM/DMARC
    validation, and endpoint detection) aim to minimize the volume of
    malicious inputs reaching an inbox. At what exact stage of the
    phishing kill-chain do psychological heuristics actively undermine
    these technical controls, and what defensive concept mitigates the
    fallout of this human-layer compromise?

> **Where technical controls operate.** Secure email gateways,
> SPF/DKIM/DMARC, and endpoint detection all work to **reduce the volume
> of malicious mail that reaches the inbox** - i.e. the *Delivery* stage
> of the phishing kill-chain.
>
> **Where psychological heuristics take over.** The moment a
> message **survives filtering and is delivered/opened**, the defense
> hands off to the human. Heuristics (urgency, authority, scarcity) then
> drive the **Exploitation stage - the click and the credential
> submission.** In this dataset that is precisely the failure
> point: **CTR 54 %**, and **62 % of everyone who clicks then submits
> credentials**, with 86.5 % of Authority clicks landing under 30 s.
> Every technical control upstream is bypassed the instant one crafted
> email gets through, because the exploit target is the person, not the
> software.
>
> **The exact stage:** the **click / user-action (Exploitation)
> boundary** - after Delivery, once the human is in the loop.
>
> **Mitigating defensive concept: Defense-in-Depth** -
> pecifically **layered controls placed at the click boundary** so that
> no single human decision is the last line of defense:

- Link rewriting / URL detonation (sandboxing links post-delivery)

- **Phishing-resistant MFA** (so stolen credentials alone are useless)

- Credential-submission blocking / DLP at the browser boundary

- Zero-trust access controls

> The principle: assume the human layer *will* be compromised and build
> controls that **do not depend on the user's judgement in that
> sub-30-second window.** As the report puts it, *"the click, not the
> email, is the control point."*

5.  In a real-world enterprise phishing simulation program, tracking
    failure metrics down to the individual identity (employee_id) can
    lead to punitive workplace environments, anxiety, or distrust. How
    should a security department structurally manage or anonymize
    behavioral dataset collection to ensure the metrics drive positive
    behavioral conditioning rather than punitive enforcement?

> racking failures down to employee_id risks a punitive, anxious,
> distrustful culture - which undermines reporting and learning.
> Structural safeguards:
>
> **Aggregate and anonymize for reporting.** Report metrics at
> the **cohort level** (department × bias, role, region), never by named
> individual. Individual identifiers should
> be **pseudonymized/tokenized** and access-controlled, decoupled from
> the analytics dataset.
>
> **Separation of duties.** The team running analytics should see only
> de-identified data. Any re-identification (if ever needed for targeted
> help) should require a separate, logged, access-controlled process —
> not routine visibility.
>
> **Data minimization & retention limits.** Collect only what the
> behavioral analysis needs; auto-expire individual-level records after
> a short window so historical "failures" cannot follow an employee.
>
> **Positive-conditioning framing.** Use results to **auto-enroll the
> vulnerable *cohort* into training**, and reward reporting (e.g. a
> "report phish" button) rather than penalizing clicking. Make the first
> failures a coaching trigger, not an HR incident.
>
> **Transparency & consent.** Tell staff the program exists, that it
> measures the *organization's* resilience, and that individual results
> are not used for performance/disciplinary action. This preserves trust
> and keeps people willing to report real attacks.
>
> **Governance / privacy-by-design.** Align to data-protection
> principles (purpose limitation, GDPR-style safeguards), with clear
> policy that simulation data is firewalled from performance management.
>
> Goal: metrics steer **behavioral conditioning and better controls**,
> while the individual is protected from **punitive enforcement**.

**<u>TASK 2</u>**

*For more details and the script used for this task:
<https://github.com/Heroic2024/hlac-exp2>*

**1. Data Ingestion & Cleaning**

| **Check**                          | **Result**           |
|------------------------------------|----------------------|
| Shape                              | 150 rows × 8 columns |
| Missing values                     | 0 in every column    |
| Duplicate employee_id              | 0                    |
| Clicked but never opened           | 0                    |
| Submitted but never clicked        | 0                    |
| Clicked with time_to_click_sec = 0 | 0                    |

The funnel is perfectly monotonic (opened ≥ clicked ≥ entered), so no
rows had to be dropped.

**One cleaning decision was required.** time_to_click_sec = 0 is not a
zero-second click — it is a sentinel for "never clicked", and it appears
in all 84 non-clicking rows. Left as-is it drags the mean  
latency down from 32.9 s to 14.5 s. It was masked to NaN so temporal
statistics are computed on the 66 genuine clickers only.

**Global benchmarks**

| **Metric**                         | **Value**                    |
|------------------------------------|------------------------------|
| Open Rate                          | **81.33 %** (122 / 150)      |
| CTR (clicks / opens)               | **54.10 %** (66 / 122)       |
| Submission Rate (submits / clicks) | **62.12 %** (41 / 66)        |
| End-to-end compromise              | **27.33 %** of the workforce |
| Median time-to-click               | 15.0 s                       |

The steepest drop-off is at the open→click step; but of those who click,
nearly **two thirds go on to surrender credentials**. The click is
effectively the point of no return.

**2. Task 3a — CTR by Psychological Bias**

| **Bias**   | **Targeted** | **Opened** | **Clicked** | **\*\*CTR %\*\*** | **Submit-of-clicks %** | **Median TTC** |
|------------|--------------|------------|-------------|-------------------|------------------------|----------------|
| Authority  | 73           | 65         | 37          | **56.92**         | 62.16                  | 12 s           |
| Scarcity   | 46           | 39         | 22          | **56.41**         | 68.18                  | 15 s           |
| Commitment | 31           | 18         | 7           | **38.89**         | 42.86                  | 99 s           |

Authority and Scarcity are statistically indistinguishable from each
other and both clearly outrunCommitment. χ²(bias vs click) = 7.37, p =
**0.025** — bias category is a significant predictor of clicking.

**3. Task 3b — Data Submission Rate per Template**

| **Template**             | **Bias**   | **Targeted** | **CTR %** | **Submit-of-clicks %** | **\*\*Submit-of-targeted %\*\*** |
|--------------------------|------------|--------------|-----------|------------------------|----------------------------------|
| FIN_URGENT_AUDIT         | Authority  | 38           | 52.94     | **77.78**              | **36.84**                        |
| EXTERNAL_BENEFITS_RAFFLE | Scarcity   | 21           | 55.56     | 70.00                  | 33.33                            |
| FIN_BONUS_EXP            | Scarcity   | 25           | 57.14     | 66.67                  | 32.00                            |
| TECH_MANDATORY_PATCH     | Authority  | 35           | **61.29** | 47.37                  | 25.71                            |
| HR_POLICY_UPDATE         | Commitment | 31           | 38.89     | 42.86                  | 9.68                             |

Note the inversion between the two Authority templates:
TECH_MANDATORY_PATCH wins the *click* (61.3 %)  
but converts worst of the two (47.4 %), while FIN_URGENT_AUDIT gets
fewer clicks yet converts **77.8 %** of them. A patch prompt gets
curiosity clicks; an audit threat gets compliance. **Ranking templates
by CTR alone would pick the wrong most-dangerous template.**

**4. Task 3c — Department × Bias Cross-Tabulation**

**CTR % (clicks / opens)**

| **Dept** | **Authority** | **Commitment** | **Scarcity** |
|----------|---------------|----------------|--------------|
| Finance  | 50.0          | 20.0           | **69.2**     |
| HR       | **63.2**      | 50.0           | 66.7         |
| Tech     | 58.3          | 40.0           | 41.2         |

**Credential submission % (of all targeted)**

| **Dept** | **Authority** | **Commitment** | **Scarcity** |
|----------|---------------|----------------|--------------|
| Finance  | 26.1          | 9.1            | 35.3         |
| HR       | **45.5**      | 18.2           | **45.5**     |
| Tech     | 25.0          | 0.0            | 22.2         |

χ²(department vs click) = 0.914, p = **0.633** — department *on its own*
explains nothing. Vulnerability is not a property of the department; it
is a property of the **department–bias pairing**, which is exactly why
the interaction table above matters more than either marginal.

**5. Task 4 — Temporal Modelling**

| **Bias**   | **n** | **Mean** | **Median** | **Max** | **% of clicks ≤ 30 s** |
|------------|-------|----------|------------|---------|------------------------|
| Authority  | 37    | 17.2 s   | 12 s       | 58 s    | **86.5 %**             |
| Scarcity   | 22    | 17.5 s   | 15 s       | 44 s    | **81.8 %**             |
| Commitment | 7     | 164.4 s  | 99 s       | 560 s   | **0.0 %**              |

The KDE panel shows two entirely non-overlapping regimes. Authority and
Scarcity produce a single sharp  
spike at ~10–15 s — inside the reflexive **System-1** window, before
deliberation can engage. Commitment produces a broad, flat curve centred
near 100 s, with *not one* click under 30 s: every Commitment victim
read, weighed, and then clicked anyway. That is **System-2 failure**, a
different vulnerability requiring a different countermeasure — awareness
training cannot fix a decision that was already deliberate.

**6. Task 5 — Structural Vulnerabilities & Empirical Findings**

**6.1 Structural weaknesses in the dataset (must be stated before the
conclusions)**

1\. **Bias is perfectly confounded with template.** Each template_id
maps to exactly one  
psychological_bias, and Commitment is carried by the single template
HR_POLICY_UPDATE. Every "Commitment" result is therefore really a result
about *one email*. Its low CTR (38.9 %) may be poor copywriting, an
unconvincing sender, or spam-filtering — the design cannot distinguish
these from a genuine weakness of the commitment principle. **Commitment
is the least trustworthy row in every table.**

2\. **Unequal and non-randomised exposure.** Authority n=73 vs
Commitment n=31. Departments also received different mixes (Tech got 28
Authority emails but only 9 Commitment). Marginal comparisons across
biases are not like-for-like.

3\. **Thin interaction cells.** Finance×Commitment has 5 opens and **1
clicker** — its "20 % CTR" is one person. Tech×Commitment's "0 %
submission" rests on 2 clickers. These cells are illustrative, not
evidence.

4\. **Sentinel-coded timing.** time_to_click_sec = 0 overloads "no
click" onto a numeric measurement column. Any naive .mean() on the raw
column is wrong.

5\. **One extreme outlier.** EMP148 (HR, Commitment) clicked at **560
s** — 3.7× the next-largest value. It alone lifts the Commitment mean
from ~98 s to 164 s; the median (99 s) is the honest statistic.

6\. **No control group and no time-of-day / seniority / tenure fields**,
so no baseline click rate exists and  
confounders cannot be adjusted for.

**6.2 Which group is most vulnerable to which bias**

**Ranked by end-to-end compromise (credentials submitted / targeted):**

| **Dept × Bias**      | **Targeted** | **CTR %** | **\*\*Compromise %\*\*** | **Median TTC** |
|----------------------|--------------|-----------|--------------------------|----------------|
| **HR × Authority**   | 22           | 63.2      | **45.5**                 | 10.5 s         |
| **HR × Scarcity**    | 11           | 66.7      | **45.5**                 | 22.5 s         |
| Finance × Scarcity   | 17           | 69.2      | 35.3                     | 14.0 s         |
| Finance × Authority  | 23           | 50.0      | 26.1                     | 15.0 s         |
| Tech × Authority     | 28           | 58.3      | 25.0                     | 16.5 s         |
| Tech × Scarcity      | 18           | 41.2      | 22.2                     | 15.0 s         |
| HR × Commitment      | 11           | 50.0      | 18.2                     | 103.5 s        |
| Finance × Commitment | 11           | 20.0      | 9.1                      | 99.0 s         |
| Tech × Commitment    | 9            | 40.0      | 0.0                      | 109.5 s        |

**Finding 1 — HR is the organisation's soft target, and Authority is the
key that opens it.**  
HR × Authority: 63.2 % CTR, **45.5 % of everyone targeted surrendered
credentials**, at a median of **10.5 s** — the fastest cell in the
study. HR is trained to respond promptly to directives from  
leadership, and that professional reflex is precisely the attack
surface. Sample is adequate (n=22).

**Finding 2 — HR × Scarcity is equally lethal but n=11; treat as
corroborating, not independent.**  
It reproduces the HR pattern rather than proving a second one.

**Finding 3 — Finance is bought, not commanded.** Finance is the *most*
click-prone department for Scarcity (69.2 % CTR, highest in the matrix)
yet only average on Authority (50.0 %). Financial-incentive framing
("bonus expiring", "raffle") beats hierarchical pressure for this group.

**Finding 4 — Tech is the most resilient department but is not immune to
Authority.** Tech resists  
Scarcity (41.2 % CTR, lowest non-Commitment cell) — but
TECH_MANDATORY_PATCH still produced the campaign's highest
single-template CTR at 61.3 %. **Technical fluency is not protection
when the lure is phrased in the target's own professional vocabulary.**

**Finding 5 — The click, not the email, is the control point.** 62 % of
clickers submitted credentials.  
With 86.5 % of Authority clicks landing under 30 s, awareness messaging
that asks people to "stop and think" is competing against a reaction
that completes before deliberation begins. Effort is better spent on
controls that do not depend on the user's judgement in that window.

**6.3 Recommendations**

1\. **Prioritise HR for Authority-themed re-training**, using
verify-out-of-band drills rather than slide decks — the 10.5 s latency
means the countermeasure must be procedural, not cognitive.

2\. **Target Finance with incentive/scarcity-framed simulations**, not
executive-impersonation ones.

3\. **Do not exempt Tech from Authority testing.** Their resilience is
domain-specific.

4\. **Deploy technical controls at the click boundary** (link
rewriting/detonation, phishing-resistant MFA, credential-submission
blocking) since 62 % of clicks convert.

5\. **Fix the experiment before the next round:** run ≥2 templates per
bias, randomise and balance exposure across departments, add a control
group, and record non-clicks as NULL rather than 0. Until then, all
Commitment conclusions should be reported as provisional.

![[IMG-20260806091932059.png]]
# References


###### Information
- date: 2026.08.06
- time: 09:19