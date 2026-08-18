---
name: parse-docs
description: Extract maximum content from teacher documents (PDF, PPTX/DOCX/XLSX, RTF, CSV, HTML, images) into Obsidian markdown notes with tables, speaker notes, embedded images, links, and OCR for scanned files. Use when the user asks to parse, read, extract, summarize or study from lecture slides, PDFs, PowerPoint/Word/Excel files, scanned documents, or any course material files they dropped into the vault or Downloads folder. Also use when files cannot be read directly (binary formats) or when the user mentions OCR.
---

# Parse Docs — maximum data extraction

Turn one (or many) files into a rich markdown note the agent can read, cite,
and embed into the user's vault. The script is the single entry point — never
reimplement extraction inline; always call it.

## Location

Script: `scripts/ingest.py` (same folder as this SKILL.md)
Output default: `Extracted/` at the vault root (create it if missing).
Note: `Extracted/` is gitignored — it is scratch space. Anything worth keeping
must be written into the vault as a proper note.

## When to use

- User hands over a `.pdf`, `.pptx`, `.docx`, `.xlsx`, `.rtf`, `.doc`, `.odt`,
  `.csv`, `.html`, or image (`.png`/`.jpg`/`.jpeg`/`.tiff`/`.webp`) — from
  anywhere (vault, Downloads, drag-drop, pasted path).
- User asks to "read my slides", "study this lecture", "make notes from this
  PDF", or references a file the model cannot read directly.
- A PDF renders blank / images-only (scanned): force OCR.

## Workflow

1. **Locate the file(s).** Check the vault and user-provided paths. If the user
   pasted a blob or the file is elsewhere, find it with glob/search first.
2. **Run the script** from the vault root (cwd = vault):

   ```bash
   uv run --script ".opencode/skills/parse-docs/ingest.py" <file-or-dir> [--out Extracted] [--ocr-all] [--lang eng]
   ```

   - Pass a directory to ingest every supported file inside it (non-recursive unless you add `--recursive`).
   - `--ocr-all`: OCR every PDF page even if it has a text layer (scanned copies).
   - `--lang`: tesseract language for OCR (default `eng`; e.g. `--lang eng+spa`).
   - Never pass more than ~5 large files per run; chunk directory ingests.
3. **Read the output.** Each file produces `<stem>.extracted.md` plus an
   `<stem>.extracted_assets/` folder next to it. Skim the markdown (or grep for
   key sections). Verify it actually contains the content — open the file if
   output looks thin.
4. **Use the content.** Summarize, make flashcards, create study notes, or
   link it into the user's notes with `![[<stem>.extracted]]`. Follow the
   user's existing note style (see existing markdown files in the vault root).
5. **Clean up** only if the user asks. Never delete assets — Obsidian notes
   reference them via `![[...]]` wikilinks.

## What the script extracts (max data per type)

| Type | Extracted |
| ---- | --------- |
| PDF | metadata, TOC/outline, per-page markdown (text + tables), all embedded images, external links, OCR for scanned pages |
| PPTX | per-slide title + all text, tables as markdown, charts (data dump), speaker notes, embedded images |
| DOCX | full text with heading structure, tables, embedded images, hyperlinks |
| XLSX | every sheet, all values + formulas, merged cells, cell comments, embedded images |
| RTF / .doc / .odt / HTML | full text via macOS `textutil` |
| CSV | markdown table |
| PNG/JPG/TIFF/WebP | OCR text via `tesseract` |
| .ppt / .xls (legacy) | NOT supported — tell the user to convert first (LibreOffice or Google Drive) |

## Edge cases

- **Password-protected PDF**: script reports it — ask the user for the password
  and rerun manually (`qpdf --password=... --decrypt file.pdf out.pdf` or
  Preview > export). Do not silently skip.
- **Scanned/no-text PDFs**: script auto-OCRs pages with no text. If the result
  is garbled, retry with `--lang` for the right language or `--ocr-all`.
- **Degenerate files** (1-slide deck, empty sheet): still emit the note with
  what exists — a stub beats nothing.
- **Huge files**: multi-hundred-page PDFs or image-heavy decks — the script
  prints progress to stderr; be patient, or run on a single file.
- **Assets**: images land in `<stem>.extracted_assets/` and are referenced
  with Obsidian wikilinks (`![[stem.extracted_assets/foo.png]]`) so they
  render in the vault. Do not move them after extraction.
- **Existing output**: the script overwrites `<stem>.extracted.md`. If the
  user has hand-edited a previous extraction, confirm before re-running on
  the same file (or pass a different `--out`).

## Failures

- If a file fails mid-way the script prints `ERR <file>: <reason>` and
  continues with the others. Tell the user which files failed and why.
- If `uv` / `tesseract` are missing, install via:
  `brew install uv tesseract` (tesseract langs: `brew install tesseract-lang`).