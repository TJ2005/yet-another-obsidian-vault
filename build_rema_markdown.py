from __future__ import annotations

import re
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent
STAGING = ROOT / "Private" / "Staging Chamber" / "Rema"
OUT = ROOT / "Public" / "Study" / "(REMA) Reverse Engineering and Malware Analysis" / "Lab Experiments"
ATTACHMENTS = OUT / "attachments" / "rema"

NAME = "Tejas Sahoo"
ROLL = "K057"
DATE = "2026.04.24"


LABS = [
    {
        "lab": "1",
        "pdf": "K005_REMA_LAB_1.pdf",
        "title": "Dynamic Analysis of given Exe",
        "filename": "(REMA LAB 1) Dynamic Analysis of given Exe.md",
    },
    {
        "lab": "2",
        "pdf": "K005_REMA_LAB_2.pdf",
        "text": "REMA_LAB_2.extracted.txt",
        "title": "Study of Operating System and Assembly Concepts",
        "filename": "(REMA LAB 2) Study of Operating System and Assembly Concepts.md",
    },
    {
        "lab": "3",
        "pdf": "K005_REMA_LAB_3.pdf",
        "text": "REMA_LAB_3.extracted.txt",
        "title": "Disassembly using IDA and Ghidra",
        "filename": "(REMA LAB 3) Disassembly using IDA and Ghidra.md",
    },
    {
        "lab": "4",
        "pdf": "K005_REMA_LAB_4.pdf",
        "text": "REMA_LAB_4.extracted.txt",
        "title": "Basic Malware Analysis",
        "filename": "(REMA LAB 4) Basic Malware Analysis.md",
    },
    {
        "lab": "5",
        "pdf": "K005_REMA_Lab5 1.pdf",
        "title": "Agent Tesla Reverse Engineering",
        "filename": "(REMA LAB 5) Agent Tesla Reverse Engineering.md",
    },
    {
        "lab": "6",
        "pdf": "K005_REMA_LAB_6.pdf",
        "text": "REMA_LAB_6.extracted.txt",
        "title": "Website Malware Analysis",
        "filename": "(REMA LAB 6) Website Malware Analysis.md",
    },
    {
        "lab": "7",
        "pdf": "K005_REMA_Lab_7_new.pdf",
        "text": "REMA_LAB_7.extracted.txt",
        "title": "Malware Analysis of Various File Types",
        "filename": "(REMA LAB 7) Malware Analysis of Various File Types.md",
    },
    {
        "lab": "8",
        "pdf": "K005_Malware_Analysis_Report_REMA_Exp8.pdf",
        "text": "K005_REMA_Exp8.extracted.txt",
        "title": "Case Study of a Real-time Malware Attack and its Analysis",
        "filename": "(REMA LAB 8) Case Study of a Real-time Malware Attack and its Analysis.md",
    },
    {
        "lab": "9",
        "pdf": "K005_REMA_Lab9 (1).pdf",
        "text_root": "K005_REMA_Lab9.extracted.txt",
        "title": "Malware Obfuscation Techniques",
        "filename": "(REMA LAB 9) Malware Obfuscation Techniques.md",
    },
    {
        "lab": "10",
        "pdf": "K005_REMA_Lab10 (1).pdf",
        "text_root": "K005_REMA_Lab10.extracted.txt",
        "title": "Evidence Extraction from Live System and Malware Analysis",
        "filename": "(REMA LAB 10) Evidence Extraction from Live System and Malware Analysis.md",
    },
]

