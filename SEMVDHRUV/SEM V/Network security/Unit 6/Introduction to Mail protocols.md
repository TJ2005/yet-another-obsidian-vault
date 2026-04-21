# Introduction

## E-mail Components
**Message User Agents**: Operates on the behalf of user. Typically installed on user's computer and is referred as *==client email program==* or *==local network e-mail server==* 

**Message Handling Service:** Consists of MSA, MTA, MDA.
	1) **Message Submission Service**: Accepts the message submitted by the MUA and enforces the policies of the hosting domain on the message. Maybe installed along with MUA or can exist as a separate functional model.
	2) **Message Transfer Agent:** Relays message for one application-level hop. It acts like a packet switch or IP router with a goal of making the message closer to the recipients
	3) **Message Delivery Agent:** Responsible for transferring the message from MHS to the MS

**Message Store:** A MUA can employ a leg term MS. MS can be located on a remote server or can exist with MUA on the user's machine. MUA typically retrieves message from MS using POP (Post Office Protocol) or IMAP (Internet Message Access Protocol).

**Message User Agent:** The other receiver end.

![[IMG-20251117143944739.png| 600]]

---
## Email Protocols
Two major types exist.

### SMTP
Simple Mail Transfer Protocol. 
**Method**:
- Encapsulates an email message in an envelope. 
- Relays the envelope from source to destination.
- Recurs over a single TCP Connection
- Port Number : 25, 465, 587.

**Function:**
	- SMTP consists of a series of commands and responses exchanged between the STMP sender and receiver. Initiative is with the SMTP sender who establishes the TCP connection
	- Once the TCP connection is established 
- The **SMTP sender** initiates the process.
- It **establishes a TCP connection** with the **SMTP receiver**.
- Once connected, the **sender takes the initiative** and sends commands.
- Each **command**:
    - Is a **single line of text**.
    - **Begins with a four-letter command code** (e.g., `HELO`, `MAIL`, `RCPT`, `DATA`, etc.).
    - May be **followed by arguments** (e.g., an email address).
- For **every command**, the **receiver sends exactly one reply**.
- A **reply** can be:
    - **Single-line**, or
    - **Multi-line** (for extended responses).
- Each line of reply:
    - **Begins with a three-digit code**, indicating the status.
    - May include **optional explanatory text**.

```smtp 
S: 220 foo.com Simple Mail Transfer Service Ready
C: HELO bar.com
S: 250 OK
C: MAIL FROM:<Smith@bar.com>
S: 250 OK
C: RCPT TO:<Jones@foo.com>
S: 250 OK
C: RCPT TO:<Green@foo.com>
S: 550 No such user here
C: RCPT TO:<Brown@foo.com>
S: 250 OK
C: DATA
S: 354 Start mail input; end with <crlf>.<crlf>
C: Blah blah blah . . .
C: . . . etc. etc. etc.
C: <crlf><crlf>
S: 250 OK
C: QUIT
S: 221 foo.com Service closing transmission channel
```

## Mail Access Protocol

### POP3
POP3 allows MUA's to download the e-mails from an e-mail server. POP3 user agents connect via TCP connection. Username and Password is used to authenticate the user's. Once Authenticated User's use POP3 commands to delete or retrieve mails
Characteristics:
	Typically operates on port 110
### IMAP
Similar to POP3, Internet Mail Access Protocol Also uses an email client to access mail on an email server.
IMAP offers additional functionalities than POP. 
*Characteristics*:
	Provides a stronger authentication.
	More complex than POP3
	Provides everything that POP3 has
	Typically operates on port 140



## Email Formats
To understand S/MIME we need to understand MIME and to understand RFC.

### RFC 5322 – Internet Message Format (Summary)

* Defines the basic structure of Internet email messages.
* RFC 5322 focuses on the **format**, not the content or transmission.

### MIME

Multipurpose Internet Mail is a extension of RFC 5322 a framework that is intended to solve some problems and limitations of the use of SMTP  

Limitations of SMTP
- SMTP cannot transfer binary of executable files
* Limited to **7-bit ASCII**, so **non-English characters** aren’t supported.
* **Message size** may be restricted 
* Some implementations **don’t fully follow RFC 821**, leading to issues like:
  * Line truncation or wrapping
  * Lost whitespace or tabs
  * Inconsistent line endings
  * Unwanted padding or conversions

## E-mail Threats and E-mail Security
* **Authenticity threats:** Unauthorized access to email systems.
* **Integrity threats:** Unauthorized modification of email content.
* **Confidentiality threats:** Unauthorized disclosure of sensitive information.
* **Availability threats:** Blocking users from sending or receiving email.

## Topics we are gonna cover....

**SP 800-177 (Trustworthy Email)** recommends the following standardized countermeasures:

* **STARTTLS:** SMTP extension that runs over TLS to provide authentication, integrity, non-repudiation, and confidentiality for messages.
* **S/MIME:** Provides digital signatures and encryption for message authentication, integrity, and confidentiality.
* **DNSSEC:** Protects DNS data from tampering and ensures authenticity; supports other email security protocols.
* **DANE:** Uses DNSSEC to authenticate public keys and verify mail server certificates, reducing dependence on certificate authorities.
* **SPF (Sender Policy Framework):** Uses DNS records to specify authorized IP addresses for a domain’s mail senders; helps prevent spoofing.
* **DKIM (DomainKeys Identified Mail):** Lets mail servers sign message headers and bodies, verifying source domains and ensuring integrity.
* **DMARC (Domain-based Message Authentication, Reporting, and Conformance):** Builds on SPF and DKIM to report their effectiveness and instruct receivers how to handle suspicious messages.

DANE = DNS-based Authentication of Named Entities
DKIM = DomainKeys Identified Mail
DMARC = Domain-based Message Authentication, Reporting, and Conformance
DNSSEC = Domain Name System Security Extensions
SPF = Sender Policy Framework
S/MIME = Secure Multi-Purpose Internet Mail Extensions
TLSA RR = Transport Layer Security Authentication Resource Record