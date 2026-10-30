# Sri Lanka: law history in git

The Constitution of Sri Lanka as a git repository: one file per provision, one commit per version on the day it took effect, and the law that made each change as the commit's author. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `lk/`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | The Constitution of the Democratic Socialist Republic of Sri Lanka | 2 | The Parliament's consolidated edition as amended to the Twenty First Amendment (31 October 2022), then the Twenty Second Amendment (Articles 107 and 137, certified 25 September 2026) |

**Source.** The Parliament of Sri Lanka publishes consolidated editions of the Constitution as PDFs with a text layer, and each Amendment Act. The first version is the edition as amended up to the Twenty First Amendment; it is credited to the publisher, because earlier editions are not built. The second version replays the Twenty Second Amendment onto Articles 107 and 137, and its words match the Act exactly. The English text is unofficial; the Sinhala and Tamil texts prevail.

**What it does not show.** Earlier amendments (the 1st to the 21st) are not separate commits. The transitional provisions of the Twenty First Amendment that Parliament prints in the consolidated edition are not built. Ordinary statutes, including the Penal Code and the Personal Data Protection Act, are not built.

**How it was checked.** All 267 units of the first version were compared word by word with an independent text extraction of the edition's PDF; about 35 units were corrected for lost paragraph numbers, line-end hyphens, headings joined to the previous unit and text cut at page breaks. The oath wording (Article 63 and the Fourth and Seventh Schedules) was read again against the PDF. Articles 5 and 8 end without a full stop in the source and are kept so.

## Dates

Each commit is dated at noon, Asia/Colombo. A Bill becomes law when the Speaker's certificate is endorsed on it (Article 80(1)), so the Twenty Second Amendment is dated 25 September 2026.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist. The committer is Lexifina.

This is a research aid, not an official version and not legal advice. For anything that matters, read the original.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

See [REPRODUCE.md](REPRODUCE.md).
