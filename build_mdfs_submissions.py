from __future__ import annotations

from datetime import datetime
from pathlib import Path
import re

from docx import Document
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
TARGET_DIR = ROOT / "Public" / "Study" / "(MDFS) Mobile Device Forensics and Security TO BE DISCARDED" / "Study (MDFS) Mobile Device Forensics Security"
ASSETS_DIR = TARGET_DIR / "assets"

# Keep destination filenames compatible with the existing MDFS folder structure.
LABS = [
    {
        "src": "K057_TejasSahoo_MDSF1.pdf",
        "dst": "MDFS Lab 01 - Insider Threat Investigation.md",
        "title": "MDFS Lab 01 - Insider Threat Investigation",
    },
    {
        "src": "K057_MDSF_Lab02_Tejas_Sahoo.docx",
        "dst": "MDFS Lab 02 - Android and iOS Analysis with Autopsy.md",
        "title": "MDFS Lab 02 - Android and iOS Analysis with Autopsy",
    },
    {
        "src": "K057_MDSF_Lab03.pdf",
        "dst": "MDFS Lab 03 - LastPass and Keeper.md",
        "title": "MDFS Lab 03 - LastPass and Keeper",
    },
    {
        "src": "K057_Tejas_Sahoo_MDSF LAB-5 - Android Emulator Rooting.pdf",
        "dst": "MDFS Lab 05 - Android Emulator Rooting.md",
        "title": "MDFS Lab 05 - Android Emulator Rooting",
    },
    {
        "src": "K057_MDSF LAB-6 - Logical Data Extraction using Andriller.pdf",
        "dst": "MDFS Lab 06 - Logical Data Extraction using Andriller.md",
        "title": "MDFS Lab 06 - Logical Data Extraction using Andriller",
    },
    {
        "src": "K057_TejasSahoo_MDSF LAB-7 - Data Extraction using ALEAPP.pdf",
        "dst": "MDFS Lab 07 - Data Extraction using ALEAPP.md",
        "title": "MDFS Lab 07 - Data Extraction using ALEAPP",
    },
    {
        "src": "K057_Tejas_Sahoo_MDSF LAB-8 - Recovering Deleted Data using PhotoRec.docx",
        "dst": "MDFS Lab 08 - Recovering Deleted Data using PhotoRec.md",
        "title": "MDFS Lab 08 - Recovering Deleted Data using PhotoRec",
    },
    {
        "src": "K057_MDSF_LAB 9.docx",
        "dst": "MDFS Lab 09 - Android Malware Analysis using Mobile SF.md",
        "title": "MDFS Lab 09 - Android Malware Analysis using Mobile SF",
    },
    {
        "src": "K057_TejasSahoo_MDSF10.pdf",
        "dst": "MDFS Report 10 - Mobile Forensics Literature Review.md",
        "title": "MDFS Report 10 - Mobile Forensics Literature Review",
    },
]


