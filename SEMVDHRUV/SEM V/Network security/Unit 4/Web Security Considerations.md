The following characteristics of Web usage suggests the need for web security
1. Web applications are getting relatively easy to develop but the underlying software is extraordinarily complex. This complex software may hide many potential security flaws underneath. 
2. Web servers can be exploited as a entry point to an organization's network infrastructure. Once these Web Servers are compromised, attackers may be able to gain access to the data and servers that are not connected to the Web itself.
3. Laymen users are a common type of customers to most kind of web applications. These users may not be necessarily aware of the security risks that exists.

## Threats on the Web
![[IMG-20251119182523819.png|600]]

## Security Mechanism layered within TCP/IP stack
![[IMG-20251119185919378.png|600]]
**(a) Network-Level Security**
- Uses **IPSec** at the IP layer to secure all traffic regardless of application.
- Transparent to applications but requires system-level configuration.
    
**(b) Transport-Level Security**
- Uses **SSL/TLS** between applications and TCP to secure specific sessions (e.g., HTTPS).
- Common for web and email services; balances security and flexibility.
    
**(c) Application-Level Security**
- Security is built into the application itself (e.g., **S/MIME**, **Kerberos**).
- Offers end-to-end protection but requires application support and configuration.
    
