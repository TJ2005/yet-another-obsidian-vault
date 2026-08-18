# **Common Security Principles**

We will talk about some widely enforced security principles that organizations use to strengthen their systems and reduce vulnerabilities.

---

## **Separate Privilege Principle**

* No single person should have enough authority to cause a critical event by themselves.
* Key authorities should be divided between two or more people.
* This reduces fraud, mistakes, and misuse of power.

**Example:**

* In accounting, the privilege to create a payment (maker) and the privilege to approve it (checker) are kept separate.
* In data centers, one person may have the key to the room while another has the key to the server rack.

---

## **Least Privilege**

* Users should receive the **minimum privileges necessary** to perform their tasks and nothing more.
* Reduces damage if an account is compromised.
* A common violation occurs when admins give broad access due to convenience or inattention.

**Example:**

* A receptionist should not have admin rights to install software on every machine.
* A web server process should only be able to read the folders it needs—not the whole filesystem.

---

## **Defense in Depth Principle**

* Security should be implemented in **multiple layers**.
* Even if one layer fails, other layers still protect the system.
* Also known as cascading security.

**Example:**

* Firewall → Antivirus → Intrusion Detection → Access Control → Encryption.
* A hacker must break each layer to reach the internal system.

---

## **Security Through Obscurity**

* This principle assumes the attacker does *not* know the internal system details.
* You “hide” the structure and hope attackers never understand it.
* **Not effective** as a primary security method but can be used as a *secondary* layer.

**Example:**

* Hiding admin panels at unusual URLs (e.g., `/admin98234/`)
* Keeping configuration paths secret
* But *not* a replacement for actual security controls

---

## **Fail Safes (Fail-Safe Defaults)**

* Unless a subject is **explicitly allowed access**, it should be **denied** by default.
* Default settings must be secure, not permissive.

**Example:**

* A firewall that blocks all ports and only opens the ones explicitly allowed.
* A file system that denies access to all users unless permissions are granted.

---

## **Economy of Mechanism**

* Security mechanisms should be **as simple as possible**.
* Complex systems introduce bugs, misconfigurations, and hidden vulnerabilities.

**Benefits:**

* Fewer bugs
* Easier auditing and testing
* Easier maintenance
* Harder for attackers to find weaknesses

**Example:**

* A small, clear access control policy is safer than a long, complicated one full of exceptions.

---

## **Complete Mediation**

* Every access to an object must be **checked every time**.
* The system should not rely on cached permissions or assume that earlier checks still hold.

**Example:**

* If a user is removed from a group, the system must check permissions on every file access—otherwise the user may still access resources until the next refresh.

---

## **Psychological Acceptability**

* Security mechanisms should **not make systems harder to use**.
* If security is too inconvenient, users will ignore it or try to bypass it.

**Example:**

* Password rules that are too strict cause users to write passwords on sticky notes.
* A simple, clean login system is more secure than a confusing one.

---

## **Least Common Mechanism**

* Mechanisms for resource access should **not be shared** across users if possible.
* Shared mechanisms increase the chance of interference, information leakage, or unintended access.

**Example:**

* Instead of all users sharing the same temporary folder, each user should have their own isolated temp directory.
* Avoid shared system-wide services that run with high privileges.

---

# **Considering Security Tradeoffs**

Security is always a tradeoff between **risk**, **benefit**, **cost**, and **user convenience**.
Organizations must find the right balance.

---

## **Security as a Tradeoff**

Security decisions involve:

* **Risk:** Likelihood and impact of an attack
* **Benefit:** How much protection a mechanism provides
* **Cost:** Money, time, training, performance impact

**Example:**
Biometric authentication is secure but expensive and slower.
A business must decide if the added security is worth the cost.

---

## **Key Tradeoff Factors**

* Security level required
* User convenience
* Business goals
* Financial cost

**Example:**
Strong encryption may be secure but might slow down processing for high-volume operations.

---

## **User Convenience vs. Security**

If security becomes too complicated:

* Users may avoid using the system
* They might find shortcuts
* They might disable security features
* This can make the system more vulnerable than before

**Examples:**

* Overly strict password rules cause users to reuse passwords or store them insecurely.
* Complicated multi-factor processes cause employees to switch to personal devices outside controls.

---

## **Bottom Line**

Security must protect the system **without blocking people from doing their work**.
The ideal design balances:

* Protection
* Usability
* Business requirements
* Costs

---
