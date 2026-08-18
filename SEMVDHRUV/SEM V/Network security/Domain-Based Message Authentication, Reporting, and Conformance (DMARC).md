### **DMARC (Domain-Based Message Authentication, Reporting, and Conformance)**

**RFC 7489 – March 2015**

* Enables senders to specify:

  * How receivers should handle their mail (deliver, flag, reject).
  * What kind of reports to send back and how often.

* Works **with SPF and DKIM** to verify sender authenticity.

* **SPF/DKIM Limitations:**
  * Don’t specify if they’re in use.
  * Don’t provide feedback to sender.
  * Receiver can’t tell if unsigned mail is legitimate or spoofed.

* **DMARC fixes this by:**

  * Standardizing receiver behavior when checking SPF/DKIM.
  * Adding reporting and policy mechanisms via DNS records.

---

### **Identifier Alignment (Core of DMARC)**

| Mechanism | Authenticates        | Domain Checked          | Alignment Requirement                 |
| --------- | -------------------- | ----------------------- | ------------------------------------- |
| **SPF**   | SMTP envelope sender | MAIL FROM / HELO        | Must align with “From” header domain  |
| **DKIM**  | Signing domain       | `d=` tag in DKIM header | Must align with “From” header domain  |
| **DMARC** | Visible sender       | RFC 5322 “From” field   | Must match at least one (SPF or DKIM) |

* **Alignment ensures:** the visible “From” domain is authenticated by SPF or DKIM.
* Prevents spoofing using mismatched domains.
* Uses “From” header since it’s always present and shown to end users.


### **DMARC Operation (Concise Notes)**

#### **Sender Side**
* **Prerequisite:** Sender must use **SPF**, **DKIM**, or both.
* **Policy Setup:**
  * Publishes **DMARC policy** in DNS as a **TXT record** (`tag=value` pairs).
  * Includes email addresses for **aggregate** and **forensic reports** (may attract spam → need countermeasures).
* **Message Flow:**

  1. Domain owner publishes **SPF**, **DKIM**, and **DMARC** policies.
  2. Author creates message → submits to **mail submission service**.
  3. Submission service generates **DKIM signature**.
  4. Message is sent to **transport service** for delivery.

#### **Receiver Side**
1. Perform basic checks (IP blocklist, domain reputation, rate limits).
2. Extract **RFC 5322 From** address (must be valid, single address).
3. Query DNS for **DMARC record** → if missing, stop DMARC checks.
4. Verify **DKIM signature(s)** (at least one must pass).
5. Query and validate **SPF record**.
6. Perform **Identifier Alignment** → ensure *From domain* matches DKIM/SPF-authenticated domain.
