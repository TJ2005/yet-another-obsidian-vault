Virtualized security is a flexible, software-based system that provides security to VMs. 
We need it on each VM so it can operate in their own environment and are protected against malicious threats. 

They are virtual computer security systems like firewalls, intrusion protection, and anti-malware software in a virtual form ( Software ).
It Operates at the Hypervisor Layer. This protection Provides Virtual Endpoints 

- Each VM has _virtual_ components (virtual CPU, virtual RAM, virtual disk).
- But all of these virtual components still map to the **same physical hardware** underneath.
- Because everything is shared, VMs must be **isolated** from one another so that one VM cannot access or interfere with another.


Virtualized Security uses various security controls to achieve this separation and limit potential Attacks
- Encryption
- Micro Segmentation


## Security Virtualization
Turns a physical server into multiple independent virtual machines. Each VM runs separately from the others.

- Improves Hardware efficiency
- Providing Strong Isolation.
## Desktop Virtualization
Similar to Security Virtualization except that it refers to the creation of a virtual desktop computer. Users can log into their computer from any location. Files and Data are secured on a server not portable devices.



## Storage Virtualization

Creating Virtual Storage servers associated with virtual hard drives. Lets users store data that is centrally accessible.

## Network Virtualization

Combines physical and virtual resources to create a virtual corporate network. 
Example Cloudflare.

## Application Virtualization

Software that can run on any machine. Example Docker.

## Benefits of Virtualization

Outsourcing security as a service enables one to distribute the risks and reduce investment costs.

- **Cost Effective** : Maintenance in bulk Done by the service provider
- **Flexibility:**
	- Buy as u go
	- Administrators can scale up
- **Better Data Protection:**
	- Recover from Data Loss
	- Raid Configurations
- **Improved Operational Efficiency:**
	- Quick Deploy
	- Quick Patch
	- Closer to better network
- **Regulatory Compliance:** Service providers are in touch with the compliance policies and the customer can stay worry free.


## Infrastructure as a code ( IaC )

Its the ability provide compute infrastructure on demand that can be managed and created using easily using Code/Software

Many infrastructure components like:
- Database
- Storage
- Buckets
- GPU Compute
- DNS Records

Can be purchased as requested depending on the demand.


### Benefits

- **Duplicating an environment:** Imagine you outsourced a bucket storage service which is used via a GPU Compute unit. One can literally access the same data without creating redundant copies using the same Endpoint.

	One can also recreate already built images on docker to be deployed.

- **Reduce Configuration Errors:** Environment Configurations can be copied and cloned and projects can be run ASAP. One can avoid all the Configuration Jargon. Also Error checking becomes easy

- **Iterate on Best Practice Environment:**  A developer could branch the application’s IaC to initiate, use, and stop a  high-performance Amazon Elastic Compute Cloud (Amazon EC2) Trn1  instance. They can set the deployment region as dependent on the region of  the application deployment


****

## Configuration Declarative and Imperative

The goal is to have all the desired conditions met before we start running the project. It should always provide the same results.

### Declarative 
Here you specify what the final condition should be for the project to run smoothly. The server / provider will have to develop a framework to figure out how to get that on the service. It requires less information on the user side. 

### Imperative
This is a Procedural approach where you write scripts like `.sh` or `.bat` depending on the operating system / stack its running on. One can create very complex and detailed configurations in this. But developer needs to pour more effort to build such a configuration.

---
## Security Concerns

- **VM Sprawls**: Periodically review and decommission unused VMS.
- **Malware and Ransomware Attacks**: One infected VM could lead to a domino effect of loss even when there is no fault of the neighbours. 
- **Network Configuration:** Poorly configured servers are what black and grey hats look for. 
- **Access Control:** Unauthorized access to vmware could lead to breaking of confidentiality contracts etc. Organizational Data is easy to leak once gaining access.
- **Hypervisor Security Controls**