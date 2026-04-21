Why hypervisors? because we cant just give bare hardware access to the user. We need some kinda Isolation to make a secure environment.

## Bare Metal Hypervisor ( Type 1 )

**Definition**: Installed directly on the host machine’s hardware without the need for a host operating system.
**Example**: VMware ESXi or Microsoft Hyper-V (Server version).

**Use case:** A business data center might use VMware ESXi to run multiple virtual servers (like a web server, database server, and mail server) on a single powerful physical server

## Hosted Hypervisor ( Type 2 )

Type 2 hypervisors run on top of a host operating system and rely on it for hardware resource management.  
**Example**: VirtualBox, VMware Workstation  
**Use case**: Running Linux on a Windows laptop for learning and testing.

## Differences Between Type 1 and Type 2 Hypervisors

|Aspect|Type 1 (Bare Metal)|Type 2 (Hosted)|
|---|---|---|
|Layer Position|Runs directly on hardware|Runs on a host OS|
|Performance|Faster, low latency|Slower due to host OS layer|
|Resource Access|Full access to hardware|Shared with host OS|
|Security|Smaller attack surface|Larger attack surface|
|Stability|More stable, no host OS issues|Dependent on host OS stability|
|Cost|More expensive|More affordable|
|Ease of Use|Harder to set up, admin-heavy|Easy to use, beginner-friendly|
|Management|Requires external interface|Managed within host OS|

## Advantages of Type 1 Hypervisors

|Advantage|Summary|
|---|---|
|Speed|Direct hardware access gives low latency|
|Resource Rich|No host OS, full access to resources|
|Security|Smaller attack surface|
|Stability|No host OS failures affecting VMs|

## Disadvantages of Type 1 Hypervisors


## Advantages of Type 2 Hypervisors

|Advantage|Summary|
|---|---|
|Cost|Cheaper than Type 1|
|Ease of Use|Simple installation and UI|

## Disadvantages of Type 2 Hypervisors

|Disadvantage|Summary|
|---|---|
|Performance|Host OS adds latency|
|Resource Limits|Shares hardware with host OS|
|Security|Larger attack surface|
|Stability|Host OS issues affect VMs|


