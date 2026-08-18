
***Definition:*** Controlling access to resources is one of the central themes of security.

***Goal:*** The goal of AC is to protect an organization’s resources from unauthorized access while facilitating seamless and legitimate use of these resources.

Access control is about the relationships between subjects and objects. The transfer of information from an object to a subject is called access. Subjects are active entities that, through the exercise of access, seek information about or data from passive entities, or objects.

### How Access Control helps Security Management

AC enables management to
- Specify ***which*** users can access the systems
- Specify ***what*** resources they can access
- Specify ***what*** operations they can perform
- Provide individual ***accountability***

### Key Idea
- Controlling **who** can use **what resources** is a central part of security.

## What Is Access?
- Access = **transfer of information** from an *object* to a *subject*.

## Subjects and Objects
- **Subjects**  
  - Active entities (e.g., users, processes).  
  - They request access to data or resources.
- **Objects**  
  - Passive entities (e.g., files, databases, devices).  
  - They contain the information or resource being protected.

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

# Access Control Models

## Bell-LaPadula Model

The model is a "state machine reference model". In other words, a model of an automated system that is able to manipulate its state or status over time.
- Used for enforcing access control in **government** and **military applications**
- Enforces **Confidentiality** in access control for an organization
- Simple Security Property (Read Property)
	- No read up i.e. Only allows reading access if the clearance level is equal or higher than the classification, but it allows a subject with a higher clearance level to read an object at a lower level (read down).
- Star Property (Write property)
	- No write down.  i.e. prevents writing to objects of lower classified objects
- Discretionary Security Property
	- Access is also controlled by access matrix rules like **DAC**

## Biba Integrity Model

The intent is to provide access controls to ensure that objects or subjects cannot have less integrity as a result of read/write operations. The Biba model assigns integrity levels to subjects and objects using two properties: the simple integrity (read) property and the integrity * property (write).

- Simple integrity property 
	- permits a subject to have read access to an object only if the subject’s security level is lower than or equal to the level of the object. 
- Integrity * property
	- permits a subject to have write access to an object only if the subject’s security level is equal to or higher than that of the object.

## Clark-Wilson Integrity Model

The Clark-Wilson integrity model, which is built upon principles of change control rather than integrity levels, was designed for the commercial environment.

The model’s change control principles are:
• No changes by unauthorized subjects
• No unauthorized changes by authorized subjects
• The maintenance of internal and external consistency

The following controls are part of the Clark-Wilson model:
• Subject authentication and identification
• Access to objects by means of well-formed transactions
• Execution by subjects on a restricted set of programs

The elements of the Clark-Wilson model are:
• Constrained data item (CDI): Data item with protected integrity
• Unconstrained data item: Data not controlled by Clark-Wilson; non-validated input or any output
• Integrity verification procedure (IVP): Procedure that scans data and confirms its integrity
• Transformation procedure (TP): Procedure that only allows changes to a constrained data item


Model consists of two types of rules

| Certification Rules                                                                                                                                                | Enforcement Rules                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| C1 When an IVP is executed, it must ensure all the CDIs are valid                                                                                                  | E1 System must maintain a list of certifies relations and ensure TPs certified to run on a CDI can change CDI                             |
| C2 A TP must transform CDIs from one valid state to another valid state                                                                                            | E2 System must associate a user with each TP and a set of CDIs. TP may access CDI on behalf of the user if its legal for the organization |
| C3 Allowed relations must meet the requirements of "separation of duty"                                                                                            | E3 The system must authenticate the identity of each user attempting to execute a TP                                                      |
| C4 All TPs must append the log enough information to reconstruct the operation                                                                                     | E4 Only the certifier of that TP may change the list of entities associated by that TP                                                    |
| C5 Any TP that takes a UDI as input may only perform valid transactions for all possible values of UDI.<br>The TP will either accept (convert to CDI) or reject it |                                                                                                                                           |
## Chinese Wall

Chinese Wall is designed to prevent conflict of interests. The model requires to users to select one of the two conflicting sets of data, after which they cannot access conflicting data.

Commonly used by consulting and accounting firms.

The elements of Chinese Wall model are:
- Objects: Items of information related to a company
- Company Dataset (CD): Contains objects related to a single company
- Conflict of Interest class (COI): Contains datasets of companies in competition