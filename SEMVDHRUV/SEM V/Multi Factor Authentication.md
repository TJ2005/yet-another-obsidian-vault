# Multifactor Authentication

## Why Single-Factor Is Weak
- Each single authentication method has weaknesses:  
  - **Tokens** can be lost, stolen, or given away.  
  - **Passwords** can be observed (shoulder surfing).  
- Using only one factor means one failure can break the whole authentication.

## Combining Factors
- Using more than one factor compensates for individual weaknesses.
- Example: **Identity cards**  
  - The card = token  
  - Photo = biometric (appearance)  
  - Signature comparison = biometric  
- Even when multiple factors exist (e.g., signatures on credit cards), they are not always used.

## Multifactor Process
- Can use **2, 3, 4, or more factors**, as long as it is not overly burdensome.
- Example:  
  - Enter secret code (knowledge)  
  - Slide badge (token)  
  - Hand on plate (biometric)

## Definition
- **Multifactor Authentication (MFA)** = combining authentication information from multiple factors.
- **Two-factor authentication (2FA)** = using two different strong factors.

## Trade-Offs
- More factors → more confidence **assumed**, but not strongly supported by studies.
- More factors also mean:  
  - More work for system, administrators, and users  
  - More software components and readers  
  - More time required to authenticate  
- Very high number of factors (**large n**) can cause user frustration → may **reduce** security instead of improving it.

