from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent


@dataclass
class PageBlob:
    page_num: int  # 1-based
    text: str
    image_name: str


def _clean_text(text: str) -> str:
    text = (text or "").replace("\r", "\n")
    # Keep it vault-friendly: normalize to ASCII-ish with whitespace preserved.
    text = re.sub(r"[^\x09\x0a\x0d\x20-\x7e]", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _render_pages(pdf_path: Path, out_dir: Path, unit_num: int) -> list[str]:
    import pypdfium2 as pdfium

    out_dir.mkdir(parents=True, exist_ok=True)
    pdf = pdfium.PdfDocument(str(pdf_path))
    names: list[str] = []
    for idx in range(len(pdf)):
        page_num = idx + 1
        name = f"unit{unit_num}_p{page_num:02d}.png"
        names.append(name)
        out_path = out_dir / name
        if out_path.exists():
            continue
        page = pdf[idx]
        img = page.render(scale=2).to_pil()
        img.save(out_path)
    return names


def parse_unit_pdf(*, unit_num: int, pdf_path: Path, out_dir: Path) -> Path:
    """
    Produces:
      - out_dir/attachments/unit{unit}_pXX.png for every PDF page
      - out_dir/unit{unit}_raw.md with alternating text+image blobs per page
    """
    attachments = out_dir / "attachments"
    img_names = _render_pages(pdf_path, attachments, unit_num)

    reader = PdfReader(str(pdf_path))
    blobs: list[PageBlob] = []
    for idx, page in enumerate(reader.pages):
        page_num = idx + 1
        text = _clean_text(page.extract_text() or "")
        blobs.append(PageBlob(page_num=page_num, text=text, image_name=img_names[idx]))

    md_lines: list[str] = []
    md_lines.append(f"# (REMA) Unit {unit_num} Raw Parse")
    md_lines.append("")
    md_lines.append(f"Source: `{pdf_path}`")
    md_lines.append("")

    for blob in blobs:
        md_lines.append(f"## Page {blob.page_num}")
        md_lines.append("")
        md_lines.append(f"![[attachments/{blob.image_name}]]")
        md_lines.append("")
        md_lines.append("```text")
        if blob.text:
            md_lines.append(blob.text)
        md_lines.append("```")
        md_lines.append("")

    out_dir.mkdir(parents=True, exist_ok=True)
    out_md = out_dir / f"unit{unit_num}_raw.md"
    out_md.write_text("\n".join(md_lines).rstrip() + "\n", encoding="utf-8")
    return out_md


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Parse a REMA unit PDF into raw markdown + page images.")
    parser.add_argument("--unit", type=int, default=1, help="Unit number (default: 1)")
    args = parser.parse_args()

    unit_num = int(args.unit)
    pdf_path = (
        ROOT
        / "Public"
        / "Study"
        / "(REMA) Reverse Engineering and Malware Analysis"
        / "Lectures"
        / f"unit{unit_num}.pdf"
    )
    out_dir = ROOT / "Private" / "Staging Chamber" / "REMA Lectures Parsed" / f"Unit {unit_num}"

    if not pdf_path.exists():
        raise SystemExit(f"PDF not found: {pdf_path}")

    out_md = parse_unit_pdf(unit_num=unit_num, pdf_path=pdf_path, out_dir=out_dir)
    print(f"Wrote: {out_md}")


if __name__ == "__main__":
    main()
