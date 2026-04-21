from __future__ import annotations

from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import ContentStream, NameObject
from reportlab.pdfgen import canvas

INPUT_PDF = Path("K005_REMA_Lab9.pdf")
OUTPUT_PDF = Path("K005_REMA_Lab9_updated.pdf")

NAME_TEXT = "Name: tejas kamal sahoo"
ROLL_TEXT = "Roll number: k057"


def strip_text_from_page(page, reader: PdfReader) -> None:
    """Remove all text drawing operations while preserving images/graphics."""
    contents = page.get_contents()
    if contents is None:
        return

    stream = ContentStream(contents, reader)
    cleaned_ops = []
    in_text_block = False

    for operands, operator in stream.operations:
        if operator == b"BT":
            in_text_block = True
            continue
        if operator == b"ET":
            in_text_block = False
            continue

        if in_text_block:
            continue

        if operator in {b"Tj", b"TJ", b"'", b'"'}:
            continue

        cleaned_ops.append((operands, operator))

    stream.operations = cleaned_ops
    page[NameObject("/Contents")] = stream


def make_overlay_page(width: float, height: float):
    """Create a one-page PDF overlay that carries only the requested details."""
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=(float(width), float(height)))
    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, float(height) - 60, NAME_TEXT)
    c.setFont("Helvetica", 14)
    c.drawString(40, float(height) - 84, ROLL_TEXT)
    c.save()

    buf.seek(0)
    return PdfReader(buf).pages[0]


def main() -> None:
    if not INPUT_PDF.exists():
        raise FileNotFoundError(f"Input PDF not found: {INPUT_PDF}")

    reader = PdfReader(str(INPUT_PDF))
    writer = PdfWriter()

    for idx, page in enumerate(reader.pages):
        strip_text_from_page(page, reader)

        if idx == 0:
            overlay = make_overlay_page(page.mediabox.width, page.mediabox.height)
            page.merge_page(overlay)

        writer.add_page(page)

    with OUTPUT_PDF.open("wb") as f:
        writer.write(f)

    print(f"Created: {OUTPUT_PDF.resolve()}")


if __name__ == "__main__":
    main()
