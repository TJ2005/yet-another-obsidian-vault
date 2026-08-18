
**Threat:** A potential for violation of security which exists when there is a opportunity or a circumstance that could breach the security of the system. Meaning, threat is a potential danger that might exploit a vulnerability.

**Attack:** An Assault on the system's security that is derived from an intelligent threat. A intelligent threat can be described as a deliberate attempt to evade the security services to breach the system.

***Definition:*** OSI security architecture provides an abstract overview of the concepts of Network Security. These can be defined as follows:

1. [[#Security Attacks|Security Attack]]: Any action that compromises security of the information owned by the organization
2. [[#Security Mechanism|Security Mechanism]]: A process that is designed to detect, prevent, or recover from a security attack
3. [[# Security Service|Security Service]]: A service that enhances the security of the system.

## Security Attacks
Attacks can be classified into two types: Active, Passive

[[#Passive Attack]] attempts to learn from the information of the system but doesn't affect the system's resources
But an [[#Active attack]] attempts to alter system's resources or tries to affect their operation

### Passive Attack

Passive attacks has the goal to obtain information about the transmission between the parties. This is a violation of Confidentiality from the CIA Triad. There are two types of Passive Attack:
1. Release of Message Contents: Refers to an adversary eavesdropping on a communication channel to extract confidential information. It aims to extract the sensitive info that's being transmitted.
2. Transmission Analysis: Refers to Analysis of the Traffic to determine other important information about the parties like location, time of communication.
### Active Attack

An active attack aims to alter with the organization's resources or attempts to affect their operation. Here, an attacker's goal is to violate the Integrity or/and Availability of service provided by the Organization. Each Active Attack can be classified into 4 categories:
1. **Masquerade:** takes place when the attacker tries to impersonate a authorized entity. Masquerade usually includes one of the other forms of active attack with it.
2. **Replay attack:** utilizes data captured during a passive attack to replay the exact sequence of transmission to produce an unauthorized effect.
3. **Modification of Message:** means when an attacker tries to modify a legitimate message by updating, inserting, re-ordering the content in-order to produce an unauthorized effect.
4. **Denial of Service:** prevents or inhibits the normal use of services provided by the organization. This prevention can be caused by overloading the service with tons of request causing the service to get disrupted.

## Security Service
Security service $\implies$ something that supports one or more of C, I, A.

- Authentication
	- Peer Entity Authentication
	- Data Origin Authentication
- Access Control
- Data Confidentiality
- Data Non Repudation
- Data Availability


## Security Mechanisms
Mechanisms used to enforce the security.

- Cryptographic Algorithms
	- Keyless
- Data Integrity
	- Signatures
- Digital Signatures
	- Non Repudiation
- Auth Exchange
	- Exchange of keys
- Routing Control
- Notarization