DETAILS = {
    "1": {
        "aim": "Perform dynamic analysis of a given executable in a controlled environment.",
        "tools": ["Windows analysis VM", "Process monitoring tools", "Network monitoring tools", "Hashing and file inspection utilities"],
        "procedure": [
            "Prepare an isolated analysis environment before executing the sample.",
            "Record file properties, hash values, and initial indicators.",
            "Execute the sample and observe process, file-system, registry, and network activity.",
            "Capture screenshots and document the observed behavior.",
        ],
        "observations": [
            "Dynamic analysis helps reveal runtime behavior that may not be visible during static inspection.",
            "Evidence must be collected in sequence so the execution flow can be reconstructed later.",
        ],
        "conclusion": "The experiment demonstrates how controlled execution can be used to understand executable behavior and collect useful malware-analysis evidence.",
    },
    "2": {
        "aim": "Study operating-system and assembly concepts relevant to reverse engineering.",
        "tools": ["ctoaassembly.com", "8086 assembler references", "C language examples", "Browser-based assembly converter"],
        "procedure": [
            "Review the relationship between high-level code, assembly language, and machine code.",
            "Write simple C programs and convert them into assembly-level output.",
            "Compare the source code with the generated assembly instructions.",
            "Document the output screenshots and interpret the main instruction flow.",
        ],
        "observations": [
            "Assembly language exposes low-level program behavior such as memory access, branching, and function calls.",
            "Reverse engineering relies on reading these lower-level representations when source code is unavailable.",
        ],
        "conclusion": "The practical conversion from C to assembly clarifies how programs are represented at a level useful for reverse engineering.",
    },
    "3": {
        "aim": "Explore reverse-engineering tools and disassemble a given file using IDA and Ghidra.",
        "tools": ["IDA", "Ghidra", "Disassembler view", "Decompiler view", "Function graph analysis"],
        "procedure": [
            "Load the target file into the selected reverse-engineering tool.",
            "Allow the tool to identify sections, functions, strings, and imports.",
            "Inspect disassembly and decompiler output to understand program control flow.",
            "Capture relevant screenshots and compare tool output.",
        ],
        "observations": [
            "IDA and Ghidra both help convert binary code into readable assembly and higher-level representations.",
            "The decompiler output is useful for quick understanding, but disassembly remains important for accuracy.",
        ],
        "conclusion": "The lab shows how professional RE tools support binary inspection, control-flow analysis, and program understanding.",
    },
    "4": {
        "aim": "Perform basic malware analysis using static and dynamic analysis concepts.",
        "tools": ["IDA", "Ghidra", "Static analysis utilities", "Sandboxed analysis environment"],
        "procedure": [
            "Identify the malware sample and document its basic file properties.",
            "Perform static inspection without executing the file.",
            "Use disassembly tools to inspect imports, strings, and code structure.",
            "Summarize suspected behavior based on the collected indicators.",
        ],
        "observations": [
            "Static analysis can reveal intent, suspicious API usage, embedded strings, and packing indicators.",
            "Dynamic analysis should only be performed inside an isolated environment.",
        ],
        "conclusion": "The experiment builds a foundation for malware triage by combining safe inspection with structured evidence collection.",
    },
    "5": {
        "aim": "Study Agent Tesla malware behavior through reverse-engineering techniques.",
        "tools": ["Static analysis tools", "Disassembler", "String inspection", "Malware-analysis references"],
        "procedure": [
            "Review the characteristics of Agent Tesla as an information-stealing malware family.",
            "Inspect the sample for strings, imports, and suspicious indicators.",
            "Identify behavior associated with credential theft, persistence, or exfiltration.",
            "Document the analysis findings with supporting screenshots.",
        ],
        "observations": [
            "Agent Tesla is commonly associated with credential theft and information exfiltration.",
            "Reverse engineering helps identify indicators that can support detection and response.",
        ],
        "conclusion": "The lab demonstrates how reverse-engineering workflow can be applied to understand a real malware family.",
    },
    "6": {
        "aim": "Analyze website malware using multiple analysis tools and indicators.",
        "tools": ["Website malware scanners", "Source-code inspection", "URL reputation checks", "Browser developer tools"],
        "procedure": [
            "Review the concept of website malware and common infection vectors.",
            "Inspect suspicious scripts, redirects, injected content, and hidden code.",
            "Use online and local tools to validate malicious indicators.",
            "Record evidence and summarize remediation steps.",
        ],
        "observations": [
            "Website malware often appears as injected scripts, redirects, skimmers, or defacement payloads.",
            "A complete analysis considers both the visible page and the server-side compromise path.",
        ],
        "conclusion": "The experiment highlights how web malware analysis combines code review, reputation checks, and evidence-driven remediation.",
    },
    "7": {
        "aim": "Analyze malicious file types such as JavaScript, PDF, and office documents.",
        "tools": ["File-format inspection tools", "OOXML/OLE analysis", "PDF analysis utilities", "JavaScript inspection"],
        "procedure": [
            "Identify the file type and internal document structure.",
            "Inspect embedded scripts, macros, objects, and metadata.",
            "Look for suspicious indicators such as obfuscation, embedded payloads, or external URLs.",
            "Document findings with screenshots in the order of analysis.",
        ],
        "observations": [
            "Document malware often abuses macros, embedded objects, JavaScript, or malformed file structures.",
            "Understanding OOXML and OLE structure helps locate hidden or embedded malicious components.",
        ],
        "conclusion": "The lab demonstrates safe inspection methods for document-based malware and other malicious file formats.",
    },
    "8": {
        "aim": "Prepare a case study on the role of a malware analyst using a real-world malware incident.",
        "tools": ["Threat-intelligence sources", "MITRE ATT&CK", "Incident timeline analysis", "IOC documentation"],
        "procedure": [
            "Select a real malware incident and identify the affected parties.",
            "Study the attack vector, malware behavior, and impact.",
            "Map observed tactics and techniques to MITRE ATT&CK where applicable.",
            "Summarize prevention, detection, and remediation measures.",
        ],
        "observations": [
            "A malware analyst connects technical evidence with incident response and threat intelligence.",
            "Real-world case studies help explain how malware behavior translates into business and operational impact.",
        ],
        "conclusion": "The case study shows the importance of malware analysis in identifying behavior, documenting IOCs, and guiding defensive action.",
    },
    "9": {
        "aim": "Recognize packed malware and unpack it using appropriate analysis tools.",
        "tools": ["PE inspection tools", "UPX", "Disassembler", "Import table analysis", "Packed sample"],
        "procedure": [
            "Inspect the executable for signs of packing or obfuscation.",
            "Identify packer indicators such as unusual sections, entropy, or broken imports.",
            "Attempt unpacking and compare the unpacked file with the original sample.",
            "Review imports and code visibility after unpacking.",
        ],
        "observations": [
            "Packing changes the structure of an executable to hide its original code and imports.",
            "Unpacking can restore visibility into the malware's real behavior and dependencies.",
        ],
        "conclusion": "The experiment shows why packed malware complicates analysis and how unpacking improves visibility into malicious code.",
    },
    "10": {
        "aim": "Extract and analyze volatile evidence collected from RAM during live malware investigation.",
        "tools": ["RAM capture tools", "Volatility-style memory analysis", "Process and network inspection", "Forensic reporting"],
        "procedure": [
            "Capture volatile system evidence before shutdown.",
            "Analyze memory for running processes, network connections, handles, and suspicious artifacts.",
            "Correlate volatile indicators with malware behavior.",
            "Document findings and preserve evidence for reporting.",
        ],
        "observations": [
            "RAM can contain evidence that disappears when a machine is powered off.",
            "Live acquisition is especially important when encryption, running malware, or active network connections are involved.",
        ],
        "conclusion": "The lab demonstrates why volatile evidence collection is essential during live response and malware investigation.",
    },
}


