---

Title: "System Adminstrator Lab 5"

Status:

marker:

tags:

Date: "2026.02.12"

Time: "13:11"

---
# **Experiment 5: Configuring Apache Web Server**

---
**Name:** Tejas Sahoo
**Roll Number:** K057

## **Aim**

To install and configure Apache web server and set up virtual hosting.

---

## **Learning Outcomes**

1. Install and configure Apache web server.
2. Set up virtual hosts to serve multiple websites from a single server.

---

## **Theory**

**Forward Proxy** — sits between the client and the internet, requesting content on behalf of the client. Protects intranet clients, enables filtering, and caches responses to save bandwidth.

**Reverse Proxy** — sits in front of internal servers. Accepts external requests and routes them to backend servers. Hides internal infrastructure and shares load.

**Apache HTTP Server** — free, open-source, cross-platform web server. Supports compiled modules extending core functionality:
- `mod_ssl` — SSL/TLS support
- `mod_proxy` — proxy support
- `mod_rewrite` — URL rewriting
- `mod_auth` / `mod_auth_digest` — authentication
- Virtual hosting — one Apache installation can serve multiple domains simultaneously

---

## **Procedure & Observations**

---

### **Task 1: Installation of Apache2 Web Server**

```bash
sudo apt update
```

```bash
sudo apt install apache2
```

```bash
sudo systemctl status apache2
```

```shell
┌──(user㉿G)-[/mnt/c/Users/tejas]
└─$ sudo systemctl status apache2
○ apache2.service - The Apache HTTP Server
     Loaded: loaded (/usr/lib/systemd/system/apache2.service; disabled; preset: disabled)
     Active: inactive (dead)
       Docs: https://httpd.apache.org/docs/2.4/
```


Test in browser — open: `http://localhost` or `http://127.0.0.1`
Default Apache2 Ubuntu page should appear.

Test via terminal:
```bash
wget 127.0.0.1
```

```shell

┌──(no㉿G)-[/mnt/c/Users/tejas]
└─$ sudo systemctl status apache2
● apache2.service - The Apache HTTP Server
     Loaded: loaded (/usr/lib/systemd/system/apache2.service; disabled; preset: disab>
     Active: active (running) since Mon 2026-02-23 13:48:05 IST; 5s ago
 Invocation: 52ca2e844b4444a2969a7d2d88f00bff
       Docs: https://httpd.apache.org/docs/2.4/
    Process: 4092 ExecStart=/usr/sbin/apachectl start (code=exited, status=0/SUCCESS)
   Main PID: 4108 (apache2)
      Tasks: 55 (limit: 9055)
     Memory: 9.2M (peak: 10.4M)
        CPU: 75ms
     CGroup: /system.slice/apache2.service
             ├─4108 /usr/sbin/apache2 -k start
             ├─4110 /usr/sbin/apache2 -k start
             └─4111 /usr/sbin/apache2 -k start

Feb 23 13:48:05 G systemd[1]: Starting apache2.service - The Apache HTTP Server...
Feb 23 13:48:05 G systemd[1]: Started apache2.service - The Apache HTTP Server.
```

Service control commands:
```bash
sudo systemctl stop apache2
sudo systemctl start apache2
sudo systemctl restart apache2
sudo systemctl reload apache2
```
> `reload` is preferred after config changes — no connection drop.

**Observation:** Apache2 installed successfully. Default page loads on port 80. Service starts, stops, and reloads correctly.

---

### **Task 2: Setting Up a Virtual Host**

Replace `tejas` with your chosen domain name throughout.

**Step 1 — Create website directory:**
```bash
sudo mkdir /var/www/tejas
```

**Step 2 — Assign ownership:**
```bash
sudo chown -R $USER:$USER /var/www/tejas
```

**Step 3 — Set permissions:**
```bash
sudo chmod -R 755 /var/www/tejas
```

**Step 4 — Create sample webpage:**
```bash
sudo nano /var/www/tejas/index.html
```

Paste this content:
```html
<html>
  <head>
    <title>Welcome to Tejas!</title>
  </head>
  <body>
    <h1>Success! The tejas virtual host is working!</h1>
  </body>
</html>
```
Save: `Ctrl+O` → Exit: `Ctrl+X
`
![[IMG-20260420174733189.png]]

