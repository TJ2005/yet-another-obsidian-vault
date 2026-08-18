	
- Identification is the act of asserting who a person is.
- Authentication is proving that asserted identity.

such recognition occurs between people, computer processes (executing programs), network connections, devices, and similar active entities. In security, all these entities are called **==subjects==**..

_**Authentication Basics**_

1. **Definition:** **Authentication** is the process of binding an identity (that of the external entity, like a person) to a subject (the computer entity, like a process).
2. **Establishing Identity:** Identity is typically established using one or more of the following factors:
    - What the entity **knows** (e.g., **password**, PIN). 
    - What the entity **has** (e.g., badge, smart card).
    - What the entity **is** (e.g., fingerprints, retinal characteristics).
    - Where the entity **is** (e.g., in front of a specific terminal).
3. **Authentication System Components:** An authentication system is formally described by the tuple (A, C, F, L, S), where:
    - **A** is the authentication information that proves identity.
    - **C** is the complementary information stored on the computer used to validate A.
    - **F** is the complementation function ($f: A \rightarrow C$).
    - **L** represents authentication functions that prove identity.
    - **S** represents selection functions enabling the entity to create or alter information in A or C.

_**Passwords**_

### **Definition and Types:**
A password is a sequence of characters (e.g., 10 digits, strings of letters) or a sequence of words (pass-phrases). They can be generated randomly, by the user, or by the computer with user input.

- **Storage Methods:**
    - **Clear Text:** Storing passwords in clear text in the user database means they are vulnerable, as they also travel in clear text from the user's computer to the server.
    - **Message Digests (MD):** Systems often store message digests (hashes) of passwords in the user database instead of the clear text passwords. The server calculates the MD of the entered password and compares it to the stored MD.
	    - **MD Drawback:** Using MDs alone is vulnerable to a **replay attack** if the user sends their username (UN) and the calculated MD directly to the server.
	    - **Adding Entropy:**
		    - It is the easiest way to avoid a replay attack
		    - We basically make the server give a random challenge to the user.
		    - The user hashes the password and hashes it again and sends it to server.
		    - Server hashes its MD Record for the user with the nonce and checks $L$ and then the user is authenticated if the match is true.

![[Pasted image 20251122145711.png]]


## **Password Selection & Attacks:**
**User Selection Issues:** Users tend to select easily guessable passwords, such as those based on names, dictionary words, license plates, personal characteristics, or passwords that are too short, or only contain digits or letters.

### **Dictionary Attacks**
These involve trial-and-error using a list of potential passwords.

- **Off-line attacks** occur when the attacker knows the function ($f$) and the stored complementary information ($C$'s, like hashes) and repeatedly tries guesses until the password is found (e.g., tools like `crack` or `john-the-ripper`).

- **On-line attacks** involve attempting to log in by guessing the password through access to the authentication functions ($L$).

### **Password Security Management**
- **Guessing Prevention:** Although attacks through $L$ (on-line guessing) cannot be completely prevented (or legitimate users couldn't log in), they can be slowed down using techniques like **Backoff, Disconnection, Disabling**, or **Jailing** (allowing restricted activities).
- **Proactive Password Checking:** This continuously analyzes a proposed password for "goodness". It is always invoked and can reject passwords deemed "bad" based on pattern matching or execution of subprograms like a spell checker.
- **Password Aging:** This forces users to change passwords after a set time. To prevent reuse, the system may record previous passwords or block changes for a defined period.

#### **Dictionary Attacks**

- **Method:** Trial-and-error using a list of potential passwords.
- **Off-line Attack:** Attacker knows the complementation function ($f$) and the stored complementary information ($C$'s), repeatedly trying different guesses ($g$) until the password is guessed.
    - _Examples:_ `crack`, `john-the-ripper`.
- **On-line Attack:** Attacker accesses the authentication functions ($L$) and tries guesses ($g$) until one succeeds.
    - _Example:_ Trying to log in by guessing a password.

### Andersons

The components of Anderson's formula are defined as follows:

- **P:** The **probability** of guessing a password in a specified period of time.
- **G:** The **number of guesses tested in 1 time unit**.
- **T:** The **number of time units**.
- **N:** The **number of possible passwords**. $N$ is also equal to $|A|^s$, where $A$ is the set of strings making up passwords, and $s$ is the length of the password.
- The relationship is expressed as: **$P \geq TG/N$**.

This formula is typically applied in the context of analyzing the minimum required password length to resist dictionary or brute-force attacks over a given period.

For instance, an example using this formula seeks to find the minimum password length ($s$) needed if:

1. Passwords are drawn from a 96-character alphabet (implying the size of the set $A$ is 96).
2. The system can test $10^4$ guesses per second ($G = 10^4$).
3. The probability of success ($P$) is set to 0.5 over a 365-day period ($T = 365 \times 24 \times 60 \times 60$ seconds).

The solution calculates $N \geq TG/P = (365 \times 24 \times 60 \times 60) \times 10^4 / 0.5 \approx 6.31 \times 10^{11}$. By then choosing the length ($s$) such that the sum of possible passwords ($\Sigma_{j=0}^{s} 96^j$) is greater than or equal to $N$, the result suggests that passwords must be at least 6 characters long ($s \geq 6$).


---

### Pronounceable Passwords

* Generate using random phonemes (cv, vc, cvc, vcv)
* Examples: helgoret, juttelon are more likely to occur | przbqxdfl, zxrptglfn $\times$
* Problem: too few possibilities
* Solution: **key crunching** → hash long key → convert to printable sequence → use as password

---
### User-Selected Passwords

* People pick easy-to-guess passwords
* Patterns: account names, usernames, computer/place names, dictionary words
* Weak formats: too short, digits-only, letters-only, license plates, acronyms, SSN, personal traits

---

### Proactive Password Checking

* Always checks password “goodness” when chosen
* Can reject weak passwords per user/site rules
* Uses pattern matching, subprograms (spell checker)
* Easy to integrate into selection system

---

### Guessing via Login

* Cannot fully prevent (legitimate users must log in)
* Mitigate: slow attacks, backoff, disconnection, temporary disabling
* High-risk accounts: restrict activities (jailing)

---

### Password Aging

* Force password change after a set time
* Prevent reuse: record old passwords, block re-selection
* Balance: give time to create new password, warn before expiration
* Avoid forcing change before next login

---
