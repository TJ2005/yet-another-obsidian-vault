## Data Protection
Evaluating the suitability of the service provider in perspective of security.

- Solutions to secure data
	- While at Rest
	- While in Transit
	- While in Use
	- Sanitize Data
- Taking Risk into Consideration
	- Preparing for Threats and Accidents

Data protection ensures your books are safe at rest in the library, in transit when borrowed, and erased securely when retired — with cryptographic keys acting as secret combinations to the safes.

---
## Availability

Try to make data available at all times even in situations of attack. Trying to maintain continuity. Trying not to fail or stop providing service. 

- Data Backup
- Recovery

Availability ensures the library stays open, even during disasters, by having backup copies and disaster recovery plan

---
## Incident Response
Ensure that the organization can respond to incidents in a coordinated fashion with the cloud provider in accordance with their respective roles and responsibilities for the computing environment.

Incident response is the librarian’s emergency manual, outlining how to respond calmly, share accurate updates, and restore order with minimal disruption


# Secure Query Processing
Secure conversation between a **user** a **cloud server** and the **DataBase**. We are trying to make sure that only the people with the correct access control can access the Data.

- User Sends a query
- Client Side Query Processor Grabs this information 
- Transforms it into secure encrypted version that no one can understand over the internet
- Query Reaches Cloud Server
- Query Processor Queries it on the encrypted database ( w/o revealing plaintext data )
- The results are then sent back to the client
- Client Side Query Processor once again decrypts the result and formats it

