Definition: Managing access to a network.
Function: 
- Authenticate user logging into network
- Check what they can access.
- Determining health of the devices logging onto the network.


## Elements of NAC
- **Access Requestor (AR):** 
	- Called as the node that is attempting to the connect
	- Workstation, Servers, Printer, Any IP enabled devices.
	- Also called clients
- **Policy Server:** 
	- Determines what is allowed an what is not.
	- Set of rule books.
	- Relies on backend systems
		- Antivirus
		- Patch MGMT
		- User Dir
- **Network Access Server:**
	- The NAS Functions as an endpoint for people in remote locations connecting to an enterprise's internal network.
	- AKA 
		- Media Gateway
		- Remote Access Serer

![[IMG-20260420174736782.png]]


In a real life scenario there are multiple AR's that try to contact a NAS and claim their identity.
They verify their identity using some kind of authentication which involves a secure protocol and use of the cryptographic keys which may be performed by the NAS.

- Multiple AR's try to contact NAS
- Claim identity
- NAS Authenticates them and validates their id
- Based on their ID and policy the NAS determines what privileges to authorize.


### Health check
Once the server has given authentication to the user they must also check for the health of the device that's tryna connect.

This may include 
- Checking if the Operating system is updated.
- If the device has all the latest patches
- Checking the Anti Malware version.

The AR must have **both** authentication and health check to be validated to connect to the NAS.

## Network Access Enforcement Methods
To verify is one thing and enforce it constantly is another. There are many Enforcement Methods that are applied to ARs to regulate access. 

Many vendors support multiple enforcement methods so the customer can have what they want.

### IEEE 802.1X
This is a link layer protocol that enforces authorization **Before** port has been assigned to an IP address.  
- Authorization before port is assigned to an IP address
- Uses EAP ( Extensible Authentication Protocol )


### Virtual Local Area Networks
Interconnected set of LAN's are segmented logically into a number of Virtual LANS.
The NAC System decides which VLAN will a new AR will be placed into. 
Later it checks what kind of access to be given. 

VLANS are Created Dynamically.

### Firewall Method
It provides a form of NAC by allowing or denying network traffic between an enterprise host and an external user. 

### DHCP Method
DHCP Server intercepts and Assigns IP Addresses. NAC Enforcement Occurs at the IP layer based on subnet and IP assignment.
Easy to install and configure

