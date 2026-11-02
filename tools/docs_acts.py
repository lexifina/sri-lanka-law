"""Write repo/README.md, repo/LICENSE and repo/jurisdiction.json from corpus.json and the published Acts parts.

    python -X utf8 docs_acts.py
Only parts with a .PUBLISH file are described (they are what main holds).
"""
import json
from pathlib import Path

H = Path(__file__).resolve().parent
parts = sorted(p for p in (H / 'corpus.d').glob('30-acts-*.json') if p.with_suffix('.PUBLISH').exists())
acts = [a for p in parts for a in json.loads(p.read_text('utf-8'))['acts']]
acts.sort(key=lambda a: (a['versions'][0]['from'], a['slug']))
n = len(acts)
years = sorted({a['versions'][0]['from'][:4] for a in acts})
span = f'{years[0]} to {years[-1]}' if years else ''
units = sum(len(a['versions'][0]['units']) for a in acts)

rows = '\n'.join(f"| `{a['slug']}/` | {a['title']} | {a['versions'][0]['from']} |" for a in acts)
README = f"""# Sri Lanka: law history in git

The law of Sri Lanka as a git repository: one file per provision, one commit per version on the day it took effect, and the law that made each change as the commit's author. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `lk/`.

**What is in it now**

- The Constitution of the Democratic Socialist Republic of Sri Lanka (`constitution/`), 2 versions: the Parliament's consolidated edition as amended to the Twenty First Amendment (31 October 2022), then the Twenty Second Amendment (Articles 107 and 137, certified 25 September 2026).
- {n} Acts of Parliament as enacted ({span}), {units:,} files: one folder per Act, named by its number and year (`act-2007-007/` is the Companies Act, No. 07 of 2007). The table at the end lists them.

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

See [REPRODUCE.md](REPRODUCE.md).

## Acts of Parliament

| Folder | Act | Certified |
| --- | --- | --- |
{rows}
"""
LICENSE = """The legal texts are the Constitution of the Democratic Socialist Republic of Sri Lanka (unofficial English
consolidated edition), the Twenty Second Amendment to the Constitution, and Acts of the Parliament of Sri Lanka in
their English text as printed by the Department of Government Printing, all as published by the Parliament of
Sri Lanka (https://www.parliament.lk). The site states no licence. The Intellectual Property Act, No. 36 of 2003,
section 8, does not protect official texts of a legislative, administrative or legal nature. The texts are
reproduced without change to their wording.

Changes made by Lexifina: each version was converted to one Markdown file per provision, one paragraph per line;
line-end hyphenation and page furniture from the PDF were removed. The versions were arranged as git commits.
Lexifina does not claim the Parliament of Sri Lanka endorses this repository.

Lexifina's own contributions (the arrangement of the history, the commit messages, the tables and the
tools) are dedicated to the public domain under CC0 1.0 Universal:
https://creativecommons.org/publicdomain/zero/1.0/legalcode
"""
(H / 'repo' / 'README.md').write_text(README, 'utf-8', newline='\n')
(H / 'repo' / 'LICENSE').write_text(LICENSE, 'utf-8', newline='\n')
j = json.loads((H / 'repo' / 'jurisdiction.json').read_text('utf-8'))
j['build'] = (f'built: Constitution of Sri Lanka (267 units), 2 versions; {n} Acts of Parliament as enacted '
              f'({span}), {units} units, from the Parliament of Sri Lanka')
(H / 'repo' / 'jurisdiction.json').write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n', 'utf-8', newline='\n')
print(n, 'acts', units, 'units')
