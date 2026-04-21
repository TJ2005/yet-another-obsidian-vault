DNSSEC or DNS Security Extension is a suite of protocols that is used by several mail security protocols .

## DNS
DNS or Domain Naming Server is a Directory that maps name of the domains to its respective IP addresses. 

Four elements of DNS:
- **Domain name space:** DNS uses a tree-structured name space to identify resources on the Internet.
- **DNS database:** Conceptually, each node and leaf in the name space tree structure names a set of information (e.g., IP address, name server for this domainname) that is contained in resource record. The collection of all Resource Records
- is organized into a distributed database.
- **Name servers:** These are server programs that hold information about a portion of the domain name tree structure and the associated Resource Records.
- **Resolvers:** These are programs that extract information from name servers in response to client requests. A typical client request is for an IP address corresponding to a given domain name.

#### The DNS Database
DNS is based on a hierarchical database containing resource
records (RRs) that include the name, IP address, and other information about hosts.
- Variable-depth hierarchy for names: DNS allows essentially unlimited levels and uses the period (.) as the level delimiter in printed names, as described earlier

**Distributed database:** The database resides in DNS servers scattered throughout the Internet.

**Distribution controlled by the database:** The DNS database is divided into thousands of separately managed zones, which are managed by separate administrators. 

**Flow**
1. User program requests an IP for a domain.
2. Resolver queries the local name server.
3. Local server returns the IP if cached; otherwise queries other servers up to the root.
4. Response is cached for its TTL.
5. User program receives the IP or an error.

## DNSSEC 
DNSSEC provides end-to-end protection through the use of digital signatures that are created by zone admins and are verified by the recipient's resolver.
![[Pasted image 20251112140119.png| 600]]
```
Root (.)
 └── signs DS record for .com
      └── .com signs DS record for google.com
           └── google.com signs records for mail.google.com

```

#### **FC 4033 – DNS Security Introduction and Requirements**
- **Purpose:** High-level overview and design goals.
- **Describes:**    
	- Tells us the capability and limitations what they do and do not provide.
#### **RFC 4034 – Resource Records for DNSSEC**
- **Purpose:** Defines **new record types** DNSSEC adds to DNS.
- **New DNSSEC record types:**
    - **DNSKEY** – contains a zone’s public key.
    - **RRSIG** – a digital signature over a set of DNS records.
    - **DS (Delegation Signer)** – links a parent and child zone.
    - **NSEC** (and later NSEC3) – proves nonexistence of a name (prevents spoofing of “no such domain”).
- These are what make the DNS data _cryptographically verifiable_.

#### **RFC 4035 – Protocol Modifications**
- **Purpose:** Explains how DNS servers and resolvers must behave with these new records.
- **Defines:**
    - The concept of a **signed zone** (a DNS zone where every record set is signed).
    - How **resolvers verify** RRSIGs using DNSKEYs and DS chains.
    - How to handle **authenticated denial of existence** (using NSEC/NSEC3).
    - How “security-aware resolvers” (clients that support DNSSEC) operate.
---
## **DNS Operations**
Protects DNS Clients from accepting a forged or altered DNS Record. Does using Digital Signatures.

- **Data origin authentication:** Ensuring data came from correct source
- **Data Integrity Authentication:** Verifies data wasn't tampered between.

DNS Zone Admin signs each `RRset`. Publishes the set with public key. From here we can only ask DNS Zones from this `RRSet` as we trust it. So we are populating our trust from one zone to another.

The trusted node is called the **Trust Anchor**. An `RRSIG` is associated with each `RRSET`