
## Overview

Wired Equivalent Privacy (WEP) was the **original security protocol for Wi‑Fi networks**, introduced as part of the IEEE 802.11 standard in 1997. Its goal was to provide a level of confidentiality comparable to wired networks. Despite its intent, WEP is now considered **obsolete and insecure** due to fundamental cryptographic weaknesses.

---

## Key Features

- **Encryption Algorithm:** Uses RC4 stream cipher.
- **Key Lengths:** 40‑bit or 104‑bit secret key, combined with a 24‑bit Initialization Vector (IV).
- **Authentication:** Shared key or open system authentication.
- **Goal:** Protect wireless traffic from eavesdropping and unauthorized access.

---

## Operation Flow

1. A 24‑bit IV is generated for each packet.
2. The IV is concatenated with the secret key to form the RC4 seed.
3. RC4 generates a keystream, which is XORed with plaintext data to produce ciphertext.
4. The IV is sent in cleartext with the packet so the receiver can reconstruct the keystream.
5. Integrity check (CRC‑32) is appended to detect transmission errors.

---

## Weaknesses

- **Short IV (24 bits):** IVs repeat quickly, leading to keystream reuse.
- **RC4 vulnerabilities:** Weaknesses in RC4 key scheduling allow attacks.
- **Weak integrity check:** CRC‑32 is not cryptographically secure.
- **Key management issues:** Static keys rarely changed, making compromise easier.
- **Practical attacks:** Tools like Aircrack‑ng can recover WEP keys within minutes.

---

## Comparison with Successors

|Protocol|Cipher|Key Length|Security Status|
|---|---|---|---|
|WEP|RC4|40/104 bit|Broken, obsolete|
|WPA|TKIP|128 bit|Stronger but legacy|
|WPA2|AES‑CCMP|128 bit+|Secure (standard today)|
|WPA3|AES‑GCMP, SAE|192 bit+|Modern, recommended|

---

## Real‑World Impact

- WEP was widely deployed in early Wi‑Fi networks.
- Its weaknesses led to rapid adoption of WPA and WPA2.
- Today, WEP is **deprecated**; modern devices often refuse to connect to WEP networks.
- Networks still using WEP are highly vulnerable to unauthorized access.

---

## Key Insights

- WEP was a **first attempt** at wireless security but failed due to poor cryptographic design.
- Its reliance on RC4 and short IVs made it fundamentally insecure.
- Modern Wi‑Fi security relies on WPA2/WPA3, which fix WEP’s flaws with stronger encryption and authentication.
