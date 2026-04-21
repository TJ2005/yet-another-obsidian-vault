---

Title: "System Adminstrator Lab 8"

Status:

marker:

tags:

Date: ""

Time: ""

---
# **Experiment 9: DNS Server Configuration**

---
**Name:** [Your Name]
**Roll Number:** [Your Roll Number]
**Division/Batch:** [Your Division]

## **Aim**

To configure an Ubuntu Linux system to work as a DNS server.

---

## **Learning Outcomes**

After completion of this experiment, student should be able to:

1. Configure DNS server as primary and caching name server.
2. Modify various DNS records.
3. Troubleshoot DNS problems.

---

## **Theory**

Domain Name Service (DNS) is an Internet service that maps IP addresses and fully qualified domain names (FQDN) to one another. In this way, DNS reduces the need to remember IP addresses. Computers that run DNS are called name servers.

Ubuntu ships with BIND (Berkeley Internet Name Daemon), one of the most widely deployed DNS servers. Domain names are arranged in a hierarchical tree, rooted at the root domain (`.`), and organized under top-level domains such as generic TLDs (gTLDs) and country-code TLDs (ccTLDs).

A DNS zone is a portion of the namespace managed by a specific name server. Common BIND9 configurations include:

1. Caching nameserver.
2. Primary master nameserver.
3. Secondary master nameserver.

The DNS configuration files are usually stored in `/etc/bind`. The main files used in this experiment are:

| File | Purpose |
|------|---------|
| `/etc/bind/named.conf` | Primary BIND configuration |
| `/etc/bind/named.conf.options` | Global DNS options (forwarders, recursion, etc.) |
| `/etc/bind/named.conf.local` | Local zone declarations |
| `/etc/bind/db.root` | Root nameserver hints |

---

## **Procedure & Observations**

### **Task 1: Installation of BIND**

Install BIND9:

```bash
sudo apt-get update
sudo apt-get install bind9
```

Install DNS troubleshooting utilities:

```bash
sudo apt-get install dnsutils
```

**Observation:** [Write your observation here]

**Output/Screenshot:**
![[ ]] 

---

### **Task 2: Configure Caching Name Server**

Edit `/etc/bind/named.conf.options` and configure forwarders:

```conf
forwarders {
    8.8.8.8;
    8.8.4.4;
};
```

Restart DNS service:

```bash
sudo service bind9 restart
# or
sudo /etc/init.d/bind9 restart
```

**Observation:** [Write your observation here]

**Output/Screenshot:**
![[ ]]

---

### **Task 3: Configuring Primary Master Zone**

Edit `/etc/bind/named.conf.local` and add:

```conf
zone "example.com" {
    type master;
    file "/etc/bind/db.example.com";
};
```

Create zone file from template:

```bash
sudo cp /etc/bind/db.local /etc/bind/db.example.com
```

Edit `/etc/bind/db.example.com` and set SOA/NS/A records (example):

```conf
$TTL 604800
@   IN  SOA ns.example.com. root.example.com. (
           2         ; Serial
      604800         ; Refresh
       86400         ; Retry
     2419200         ; Expire
      604800 )       ; Negative Cache TTL

@   IN  NS  ns.example.com.
@   IN  A   10.0.2.15
ns  IN  A   10.0.2.15
```

Increment the serial number every time zone content is changed.

Restart BIND9:

```bash
sudo /etc/init.d/bind9 restart
```

**Observation:** [Write your observation here]

**Output/Screenshot:**
![[ ]]

---

### **Task 4: Configure Reverse Zone File**

Add reverse zone in `/etc/bind/named.conf.local` (example for `10.0.2.0/24`):

```conf
zone "2.0.10.in-addr.arpa" {
    type master;
    notify no;
    file "/etc/bind/db.10.0.2";
};
```

Create reverse zone file:

```bash
sudo cp /etc/bind/db.127 /etc/bind/db.10.0.2
```

Edit `/etc/bind/db.10.0.2`:

```conf
$TTL 604800
@   IN  SOA ns.example.com. root.example.com. (
           2         ; Serial
      604800         ; Refresh
       86400         ; Retry
     2419200         ; Expire
      604800 )       ; Negative Cache TTL

@   IN  NS  ns.example.com.
15  IN  PTR ns.example.com.
```

For each A record in forward zone, add matching PTR record in reverse zone.

Restart BIND9:

```bash
sudo /etc/init.d/bind9 restart
```

**Observation:** [Write your observation here]

**Output/Screenshot:**
![[ ]]

---

### **Task 5: Verification and Troubleshooting**

Use the following commands:

```bash
sudo named-checkconf
sudo named-checkzone example.com /etc/bind/db.example.com
dig @127.0.0.1 example.com
dig @127.0.0.1 -x 10.0.2.15
nslookup example.com 127.0.0.1
host ns.example.com 127.0.0.1
```

Check logs:

```bash
sudo tail -n 50 /var/log/syslog
```

Expected log lines can include successful zone load messages.

**Observation:** [Write your observation here]

**Output/Screenshot:**
![[ ]]

---

## **Result**

[Write the final result of the experiment here]

---

## **Review Questions**

1. What are the most common configurations for nameserver? Explain each configuration in brief.

Answer:

2. Explain the difference between domain and zone.

Answer:

3. What are various types of records in DNS?

Answer:

4. Which commands can be used to troubleshoot DNS?

Answer:

5. What is zone transfer?

Answer:

---

## **Conclusion**

[Write your conclusion here]

---

## **Note**

1. Replace example IP addresses with actual IPs used in your lab setup.
2. Replace `example.com` with the domain assigned in your practical.
3. Increment serial number after every zone-file change.

---

## **References**

1. https://ubuntu.com/server/docs/service-domain-name-service-dns
2. https://help.ubuntu.com/community/BIND9ServerHowto

###### Information
- date: 
- time: 
