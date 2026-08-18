# Types of Attacks on Authentication Schemes

## 1. Session Hijacking
### Meaning
- An attacker **takes over an active session** between a user and a system.
- They steal or guess the session ID and continue the session as if they were the real user.

### Simple Definition
- **Attacker jumps into your already-logged-in session and acts as you.**

---

## 2. Man-in-the-Middle (MITM) Attack
### Meaning
- An attacker secretly **intercepts and possibly alters** communication between two parties who think they are talking directly to each other.

### Simple Definition
- **Attacker sits in the middle and listens or changes messages between you and the website.**

---

## 3. Brute Force Attack
### Meaning
- An attacker tries **every possible password or key combination** until the right one is found.
- Requires time + computing power.

### Simple Definition
- **Trying all possible passwords until one works.**

---

## 4. Dictionary Attack
### Meaning
- A refined brute-force attack where the attacker tries **common words, names, phrases, and known password patterns** instead of random combinations.

### Simple Definition
- **Trying common passwords like “password123”, “admin”, “qwerty”, or words from a dictionary.**

---

## 5. Replay Attack
### Meaning
- An attacker captures a valid authentication message (e.g., login request) and **replays it later** to gain unauthorized access.

### Simple Definition
- **Attacker records your valid login message and plays it again to fool the system.**

