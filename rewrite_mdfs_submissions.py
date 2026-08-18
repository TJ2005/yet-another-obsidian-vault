from __future__ import annotations

from datetime import datetime
from pathlib import Path

BASE = Path(
    "d:/tijo/Tijo's notebook/Public/Study/(MDFS) Mobile Device Forensics and Security TO BE DISCARDED/Study (MDFS) Mobile Device Forensics Security"
)
ASSETS = BASE / "assets"

NAME = "tejas kamal sahoo"
ROLL = "k057"


def list_images(asset_dir: str, limit: int) -> list[str]:
    folder = ASSETS / asset_dir
    if not folder.exists():
        return []

    files = [
        p.name
        for p in sorted(folder.iterdir())
        if p.is_file() and p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif", ".tiff"}
    ]
    return files[:limit]


def section_lines(title: str, items: list[str]) -> list[str]:
    lines = [f"## {title}"]
    for item in items:
        lines.append(f"- {item}")
    lines.append("")
    return lines


def build_lab_markdown(cfg: dict, date_text: str, time_text: str) -> str:
    lines: list[str] = []

    lines.extend(
        [
            "---",
            f'Title: "{cfg["title"]}"',
            "Status: Active",
            "marker:",
            "tags:",
            f"Date: {date_text}",
            f"Time: {time_text}",
            "---",
            "",
            f"# {cfg['title']}",
            "",
            f"Source file: {cfg['source']}",
            "",
            "## Student Details",
            f"- Name: {NAME}",
            f"- Roll no: {ROLL}",
            "",
            "## Aim",
            cfg["aim"],
            "",
        ]
    )

    lines.extend(section_lines("Learning Outcomes", cfg["outcomes"]))
    lines.extend(section_lines("Tools and Environment", cfg["tools"]))

    lines.append("## Procedure")
    for idx, step in enumerate(cfg["procedure"], start=1):
        lines.append(f"{idx}. {step}")
    lines.append("")

    lines.append("## Key Findings")
    for finding in cfg["findings"]:
        lines.append(f"- {finding}")
    lines.append("")

    lines.append("## Conclusion")
    lines.append(cfg["conclusion"])
    lines.append("")

    if cfg.get("references"):
        lines.append("## References")
        for ref in cfg["references"]:
            lines.append(f"- {ref}")
        lines.append("")

    asset_dir = cfg.get("asset_dir")
    if asset_dir:
        images = list_images(asset_dir, cfg.get("image_limit", 12))
        lines.append("## Evidence Screenshots")
        lines.append(
            f"Key screenshots are embedded below. Full extracted set is available in assets/{asset_dir}/"
        )
        lines.append("")
        for img_name in images:
            lines.append(f"![[{img_name}]]")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def build_report_markdown(cfg: dict, date_text: str, time_text: str) -> str:
    lines: list[str] = []

    lines.extend(
        [
            "---",
            f'Title: "{cfg["title"]}"',
            "Status: Active",
            "marker:",
            "tags:",
            f"Date: {date_text}",
            f"Time: {time_text}",
            "---",
            "",
            f"# {cfg['title']}",
            "",
            f"Source file: {cfg['source']}",
            "",
            "## Student Details",
            f"- Name: {NAME}",
            f"- Roll no: {ROLL}",
            "",
            "## Objective",
            cfg["objective"],
            "",
        ]
    )

    lines.extend(section_lines("Scope", cfg["scope"]))

    lines.append("## Synthesized Findings")
    for item in cfg["findings"]:
        lines.append(f"- {item}")
    lines.append("")

    lines.append("## Key Challenges Identified")
    for item in cfg["challenges"]:
        lines.append(f"- {item}")
    lines.append("")

    lines.append("## Recommendations")
    for item in cfg["recommendations"]:
        lines.append(f"- {item}")
    lines.append("")

    lines.append("## Conclusion")
    lines.append(cfg["conclusion"])
    lines.append("")

    lines.append("## References")
    for ref in cfg["references"]:
        lines.append(f"- {ref}")
    lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    now = datetime.now()
    date_text = now.strftime("%Y.%m.%d")
    time_text = now.strftime("%H:%M")

    labs = [
        {
            "file": "MDFS Lab 01 - Insider Threat Investigation.md",
            "title": "MDFS Lab 01 - Insider Threat Investigation",
            "source": "K057_TejasSahoo_MDSF1.pdf",
            "aim": "Investigate a simulated insider threat case using password-manager, browser, and VPN logs to determine whether credential exfiltration occurred.",
            "outcomes": [
                "Analyze password-manager audit logs for high-risk activity.",
                "Correlate browser artifacts with credential access events.",
                "Interpret VPN metadata (time, IP, geolocation) for attribution.",
                "Build a unified forensic timeline from multiple data sources.",
                "Produce a defensible incident conclusion.",
            ],
            "tools": [
                "keeper_audit_log.txt",
                "chrome_history.csv",
                "vpn_access.log",
                "Timeline correlation and report-writing workflow",
            ],
            "procedure": [
                "Preserved the evidence set and validated that no source files were modified.",
                "Analyzed password-manager logs to identify user, credential target, and access time.",
                "Reviewed browser history for suspicious destinations after credential operations.",
                "Reviewed VPN logs for session window and anomalous geolocation.",
                "Correlated all timestamps into a single investigative timeline.",
                "Assessed intent and risk based on sequence, proximity, and context of events.",
            ],
            "findings": [
                "User j.smith accessed Prod_DB_Credentials at 21:32:10 (outside normal office hours).",
                "Credential view and password copy actions were recorded in the same session.",
                "Pastebin access occurred shortly after credential copy, indicating potential exfiltration path.",
                "VPN session originated from Romania, inconsistent with expected operating location.",
                "Combined evidence strongly supports suspicious insider misuse and escalation requirement.",
            ],
            "conclusion": "The correlated logs establish a high-confidence insider-threat pattern: sensitive credential access, immediate copy action, suspicious external site access, and anomalous VPN origin. The event sequence is consistent with potential unauthorized disclosure of production credentials and should be escalated for containment and legal review.",
            "asset_dir": "mdfs_lab_01_insider_threat_investigation",
            "image_limit": 8,
        },
        {
            "file": "MDFS Lab 02 - Android and iOS Analysis with Autopsy.md",
            "title": "MDFS Lab 02 - Android and iOS Analysis with Autopsy",
            "source": "K057_MDSF_Lab02_Tejas_Sahoo.docx",
            "aim": "Perform logical forensic analysis of Android and iOS datasets using Autopsy and relevant mobile analyzers.",
            "outcomes": [
                "Create forensic cases and import logical mobile data correctly.",
                "Use Android and iOS analyzers to extract relevant artifacts.",
                "Validate evidence integrity using hash checks before analysis.",
                "Answer evidence-driven investigation questions from artifacts.",
                "Document findings in a repeatable and forensically sound format.",
            ],
            "tools": [
                "Autopsy",
                "aLEAPP modules (Android Analyzer and iOS Analyzer)",
                "7-Zip for dataset extraction",
                "Hash verification utilities",
            ],
            "procedure": [
                "Downloaded Android and iOS forensic datasets and verified cryptographic hashes.",
                "Created separate Autopsy cases for Android and iOS analysis.",
                "Imported logical files and enabled only required mobile ingest modules.",
                "Examined extracted artifacts including calls, messages, web history, Bluetooth, GPS, and notifications.",
                "Captured answers for flagged investigation prompts and recorded evidence screenshots.",
            ],
            "findings": [
                "Android most recently installed app identified as com.u360mobile.usna.",
                "Android web activity included http://yahoo.com/ at the queried timestamp.",
                "iOS paired device evidence indicated Eli's Apple Watch.",
                "iOS evidence included phone number +15415005105 in the requested area code.",
                "Signal code and Snapchat-related notification artifacts were recoverable from dataset evidence.",
            ],
            "conclusion": "Autopsy-based logical analysis successfully recovered cross-platform mobile artifacts and answered investigation questions from both Android and iOS evidence. The exercise reinforces forensic discipline: integrity checks, targeted ingest, artifact validation, and clear documentation.",
            "references": [
                "https://resources.infosecinstitute.com/topic/android-forensic-logical-acquisition/",
                "http://sleuthkit.org/autopsy/docs/user-docs/4.18.0/aleapp_page.html",
            ],
            "asset_dir": "mdfs_lab_02_android_and_ios_analysis_with_autopsy",
            "image_limit": 10,
        },
        {
            "file": "MDFS Lab 03 - LastPass and Keeper.md",
            "title": "MDFS Lab 03 - LastPass and Keeper",
            "source": "K057_MDSF_Lab03.pdf",
            "aim": "Examine how password-manager data can appear in process memory during runtime using LastPass and Keeper workflows.",
            "outcomes": [
                "Identify target browser-extension processes for memory inspection.",
                "Perform live-memory search using correct Unicode encoding settings.",
                "Correlate process-level artifacts with credential handling behavior.",
                "Explain runtime-memory exposure risks in application security.",
            ],
            "tools": [
                "LastPass browser extension",
                "Keeper browser extension",
                "Process Explorer",
                "HxD memory viewer",
            ],
            "procedure": [
                "Configured LastPass test data and identified extension process IDs in Process Explorer.",
                "Opened target process memory in HxD and searched for known test credential strings in UTF-16 LE.",
                "Configured Keeper test record and identified associated Firefox process via extension indicators.",
                "Repeated UTF-16 memory search to locate defined test marker values.",
                "Documented recovered in-memory indicators and interpreted security implications.",
            ],
            "findings": [
                "Credential-related strings were discoverable in extension process memory during active sessions.",
                "Process selection accuracy (extension-specific PID) was essential for successful recovery.",
                "UTF-16 LE search configuration was required for expected hits in memory.",
                "Keeper workflow exposed marker sequence (43 00 43 00) in runtime memory context.",
            ],
            "conclusion": "The lab demonstrates that secure storage alone is insufficient if sensitive values are exposed in runtime memory. Memory-focused analysis should be included in application security validation, especially for password-management and browser-extension ecosystems.",
            "references": [
                "https://www.mdsec.co.uk/2022/10/analysing-lastpass-part-1/",
            ],
            "asset_dir": "mdfs_lab_03_lastpass_and_keeper",
            "image_limit": 12,
        },
        {
            "file": "MDFS Lab 05 - Android Emulator Rooting.md",
            "title": "MDFS Lab 05 - Android Emulator Rooting",
            "source": "K057_Tejas_Sahoo_MDSF LAB-5 - Android Emulator Rooting.pdf",
            "aim": "Set up Android emulators for security testing and demonstrate the difference between normal-user and rooted execution contexts.",
            "outcomes": [
                "Create Android Virtual Devices (AVDs) for forensic/security experiments.",
                "Configure emulator storage and connectivity settings.",
                "Use ADB to validate device communication.",
                "Obtain and verify root shell access in controlled environments.",
            ],
            "tools": [
                "Android Studio",
                "Android Emulator (Google Play and non-Play system images)",
                "ADB",
                "Qute Terminal Emulator",
            ],
            "procedure": [
                "Installed Android Studio and created baseline emulator configurations.",
                "Built Google Play-enabled AVD for standard user-mode behavior.",
                "Built separate x86/non-Play image for root-capable testing workflow.",
                "Connected via ADB and validated device visibility.",
                "Opened shell with adb shell and executed su to confirm root context.",
                "Collected command outputs (for example uname/ps) as operational evidence.",
            ],
            "findings": [
                "ADB connectivity confirmed stable emulator-device communication.",
                "Root access was successfully obtained only in appropriate emulator configuration.",
                "System-level visibility increased in root shell compared with user mode.",
                "The setup is suitable for controlled malware/forensic lab validation.",
            ],
            "conclusion": "The exercise clearly separated standard Android runtime behavior from rooted forensic testing behavior. Controlled emulator rooting provides a repeatable environment for security research and artifact extraction without modifying physical devices.",
            "asset_dir": "mdfs_lab_05_android_emulator_rooting",
            "image_limit": 12,
        },
        {
            "file": "MDFS Lab 06 - Logical Data Extraction using Andriller.md",
            "title": "MDFS Lab 06 - Logical Data Extraction using Andriller",
            "source": "K057_MDSF LAB-6 - Logical Data Extraction using Andriller.pdf",
            "aim": "Perform logical acquisition from an Android emulator using Andriller and analyze extracted communication artifacts.",
            "outcomes": [
                "Prepare emulator evidence state for forensic extraction.",
                "Enable debug and ADB-based connectivity for acquisition.",
                "Run full logical extraction workflow in Andriller.",
                "Interpret extracted SMS, call, and contact artifacts.",
            ],
            "tools": [
                "Andriller (Free Version)",
                "Android Studio Emulator",
                "ADB",
                "HTML/CSV report export",
            ],
            "procedure": [
                "Launched emulator and verified seeded test artifacts.",
                "Enabled Developer Options and USB debugging in emulator.",
                "Validated ADB connectivity using adb devices.",
                "Executed Andriller full analysis and selected report output format.",
                "Reviewed generated report artifacts and mapped key database sources.",
            ],
            "findings": [
                "SMS artifacts recovered from mmssms.db.",
                "Call log artifacts recovered from calllog.db.",
                "Contact artifacts recovered from contacts2.db.",
                "Device metadata extracted and preserved in report output.",
            ],
            "conclusion": "Logical extraction with Andriller produced consistent communication and metadata evidence from the emulator environment. The workflow demonstrates a practical and repeatable acquisition process suitable for introductory mobile forensic investigations.",
            "asset_dir": "mdfs_lab_06_logical_data_extraction_using_andriller",
            "image_limit": 10,
        },
        {
            "file": "MDFS Lab 07 - Data Extraction using ALEAPP.md",
            "title": "MDFS Lab 07 - Data Extraction using ALEAPP",
            "source": "K057_TejasSahoo_MDSF LAB-7 - Data Extraction using ALEAPP.pdf",
            "aim": "Analyze an Android filesystem dataset using ALEAPP to recover communication, browsing, and network artifacts.",
            "outcomes": [
                "Run ALEAPP on a logical Android dataset.",
                "Interpret artifacts across SMS, call logs, browser, WhatsApp, and Wi-Fi data.",
                "Correlate timestamps to reconstruct user activity timeline.",
                "Identify potentially suspicious indicators from multi-source evidence.",
            ],
            "tools": [
                "Python 3.x",
                "ALEAPP",
                "Android dataset containing telephony, browser, app, and Wi-Fi files",
            ],
            "procedure": [
                "Prepared dataset and ALEAPP runtime environment.",
                "Executed ALEAPP with input dataset and report output directory.",
                "Opened generated HTML report and navigated artifact categories.",
                "Extracted key fields from SMS, call logs, browser history, WhatsApp messages, and Wi-Fi profiles.",
                "Correlated extracted timestamps to produce event narrative.",
            ],
            "findings": [
                "Recovered SMS conversations with multiple phone numbers and contextual message content.",
                "Call logs included outgoing, incoming, and missed events with durations.",
                "Browser history contained high-risk entry: http://darkwebmarket.onion.",
                "WhatsApp message entries confirmed parallel chat activity.",
                "Wi-Fi profile data showed Cafe_WiFi connection around 2024-03-12 19:22:01.",
            ],
            "conclusion": "ALEAPP enabled structured artifact recovery across multiple Android data domains. Cross-artifact correlation provided a coherent behavioral timeline and demonstrated how dataset-level extraction supports forensic reconstruction.",
            "asset_dir": "mdfs_lab_07_data_extraction_using_aleapp",
            "image_limit": 10,
        },
        {
            "file": "MDFS Lab 08 - Recovering Deleted Data using PhotoRec.md",
            "title": "MDFS Lab 08 - Recovering Deleted Data using PhotoRec",
            "source": "K057_Tejas_Sahoo_MDSF LAB-8 - Recovering Deleted Data using PhotoRec.docx",
            "aim": "Recover deleted files from forensic disk images using PhotoRec and evaluate limitations of file-carving workflows.",
            "outcomes": [
                "Understand file-carving based recovery in digital forensics.",
                "Configure PhotoRec for selective and broader file-type recovery.",
                "Compare simple and complex recovery scopes.",
                "Evaluate recovery quality and structural limitations.",
            ],
            "tools": [
                "PhotoRec",
                "disk.flag.img / android_sdcard.img style forensic image",
                "Forensic workstation environment",
            ],
            "procedure": [
                "Executed simple recovery with restricted file-type options.",
                "Executed complex recovery with expanded file signature set.",
                "Collected outputs from recup_dir folders and categorized recovered types.",
                "Reviewed recovered artifacts for potentially relevant textual indicators.",
                "Compared output completeness between simple and complex runs.",
            ],
            "findings": [
                "Deleted multimedia and document artifacts were recoverable from image data.",
                "Complex configuration recovered wider file-type diversity than simple mode.",
                "Recovered outputs lacked original filename/folder structure due to carving process.",
                "Result quality depends strongly on overwrite state and filesystem behavior.",
            ],
            "conclusion": "PhotoRec-based carving successfully recovered deleted evidence candidates from disk images. The lab highlights both the strength of signature-based recovery and the practical limitation of metadata loss during reconstruction.",
            "asset_dir": "mdfs_lab_08_recovering_deleted_data_using_photorec",
            "image_limit": 9,
        },
        {
            "file": "MDFS Lab 09 - Android Malware Analysis using Mobile SF.md",
            "title": "MDFS Lab 09 - Android Malware Analysis using Mobile SF",
            "source": "K057_MDSF_LAB 9.docx",
            "aim": "Compare benign and malicious Android APKs through static analysis using MobSF in an isolated lab environment.",
            "outcomes": [
                "Set up and run MobSF safely in isolated infrastructure.",
                "Perform baseline static analysis on benign APKs.",
                "Identify suspicious indicators in malicious APK analysis.",
                "Produce a comparative risk assessment report.",
            ],
            "tools": [
                "MobSF",
                "Benign APK sources (F-Droid / APKMirror)",
                "Academic malware datasets (Drebin / Contagio)",
                "Sandbox or VM environment with network controls",
            ],
            "procedure": [
                "Prepared isolated analysis environment (no local host execution).",
                "Set up MobSF and validated service accessibility.",
                "Analyzed selected benign APK and recorded static-analysis indicators.",
                "Analyzed selected malicious APK and recorded threat indicators.",
                "Compared results across permissions, trackers, signatures, package behavior, and exposure risk.",
            ],
            "findings": [
                "Benign APK showed high security posture with limited trackers and relevant permissions.",
                "Malicious APK showed low score, heavy tracker footprint, and suspicious package behavior.",
                "Self-signed certificate and exported components increased attack surface in malicious sample.",
                "Static-analysis comparison clearly separated low-risk and high-risk application characteristics.",
            ],
            "conclusion": "MobSF static analysis provided clear, evidence-driven differentiation between benign and malicious APK behavior. The lab confirms that certificate trust, tracker count, component exposure, and package semantics are practical indicators for mobile malware triage.",
            "references": [
                "https://github.com/MobSF/Mobile-Security-Framework-MobSF",
                "https://f-droid.org",
                "https://www.apkmirror.com",
                "https://www.sec.cs.tu-bs.de/~danarp/drebin/",
                "http://contagiominidump.blogspot.com",
            ],
            "asset_dir": "mdfs_lab_09_android_malware_analysis_using_mobile_sf",
            "image_limit": 15,
        },
    ]

    report = {
        "file": "MDFS Report 10 - Mobile Forensics Literature Review.md",
        "title": "MDFS Report 10 - Mobile Forensics Literature Review",
        "source": "K057_TejasSahoo_MDSF10.pdf",
        "objective": "Synthesize recent research (2024-2025) on mobile device forensics to identify current capabilities, challenges, and methodological gaps relevant to investigators.",
        "scope": [
            "Review focus: seven peer-reviewed papers on mobile forensics foundations, challenges, and tool ecosystems.",
            "Themes: acquisition methods, encryption barriers, cloud dependencies, anti-forensics, and standardization.",
            "Application context: criminal investigations, incident response, and legal evidence workflows.",
        ],
        "findings": [
            "Mobile devices are now primary digital evidence sources in most modern investigations.",
            "Full-file-system acquisition and lock-state awareness (BFU/AFU) significantly affect evidence availability.",
            "Tool ecosystems are rich but fragmented; mapping tools to method phases remains inconsistent.",
            "AI-assisted carving, search, and triage are emerging across contemporary forensic practice.",
            "Cross-domain investigations increasingly require mobile plus cloud forensic coordination.",
        ],
        "challenges": [
            "Device and OS fragmentation across vendors and versions.",
            "Encryption and credential barriers limiting acquisition depth.",
            "Jurisdictional and privacy constraints for cloud-linked evidence.",
            "Data volatility, anti-forensics, and rapid technology churn.",
            "Lack of universally adopted standardized process-tool mapping.",
        ],
        "recommendations": [
            "Adopt phase-based standardized methodology for identification, acquisition, analysis, and reporting.",
            "Maintain regular tool validation and update cycles aligned with OS/device changes.",
            "Integrate legal/compliance checkpoints early in investigation planning.",
            "Expand training on lock-state-aware acquisition and cloud evidence handling.",
            "Use repeatable documentation templates to strengthen evidentiary defensibility.",
        ],
        "conclusion": "The literature confirms that mobile forensics is operationally critical yet technically and legally complex. Progress depends on better standardization, stronger tool-method alignment, and continuous adaptation to encryption, cloud integration, and evolving mobile ecosystems.",
        "references": [
            "Fakiha (2024)",
            "Singano et al. (2025)",
            "James (2024)",
            "Bernardo et al. (2024)",
            "Sharma et al. (2024)",
            "Vinayagam (2025)",
            "Agboola et al. (2024)",
        ],
    }

    BASE.mkdir(parents=True, exist_ok=True)

    for cfg in labs:
        out = BASE / cfg["file"]
        out.write_text(build_lab_markdown(cfg, date_text, time_text), encoding="utf-8")
        print(f"Rewrote: {out}")

    report_file = BASE / report["file"]
    report_file.write_text(build_report_markdown(report, date_text, time_text), encoding="utf-8")
    print(f"Rewrote: {report_file}")


if __name__ == "__main__":
    main()
