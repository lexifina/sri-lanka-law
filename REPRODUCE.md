# How this repository was made (Sri Lanka)

This file is written by the build on 2026-11-02, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Parliament of Sri Lanka | <https://www.parliament.lk/en/constitution/main> | 2026-10-28 | Government publication; no licence stated |
| Parliament of Sri Lanka: Acts listing and English Act PDFs | <https://www.parliament.lk/en/business-of-parliament/acts-listing> | 2026-11-02 | No licence stated on parliament.lk. Intellectual Property Act, No. 36 of 2003, section 8: no copyright protection for official texts of a legislative, administrative or legal nature. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | The Constitution of the Democratic Socialist Republic of Sri Lanka | 2 | 2022-10-31 to 2026-09-25 |
| `act-2000-038` | Inland Revenue Act, No. 38 of 2000 | 1 | 2000-08-03 to 2000-08-03 |
| `act-2004-010` | Inland Revenue (Regulation of Amnesty) Act, No. 10 of 2004 | 1 | 2004-10-20 to 2004-10-20 |
| `act-2004-013` | Value Added Tax (Amendment) Act, No. 13 of 2004 | 1 | 2004-11-18 to 2004-11-18 |
| `act-2006-010` | Inland Revenue Act, No. 10 of 2006 | 1 | 2006-03-31 to 2006-03-31 |
| `act-2007-007` | Companies Act, No. 07 of 2007 | 1 | 2007-03-20 to 2007-03-20 |
| `act-2010-012` | National Institute of Labour Studies Act, No. 12 of 2010 | 1 | 2010-10-06 to 2010-10-06 |
| `act-2013-017` | Value Added Tax (Amendment) Act, No. 17 of 2013 | 1 | 2013-04-24 to 2013-04-24 |
| `act-2017-024` | Inland Revenue Act, No. 24 of 2017 | 1 | 2017-10-24 to 2017-10-24 |
| `act-2022-009` | Personal Data Protection Act, No. 9 of 2022 | 1 | 2022-03-19 to 2022-03-19 |
| `act-2023-009` | Anti-Corruption Act, No. 9 of 2023 | 1 | 2023-08-08 to 2023-08-08 |
| `act-2024-009` | Online Safety Act, No. 9 of 2024 | 1 | 2024-02-01 to 2024-02-01 |

The build made 13 commits:

| Commits | Kind |
| ---: | --- |
| 12 | first version of an act |
| 1 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-11-02.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 12 laws in the record.
- 25 tags.

## Dates

Each commit is dated at noon (Asia/Colombo) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Constitution Art. 80(1): a Bill becomes law when the Speaker's certificate is endorsed on it, unless the Act provides otherwise https://www.parliament.lk/files/pdf/constitution/constitution-upto-21st.pdf

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `aa66f221e8181be8f767a567caae5f78ef35786e63a4f82cf6eacce4ddc36a1e` (2831546 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Built the official English text; the Sinhala and Tamil texts prevail (Constitution Art. 23 and each Act).
- Version 1 is the consolidated 21st-Amendment edition, credited to the publisher as oldest version available.
- The Twenty Second Amendment is dated by its Speaker certificate, 25 September 2026 (Art. 80(1)), and replayed by code onto Art. 107(5) and Art. 137.
- Marginal notes, running headers, footnotes and editorial brackets are dropped; repealed-article stubs are omitted.
- Acts of Parliament (parts 30-acts-*): each Act is one version, the Act as certified, dated by the Speaker's certificate printed on it ("[Certified on ...]"): under Article 80(1) of the Constitution a Bill becomes law when the certificate is endorsed on it. Where an Act brings itself or some of its provisions into operation later (an appointed day, a Minister's Order), that later day is not modelled: the version is dated by the certificate.
- Acts of Parliament: amending Acts are their own acts; their amendments are not replayed into the principal Acts, which are kept as enacted (the Parliament publishes no consolidated text).
- Acts of Parliament: read from the PDF text layer by the shared reader Lexifina's code: one file per section (its marginal note as the heading), the long title, preamble and enacting words as "preamble", and each Schedule as one file; running heads, page numbers, the certificate line and printer's codes are left out; every other printed word from the long title to the end of the Act is in a file (checked letter for letter), and an Act whose sections are not numbered 1..N without a gap is left out.
- Acts of Parliament: a line-end hyphen is dropped when the same Act prints the joined word without it elsewhere, and kept otherwise.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none at data-build time; parsers written by Claude Code (claude-opus-5-5); no model wrote legal text
- Claude Code (Claude Opus 5.5, claude-opus-5-5) wrote the reader and this driver. No model wrote, summarised or transformed legal text: the reader is deterministic code reading the PDF text layer.
