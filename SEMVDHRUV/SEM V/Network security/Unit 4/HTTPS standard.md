## Overview

HTTPS (HyperText Transfer Protocol Secure) is the secure version of HTTP, combining it with SSL/TLS to provide encrypted communication between client and server. It ensures confidentiality, integrity, and authentication for web traffic.

---

## Features

- **Encryption:** Uses SSL/TLS to encrypt data exchanged between browser and server.
- **Authentication:** Validates server identity via digital certificates issued by trusted Certificate Authorities (CAs).
- **Integrity:** Protects against tampering of data during transmission.
- **Port:** Default port is 443.

---

## Working

1. **Client Request:** Browser requests a secure connection to the server.
2. **Server Certificate:** Server presents its SSL/TLS certificate.
3. **Verification:** Browser verifies certificate authenticity using CA trust chain.
4. **Key Exchange:** Secure session key is established using asymmetric cryptography.
5. **Secure Communication:** All subsequent data is encrypted using symmetric encryption.

---

## Advantages

- Protects sensitive data such as login credentials, payment information, and personal details.
- Prevents eavesdropping and man‑in‑the‑middle attacks.
- Builds user trust through visible indicators (padlock icon, “https://”).
- Required for modern web standards (e.g., HTTP/2, browser security policies).

---

## Limitations

- Slightly higher computational overhead compared to HTTP.
- Requires valid SSL/TLS certificates, which must be renewed periodically.
- Misconfigured certificates or weak ciphers can still expose vulnerabilities.

---

## Comparison with HTTP

|Aspect|HTTP|HTTPS|
|---|---|---|
|Security|No encryption|Encrypted via SSL/TLS|
|Authentication|None|Certificate‑based|
|Integrity|Vulnerable to tampering|Ensures integrity|
|Default Port|80|443|
|Trust Indicator|None|Padlock icon / “https://”|

---
