from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent
STAGING = ROOT / "Private" / "Staging Chamber" / "DFR"
OUT = ROOT / "Public" / "Study" / "(DFIR) Digital Forensics" / "(DFIR) Labs"
ATTACHMENTS = OUT / "attachments" / "dfir"

NAME = "Tejas Sahoo"
ROLL = "K057"
DATE = "2026.04.25"


LABS = [
    {
        "lab": "1",
        "pdf": "K005_DFIR_Lab1.pdf",
        "title": "Analysis of Cybercrime Events",
        "filename": "DFIR Lab 1 Analysis Of Cybercrime Events.md",
        "aim": "To study common cybercrimes and understand the cyber forensic process.",
        "objective": "This experiment builds a foundation for digital forensics by connecting cybercrime categories with the evidence that investigators collect during a case.",
        "tools": ["Internet research", "Cybercrime case references", "Digital forensics process notes"],
        "theory": [
            "Cybercrime includes offences where computers, networks, phones, accounts, or digital services are used as the target, the tool, or the storage location for evidence.",
            "A forensic investigation follows a disciplined process: identify possible evidence, preserve it, acquire a trustworthy copy, analyze the copy, and present the findings in a clear report.",
        ],
        "procedure": [
            "Listed major types of cybercrime and grouped them by target.",
            "Studied common attacker motives and methods.",
            "Reviewed the cyber forensic process from identification to reporting.",
            "Answered review questions using the collected theory.",
        ],
        "observations": [
            "Digital evidence can be fragile because it may change through normal system use.",
            "The value of an investigation depends on preservation, documentation, and repeatable analysis.",
        ],
        "result": "Cybercrimes, cybercriminal categories, and the digital forensic process were studied and summarized.",
        "conclusion": "The experiment shows why DFIR work must combine technical evidence handling with a clear understanding of criminal behavior.",
    },
    {
        "lab": "2",
        "pdf": "K005_DFIR_Lab2.pdf",
        "title": "Cyber Forensic Tools",
        "filename": "DFIR Lab 2 Software.md",
        "aim": "To study various cyber forensic tools and their role in investigation.",
        "objective": "The objective is to understand how forensic software and hardware support acquisition, recovery, analysis, and reporting without altering original evidence.",
        "tools": ["Autopsy", "FTK Imager", "EnCase-style forensic suites", "Wireshark", "Volatility-style memory tools", "Write blockers"],
        "theory": [
            "Forensic tools reduce manual effort during evidence acquisition and analysis, but the investigator must still understand what the tool is doing.",
            "Good tools support integrity checks, repeatable workflows, timeline reconstruction, artifact recovery, and defensible reporting.",
        ],
        "procedure": [
            "Identified categories of forensic tools used in digital investigations.",
            "Compared software tools for disk, memory, network, mobile, and email evidence.",
            "Reviewed hardware considerations such as write blockers and acquisition devices.",
            "Documented how tool selection depends on the case requirement.",
        ],
        "observations": [
            "No single tool is enough for every investigation.",
            "Tool output should be validated, especially when evidence may be used for legal or disciplinary action.",
        ],
        "result": "Major cyber forensic tool categories and their investigation uses were studied.",
        "conclusion": "The lab clarifies that forensic tools are aids for evidence handling, analysis, and reporting, but reliable conclusions still depend on investigator judgment.",
    },
    {
        "lab": "3",
        "pdf": "K005_DFIR_Lab3.pdf",
        "title": "Registry Analysis",
        "filename": "DFIR Lab 3 Registry Analysis.md",
        "aim": "To analyze the registry of a Windows system.",
        "objective": "This lab studies the Windows Registry as a forensic artifact source for system configuration, user activity, installed software, and persistence clues.",
        "tools": ["Windows Registry Editor", "Command Prompt", "Registry hives", "Windows forensic artifact notes"],
        "theory": [
            "The Windows Registry is a hierarchical database that stores operating system, hardware, application, and user configuration data.",
            "Registry hives such as HKLM, HKCU, HKCR, HKU, and HKCC can reveal installed programs, recent activity, user preferences, and system-level settings.",
        ],
        "procedure": [
            "Opened Registry Editor using the `regedit` command.",
            "Explored major registry hives and noted their purpose.",
            "Inspected selected keys and values relevant to Windows activity.",
            "Captured evidence screenshots while navigating the registry structure.",
        ],
        "observations": [
            "Registry values can connect activity to a user profile or machine-wide configuration.",
            "Registry analysis is useful, but careless modification can affect the system, so investigation should be read-only wherever possible.",
        ],
        "result": "Windows Registry structure and forensic relevance were analyzed through practical navigation.",
        "conclusion": "The Registry is an important source of DFIR evidence because it records configuration and user activity that may support incident timelines.",
    },
    {
        "lab": "4",
        "pdf": "K005_DFIR_Lab4.pdf",
        "title": "MBR and GPT Analysis",
        "filename": "DFIR Lab 4 MBR and GPT Analysis.md",
        "aim": "To analyze Master Boot Record and GUID Partition Table structures.",
        "objective": "This experiment focuses on how disks describe partitions and boot information, which matters during forensic acquisition and recovery.",
        "tools": ["Disk Management", "Hex/disk inspection concepts", "MBR structure notes", "GPT structure notes"],
        "theory": [
            "MBR stores boot code, a small partition table, and a boot signature in the first sector of a disk.",
            "GPT is the newer partitioning scheme used with UEFI systems and supports larger disks, more partitions, and redundant partition metadata.",
        ],
        "procedure": [
            "Reviewed the layout of MBR and GPT partition structures.",
            "Compared BIOS/MBR and UEFI/GPT boot approaches.",
            "Analyzed partition metadata and disk layout evidence.",
            "Captured screenshots showing the analysis workflow.",
        ],
        "observations": [
            "MBR is limited to four primary partitions unless extended partitions are used.",
            "GPT improves reliability by storing backup partition information and CRC checks.",
        ],
        "result": "MBR and GPT disk structures were compared and analyzed from a forensic perspective.",
        "conclusion": "Understanding partition structures helps investigators interpret disk images, recover partitions, and explain boot-related evidence.",
    },
    {
        "lab": "5",
        "pdf": "K005_DFIR_Lab5.pdf",
        "title": "Email Header Analysis and Tracing",
        "filename": "DFIR Lab 5 Email Header Analysis and Tracing.md",
        "aim": "To analyze an email header and trace it to the source.",
        "objective": "This lab studies email metadata so suspicious messages can be traced, authenticated, and evaluated for spoofing or phishing indicators.",
        "tools": ["Email header viewer", "MXToolbox-style header analyzer", "IP lookup tools", "WHOIS/DNS references"],
        "theory": [
            "Email headers contain routing metadata added by mail servers as a message travels from sender to recipient.",
            "Fields such as Received, From, Return-Path, Message-ID, SPF, DKIM, and DMARC help assess origin and authenticity.",
        ],
        "procedure": [
            "Collected the full email header from the sample message.",
            "Inspected sender, recipient, date, subject, return path, and received lines.",
            "Traced the routing path using server and IP information.",
            "Checked for mismatches that may indicate spoofing or phishing.",
        ],
        "observations": [
            "The visible From address alone is not reliable evidence of sender identity.",
            "Received lines and authentication results provide stronger clues about the actual message path.",
        ],
        "result": "The email header was analyzed and the message path was traced using metadata fields.",
        "conclusion": "Email header analysis is a practical DFIR technique for validating message origin and identifying phishing indicators.",
    },
    {
        "lab": "6",
        "pdf": "K005_DFIR_Lab6.pdf",
        "title": "Rodeo Challenge",
        "filename": "DFIR Lab 6 Rodeo Challenge.md",
        "aim": "To analyze the Rodeo Challenge case using Autopsy.",
        "objective": "This lab uses a forensic image and supporting evidence to recover files and answer case questions through an Autopsy workflow.",
        "tools": ["Autopsy", "Forensic disk image", "Network trace evidence", "Hash verification"],
        "case": "The investigation involves a seized USB image and network traces connected to suspected illegal image possession and transfer activity.",
        "procedure": [
            "Created a case in Autopsy and added the provided evidence image.",
            "Allowed ingest modules to process files, metadata, and recovered artifacts.",
            "Searched for relevant images and supporting traces.",
            "Documented recovered artifacts and case answers with screenshots.",
        ],
        "observations": [
            "Autopsy helps organize recovered files, metadata, and keyword search results in one case workspace.",
            "Hash values and evidence descriptions are important for confirming that the correct source material was examined.",
        ],
        "result": "The Rodeo Challenge evidence was analyzed and relevant artifacts were documented.",
        "conclusion": "The experiment demonstrates how forensic suites support image recovery, evidence review, and structured case reporting.",
    },
    {
        "lab": "7",
        "pdf": "K005_DFIR_Lab7.pdf",
        "title": "Ann's Rendezvous Case",
        "filename": "DFIR Lab 7 Ann's Rendezvous Case.md",
        "aim": "To recover email messages from packet capture and analyze the same.",
        "objective": "This lab examines SMTP traffic in a packet capture to recover communications, credentials, attachments, and location clues.",
        "tools": ["Wireshark", "SMTP filters", "Packet stream reconstruction", "Exported objects/files"],
        "case": "Investigators captured Ann Dercover's network activity and need the packet evidence analyzed for communications with a possible contact.",
        "procedure": [
            "Opened the evidence packet capture in Wireshark.",
            "Filtered for SMTP and related email traffic.",
            "Followed TCP streams to reconstruct message content.",
            "Looked for aliases, credentials, attachments, and location indicators.",
        ],
        "observations": [
            "Email content can often be reconstructed from unencrypted SMTP traffic.",
            "Network packets may reveal both message content and supporting metadata such as addresses and hosts.",
        ],
        "result": "SMTP evidence from the packet capture was inspected and relevant case artifacts were recovered.",
        "conclusion": "The lab shows how packet analysis can turn raw network traffic into useful investigative evidence.",
    },
    {
        "lab": "9",
        "pdf": "K005_DFIR_Lab9.pdf",
        "title": "Data Leak Case - Part 2",
        "filename": "DFIR Lab 9 Data Leak Case Part 2.md",
        "aim": "To analyze a data leak case using forensic artifacts.",
        "objective": "This lab continues the data leak investigation by using Autopsy and artifact review to connect user behavior with possible confidential data movement.",
        "tools": ["Autopsy", "Forensic image", "File metadata review", "Timeline analysis", "USB/CD artifact review"],
        "case": "A company employee is suspected of leaking sensitive technology data through cloud storage and removable media.",
        "procedure": [
            "Loaded the provided evidence into Autopsy.",
            "Reviewed user activity, file access, and removable-media indicators.",
            "Searched for confidential files, transfer traces, and communication artifacts.",
            "Captured evidence supporting the investigation questions.",
        ],
        "observations": [
            "Data leak cases require timeline correlation across files, devices, and communications.",
            "Removable media and cloud artifacts can show intent, access, and possible exfiltration paths.",
        ],
        "result": "Part 2 of the data leak case was analyzed and the relevant forensic artifacts were documented.",
        "conclusion": "The experiment highlights the importance of correlating multiple artifacts before making claims about insider data leakage.",
    },
    {
        "lab": "10",
        "pdf": "K005_DFIR_Lab10.pdf",
        "title": "Data Leak Case - Part 3",
        "filename": "DFIR Lab 10 Data Leak Case Part 3.md",
        "aim": "To analyze a data leak case using forensic artifacts.",
        "objective": "This lab completes another stage of the data leak case by reviewing evidence for policy violations, file movement, and suspicious communication.",
        "tools": ["Autopsy", "Forensic image", "Artifact review", "Timeline analysis", "Case reporting"],
        "case": "The same suspected insider data leak scenario is examined further to identify evidence of confidential data handling and transfer.",
        "procedure": [
            "Opened the case evidence in Autopsy.",
            "Reviewed file-system artifacts, user activity, and communication traces.",
            "Compared findings against the organization's security policy constraints.",
            "Prepared screenshots and conclusions for the case report.",
        ],
        "observations": [
            "Policy context helps interpret whether a discovered artifact is normal activity or suspicious behavior.",
            "A defensible conclusion should connect the artifact, timestamp, user, and suspected action.",
        ],
        "result": "Part 3 of the data leak case was analyzed and evidence was summarized.",
        "conclusion": "The lab reinforces that insider investigations depend on careful artifact correlation and policy-aware interpretation.",
    },
]


