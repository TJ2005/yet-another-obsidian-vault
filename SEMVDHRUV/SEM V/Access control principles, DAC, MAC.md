# Introduction to Access Control

## Key Idea
- Controlling **who** can use **what resources** is a central part of security.

## Goal of Access Control (AC)
- **Protect resources** from unauthorized access.
- Allow **legitimate users** to access resources easily and correctly.
- Balance **security** with **usability**.

## What Is Access?
- Access = **transfer of information** from an *object* to a *subject*.

## Subjects and Objects
- **Subjects**  
  - Active entities (e.g., users, processes).  
  - They request access to data or resources.
- **Objects**  
  - Passive entities (e.g., files, databases, devices).  
  - They contain the information or resource being protected.



# How Access Control (AC) Helps Security Management

## Management Benefits
AC enables management to:
- Specify **which users** can access the system.
- Specify **what resources** they can access.
- Specify **what operations** they are allowed to perform.
- Provide **individual accountability** (tracking who did what).

---

# Key Definitions

## Security Policy
- High-level rules that determine **how access control must be regulated**.

## Security Model
- A **formal representation** of the security policy.
- Allows **proofs** about the properties of the access control system.

## Security Mechanism
- Low-level **software/hardware functions** that implement the policy.
- Implements the controls defined in the model.

---

# Types of Access Control Policies
Three main categories:
1. **Discretionary Access Control (DAC)**
2. **Mandatory Access Control (MAC)**
3. **Role-Based Access Control (RBAC)**

---

# Discretionary Access Control (DAC)

## Key Points
- Also known as:
  - **Identity-Based Access Control (IBAC)**
  - **Authorization-Based Access Control**
- The **owner/creator** of an object controls access.
- Access depends on the **identity** of the subject.
- Often implemented using **Access Control Lists (ACLs)**.
- Not centrally controlled — owners can change ACLs.
- More dynamic compared to MAC.

## Advantages
- Simple  
- Flexible  
- Easy to implement  

## Drawback
- No formal assurance about controlling **information flow**.

## Examples
- Password-protected files  
- Owner/Group/Other permissions  
- ACLs  

---

# Access Matrix Model

## Concept
- Framework for describing **discretionary access control**.
- Proposed by **Lampson**.
- Authorization state is represented as a **matrix**:
  - Rows = Subjects  
  - Columns = Objects  
  - Cell = Allowed operations

## Purpose
- Gives an **abstract representation** of a protection system.

---

# Example Access Control Matrix

|      | File 1    | File 2 | File 3 | Program 1 |
| ---- | --------- | ------ | ------ | --------- |
| Ann  | Own, R, W | R,W    |        | Execute   |
| Bob  | R         | —      | R, W   | —         |
| Carl | —         | R      | —      | Execute,R |

---

# Implementing the Access Matrix

Three practical approaches:

## 1. Authorization Table
- Stores only **non-empty** entries.
- Table columns: **Subject, Action, Object**.
- Common in DBMS (stored as relational tables).

## 2. Access Control Lists (ACL)
- Stored **by column** (per object).
- Each object has a list of subjects and what they can do.

## 3. Capability Lists
- Stored **by row** (per user).
- Each subject has a list of objects + allowed operations.

---

# Access Control List (ACL)

## What It Is
- A list of **permissions attached to an object**.
- Specifies **which subjects** can perform **which operations**.

## Example
- (Alice, delete) in the ACL of file *WXY* → Alice can delete file WXY.

## How ACL Works
- When a subject requests access:
  - The OS checks the ACL entry to decide if the operation is allowed.

## Key Issue
- Who is allowed to **modify** the ACL?

## Scope
- Can be applied to:
  - Individual objects  
  - Collections of objects  
  - Higher-level system entities  

---

# Vulnerabilities of DAC

## Key Weakness
- No control over **information flow** once a subject receives data.
- A process can **leak** data to unauthorized users.

## Example
- **Trojan Horse** attacks can misuse access and leak information.

---

# Mandatory Access Control (MAC)

## Key Points
- OS enforces strict control over access.
- Uses **classification labels**:
  - Subjects → clearance level  
  - Objects → classification/sensitivity  
- Example labels: Top Secret, Secret, Confidential, SBU, Unclassified.

## Access Rules
- Subjects can access objects of:
  - **Same** classification level
  - **Lower** classification level  
- **Need-to-know** can further restrict access to highly sensitive resources.

## Characteristics
- **Prohibitive** model → if not explicitly allowed, it is forbidden.
- More **secure** than DAC.
- Less **flexible** and less **scalable**.


