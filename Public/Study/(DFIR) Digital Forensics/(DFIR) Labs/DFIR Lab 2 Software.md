---

Title: "DFIR Software Lab 2"

Status:

marker:

tags:

Date: "2026.01.29"

Time: "10:42"

---
# Experiment 2: Cyber Forensic Tools

## Aim
To study various cyber forensics tools, evaluate needs for digital forensics, and understand the hardware/software landscape.

## Learning Outcomes
1. Explain how to evaluate needs for [[Digital Forensics]] tools.
2. Describe available digital forensics software tools.
3. List considerations for digital forensics hardware tools.

---

## Task 1: Understanding Cyber Forensics Tools

### 1. Data Acquisition Tools
*Function:* Collecting and preserving data from devices without altering original evidence (Forensic Imaging).

| Tool | Type | Description | Link |
| :--- | :--- | :--- | :--- |
| **FTK Imager** | Commercial / Free | User-friendly GUI. Creates verified images (E01, DD). Good for previewing data. | [Link](https://www.exterro.com/ftk-imager) |
| **dd** | Open Source (Unix) | Command-line utility. Powerful but risky ("disk destroyer" if typed wrong). Standard for raw dumps. | [Link](https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html) |
| **EnCase** | Commercial | Industry standard. Robust, supports scripting, wide court acceptance. | [Link](https://www.opentext.com/products/encase-forensic) |
| **X1 Social Discovery**| Commercial | Specialized for social media and web collection. | [Link](https://www.x1.com/products/x1-social-discovery) |

### 2. Data Analysis Tools
*Function:* Processing acquired data, file carving, timeline analysis, and metadata extraction.

> [!INFO] Comparison
> **Autopsy** is excellent for learning and budgets (Open Source), while **EnCase** is the heavyweight standard for corporate/law enforcement environments.

* **[Autopsy](https://www.autopsy.com)**: Open-source GUI for [[The Sleuth Kit]]. Great for timeline analysis and hash lookups.
* **[EnCase Forensic](https://www.opentext.com/products/encase-forensic)**: Deep scripting capabilities (EnScript) and processing speed.
* **[X1 Search](https://www.x1.com/products/x1-search)**: Fast indexing and search capabilities.



### 3. Disk and Data Recovery Tools
*Function:* Recovering lost, deleted, or corrupted data from storage media.

* **[TestDisk](https://www.cgsecurity.org/wiki/TestDisk)**: Open Source. Fixes partition tables and recovers deleted partitions.
* **[R-Studio](https://www.r-studio.com)**: Commercial. Advanced algorithms for heavy damage and RAID recovery.
* **[Recuva](https://www.ccleaner.com/recuva)**: User-friendly recovery for accidental deletions.

### 4. Network Forensics Tools
*Function:* Analyzing network traffic (packets/flow) to detect malicious activity.

| Tool | Focus | Link |
| :--- | :--- | :--- |
| **[Wireshark](https://www.wireshark.org)** | **Packet Capture**: Deep inspection of protocols. The standard for packet analysis. | [Link](https://www.wireshark.org) |
| **[NetFlow Analyzer](https://www.manageengine.com/products/netflow)** | **Traffic Analysis**: Bandwidth monitoring and volume anomalies. | [Link](https://www.manageengine.com/products/netflow) |
| **[Xplico](https://www.xplico.org)** | **Reconstruction**: Extracts application data from internet traffic. | [Link](https://www.xplico.org) |

### 5. Mobile Forensics Tools
*Function:* Extracting data from smartphones and tablets.

* **[Cellebrite UFED](https://www.cellebrite.com/en/ufed/)**: Market leader. High compatibility for bypassing locks and physical extraction.
* **[MOBILedit Forensic](https://www.mobiledit.com/forensic)**: Strong content analysis and reporting.
* **[Oxygen Forensics](https://www.oxygen-forensic.com)**: Comprehensive extraction capabilities including cloud data.

### 6. Malware Forensics Tools
*Function:* Reverse-engineering and behavioral analysis of malicious software.

* **[Cuckoo Sandbox](https://cuckoosandbox.org)**: Dynamic analysis. Runs malware in an isolated environment to watch behavior.
* **[IDA Pro](https://hex-rays.com/ida-pro/)**: Static analysis. Disassembler for reading code logic.
* **[OllyDbg](http://www.ollydbg.de)**: Assembler level analyzing debugger.

---

## Task 2: Scenario Analysis
**Scenario:** Internal employee suspected of leaking sensitive financial data via USB and Email.

### Tool Selection Matrix

| Investigation Stage | Recommended Tool | Why? |
| :--- | :--- | :--- |
| **1. Initial Data Collection** | **[FTK Imager](https://www.exterro.com/ftk-imager)** | To create a forensically sound image of the disk and capture volatile RAM. |
| **2. Disk Forensics** | **[Autopsy](https://www.autopsy.com)** | To carve for deleted files and analyze file system artifacts. |
| **3. Network Forensics** | **[Wireshark](https://www.wireshark.org)** | To analyze historical PCAP files or monitor for active data exfiltration channels. |
| **4. Email Analysis** | **[MailXaminer](https://www.mailxaminer.com)** | Specialized for parsing PST/OST files and searching keyword "Confidential". |
| **5. Report Generation** | **[EnCase](https://www.opentext.com/products/encase-forensic)** | For generating a court-admissible Chain of Custody report. |

---

## Review Questions

### 1. Selection Criteria for Forensic Tools
When choosing a tool for an investigation, consider:
* **Admissibility:** Does it meet the [[Daubert Standard]]?
* **Compatibility:** Does it support the target File System (NTFS, APFS, EXT4)?
* **Cost:** Commercial vs. Open Source budget.
* **Scalability:** Can it handle Terabytes of data?

### 2. Forensic Workstation
> [!NOTE] Definition
> A high-performance computer dedicated to analyzing digital evidence, usually isolated to prevent cross-contamination.

**Key Specs:**
* **RAM:** 64GB+ for memory-intensive indexing.
* **Storage:** Fast NVMe SSDs for processing; large HDDs for evidence storage.
* **I/O:** USB 3.0/C, FireWire, eSATA for legacy drives.
* **Isolation:** Air-gapped (no internet) to prevent leaks or malware triggers.

### 3. Write Blockers
> [!NOTE] Definition
> A tool that allows read-only access to a drive, preventing accidental modification of evidence.



**Types:**
1.  **Hardware Write Blocker:** Physical bridge. High reliability. Preferred in court.
    * *Examples:* Tableau, WiebeTech.
2.  **Software Write Blocker:** OS utility (e.g., Registry edit). Cheaper but less reliable (prone to OS glitches).

---

## References & Resources
- **Imaging:** [FTK Imager](https://www.exterro.com/ftk-imager), [dd](https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html)
- **Analysis:** [Autopsy](https://www.autopsy.com), [Sleuth Kit](https://www.sleuthkit.org), [EnCase](https://www.opentext.com/products/encase-forensic)
- **Recovery:** [R-Studio](https://www.r-studio.com), [Recuva](https://www.ccleaner.com/recuva), [TestDisk](https://www.cgsecurity.org/wiki/TestDisk)
- **Network:** [Wireshark](https://www.wireshark.org), [Xplico](https://www.xplico.org), [tcpdump](https://www.tcpdump.org)
- **Mobile:** [Cellebrite](https://www.cellebrite.com/en/ufed/), [XRY](https://www.msab.com/products/xry/)
- **Malware:** [IDA Pro](https://hex-rays.com/ida-pro/), [Process Explorer](https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer)
- **Encryption:** [Passware](https://www.passware.com), [ElcomSoft](https://www.elcomsoft.com), [BitCrack](https://github.com/brichard19/BitCrack)
- **Cloud:** [Cloud Forensic Toolkit](https://github.com/google/cloud-forensics-utils)
  

# References


###### Information
- date: 2026.01.29
- time: 10:42