REPORT = {
    "pdf": "K005_DFIR_Report.pdf",
    "title": "Breakthrough Through Digital Evidence - Real-Life Case Study",
    "filename": "DFIR Report Breakthrough Through Digital Evidence.md",
    "subtitle": "The State of Minnesota v. Stephen Carl Allwine (2018)",
    "aim": "To study how digital forensic evidence contributed to a real-life criminal investigation.",
    "sections": [
        (
            "Case Summary",
            [
                "The report studies the Stephen Carl Allwine case, where digital evidence helped investigators challenge an attempted suicide narrative and establish a murder-for-hire plot.",
                "The case involved artifacts from multiple devices, dark web activity, cryptocurrency transactions, cloud data, and timeline reconstruction.",
            ],
        ),
        (
            "Forensic Importance",
            [
                "The case is useful for DFIR study because it shows how small digital traces from different sources can become powerful when correlated.",
                "It also demonstrates why investigators must preserve device data, browser artifacts, account records, and financial traces carefully.",
            ],
        ),
        (
            "Key Evidence Themes",
            [
                "Dark web browsing artifacts and Tor-related traces.",
                "Bitcoin and blockchain transaction analysis.",
                "Deleted notes, cloud backups, and device timelines.",
                "Security camera footage and multi-device correlation.",
            ],
        ),
        (
            "Conclusion",
            [
                "The case demonstrates that digital evidence can be decisive when investigators preserve sources properly and build a timeline that connects intent, preparation, and action.",
            ],
        ),
    ],
}


