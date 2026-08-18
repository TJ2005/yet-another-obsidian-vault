---
Title: "DFIR Lab 6 - Ann's Rendezvous: Wireshark SMTP Analysis"
Status: Incomplete
marker: 
tags: incomplete
Date: "2026.03.05"
Time: "11:02"
---

# Experiment 7: Ann's Rendezvous Case

## Aim
To recover email messages from packet capture and analyze the same.

## Learning Outcomes
After completion of this experiment, the student should be able to analyze SMTP packets using Wireshark.

---

## Case Description

After being released on bail, Ann Dercover disappears! Fortunately, investigators were carefully monitoring her network activity before she skipped town.

> "We believe Ann may have communicated with her secret lover, Mr. X, before she left," says the police chief. "The packet capture may contain clues to her whereabouts."

You are the forensic investigator. Analyze the given packet capture to answer the following questions:

- Provide any online aliases or addresses and corresponding account credentials that may be used by the suspects under investigation.
- Who did Ann communicate with? Provide a list of email addresses and any other identifying information.
- Extract any transcripts of Ann's conversations and present them to investigators.
- If Ann transferred or received any files of interest, recover them.
- Are there any indications of Ann's physical whereabouts? If so, provide supporting evidence.

---

## Network Information

| Segment          | Range               |
|------------------|---------------------|
| Internal Network | 192.168.30.0/24     |
| DMZ              | 10.30.30.0/24       |
| The Internet     | 172.30.1.0/24 *(for purpose of this case study)* |

---

## Evidence

Investigators provide you with a packet capture from Ann's home network. The evidence file is available on the local server under `ISAF\AnnCase`.

They also inform you that in the course of their monitoring, they have found that **Ann's laptop has a MAC address of `00:21:70:4D:4F:AE`**.

---

## Procedure

Firstly I have merged the pcap file because it spans over multiple months and its easier to make a timeline with that.

```wireshark

First packet:
2009-08-13 11:27:03
Last packet:
2010-02-03 05:14:13
Elapsed:
173 days 17:47:09

```


## Open the evidence file using Wireshark.

Click **Statistics → Protocol Hierarchy**. Note the percentage of the following protocols:
   - IP
   - UDP
   - TCP
   - DNS
   - Bootstrap (BOOTP/DHCP)
   - SMTP
   - IMAP
   - HTTP!

![[IMG-20260420174731496.png]]

### Use Wireshark display filter:
   ```
   eth.addr==00:21:70:4d:4f:ae and bootp
   ```
   Note the following:
   - MAC address
   - IP address
   - Host Name
   - Lease time
   - DNS server address
   - Router address
   - Subnet mask
![[IMG-20260420174731549.png]]

#### Output
For some reason there are no bootp packets in the entire PCAP File



### Use Wireshark display filter:
   ```
   smtp.command_line
   ```
   Note the number of EHLO messages and email addresses.

```
57	82.998439	192.168.1.159	64.12.102.142	SMTP	70	C: EHLO annlaptop
60	83.109678	192.168.1.159	64.12.102.142	SMTP	66	C: AUTH LOGIN
69	83.465436	192.168.1.159	64.12.102.142	SMTP	87	C: MAIL FROM: <sneakyg33k@aol.com>
72	83.579698	192.168.1.159	64.12.102.142	SMTP	83	C: RCPT TO: <sec558@gmail.com>
75	83.698197	192.168.1.159	64.12.102.142	SMTP	60	C: DATA
83	84.149429	192.168.1.159	64.12.102.142	SMTP	60	C: QUIT
117	243.079029	192.168.1.159	64.12.102.142	SMTP	70	C: EHLO annlaptop
120	243.193067	192.168.1.159	64.12.102.142	SMTP	66	C: AUTH LOGIN
129	243.540579	192.168.1.159	64.12.102.142	SMTP	87	C: MAIL FROM: <sneakyg33k@aol.com>
132	243.658756	192.168.1.159	64.12.102.142	SMTP	88	C: RCPT TO: <mistersecretx@aol.com>
135	243.775217	192.168.1.159	64.12.102.142	SMTP	60	C: DATA
564	246.795834	192.168.1.159	64.12.102.142	SMTP	60	C: QUIT

```
### Use Wireshark display filter:

   ```
   smtp
   ```
   Right-click on the first message and select **Follow TCP Stream**. Note: Is authentication detail encrypted?

