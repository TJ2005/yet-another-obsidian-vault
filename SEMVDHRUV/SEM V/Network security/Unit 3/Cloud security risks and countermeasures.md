
---
## Abuse and nefarious use of cloud resources

Expensive infrastructure can be used to attack on a larger scale and an even larger attack surface.
- Sending Spam Emails
- Spreading Viruses
- DoS Attack
- Data Centre Leaks

And the worst part that the people trust these services for their reliability already.
### Counter Measures

- Strict Access Control
	- Registration
	- Validation Process
- Credit Card Monitoring
	- Reuse frequency
- Inspect network traffic from customer
- Have a public common blacklist that denies certain users or group of users access

---
## Insecure Interface or API's

API's are endpoints for the end user to fetch important data from. Due to malicious or accidental reasons API's can become insecure due to unsanitary reasons etc. 
In these situations attackers can either:
- Deny the service (DoS)
- Spawn shells in Servers
- Access Data to which they didnt have access
- Etc

### Counter Measures

- Analyze Security Model
- Better Auth
	- 2FA
	- Encryption channels
- Dependency Chain to find potential point of failures
---
## Malicious Insiders

Employees Inside cloud service providers can intentionally harm services for their own uses.
- Sabotaging Services
- Writing backends for accessing Later
### Counter Measures

- They vet all partners and suppliers for security compliance.
- They define HR responsibilities in contracts for accountability.
- They require transparency and regular security-compliance reports.
- They establish clear breach-notification procedures for rapid response.

---
## Shared Technology Issues

InfraStructure as a Service often  live in separate units logically. However in perspective of hardware they might be together. Infrastructure isnt design to isolate everyone. One tenant could access others data.

### Counter Measures

- Install and configure systems properly
	- Minimize risk
	- Isolation Configs
- Constantly monitor the activity
- Strict Access Control Protocol
- Strong Auth

---
# Account or Service Hijacking

This occurs when attackers steal credentials—passwords, usernames, or API keys—and take over a cloud account. Once inside, they can steal data (breaking confidentiality), alter or delete information (harming integrity), or disrupt services (impacting availability).

### Countermeasures

1. Avoid sharing credentials across users or services.
2. Use strong 2FA so stolen passwords alone won’t work.
3. Monitor accounts for unusual or unauthorized activity.
4. Know your provider’s security policies and SLAs to understand protection and response measures.
---
# Unknown Risk Profile

Using the cloud means giving some control to the provider, but clients may not fully know the provider’s security setup. This creates uncertainty about hidden risks. Clear visibility and shared responsibility are essential.

### Countermeasures

1. Providers should share logs and activity data with clients.
2. Offer partial or full disclosure of infrastructure details (patch levels, firewall setups, etc.).
3. Use strong monitoring and alerting to detect suspicious or critical events in real time.

---
