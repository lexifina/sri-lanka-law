"""Sri Lanka: build corpus.json from the cache only (no network).

Version 1: Parliament's consolidated English edition "as amended up to 31st October 2022"
(21st Amendment), credited to the publisher as the oldest version available.
Version 2: the Twenty Second Amendment (certified 2026-09-25) replayed onto Articles 107 and 137.
"""
import hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import constitution as C

B = 'https://www.parliament.lk'
ED21 = B + '/files/pdf/constitution/constitution-upto-21st.pdf'
A22 = B + '/uploads/acts/gbills/english/6433.pdf'


def cpath(u):
    return os.path.join(HERE, '.cache', hashlib.sha256(u.encode()).hexdigest())


def sha(u):
    return hashlib.sha256(open(cpath(u), 'rb').read()).hexdigest()


def units_from(parsed):
    out = {}
    for k, v in parsed.items():
        lines = [l for l in v['lines'] if l.strip()]
        if not lines or (len(lines) == 1 and re.fullmatch(r'\W*Repealed\W*', lines[0])):
            continue
        out[k] = {'label': v['label'], 'kind': 'art' if k.startswith('art-') else k.split('-')[0],
                  'text': '# %s\n' % v['label'] + '\n'.join(lines) + '\n'}
    return out


def main():
    parsed, _ = C.parse_edition(cpath(ED21), '21')
    u21 = units_from(parsed)
    # Twenty Second Amendment, ss. 2 and 3 (text of the Act, parliament.lk 6433.pdf)
    changes = {}
    a107 = u21['art-107']['text'].split('\n')
    i5 = [i for i, l in enumerate(a107) if l.startswith('(5) The age of retirement')]
    if len(i5) == 1:
        new5 = ['(5) The age of retirement of Judges of the Supreme Court shall be sixty-seven years and of Judges of the Court of Appeal shall be sixty-five years:',
                'Provided however, the date of retirement of the Chief Justice shall be either the date on which the Chief Justice attains the age of sixty-seven years or the date on which a period of six years is completed from the date of appointment as the Chief Justice, whichever occurs earlier:',
                'Provided further, that the term limit of six years set out in the first proviso shall not apply to any person holding the office of Chief Justice as at the date of coming into operation of this Act.']
        a107 = a107[:i5[0]] + new5 + a107[i5[0] + 1:]
        changes['art-107'] = dict(u21['art-107'], text='\n'.join(a107))
    t137 = u21['art-137']['text']
    if 'not more than nineteen other Judges' in t137:
        changes['art-137'] = dict(u21['art-137'], text=t137.replace('not more than nineteen other Judges', 'not more than twenty four other Judges'))
    corpus = {
        'country': {
            'code': 'LK', 'name': 'Sri Lanka', 'slug': 'sri-lanka', 'lang': 'en', 'tz': 'Asia/Colombo',
            'future_branch': 'future',
            'publisher': {'name': 'Parliament of Sri Lanka', 'email': 'publisher@parliament.lk.invalid'},
            'default_in_force_rule': {'text': 'Constitution Art. 80(1): a Bill becomes law when the Speaker\'s certificate is endorsed on it, unless the Act provides otherwise',
                                      'source': B + '/files/pdf/constitution/constitution-upto-21st.pdf'},
            'licence_note': 'Text of the Constitution of the Democratic Socialist Republic of Sri Lanka, unofficial consolidated English edition published by the Parliament Secretariat (parliament.lk). The Sinhala and Tamil texts prevail.',
        },
        'sources': [{'name': 'Parliament of Sri Lanka', 'url': B + '/en/constitution/main', 'retrieved': '2026-10-28',
                     'requests': sum(1 for _ in open(os.path.join(HERE, '.cache', 'requests.jsonl'), encoding='utf-8')),
                     'licence': 'Government publication; no licence stated', 'notes': 'Consolidated editions (up to the 17th-21st Amendments) and Amendment Acts as text-layer PDFs'}],
        'laws': {
            'amendment-22': {'label': 'Twenty Second Amendment to the Constitution', 'title': 'Twenty Second Amendment to the Constitution',
                             'kind': 'law', 'enacted': '2026-09-25', 'published': '2026-09-25', 'url': A22,
                             'temporary_until': None, 'restores': None, 'note': None},
        },
        'acts': [{
            'slug': 'constitution', 'short': 'Constitution',
            'title': 'The Constitution of the Democratic Socialist Republic of Sri Lanka',
            'url': B + '/en/constitution/main', 'first_law': None,
            'earlier_laws': [],
            'versions': [
                {'from': '2022-10-31', 'source_url': ED21, 'sha256': sha(ED21), 'units': u21, 'credits': {},
                 'note': 'Oldest version available: Parliament consolidated edition as amended up to 31 October 2022 (Revised Edition 2023).'},
                {'from': '2026-09-25', 'source_url': A22, 'sha256': sha(A22), 'changes': changes,
                 'credits': {k: ['amendment-22'] for k in changes}},
            ],
        }],
        'applies': [],
        'decisions': [
            'Built the official English text; the Sinhala and Tamil texts prevail (Constitution Art. 23 and each Act).',
            'Version 1 is the consolidated 21st-Amendment edition, credited to the publisher as oldest version available; earlier dated editions are cached but not yet built.',
            'The Twenty Second Amendment is dated by its Speaker certificate, 25 September 2026 (Art. 80(1)), and replayed by code onto Art. 107(5) and Art. 137.',
            'Marginal notes, running headers, footnotes and editorial brackets are dropped; repealed-article stubs are omitted.',
        ],
        'ai_use': ['none at data-build time; parsers written by Claude Code (claude-opus-5-5); no model wrote legal text'],
    }
    tmp = os.path.join(HERE, 'corpus.json.tmp')
    with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(corpus, f, ensure_ascii=False, indent=1, sort_keys=True)
    os.replace(tmp, os.path.join(HERE, 'corpus.json'))
    print(len(u21), 'units;', 'replayed:', sorted(changes))


if __name__ == '__main__':
    main()