def image_suffix(name: str) -> str:
    suffix = Path(name).suffix.lower()
    if suffix in {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tif", ".tiff", ".jp2"}:
        return suffix
    return ".png"


def extract_images(pdf_name: str, slug: str, prefix: str) -> dict[int, list[str]]:
    reader = PdfReader(STAGING / pdf_name)
    asset_dir = ATTACHMENTS / slug
    asset_dir.mkdir(parents=True, exist_ok=True)

    for old in asset_dir.iterdir():
        if old.is_file():
            old.unlink()

    embeds: dict[int, list[str]] = {}
    for page_number, page in enumerate(reader.pages, start=1):
        for image_number, image in enumerate(page.images, start=1):
            suffix = image_suffix(image.name)
            filename = f"{prefix}-page-{page_number:02d}-image-{image_number:02d}{suffix}"
            (asset_dir / filename).write_bytes(image.data)
            embeds.setdefault(page_number, []).append(f"![[attachments/dfir/{slug}/{filename}]]")
    return embeds


def callout(kind: str, title: str, lines: list[str], folded: bool = False) -> list[str]:
    marker = "-" if folded else ""
    out = [f"> [!{kind}]{marker} {title}"]
    if lines:
        out.append(">")
        for line in lines:
            out.append(f"> {line}" if line else ">")
    return out


def frontmatter(title: str) -> list[str]:
    return [
        "---",
        f"Title: {title}",
        "Status: Active",
        "marker:",
        "tags:",
        f"Date: {DATE}",
        "Time: 00:00",
        "---",
        "",
    ]


def evidence_section(images: dict[int, list[str]]) -> list[str]:
    lines = ["## Evidence", ""]
    if not images:
        lines.extend(callout("note", "Screenshot Evidence", ["No embedded screenshots were detected in the source PDF."]))
        lines.append("")
        return lines

    for page in sorted(images):
        image_lines: list[str] = []
        for item in images[page]:
            image_lines.append(item)
            image_lines.append("")
        if image_lines and image_lines[-1] == "":
            image_lines.pop()
        lines.extend(callout("example", f"Page {page} Evidence", image_lines, folded=True))
        lines.append("")
    return lines


def build_lab_note(cfg: dict) -> str:
    images = extract_images(cfg["pdf"], f"dfir-lab-{int(cfg['lab']):02d}", f"lab-{int(cfg['lab']):02d}")
    subject = "Digital Forensics and Incident Response"

    lines = [
        *frontmatter(f"DFIR Lab {cfg['lab']}"),
        f"# DFIR Lab {cfg['lab']}",
        f"## {cfg['title']}",
        "",
        *callout(
            "info",
            "Submission Details",
            [
                f"**Name:** {NAME}  ",
                f"**Roll Number:** {ROLL}  ",
                f"**Subject:** {subject}  ",
                "**Branch:** B.Tech. Cyber Security, Semester 6  ",
                f"**Experiment No.:** {cfg['lab']}",
            ],
        ),
        "",
        *callout("abstract", "Aim", [cfg["aim"]]),
        "",
        *callout("tip", "Title", [cfg["title"]]),
        "",
        "## Objective",
        cfg["objective"],
        "",
    ]

    if "case" in cfg:
        lines.extend(["## Case Context", cfg["case"], ""])

    lines.extend(["## Tools and Environment", *[f"- {tool}" for tool in cfg["tools"]], ""])

    if cfg.get("theory"):
        lines.extend(["## Theory", *cfg["theory"], ""])

    lines.extend(
        [
            "## Procedure",
            *[f"{idx}. {step}" for idx, step in enumerate(cfg["procedure"], start=1)],
            "",
            "## Observations",
            *[f"- {item}" for item in cfg["observations"]],
            "",
            *evidence_section(images),
            "## Result",
            cfg["result"],
            "",
            "## Conclusion",
            cfg["conclusion"],
        ]
    )
    return "\n".join(lines).strip() + "\n"


def build_report_note() -> str:
    lines = [
        *frontmatter("DFIR Report"),
        "# DFIR Report",
        f"## {REPORT['title']}",
        "",
        *callout(
            "info",
            "Submission Details",
            [
                f"**Name:** {NAME}  ",
                f"**Roll Number:** {ROLL}  ",
                "**Subject:** Digital Forensics and Incident Response  ",
                "**Branch:** B.Tech. Cyber Security, Semester 6",
            ],
        ),
        "",
        *callout("abstract", "Aim", [REPORT["aim"]]),
        "",
        *callout("tip", "Case", [REPORT["subtitle"]]),
        "",
    ]

    for heading, paragraphs in REPORT["sections"]:
        lines.extend([f"## {heading}", *paragraphs, ""])

    return "\n".join(lines).strip() + "\n"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    ATTACHMENTS.mkdir(parents=True, exist_ok=True)

    for cfg in LABS:
        (OUT / cfg["filename"]).write_text(build_lab_note(cfg), encoding="utf-8", newline="\n")

    (OUT / REPORT["filename"]).write_text(build_report_note(), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
