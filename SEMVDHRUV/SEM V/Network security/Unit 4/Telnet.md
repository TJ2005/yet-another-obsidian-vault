### Overview

- **Definition:** Telnet is a network protocol used to provide bidirectional interactive text‑based communication between a client and a remote host.
- **Port:** Default port is **23 (TCP)**.
- **Functionality:** Allows remote login and command execution.
- **Limitations:**
    - Transmits data (including usernames and passwords) in plaintext.
    - Vulnerable to eavesdropping and man‑in‑the‑middle attacks.
    - No encryption or secure authentication.
- **Status:** Considered obsolete and insecure; replaced by secure alternatives like SSH.

---

## Telnet vs SSH

| Aspect         | Telnet                      | SSH (Secure Shell)                      |
| -------------- | --------------------------- | --------------------------------------- |
| Default Port   | 23                          | 22                                      |
| Encryption     | None (plaintext)            | Strong encryption (AES, ChaCha20, etc.) |
| Authentication | Plaintext username/password | Password, public key, multi‑factor      |
| Security       | Vulnerable to interception  | Secure against eavesdropping and MITM   |
| Integrity      | No protection               | Ensures data integrity via hashing      |
| File Transfer  | Not supported               | Supports SCP, SFTP                      |
| Usage Today    | Rare, legacy systems only   | Standard for secure remote login        |

---

## Key Points

- **Telnet** was widely used in early networking for remote administration but is insecure due to lack of encryption.
- **SSH** replaced Telnet by providing secure, encrypted communication, authentication, and additional features like tunneling and secure file transfer.

---