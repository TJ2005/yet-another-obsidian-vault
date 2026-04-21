SPF is a standardized way for sending domain information to identify and assert mail senders for a given domain. In other words, SPF allows domain admins to specify which mail servers are authorized to send the mails on behalf of their domain.

Without SPF:
- **Any server can claim to send email from any domain**, regardless of whether it actually belongs to that domain.
- This is because **SMTP (Simple Mail Transfer Protocol)** does not verify the sender’s domain against the server’s IP address.

Major drawbacks of the freedom.
1. Spam or UBE (Unsolicited Bulk Emails): Without proper verification of the sender's server domain. Anyone can send any e-mail on behalf of anyone. Abusing this spammers can forge e-mails for a phishing attack
2. ADMDs (Admin Management Domain): are understandably concerned about the ease with which unauthorized entities can make use of their domains.

### SPF on Sender's Side
SPF works by checking sender's IP address against the policy enforced by the SPF Records found in the sending domain. A sending domain has a task of identifying all the authorized users that can send mails on behalf of the domains. A Resource Record is created into DNS database for each authorized sender.

### SPF on Receiver's Side
If SPF is implemented on receiver's side then, The SPF collects the address domain and the IP of the sender which is then sent to the sending domain to query if the sender is a authorized user or not. SPF checks can start even before the contents of the mail has been received which may result in block or buffering of the mail contents until all the checks are finished. Checks must be completed before the mail message is sent to the end user’s inbox.
The checking involves the following rules:
 **1. No SPF TXT Resource Record Returned → Accept the Message**
- If the domain has **no SPF record** in DNS:
    - The receiving server **cannot verify** the sender's legitimacy.
    - Default behavior: **accept the email**.
- Why? SPF is **optional**, and absence of a record doesn’t imply malicious intent.

 **2. SPF TXT Record Exists but Has Formatting Errors → Accept the Message**
- If the SPF record is **malformed** (e.g., syntax errors, invalid directives):
    - The server **ignores the record**.
    - Default behavior: **accept the email**.
- Reason: To avoid false positives or rejecting legitimate mail due to misconfiguration.

**3. Valid SPF TXT Record Found → Evaluate Using Mechanisms and Modifiers**
- The server parses the SPF record and applies its **mechanisms** and **modifiers**:
    - **Mechanisms**: Define matching rules (e.g., `ip4`, `include`, `a`, `mx`, `all`)
    - **Modifiers**: Provide additional instructions (e.g., `redirect`, `exp`)
- Based on the evaluation, the server returns one of these results:
    - `Pass`: Sender is authorized → accept
    - `Fail`: Sender is not authorized → reject or flag
    - `SoftFail`: Sender is probably unauthorized → accept but mark suspicious
    - `Neutral`: No definitive result → accept
    - `PermError`: Permanent error in SPF → accept
    - `TempError`: Temporary DNS issue → accept


| Scenario             | Action Taken by Receiving Server |
| -------------------- | -------------------------------- |
| No SPF record        | Accept the message               |
| Malformed SPF record | Accept the message               |
| Valid SPF record     | Evaluate and act accordingly     |