```pcap
220 cia-mc06.mx.aol.com ESMTP mail_cia-mc06.1; Sat, 10 Oct 2009 15:35:16 -0400

EHLO annlaptop

250-cia-mc06.mx.aol.com host-69-140-19-190.static.comcast.net
250-AUTH=LOGIN PLAIN XAOL-UAS-MB 
250-AUTH LOGIN PLAIN XAOL-UAS-MB 
250-STARTTLS
250-CHUNKING
250-BINARYMIME
250-X-AOL-FWD-BY-REF
250-X-AOL-DIV_TAG
250-X-AOL-OUTBOX-COPY
250 HELP

AUTH LOGIN

334 VXNlcm5hbWU6

c25lYWt5ZzMza0Bhb2wuY29t

334 UGFzc3dvcmQ6

NTU4cjAwbHo=

235 AUTHENTICATION SUCCESSFUL

MAIL FROM: <sneakyg33k@aol.com>

250 OK

RCPT TO: <sec558@gmail.com>

250 OK

DATA

354 START MAIL INPUT, END WITH "." ON A LINE BY ITSELF

Message-ID: <000901ca49ae$89d698c0$9f01a8c0@annlaptop>
From: "Ann Dercover" <sneakyg33k@aol.com>
To: <sec558@gmail.com>
Subject: lunch next week
Date: Sat, 10 Oct 2009 07:35:30 -0600
MIME-Version: 1.0
Content-Type: multipart/alternative;
	boundary="----=_NextPart_000_0006_01CA497C.3E4B6020"
X-Priority: 3
X-MSMail-Priority: Normal
X-Mailer: Microsoft Outlook Express 6.00.2900.2180
X-MimeOLE: Produced By Microsoft MimeOLE V6.00.2900.2180

This is a multi-part message in MIME format.

------=_NextPart_000_0006_01CA497C.3E4B6020
Content-Type: text/plain;
	charset="iso-8859-1"
Content-Transfer-Encoding: quoted-printable

Sorry-- I can't do lunch next week after all. Heading out of town. =
Another time! -Ann
------=_NextPart_000_0006_01CA497C.3E4B6020
Content-Type: text/html;
	charset="iso-8859-1"
Content-Transfer-Encoding: quoted-printable

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML><HEAD>
<META http-equiv=3DContent-Type content=3D"text/html; =
charset=3Diso-8859-1">
<META content=3D"MSHTML 6.00.2900.2853" name=3DGENERATOR>
<STYLE></STYLE>
</HEAD>
<BODY bgColor=3D#ffffff>
<DIV><FONT face=3DArial size=3D2>Sorry-- I can't do lunch next week =
after all.=20
Heading out of town. Another time! -Ann</FONT></DIV></BODY></HTML>

------=_NextPart_000_0006_01CA497C.3E4B6020--

.

250 OK

QUIT

221 SERVICE CLOSING CHANNEL

```
### Username and Password
Note the **username** and **password**. Decode them using **Base64**. Also note the content of the email.

```
c25lYWt5ZzMza0Bhb2wuY29t

334 UGFzc3dvcmQ6

NTU4cjAwbHo=

```

![[IMG-20260420174731579.png]]
## Using **NetworkMiner** 
software (available on local host), analyze the given packet capture and note the following details related to email:
   - a. To and From email IDs
   - b. Subject
   - c. Message IDs
   - d. Timestamp values
   - e. Attachments (if any)


8. Recover any attachments and note the **hash values** of the same.

![[IMG-20260420174731640.png]]
8. Upload your document on the Student Portal by answering the questions given at the end of the case description.

---

## Review Questions

1. Develop a timeline for the given case.
2. Who did Ann communicate with? Provide a list of email addresses and any other identifying information.
3. Are there any indications of Ann's physical whereabouts? If so, provide supporting evidence.

---

## Observations

### DHCP / BOOTP Filter Results

| Field           | Value |
|-----------------|-------|
| MAC Address     |       |
| IP Address      |       |
| Host Name       |       |
| Lease Time      |       |
| DNS Server      |       |
| Router Address  |       |
| Subnet Mask     |       |

### SMTP Analysis

| Field                  | Value |
|------------------------|-------|
| Number of EHLO Messages| 2 |
| Email Addresses Found  | `sneakyg33k@aol.com`, `sec558@gmail.com`, `mistersecretx@aol.com` |

### Authentication Details (TCP Stream)

| Field              | Value |
|--------------------|-------|
| Encrypted?         | No — credentials sent as plain Base64, no TLS |
| Username (encoded) | `c25lYWt5ZzMza0Bhb2wuY29t` |
| Password (encoded) | `NTU4cjAwbHo=` |
| Username (decoded) | `sneakyg33k@aol.com` |
| Password (decoded) | `558r00lz` |

### Email Content (from TCP Stream)

