	
# Authentication Techniques Notes

## Basics
- **Authentication**: Binding of identity to subject.  
- **Identity**: External entity (e.g., person’s identity).  
- **Subject**: Computer entity (e.g., process).  

---

## Establishing Identity
- **What entity knows** → Password, PIN  
- **What entity has** → Badge, smart card  
- **What entity is** → Fingerprints, retinal characteristics  
- **Where entity is** → Location-based (e.g., at a terminal)  

---

## Authentication System (A, C, F, L, S)
- **A**: Authentication information proving identity  
- **C**: Complementary information stored on computer for validation  
- **F**: Complementation function $f:A \to C$  
- **L**: Authentication functions that prove identity  
- **S**: Selection functions enabling entity to create/alter info in A or C  

---

## Passwords
- Sequence of characters (digits, letters, words, pass-phrases).  
- Generated randomly, by user, or computer-assisted.  
- Algorithms: Challenge-response, one-time passwords.  

---

### Clear Text Passwords
- User enters UID + PW → validated → result returned.  
- **Drawbacks**:  
  - DB stores PW in clear text.  
  - PW travels in clear text → insecure.  

---

### Message Digest (MD) of Passwords
- Store **MD of PW** in DB instead of clear text.  
- User sends UN + MD → server compares with stored MD.  
- **Drawback**: Replay attacks possible.  

---

### Adding Randomness
- Server issues random challenge.  
- User signs challenge with MD of PW.  
- Server verifies encrypted challenge.  

---

## Dictionary Attacks
- **Offline**: Attacker knows $f$ and $C$, tries guesses $g \in A$.  
- **Online**: Attacker uses login functions $L$ to try guesses.  
- Tools: `crack`, `john-the-ripper`.  

---

### Anderson’s Formula
Probability of guessing password in time $T$:  
$$P \geq \frac{TG}{N}$$  

- $P$: Probability of success  
- $G$: Guesses per unit time  
- $T$: Number of time units  
- $N$: Number of possible passwords  

**Example**:  
- Alphabet size = 96 chars  
- $10^4$ guesses/sec  
- $T = 365$ days, $P=0.5$  
- $$N \geq \frac{TG}{P} = 6.31 \times 10^{11}$$  
- Password length $s \geq 6$ chars  

---

## Password Selection Approaches
- **Random selection**: Any password equally likely.  
- **Pronounceable passwords**: Generated via phonemes.  
- **User selection**: Often weak (names, dictionary words, personal info).  

---

## Proactive Password Checking
- System analyzes proposed password for strength.  
- Rejects weak passwords.  
- Uses pattern matching, spell-checkers, etc.  

---

## Guessing Through L
- Cannot prevent legitimate login attempts.  
- Mitigation:  
  - Slow down attempts (backoff, disconnection, disabling).  
  - Jailing: allow login but restrict activities.  

---

## Password Aging
- Force password changes after time expiry.  
- Prevent reuse by recording previous passwords.  
- Warn users before expiration.  

---

## Authentication Tokens
- Token + server synchronized initially.  
- Token generates fresh passwords periodically.  
- Server generates same passwords for validation.  

### Types
- **Challenge/Response Tokens**  
- **Time-based Tokens**  

---

### Challenge-Response
- User + system share secret function $f$.  
- System sends random challenge $r$.  
- User responds with $f(r)$.  
- System verifies.  

---

### Pass Algorithms
- Challenge-response where $f$ itself is secret.  
- Example: Challenge = "abcdefg", Response = "bdf".  
- Often combined with reusable password.  

---

### One-Time Passwords (OTP)
- Valid for one use only.  
- Challenge = authentication count, Response = password for that count.  
- **Problems**: Synchronization, random generation, distribution.  

---

### S/Key (Lamport’s OTP Scheme)
- Based on one-way hash function $h$.  
- User chooses seed $k$.  
- System computes chain:  
  $$h(k)=k_1,\ h(k_1)=k_2,\ ...,\ h(k_{n-1})=k_n$$  
- Passwords used in reverse order:  
  $$P_1=k_n,\ P_2=k_{n-1},...,\ P_n=k_1$$  

---

### Encrypted Key Exchange (EKE)
- Defeats offline dictionary attacks.  
- Alice + Bob share secret password $s$.  
- Random challenges encrypted → attacker cannot verify.  
- Session key $k$ established securely.  

---

### Time-Based Tokens
- Passwords generated periodically (e.g., every 60s).  
- Based on **seed value + current system time**.  
- Steps:  
  1. Password generation + login request  
  2. Server-side verification  
  3. Outcome  

---

## Certificate-Based Authentication
- Based on **digital certificates**.  
- Standard: **FIPS-196**.  
- Steps:  
  1. Create, store, distribute certificates  
  2. Login request  
  3. Server creates random challenge  
  4. User signs challenge  
  5. Server verifies and responds  

---

## Biometric Authentication
- **Physiological**: Fingerprints, retinal scans, hand geometry.  
- **Behavioral**: Voice, keystroke dynamics.  
- Uses approximate matching algorithms.  

### Considerations
- Template security, resistance to counterfeiting, durability, user acceptance, speed, revocation.  

### Metrics
- **False Reject Rate (FRR)**: Authorized user rejected.  
- **False Accept Rate (FAR)**: Unauthorized user accepted.  
- **Crossover Error Rate (CER)**: Point where FAR = FRR → lower CER = better accuracy.  

---

## Single Sign-On (SSO)
- Allows user to authenticate once and access multiple systems.  
- **Approaches**:  
  - Script-based  
  - Agent-based  

### Script-Based Approach
- SSO software mimics user actions.  
- Holds multiple sets of authentication info.  
- Batch files/scripts created with credentials for each application.  

---

### Agent-Based Approach
- Each web server runs an **agent**.  
- Agent interacts with SSO server.  
- SSO server validates credentials via user DB.  
- Agent checks for cookie:  
  - If present → validate contents.  
  - If absent → prompt login, validate, then create cookie.  

---

![[Pasted image 20251122145806.png]]