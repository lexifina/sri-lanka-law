# Sri Lanka: law history in git

The law of Sri Lanka as a git repository: one file per provision, one commit per version on the day it took effect, and the law that made each change as the commit's author. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `lk/`.

**What is in it now**

- The Constitution of the Democratic Socialist Republic of Sri Lanka (`constitution/`), 2 versions: the Parliament's consolidated edition as amended to the Twenty First Amendment (31 October 2022), then the Twenty Second Amendment (Articles 107 and 137, certified 25 September 2026).
- 11 Acts of Parliament as enacted (2000 to 2024), 1,218 files: one folder per Act, named by its number and year (`act-2007-007/` is the Companies Act, No. 07 of 2007). The table at the end lists them.

**Sources.** Both come from the Parliament of Sri Lanka (parliament.lk). The Constitution is the Parliament's consolidated English edition; its first version is credited to the publisher, because earlier editions are not built, and the second replays the Twenty Second Amendment, whose words match the Act exactly. Each Act is the English text as printed by the Department of Government Printing and published by Parliament in its Acts listing. The Sinhala text of an Act prevails over the English and Tamil texts.

**What it does not show.** Acts are as enacted: later amending Acts are their own folders, and their changes are not replayed into the Acts they amend, because no official consolidated text is published. Acts printed before about 2000 are scans without a text layer and are not built yet, nor are the Penal Code, the Civil Procedure Code and the other pre-1978 enactments, which Parliament lists only as revised-edition chapters. Earlier amendments of the Constitution (the 1st to the 21st) are not separate commits.

**How it was checked.** Each Act is read from its PDF text layer. Every printed word from the long title to the end of the Act is in a file (checked letter for letter), except the running heads, page numbers, printer's codes, the certificate line and the Part and Chapter headings printed above sections; each section's marginal note is its file's first line. An Act whose sections are not numbered 1, 2, 3 and so on without a gap is left out. For the Constitution, all 267 units of the first version were compared word by word with an independent text extraction of the edition's PDF.

## Dates

Each commit is dated at noon, Asia/Colombo. A Bill becomes law when the Speaker's certificate is endorsed on it (Article 80(1) of the Constitution), so each Act is dated by the day of the certificate printed on it ("[Certified on ...]"). Where an Act, or part of it, comes into operation later, on a day a Minister appoints by Order, that later day is not shown.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist. The committer is Lexifina.

This is a research aid, not an official version and not legal advice. For anything that matters, read the original.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

See [REPRODUCE.md](REPRODUCE.md).

## Acts of Parliament

| Folder | Act | Certified |
| --- | --- | --- |
| `act-2000-038/` | Inland Revenue Act, No. 38 of 2000 | 2000-08-03 |
| `act-2004-010/` | Inland Revenue (Regulation of Amnesty) Act, No. 10 of 2004 | 2004-10-20 |
| `act-2004-013/` | Value Added Tax (Amendment) Act, No. 13 of 2004 | 2004-11-18 |
| `act-2006-010/` | Inland Revenue Act, No. 10 of 2006 | 2006-03-31 |
| `act-2007-007/` | Companies Act, No. 07 of 2007 | 2007-03-20 |
| `act-2010-012/` | National Institute of Labour Studies Act, No. 12 of 2010 | 2010-10-06 |
| `act-2013-017/` | Value Added Tax (Amendment) Act, No. 17 of 2013 | 2013-04-24 |
| `act-2017-024/` | Inland Revenue Act, No. 24 of 2017 | 2017-10-24 |
| `act-2022-009/` | Personal Data Protection Act, No. 9 of 2022 | 2022-03-19 |
| `act-2023-009/` | Anti-Corruption Act, No. 9 of 2023 | 2023-08-08 |
| `act-2024-009/` | Online Safety Act, No. 9 of 2024 | 2024-02-01 |