OLD_MARKDOWN = [
    "(REMA LAB 0) Dynamic Analysis of given Exe.md",
    "(REMA LAB 7) Malicious Files.md",
    "(REMA LABX) Study of Assembly Using CtoAssembly.com.md",
]


def clean_identity(text: str) -> str:
    replacements = {
        r"\bJal\s+Bafana\b": NAME,
        r"\bK005\b": ROLL,
        r"\bk005\b": ROLL,
        r"Student Name\s+Tejas Sahoo": f"Student Name {NAME}",
        r"Roll Number\s+K057": f"Roll Number {ROLL}",
        r"Roll no:\s*K057": f"Roll no: {ROLL}",
    }
    for pattern, value in replacements.items():
        text = re.sub(pattern, value, text, flags=re.IGNORECASE)
    text = text.replace("Btech.", "B.Tech.")
    text = text.replace("Defénse", "Defense")
    return text


def read_text(cfg: dict) -> str:
    if "text" in cfg:
        return (STAGING / cfg["text"]).read_text(encoding="utf-8", errors="replace")
    if "text_root" in cfg:
        return (ROOT / cfg["text_root"]).read_text(encoding="utf-8", errors="replace")

    reader = PdfReader(STAGING / cfg["pdf"])
    pages = []
    for index, page in enumerate(reader.pages, start=1):
        pages.append(f"===== PAGE {index} =====\n{page.extract_text() or ''}")
    return "\n\n".join(pages)