**Step 5 — Create Virtual Host config:**
```bash
sudo nano /etc/apache2/sites-available/tejas.conf
```

Paste:
```apache
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    ServerName tejas
    ServerAlias www.tejas

    DocumentRoot /var/www/tejas

    <Directory /var/www/tejas>
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/tejas_error.log
    CustomLog ${APACHE_LOG_DIR}/tejas_access.log combined
</VirtualHost>
```
Save and exit.

![[IMG-20260420174733226.png]]

**Step 6 — Enable the virtual host:**
```bash
sudo a2ensite tejas.conf
```

**Step 7 — Disable the default site:**
```bash
sudo a2dissite 000-default.conf
```

**Step 8 — Test configuration:**
```bash
sudo apache2ctl configtest
```
Output should be:
```
Syntax OK
```

**Step 9 — Restart Apache:**
```bash
sudo systemctl restart apache2
```

**Step 10 — Test in browser:**
Open: `http://tejas`
*"Success! The tejas virtual host is working!"*

![[IMG-20260420174733284.png]]


**Observation:** Virtual host configured successfully. Custom domain serves content from `/var/www/tejas`. Configuration validated without errors.

![[IMG-20260420174733305.png]]
---

### **Task 3: Important Apache Files and Directories**

| Path | Purpose |
|------|---------|
| `/etc/apache2/` | Main configuration directory |
| `/etc/apache2/apache2.conf` | Global Apache configuration |
| `/etc/apache2/ports.conf` | Ports Apache listens on (80, 443) |
| `/etc/apache2/sites-available/` | Stored virtual host configs (inactive until linked) |
| `/etc/apache2/sites-enabled/` | Active virtual hosts (linked from sites-available via `a2ensite`) |
| `/etc/apache2/conf-available/` | Extra config fragments (enable with `a2enconf`) |
| `/etc/apache2/conf-enabled/` | Active extra config fragments |
| `/etc/apache2/mods-available/` | Available modules (`.load` / `.conf`) |
| `/etc/apache2/mods-enabled/` | Enabled modules (via `a2enmod` / `a2dismod`) |
| `/var/log/apache2/access.log` | Every request to the server |
| `/var/log/apache2/error.log` | All errors with detail set by `LogLevel` |

Explore config files:
```bash
cat /etc/apache2/apache2.conf
cat /etc/apache2/ports.conf
ls /etc/apache2/sites-available/
ls /etc/apache2/sites-enabled/
ls /etc/apache2/mods-enabled/
cat /var/log/apache2/access.log
cat /var/log/apache2/error.log
```

---

## **Observations**

- Apache service runs successfully on port 80.
- Default website loads at `http://localhost`.
- Virtual host serves content from custom directory `/var/www/tejas`.
- Configuration validated without errors (`Syntax OK`).
- Log files correctly record access and error events.

---

## **Result**

Apache Web Server was successfully installed and configured. Virtual hosting was implemented, allowing a custom domain to be served from a dedicated directory on a single server.

---

## **Conclusion**

Apache Web Server was successfully installed and configured. Virtual hosting was implemented, allowing multiple websites to be hosted on a single server. Important configuration files and logs were studied for effective server management.

---

## **See Also**

- [[System Adminstrator Lab 1]] — Apache's config (`/etc/apache2`), web root (`/var/www`), and logs (`/var/log/apache2`) are all directories in the Linux file hierarchy from Lab 1
- [[System Adminstrator Lab 2]] — `chown -R $USER:$USER` and `chmod -R 755` used in Task 2 here are user/permission commands covered in Lab 2
- [[System Adminstrator Lab 3]] — `wget` tests the Apache server; `host`/`nslookup` resolve domain IPs; `netstat` verifies Apache is on port 80; `ifconfig` gives the server IP — all from Lab 3
- [[System Adminstrator Lab 4]] — `tcpdump` captures HTTP traffic to/from this server; `lsof` shows Apache's open port 80; `iftop`/`iptraf-ng` monitor web server bandwidth
- [[System Adminstrator Lab 6]] — If iptables default policy is DROP, port 80 must be explicitly allowed (`--dport 80 -j ACCEPT`) for this Apache server to be reachable

---

# References


###### Information
- date: 2026.02.12
- time: 13:11
