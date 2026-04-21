Security in the Design of Operating Systems  Simplicity of Design  Layered Design  Kernelized Design  Reference Monitor  Correctness and Completeness  Secure Design Principles  Trusted Systems 12 Pintu R Shah MPSTME SVKM

## Security kernel

- **Coverage** Checking every access THROUGH the kernel
- **Seperation** Isolate mechanisms to ensure security from OS
- **Unity** All sec functions tossed in together in a single blob of code to debug quicker?
- **Modifiability** Make modification in security functions easier.
- **Compactness** Make security kernel small because its only responsible for security functions
- **Verifiability** Like we prove some math functions we should be able to prove the functions written in the security kernel are 100% secure.

## Reference Monitor 

- Tamper Proof
	- Impossible to weaken/disable
- Unbypassable
	- Shouldn't be able to bypass this function
- Analyzable
	- Ensuring it is secure

## Trusted Systems

- Looking for key characteristics to analyse whether to trust a program or not
	- **Functional Correctness** Does what its supposed to correctly
	- **Enforcement of Integrity** Program Maintains correctness of data
	- **Limited Privilege** only give minimal access to secure data that program needs to function and the returned values are supposed to be put in a security classification as secure as the input data 
	- **Appropriate Confidence Level** The program is rated to be rated at a degree of trust for the kind of place where its supposed to be used
- A Trusted System has a defined policy
- Appropriate Measures and mechanisms to enforce security
- Independent Scrutiny or evaluation to ensure that the mechanisms have been selected are properly implemented

## Trusted System Functions

All hardware, software, controls & resourced needed to ensure that the security policy is enforced. 

- TCB Functions 
	- Activating Processes
	- Domain Switching ( Domains of security ) 
	- Memory protection
	- I/O operation

- Trusted System Functions
	- Secure Startup ensures no malicious code can enter or block the security enforcement
	- A secure path between the user and security mechanism
		- User should know how to spot an authentic authentication portal
		- User should know and trust that they are talking to the real deal
		- No one should be able to fake the authentication.
		- Example : Windows Administrative Prompts
	- Object Sanitization ensure no leakage of data if another 