def normalize_markdown(text: str) -> str:
    text = clean_identity(text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"^Name:.*(?:\n.*Roll.*)?$", "", text, flags=re.MULTILINE | re.IGNORECASE)
    text = re.sub(r"^Student Name.*$", "", text, flags=re.MULTILINE | re.IGNORECASE)
    text = re.sub(r"^Roll Number.*$", "", text, flags=re.MULTILINE | re.IGNORECASE)
    text = re.sub(r"^Submitted by\s*$", "", text, flags=re.MULTILINE | re.IGNORECASE)
    text = re.sub(r"^===== PAGE (\d+) =====$", r"## Page \1", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*•\s+", "- ", text, flags=re.MULTILINE)

    heading_patterns = [
        (r"^(Experiment No\.?\s*:?\s*.*)$", r"## \1"),
        (r"^(Aim\s*:?\s*.*)$", r"## \1"),
        (r"^(AIM\s*:?\s*.*)$", r"## Aim"),
        (r"^(Title\s*:?\s*.*)$", r"## \1"),
        (r"^(TITLE\s*:?\s*.*)$", r"## Title"),
        (r"^(Part [A-Z]\s*:?\s*)$", r"## \1"),
        (r"^(Conclusion\s*:?\s*.*)$", r"## \1"),
        (r"^(References?\s*:?\s*)$", r"## \1"),
    ]
    for pattern, repl in heading_patterns:
        text = re.sub(pattern, repl, text, flags=re.MULTILINE)

    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def image_suffix(name: str) -> str:
    suffix = Path(name).suffix.lower()
    if suffix in {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tif", ".tiff", ".jp2"}:
        return suffix
    return ".png"


def extract_images(cfg: dict) -> dict[int, list[str]]:
    pdf_path = STAGING / cfg["pdf"]
    reader = PdfReader(pdf_path)
    asset_dir = ATTACHMENTS / f"rema-lab-{int(cfg['lab']):02d}"
    asset_dir.mkdir(parents=True, exist_ok=True)

    for old in asset_dir.iterdir():
        if old.is_file():
            old.unlink()

    embeds: dict[int, list[str]] = {}
    for page_number, page in enumerate(reader.pages, start=1):
        for image_number, image in enumerate(page.images, start=1):
            suffix = image_suffix(image.name)
            filename = f"lab-{int(cfg['lab']):02d}-page-{page_number:02d}-image-{image_number:02d}{suffix}"
            out_path = asset_dir / filename
            out_path.write_bytes(image.data)
            embeds.setdefault(page_number, []).append(
                f"![[attachments/rema/rema-lab-{int(cfg['lab']):02d}/{filename}]]"
            )
    return embeds


def frontmatter(title: str) -> str:
    return "\n".join(
        [
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
    )


def callout(kind: str, title: str, lines: list[str], folded: bool = False) -> list[str]:
    marker = "-" if folded else ""
    out = [f"> [!{kind}]{marker} {title}"]
    if not lines:
        return out
    out.append(">")
    for line in lines:
        if line == "":
            out.append(">")
        else:
            out.append(f"> {line}")
    return out


def strip_page_markers(body: str) -> str:
    body = re.sub(r"^## Page (\d+)$", r"### Source Page \1", body, flags=re.MULTILINE)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def evidence_section(images: dict[int, list[str]]) -> list[str]:
    lines = ["## Evidence and Screenshots", ""]
    if not images:
        lines.extend(callout("note", "Image Evidence", ["No embedded images were detected in the source PDF."]))
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


def build_note(cfg: dict, body: str, images: dict[int, list[str]]) -> str:
    details = DETAILS[cfg["lab"]]
    body = strip_page_markers(body)

    lines = [
        frontmatter(f"REMA LAB {cfg['lab']}"),
        f"# REMA LAB {cfg['lab']}",
        f"## {cfg['title']}",
        "",
        *callout(
            "info",
            "Submission Details",
            [
                f"**Name:** {NAME}",
                f"**Roll Number:** {ROLL}",
                "**Subject:** Reverse Engineering and Malware Analysis",
                "**Branch:** B.Tech. Cyber Security (Sem-6)",
                f"**Experiment No.:** {cfg['lab']}",
            ],
        ),
        "",
        *callout("abstract", "Aim", [details["aim"]]),
        "",
        *callout("tip", "Title", [cfg["title"]]),
        "",
        "## Tools Used",
        *[f"- {tool}" for tool in details["tools"]],
        "",
        "## Procedure",
        *[f"{idx}. {step}" for idx, step in enumerate(details["procedure"], start=1)],
        "",
        "## Key Observations",
        *[f"- {item}" for item in details["observations"]],
        "",
        "## Conclusion",
        details["conclusion"],
        "",
        *evidence_section(images),
        "## Appendix",
        "",
        *callout("quote", "Cleaned Source Text", body.splitlines(), folded=True),
    ]
    return "\n".join(lines).strip() + "\n"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    ATTACHMENTS.mkdir(parents=True, exist_ok=True)

    for cfg in LABS:
        text = normalize_markdown(read_text(cfg))
        images = extract_images(cfg)
        note = build_note(cfg, text, images)
        (OUT / cfg["filename"]).write_text(note, encoding="utf-8", newline="\n")

    for old_name in OLD_MARKDOWN:
        old_path = OUT / old_name
        if old_path.exists():
            old_path.unlink()


if __name__ == "__main__":
    main()
