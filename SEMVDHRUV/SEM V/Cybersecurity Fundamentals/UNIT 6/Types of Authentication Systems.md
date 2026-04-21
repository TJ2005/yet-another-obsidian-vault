	
## Authentication Tokens

Authentication tokens are digital keys that prove a user's identity and grant access to the system without repeatedly providing the credentials.

### Types of Authentication Tokens
1. Challenge/Response Tokens
2. Time-based Tokens

| Feature               | Challenge/Response Tokens                         | Time-Based Tokens (e.g., TOTP, expiring JWTs)         |
| --------------------- | ------------------------------------------------- | ----------------------------------------------------- |
| **Trigger**           | Server sends a challenge; client must respond     | Token is valid only for a specific time window        |
| **Client Input**      | Challenge + secret (e.g., seed, password)         | Time + secret (e.g., seed or shared key)              |
| **Server Role**       | Issues challenge, verifies response               | Verifies token based on current time and secret       |
| **Replay Protection** | Strong (challenge is unique per session)          | Moderate (short expiry reduces replay window)         |
| **Clock Dependency**  | No dependency on synchronized clocks              | Requires accurate time sync between client/server     |
| **Token Format**      | Often opaque or HMAC of challenge                 | Often numeric (TOTP) or structured (JWT with `exp`)   |
| **Use Case**          | Login, MFA, API auth with nonce                   | MFA (TOTP), session tokens, JWT-based APIs            |
| **Example Protocols** | SCRAM, CHAP, custom HMAC challenge schemes        | TOTP (RFC 6238), JWT with `exp`, OAuth2 access tokens |
| **Seed Usage**        | Used to derive HMAC of challenge                  | Used to derive HMAC of time slice                     |
| **Auditability**      | High (challenge logs, nonce tracking)             | Moderate (token expiry logs)                          |
| **Complexity**        | Higher (requires challenge issuance and tracking) | Lower (stateless validation possible)                 |
| **Offline Usability** | Poor (requires server challenge)                  | Good (TOTP works offline if clocks are synced)        |
|                       |                                                   |                                                       |
### 3. OTPs
These types of passwords can be used exactly once
Challenge is number of authentications and responses password for that particular number.

### 4. S/Key
### 5. Encrypted Key Exchange (EKE)
Diffie-Hellman and Elliptic Curve Method
### 6. Certificate based Authentication
1. User sends a login request
2. Server creates a random challenge
3. User signs the random challenge
4. Server returns an appropriate Message back to the user

### 7. Biometric Authentication
Two Types
1. Physiological: Relies on unique physical characteristics e.g. fingerprint, face
2. Behavioral: Relies on traits associated with behavior e.g. keystrokes interval
### 8. Kerberos Server

### 9. 2FAs/Multifactor Authentication