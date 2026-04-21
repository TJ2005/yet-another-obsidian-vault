# Obsidian Rewrite Instruction (Session Standard)

## 1) Analysis of your current writing style

Your notes follow a recognizable pattern that we will preserve while improving structure and readability:

1. **Consistent frontmatter shell** with keys like `Title`, `Status`, `marker`, `tags`, `Date`, `Time`.
2. **Topic-first headings** (`# Title`, then `##`/`###`) and mostly bullet-driven content.
3. **Mixed depth**: some notes are skeletal outlines, while others are detailed technical writeups with tables and commands.
4. **Closing section pattern**: `# References` and `###### Information` with date/time metadata.
5. **Current gaps to fix in rewrites**: inconsistent grammar/spelling, uneven capitalization, weak cross-linking, and almost no callouts.

## 2) Rewrite goals for every note

For each note rewrite, keep your voice and domain intent, but normalize formatting to Obsidian-native standards:

1. Preserve original meaning; improve clarity and flow.
2. Keep or improve frontmatter, but use valid YAML values.
3. Add contextual **wikilinks** to related notes.
4. Add relevant **callouts** for definitions, warnings, tips, tools, and key takeaways.
5. Convert formulas/technical expressions to proper **MathJax/LaTeX**.
6. Keep `# References` at the end, plus clean metadata.

## 3) Obsidian syntax rules we will use

### Internal links (preferred)

```md
[[Note Name]]
[[Note Name#Heading]]
[[Note Name#^block-id]]
[[Note Name|Custom display text]]
```

### Embeds

```md
![[Note Name]]
![[image.png|300]]
```

### Callouts

```md
> [!note] Title
> Content

> [!tip] Useful shortcut
> Content

> [!warning]- Risk
> Collapsed by default
```

Primary callout types to use: `note`, `tip`, `info`, `warning`, `success`, `question`, `example`, `quote`.

### MathJax / LaTeX

Inline math:

```md
Latency is modeled as $T = \frac{d}{v}$.
```

Block math:

```md
$$
\text{Risk} = \text{Likelihood} \times \text{Impact}
$$
```

### Lists, tasks, and tables

```md
- bullet
  - nested bullet
- [ ] task
- [x] done
```

```md
| Item | Use |
| --- | --- |
| Nmap | Recon |
```

## 4) Standard rewrite template

```md
---
Title: "..."
Status: ...
marker:
tags:
  - ...
Date: "YYYY.MM.DD"
Time: "HH:MM"
---
# <Note Title>

> [!abstract] Summary
> 2-4 lines describing the note.

## Core Concepts
...

## Tools / Methods
...

## Key Formulae
Inline: $...$

$$
...
$$

## Related Notes
- [[...]]
- [[...]]

# References
...

###### Information
- date: YYYY.MM.DD
- time: HH:MM
```

## 5) Classification schema for this vault

Use one primary category tag (plus optional secondary tags):

1. `#domain/cybersecurity`
2. `#domain/networking`
3. `#domain/reverse-engineering`
4. `#domain/digital-forensics`
5. `#domain/supply-chain`
6. `#domain/project-management`
7. `#status/unfinished` (when applicable)

## 6) Rewrite quality checklist (applied to each note)

1. Title and headings cleaned.
2. Grammar/spelling corrected.
3. At least 2 relevant internal links added where possible.
4. At least 1 meaningful callout added.
5. LaTeX/math formatting corrected (if formulas exist).
6. Metadata and references section preserved and normalized.

