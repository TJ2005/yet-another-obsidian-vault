---
Title: "Heuristics and Biases"
Status:
tags: [hlacs, unit-1]
Date: "2026.08.24"
---

# Heuristics and Biases

> [!DEF] Two distinct things
> - **Heuristics** — mental shortcuts enabling fast judgments; rule-of-thumb strategies that shorten decision-making time (fuel of [[Decision Making in Cybersecurity|System 1]])
> - **Biases** — *systematic errors* in reasoning leading to wrong security decisions

## Affect heuristic

- **Definition:** choices influenced by the emotions felt at that moment
- Positive mood → risks seem lower, benefits higher; negative mood → focus shifts to downsides
- **Example 1:** after news of a major ransomware outbreak, a fearful analyst overestimates routine phishing risk and escalates harmless emails
- **Example 2:** someone who just watched a plane-crash documentary drives 12 hours instead of flying, despite flying being statistically safer

## Anchoring bias

- **Definition:** the first piece of information is accepted as gospel truth when deciding
- Security teams fixate on leadership's stated priority instead of assessing the entire threat landscape
- **Example 1:** the CISO declares ransomware the top threat → analysts judge every incident against it and under-investigate insider threats
- **Example 2:** a product slashed from ~~₹9,999~~ to ₹4,999 feels like a bargain — the first price anchors perceived value, even if rivals sell it for ₹4,500

## Availability heuristic

- **Definition:** the more often a situation is encountered, the more easily it comes to memory — memory/experience replaces methodical evaluation of all risks
- Teams rely on recent incidents or industry trends rather than full risk analysis
- **Example 1:** deepfake fraud dominates headlines → the team over-invests in deepfake defence while ignoring far likelier credential-stuffing attacks
- **Example 2:** a viral shark-attack video makes swimmers fear sharks, though drowning kills vastly more people

## Confirmation bias

- **Definition:** tendency to favour information that confirms existing beliefs
- Analysts anchor on a suspected cause before investigating, seeking only supporting evidence
- **Example 1:** an analyst convinced entry came via email reviews only mail logs, missing firewall evidence of the unpatched VPN exploit actually used
- **Example 2:** believing a colleague is dishonest, you notice only behaviour that fits and dismiss every genuine act of help as manipulation

## Optimism bias

- **Definition:** the misbelief "this won't happen to me" (~80% of people exhibit it)
- Structured processes and tools create false immunity
- **Example 1:** an SMB owner thinks *"we're too small to attack"* → skips MFA and backups, exactly the soft target ransomware groups prefer
- **Example 2:** drivers rate themselves above average and text at the wheel, certain accidents only happen to others

## Framing effect

- **Definition:** decisions swayed by how choices are *presented*, not by examining the facts
- Exploited by hackers framing phishing mails as urgent messages from senior officials or product updates
- **Classic pair:** *"Anti-malware A fails to detect 10%"* vs *"anti-malware B successfully detects 90%"* — identical fact, B wins
- **Example 1:** *"this control saves ₹50 lakh in breach costs"* gets approved, while *"it costs ₹10 lakh"* was rejected last quarter
- **Example 2:** yoghurt labelled **"95% fat-free"** outsells the identical **"contains 5% fat"**

## Dunning–Kruger effect

- **Definition:** unskilled individuals overestimate their ability; experts underestimate theirs
- **Example 1:** an employee finishes a 30-minute awareness module confident they can spot *any* scam — then clicks a sophisticated spear-phish, while the veteran analyst double-checks everything
- **Example 2:** a beginner who has played racing games believes they can handle highway traffic; the 20-year driver stays cautious

## Sunk cost fallacy (irrational escalation)

- **Definition:** justifying increased investment based on cumulative prior investment, despite new evidence the decision was wrong
- **Example 1:** a company keeps pouring money into an underperforming SIEM for years — *"we've already spent crores"* — instead of migrating to a better tool
- **Example 2:** sitting through a terrible three-hour movie to the end *"because we paid for the tickets"*, losing the evening too

![[p82_img_17.png]]
*Cognitive Bias Codex — 188 biases mapped by Benson/Manoogian.*

## Related

- [[Decision Making in Cybersecurity]] ← System 1 runs on heuristics
- [[SETA Program]]
- [[Security Fatigue]]
- [[HLACS Unit 1 Glossary]]