**Email 1 — To `sec558@gmail.com` (Subject: lunch next week)**
> Sorry-- I can't do lunch next week after all. Heading out of town. Another time! -Ann

**Email 2 — To `mistersecretx@aol.com` (Subject: rendezvous)**
> Contains attachment (285 KB). Message body details the planned rendezvous — meeting location is **Mexico**.

### NetworkMiner Email Analysis

#### IMAP/Chat Messages (evidence01.pcap — 2009-08-13)

| Packet | From IP | To IP | From User | To User | Message | Timestamp (UTC) |
|--------|---------|-------|-----------|---------|---------|------------------|
| 25 | 192.168.1.158 | 64.12.24.50 | — | Sec558user1 | Here's the secret recipe... I just downloaded it from the file server. Just copy to a thumb drive... | 2009-08-13 05:57:37 |
| 167 | 64.12.24.50 | 192.168.1.158 | Sec558user1 | — | thanks dude | 2009-08-13 05:58:12 |
| 184 | 64.12.24.50 | 192.168.1.158 | Sec558user1 | — | can't wait to sell it on ebay | 2009-08-13 05:58:26 |
| 212 | 192.168.1.158 | 64.12.24.50 | — | Sec558user1 | see you in hawaii! | 2009-08-13 05:58:33 |

#### SMTP Emails (evidence02.pcap — 2009-10-10)


| Field      | Email 1                             | Email 2                             |
| ---------- | ----------------------------------- | ----------------------------------- |
| From       | `sneakyg33k@aol.com` (Ann Dercover) | `sneakyg33k@aol.com` (Ann Dercover) |
| To         | `sec558@gmail.com`                  | `mistersecretx@aol.com`             |
| Subject    | lunch next week                     | rendezvous                          |
| Timestamp  | 2009-10-10 13:35:31 UTC             | 2009-10-10 13:38:13 UTC             |
| Size       | 1350 bytes                          | 285628 bytes                        |
| Attachment | None                                | **Yes** (285 KB — likely a file)    |
| Server     | smtp.cs.com / smtp.aol.com          | smtp.cs.com / smtp.aol.com          |

### Attachment Recovery

| Field          | Value |
|----------------|-------|
| File Name      |       |
| MD5 Hash       |       |
| SHA1 Hash      |       |

---

## Answers to Review Questions

### 1. Timeline

| Date & Time (UTC) | Event |
|---|---|
| 2009-08-13 05:57:37 | Ann (192.168.1.158) sends a **secret recipe file** downloaded from the internal file server to Sec558user1 (Oscar) via IM chat |
| 2009-08-13 05:58:12 | Oscar replies: *"thanks dude"* |
| 2009-08-13 05:58:26 | Oscar says: *"can't wait to sell it on ebay"* — confirms intent to sell stolen data |
| 2009-08-13 05:58:33 | Ann says: *"see you in hawaii!"* — indicates a planned physical meetup |
| 2009-10-10 13:35:31 | Ann sends email from `sneakyg33k@aol.com` to `sec558@gmail.com` — subject **"lunch next week"**, cancels plans, says she is *"heading out of town"* |
| 2009-10-10 13:38:13 | Ann sends email from `sneakyg33k@aol.com` to `mistersecretx@aol.com` — subject **"rendezvous"**, 285 KB attachment, arranging meetup in **Mexico** |
| 2010-02-02 23:34–23:44 | Additional network activity captured (evidence04.pcap) — SMTP, POP3, IMAP, HTTP traffic |

---

### 2. Communication List

| Contact | Identifier | Method | Notes |
|---------|------------|--------|-------|
| Oscar / Mr. X | `Sec558user1`, IP `64.12.24.50` | Instant Messaging | Received stolen recipe file; planned to sell it on eBay |
| Unknown | `sec558@gmail.com` | SMTP Email | Received decoy "lunch" cancellation email |
| Mr. X (secret lover) | `mistersecretx@aol.com` | SMTP Email | Received **rendezvous** email with 285 KB attachment — Mexico meetup |

---

### 3. Physical Whereabouts

Ann's intended destination is **Mexico**.

**Supporting evidence:**
- Email sent **2009-10-10 13:38 UTC** from `sneakyg33k@aol.com` to `mistersecretx@aol.com`, subject *"rendezvous"* — contained a **285 KB attachment** with details of a planned meeting in Mexico.
- Earlier IM chat on **2009-08-13** referenced meeting *"in hawaii"*, showing Ann had been planning to flee with her contact over several months.
- Email to `sec558@gmail.com` on **2009-10-10** explicitly states she is *"heading out of town"*, consistent with a planned escape.

---

# References

###### Information
- date: 2026.03.05
- time: 11:02