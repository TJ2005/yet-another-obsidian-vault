# VPNs

**Definition** - VPNs (Virtual Private Networks) help create private and secure network connection between systems. It relies on using data communication capabilities of unsecured and public networks.

***Types of VPN techs defined***:
1) Trusted VPN (Legacy VPN)
	Uses leased circuits from service provider and uses packet switching.
		Organization must trust the service provider
2) Secure VPN
	Uses security protocols like IPSEC to encrypt traffic
3) Hybrid VPN
	 Both

### **Goals of a VPN:**
1) Encapsulation 
2) Encryption
3) Authentication

### **Types of VPNs:**
1) Remote Access VPN: Connects a single device to a private network over the internet. e.g. Remote worker from Virar trying to connect to theirs's organization network in Mumbai. 
2) Site-to-Site VPN: Used by organizations to connect multiple networks. e.g. Connection between MPSTME `Mumbai Campus <--> Shirpur Campus`
3) Mobile VPN: Maintains a secure connection when the device switches connection
4) SSL VPN: Provides Secure remote access to web applications via a browser and an SSL/TLS tunnel

> VPNs operates on *two modes* namely; ***Transport mode, Tunnel mode***

### Transport Mode

* Only Data within the IP packet is encrypted and header information is not encrypted. Meaning network devices like routers and firewalls can read where the packets are coming from and where is it going to. But the data still remains encrypted 
* Use Cases: 
	* End-to-End transport of encrypted data
	* Remote access workers trying to connect to office network over the internet

### Tunnel Mode

* Organization Establishes two perimeter tunnel servers
* These servers act as encryption points, encrypting all the traffic that traverses through the network
* In this mode, everything included with IP headers is encrypted. Meaning public network devices like routers and firewalls will be only able read IP addresses of the tunnel servers not the actual specific device which has sent the packets/frames.





