# Role-Based Access Control (RBAC)

## What is RBAC?
- Access is based on **roles** inside an organization instead of individual identity.
- A *role* represents a job function or responsibility (e.g., Manager, HR, Student).
- Users are assigned to roles; roles are assigned permissions.

## Key Points
- Users → get roles  
- Roles → have permissions  
- Hence, **users get permissions indirectly** through roles.
- Easier to manage large organizations since roles group many users.

## Advantages of RBAC
- Centralized management of permissions.
- Easy to add/remove users by changing role membership.
- Consistent permission assignment for similar job functions.

---

# Comparison of DAC, MAC, and RBAC

| Feature | DAC | MAC | RBAC |
|--------|-----|-----|------|
| Control | Owner controls access | System controls access | Role controls access |
| Flexibility | High | Low | Medium–High |
| Security Level | Low–Medium | High | High |
| Example | ACLs, file permissions | Military classification | Organizational roles |

---

# Access Control Models Summary

## 1. Discretionary Access Control (DAC)
- Owner controls access.
- Uses ACLs, permissions.
- Flexible but weaker; can leak information.

## 2. Mandatory Access Control (MAC)
- System enforces strict control.
- Based on clearance & classification.
- Very secure, less flexible.

## 3. Role-Based Access Control (RBAC)
- Access based on job roles.
- Scalable and easy to administer.

---

# MAC Security Principles (Bell–LaPadula Highlights)

*(If this is coming in the next slides — adding now)*

## Bell–LaPadula Model (Confidentiality-focused)
- **Simple Security Property ("no read up")**  
  A subject cannot read data at a higher classification.
- ***-Property ("no write down")**  
  A subject cannot write information to a lower classification.

## Purpose
- Prevent leakage of classified information.

---

# Summary Diagram (Quick Recall)

Subjects → request access → Access Control Policy → Access Control Mechanism → Objects

---