def slugify(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_")
    return slug.lower() or "submission"


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\u00a0", " ")

    lines = [line.rstrip() for line in text.split("\n")]
    cleaned_lines: list[str] = []
    prev_blank = False

    for line in lines:
        normalized = re.sub(r"[ \t]+", " ", line).strip()
        if not normalized:
            if not prev_blank:
                cleaned_lines.append("")
            prev_blank = True
            continue

        cleaned_lines.append(normalized)
        prev_blank = False

    return "\n".join(cleaned_lines).strip()


def normalize_identity(text: str) -> str:
    # Replace common old student identity markers found in source files.
    text = re.sub(r"(?i)\bPrakhar\s+Mehta\b", "tejas kamal sahoo", text)
    text = re.sub(r"(?i)\bJal\s+Bafana\b", "tejas kamal sahoo", text)

    # Replace explicit name fields.
    text = re.sub(
        r"(?im)^\s*name\s*[:\-]\s*.*$",
        "Name: tejas kamal sahoo",
        text,
    )

    # Replace explicit roll fields.
    text = re.sub(
        r"(?im)^\s*roll\s*(?:no\.?|number)?\s*[:\-]\s*.*$",
        "Roll no: k057",
        text,
    )

    # Replace standalone old roll IDs that may appear in title lines.
    text = re.sub(r"\bK037\b", "k057", text)
    text = re.sub(r"\bK005\b", "k057", text)

    return text


def extract_from_pdf(pdf_path: Path) -> tuple[str, list[tuple[str, bytes]]]:
    reader = PdfReader(str(pdf_path))
    page_blocks: list[str] = []
    images: list[tuple[str, bytes]] = []

    for page_idx, page in enumerate(reader.pages, start=1):
        page_text = (page.extract_text() or "").strip()
        if page_text:
            page_blocks.append(f"### Page {page_idx}\n{page_text}")
        else:
            page_blocks.append(f"### Page {page_idx}\n(No extractable text on this page.)")

        try:
            for img_idx, image in enumerate(list(page.images), start=1):
                ext = Path(image.name).suffix.lower() or ".png"
                if ext not in {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff", ".gif"}:
                    ext = ".bin"
                img_name = f"page{page_idx:02d}_img{img_idx:02d}{ext}"
                images.append((img_name, image.data))
        except Exception:
            # Continue text conversion even if image extraction fails for a page.
            pass

    return "\n\n".join(page_blocks), images


def extract_from_docx(docx_path: Path) -> tuple[str, list[tuple[str, bytes]]]:
    doc = Document(str(docx_path))
    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text and p.text.strip()]
    text = "\n".join(paragraphs)

    images: list[tuple[str, bytes]] = []
    idx = 1
    for rel in doc.part.rels.values():
        if "image" not in rel.reltype:
            continue
        part = rel.target_part
        ext = Path(part.partname).suffix.lower() or ".png"
        img_name = f"doc_img{idx:02d}{ext}"
        images.append((img_name, part.blob))
        idx += 1

    return text, images


def write_submission(title: str, source_name: str, dst_path: Path, text: str, images: list[tuple[str, bytes]]) -> None:
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    asset_rel_paths: list[str] = []
    if images:
        image_folder = ASSETS_DIR / slugify(dst_path.stem)
        image_folder.mkdir(parents=True, exist_ok=True)

        for img_name, img_data in images:
            out_path = image_folder / img_name
            out_path.write_bytes(img_data)
            asset_rel_paths.append(f"./assets/{image_folder.name}/{img_name}")

    now = datetime.now()
    fm_date = now.strftime("%Y.%m.%d")
    fm_time = now.strftime("%H:%M")

    content_parts = [
        "---",
        f'Title: "{title}"',
        "Status: Active",
        "marker:",
        "tags:",
        f"Date: {fm_date}",
        f"Time: {fm_time}",
        "---",
        "",
        f"# {title}",
        "",
        f"Source file: {source_name}",
        "",
        "## Student Details",
        "- Name: tejas kamal sahoo",
        "- Roll no: k057",
        "",
        text.strip(),
    ]

    if asset_rel_paths:
        content_parts.append("")
        content_parts.append("## Evidence Images")
        content_parts.append("")
        for path in asset_rel_paths:
            content_parts.append(f"![Evidence Image]({path})")
            content_parts.append("")

    content = "\n".join(content_parts).rstrip() + "\n"
    dst_path.write_text(content, encoding="utf-8")


def main() -> None:
    generated: list[Path] = []

    for lab in LABS:
        src_path = ROOT / lab["src"]
        dst_path = TARGET_DIR / lab["dst"]
        title = lab["title"]

        if not src_path.exists():
            print(f"SKIP missing source: {src_path}")
            continue

        if src_path.suffix.lower() == ".pdf":
            text, images = extract_from_pdf(src_path)
        else:
            text, images = extract_from_docx(src_path)

        text = normalize_identity(clean_text(text))
        write_submission(title=title, source_name=src_path.name, dst_path=dst_path, text=text, images=images)
        generated.append(dst_path)

    print("Generated files:")
    for path in generated:
        print(path)


if __name__ == "__main__":
    main()
