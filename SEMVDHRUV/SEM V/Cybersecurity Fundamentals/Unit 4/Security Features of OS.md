## Seccurity Features of ordinary operating systems

- Enforced Sharing
- Interprocess Communication and synchronization
- Protection of critical operating system data
- Guaranteed fair service
- Interface to hardware
- User Auth
- Mem protection

## Layered Operating System

Add image


## Separation and Sharing

- Physically separate processes that uses different hardware.
	- Such as printers
- Temporal Seperation
	- Processes with different security levels are executed at different times than each other so that one cannot inject into a high security process.
- Logical Seperation
	- Process is executed in such a way that it is isolated and segmented from all the other processes in a way that it thinks that there are no other proceses.
- Cryptographic Separation
	- Processes are encrypting their own data adding processing overhead but ensuring security.
- Share All or Share Nothing
	- Public Object is visible to all
	- Private Object is available to ONLY the owner
- Share but Limit Access
	- Access Lists
- Limit Use of an object
	- A process that uses a highly secure object is also made secure on the same level to ensure no leaks.


## Hardware Protection of Memory
A **fence register** provides protection in only **one direction**. It can stop a **user program** from accessing memory that belongs to the **operating system**, but it **cannot** prevent one user’s program from accessing or interfering with another user’s memory.

In other words:

- The OS can protect itself from a user program using a fence register.
- But a fence register cannot protect **users from each other**, because it only enforces a single boundary, not multiple isolated memory regions.

Additionally, a user program cannot mark specific memory regions—such as its own **program code**, **read-only data**, or **critical variables**—as protected. With only a fence register, the hardware does not support multiple protected segments, so a program might accidentally or maliciously overwrite its own code or read-only data.

This is why more advanced memory protection mechanisms (like base-limit registers, segmentation, and paging) are needed to achieve full isolation and multi-user safety.

---

## Segmentation 

Segmentation enables hardware level access control to different memory sections in different access modes.

- Each address is reference checked with the lower and upper bound
- Different Classes of data can be given different protection
- Sharing access of segments with potentially different access rights
- A user cant generate an address, Figure out the address of an unpermitted segment
- 