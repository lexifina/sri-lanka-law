# Sri Lanka: law history in git

The law of Sri Lanka as a git repository: one file per provision, one commit per version on the day it took effect, and the law that made each change as the commit's author. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `lk/`.

**What is in it now**

- The Constitution of the Democratic Socialist Republic of Sri Lanka (`constitution/`), 2 versions: the Parliament's consolidated edition as amended to the Twenty First Amendment (31 October 2022), then the Twenty Second Amendment (Articles 107 and 137, certified 25 September 2026).
- 302 Acts of Parliament as enacted (2000 to 2026), 8,306 files: one folder per Act, named by its number and year (`act-2007-007/` is the Companies Act, No. 07 of 2007). The table at the end lists them.

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
| `act-2000-025/` | Minimum Wages (Indian Labour) (Amendment) Act, No. 25 of 2000 | 2000-07-12 |
| `act-2000-034/` | Civil Procedure Code (Amendment) Act, No. 34 of 2000 | 2000-07-21 |
| `act-2000-038/` | Inland Revenue Act, No. 38 of 2000 | 2000-08-03 |
| `act-2000-042/` | Suppression of Unlawful Acts against the Safety of Maritime Navigation Act, No. 42 of 2000 | 2000-08-09 |
| `act-2001-008/` | Inland Revenue (Amendment) Act, No. 8 of 2001 | 2001-07-24 |
| `act-2002-003/` | Competent Authority (Powers and Functions) Act, No. 3 of 2002 | 2002-03-25 |
| `act-2002-004/` | Administrative Appeals Tribunal Act, No. 4 of 2002 | 2002-03-25 |
| `act-2002-008/` | Save the Nation Contribution (Abolition) Act, No. 8 of 2002 | 2002-06-19 |
| `act-2002-012/` | Penal Code (Amendment) Act, No. 12 of 2002 | 2002-07-17 |
| `act-2003-007/` | Value Added Tax (Amendment) Act No. 7 of 2003 | 2003-02-27 |
| `act-2003-008/` | Employment of Women, Young Persons and Children (Amendment) Act, No. 8 of 2003 | 2003-03-17 |
| `act-2003-011/` | Industrial Disputes (Amendment) Act, No. 11 of 2003 | 2003-03-20 |
| `act-2003-031/` | Inland Revenue (Special Provisions) (Amendment) Act, No. 31 of 2003 | 2003-10-22 |
| `act-2003-035/` | Grant of Citizenship to Persons of Indian Origin Act, No. 35 of 2003 | 2003-11-11 |
| `act-2003-044/` | Appropriation Act, No. 44 of 2003 | 2003-12-31 |
| `act-2004-010/` | Inland Revenue (Regulation of Amnesty) Act, No. 10 of 2004 | 2004-10-20 |
| `act-2004-012/` | Inland Revenue (Amendment) Act, No. 12 of 2004 | 2004-11-18 |
| `act-2004-013/` | Value Added Tax (Amendment) Act, No. 13 of 2004 | 2004-11-18 |
| `act-2004-015/` | Appropriation Act, No. 15 of 2004 | 2004-12-21 |
| `act-2005-004/` | Civil Procedure Code (Amendment) Act, No. 4 of 2005 | 2005-02-22 |
| `act-2005-010/` | Workmen's Compensation (Amendment) Act, No. 10 of 2005 | 2005-04-20 |
| `act-2005-023/` | Corporal Punishment (Repeal) Act, No. 23 of 2005 | 2005-08-02 |
| `act-2005-029/` | Evidence (Amendment) Act, No. 29 of 2005 | 2005-09-20 |
| `act-2005-030/` | Convention on Preventing and Combating Trafficking in Women and Children for Prostitution Act, No. 30 of 2005 | 2005-09-20 |
| `act-2005-032/` | Sri Lanka Accreditation Board for Conformity Assessment Act, No. 32 of 2005 | 2005-09-23 |
| `act-2005-036/` | Budgetary Relief Allowance of Workers Act, No. 36 of 2005 | 2005-10-18 |
| `act-2006-003/` | Merchant Shipping (Change of Designation) Act, No. 3 of 2006 | 2006-02-13 |
| `act-2006-004/` | Geneva Conventions Act, No. 4 of 2006 | 2006-02-26 |
| `act-2006-010/` | Inland Revenue Act, No. 10 of 2006 | 2006-03-31 |
| `act-2006-019/` | Electronic Transactions Act, No. 19 of 2006 | 2006-05-19 |
| `act-2006-021/` | Private Medical Institutions (Registration) Act, No. 21 of 2006 | 2006-07-14 |
| `act-2006-024/` | Employment of Women, Young Persons and Children (Amendment) Act, No. 24 of 2006 | 2006-08-21 |
| `act-2006-027/` | National Authority on Tobacco and Alcohol Act, No. 27 of 2006 | 2006-08-29 |
| `act-2006-028/` | National Insurance Trust Fund Act, No. 28 of 2006 | 2006-08-29 |
| `act-2006-029/` | Social Security Benefit Scheme for Media Personnel Act, No. 29 of 2006 | 2006-09-05 |
| `act-2006-030/` | Payment Devices Frauds Act, No. 30 of 2006 | 2006-09-12 |
| `act-2006-047/` | Appropriation Act, No. 47 of 2006 | 2006-12-15 |
| `act-2006-049/` | Value Added Tax (Amendment) Act, No. 49 of 2006 | 2006-12-15 |
| `act-2006-051/` | Regional Infrastructure Development Levy Act, No. 51 of 2006 | 2006-12-15 |
| `act-2007-007/` | Companies Act, No. 07 of 2007 | 2007-03-20 |
| `act-2007-010/` | Inland Revenue (Amendment) Act, No. 10 of 2007 | 2007-03-30 |
| `act-2007-011/` | Prevention of Mosquito Breeding Act, No. 11 of 2007 | 2007-04-11 |
| `act-2007-014/` | Value Added Tax (Amendment) Act, No. 14 of 2007 | 2007-04-12 |
| `act-2007-024/` | Computer Crime Act, No.24 of 2007 | 2007-07-09 |
| `act-2007-025/` | Ceylon Hotels Corporation (Repeal) Act, No. 25 of 2007 | 2007-07-12 |
| `act-2007-026/` | National Institute of Language Education and Training Act, No. 26 of 2007 | 2007-07-13 |
| `act-2007-031/` | Judicature (Amendment) Act, No. 31 of 2007 | 2007-08-08 |
| `act-2007-035/` | Sri Lanka Sustainable Energy Authority Act, No. 35 of 2007 | 2007-09-18 |
| `act-2007-042/` | Code of Criminal Procedure (Special Provisions) Act, No. 42 of 2007 | 2007-10-09 |
| `act-2007-048/` | Special Commodity Levy Act, No. 48 of 2007 | 2007-10-15 |
| `act-2007-051/` | Gampaha Wickramarachchi Ayurveda Teaching Hospital (Transfer) Act, No. 51 of 2007 | 2007-10-23 |
| `act-2007-054/` | Drug Dependant Persons (Treatment and Rehabilitation) Act, No. 54 of 2007 | 2007-11-13 |
| `act-2007-056/` | International Covenant on Civil and Political Rights (ICCPR) Act, No. 56 of 2007 | 2007-11-16 |
| `act-2007-058/` | Chemical Weapons Convention Act, No.58 of 2007 | 2007-11-20 |
| `act-2008-009/` | Inland Revenue (Amendment) Act, No. 9 of 2008 | 2008-02-29 |
| `act-2008-014/` | Strategic Development Projects Act, No. 14 of 2008 | 2008-02-29 |
| `act-2008-015/` | Value Added Tax (Amendment) Act, No. 15 of 2008 | 2008-02-29 |
| `act-2008-026/` | Environment Conservation Levy Act, No. 26 of 2008 | 2008-06-06 |
| `act-2009-009/` | Nation Building Tax Act, No. 9 of 2009 | 2009-03-11 |
| `act-2009-012/` | Sri Lanka Institute of Textile and Apparel Act, No. 12 of 2009 | 2009-03-20 |
| `act-2009-015/` | Value Added Tax (Amendment) Act, No. 15 of 2009 | 2009-03-31 |
| `act-2009-019/` | Inland Revenue (Amendment) Act, No. 19 of 2009 | 2009-03-31 |
| `act-2009-020/` | Sri Lanka Electricity Act, No. 20 of 2009 | 2009-04-08 |
| `act-2009-023/` | Institute of Certified Management Accountants of Sri Lanka Act, No. 23 of 2009 | 2009-04-20 |
| `act-2009-033/` | Sri Lanka Institute of Landscape Architects Act, No. 33 of 2009 | 2009-06-12 |
| `act-2009-035/` | Chief of Defence Staff Act, No. 35 of 2009 | 2009-07-09 |
| `act-2009-041/` | Department of Coast Guard Act, No. 41 of 2009 | 2009-08-06 |
| `act-2009-044/` | Ambuluwawa Dissanayake Mudiyanselage Jayaratne Religious Centre and Bio-diversity Complex Trust Fund Act, No. 44 of 2009 | 2009-08-21 |
| `act-2009-049/` | Secured Transactions Act, No. 49 of 2009 | 2009-09-25 |
| `act-2009-055/` | Employees' Provident Fund (Special Provisions) (Amendment) Act, No. 55 of 2009 | 2009-09-30 |
| `act-2009-056/` | Sri Lanka Bureau of Foreign Employment (Amendment) Act, No. 56 of 2009 | 2009-10-01 |
| `act-2010-007/` | Appropriation Act, No. 7 of 2010 | 2010-07-13 |
| `act-2010-010/` | Judicature (Amendment) Act, No. 10 of 2010 | 2010-08-18 |
| `act-2010-011/` | Civil Procedure Code (Amendment) Act, No. 11 of 2010 | 2010-10-05 |
| `act-2010-012/` | National Institute of Labour Studies Act, No. 12 of 2010 | 2010-10-06 |
| `act-2010-014/` | Civil Aviation Act, No. 14 of 2010 | 2010-11-03 |
| `act-2010-015/` | Secretary to the Treasury (Nomination of Representative) Act, No. 15 of 2010 | 2010-12-07 |
| `act-2010-017/` | Casino Business (Regulation) Act, No. 17 of 2010 | 2010-12-07 |
| `act-2010-018/` | Public Enterprises Reform Commission of Sri Lanka (Repeal) Act, No. 18 of 2010 | 2010-12-07 |
| `act-2010-019/` | Registration of Deaths (Temporary Provisions) Act, No. 19 of 2010 | 2010-12-10 |
| `act-2010-020/` | Appropriation Act, No. 20 of 2010 | 2010-12-10 |
| `act-2011-009/` | Value Added Tax (Amendment) Act, No. 9 of 2011 | 2011-03-31 |
| `act-2011-013/` | Provincial Councils (Transfer of Stamp Duty) Act, No. 13 of 2011 | 2011-03-31 |
| `act-2011-014/` | Debits Tax (Repeal) Act, No. 14 of 2011 | 2011-03-31 |
| `act-2011-016/` | Regional Infrastructure Development Levy (Repeal) Act, No. 16 of 2011 | 2011-03-31 |
| `act-2011-018/` | Ports and Airports Development Levy Act, No. 18 of 2011 | 2011-03-31 |
| `act-2011-021/` | Telecommunication Levy Act, No. 21 of 2011 | 2011-03-31 |
| `act-2011-022/` | Inland Revenue (Amendment) Act, No. 22 of 2011 | 2011-03-31 |
| `act-2011-023/` | Tax Appeals Commission Act, No. 23 of 2011 | 2011-03-31 |
| `act-2011-039/` | Industrial Disputes (Amendment) Act, No. 39 of 2011 | 2011-10-06 |
| `act-2011-042/` | Finance Business Act, No. 42 of 2011 | 2011-11-09 |
| `act-2011-043/` | Revival of Underperforming Enterprises or Underutilized Assets Act, No. 43 of 2011 | 2011-11-11 |
| `act-2011-044/` | National Police Academy Act, No. 44 of 2011 | 2011-11-21 |
| `act-2011-052/` | Appropriation Act, No. 52 of 2011 | 2011-12-21 |
| `act-2012-002/` | Employees' Provident Fund (Amendment) Act, No. 2 of 2012 | 2012-02-09 |
| `act-2012-007/` | Value Added Tax (Amendment) Act, No. 7 of 2012 | 2012-03-30 |
| `act-2012-008/` | Inland Revenue (Amendment) Act, No. 8 of 2012 | 2012-03-30 |
| `act-2012-023/` | Appropriation Act, No. 23 of 2012 | 2012-12-08 |
| `act-2013-001/` | Divineguma Act, No. 1 of 2013 | 2013-01-11 |
| `act-2013-002/` | Code of Criminal Procedure (Special Provisions) Act, No. 2 of 2013 | 2013-02-06 |
| `act-2013-012/` | Finance Act, No.12 of 2013 | 2013-04-23 |
| `act-2013-017/` | Value Added Tax (Amendment) Act, No. 17 of 2013 | 2013-04-24 |
| `act-2013-018/` | Inland Revenue (Amendment) Act, No. 18 of 2013 | 2013-04-24 |
| `act-2013-028/` | Parliamentary Scholarship Board (Repeal) Act, No. 28 of 2013 | 2013-07-08 |
| `act-2013-033/` | Convention against Doping in Sport Act, No. 33 of 2013 | 2013-11-11 |
| `act-2013-036/` | Appropriation Act, No. 36 of 2013 | 2013-12-20 |
| `act-2014-007/` | Value Added Tax (Amendment) Act, No. 7 of 2014 | 2014-04-24 |
| `act-2014-008/` | Inland Revenue (Amendment) Act, No. 8 of 2014 | 2014-04-24 |
| `act-2014-013/` | Companies (Amendment) Act, No. 13 of 2014 | 2014-04-24 |
| `act-2014-018/` | National Enterprise Development Authority (Amendment)Act, No. 18 of 2014 | 2014-06-04 |
| `act-2014-031/` | Ocean University Of Sri Lanka Act, No. 31 of 2014 | 2014-09-07 |
| `act-2014-033/` | Construction Industry Development Act, No. 33 of 2014 | 2014-10-16 |
| `act-2014-038/` | Land (Restrictions on Alienation) Act, No. 38 of 2014 | 2014-10-29 |
| `act-2014-039/` | DFCC Bank (Repeal and Consequential Provisions) Act, No. 39 of 2014 | 2014-11-01 |
| `act-2014-040/` | Sri Lanka Atomic Energy Act, No. 40 of 2014 | 2014-11-04 |
| `act-2014-041/` | Appropriation Act, No. 41 of 2014 | 2014-11-24 |
| `act-2015-004/` | Assistance to and Protection of Victims of Crime and Witnesses Act, No. 4 of 2015 | 2015-03-07 |
| `act-2015-005/` | National Medicines Regulatory Authority Act, No. 5 of 2015 | 2015-03-19 |
| `act-2015-008/` | National Authority on Teacher Education (Repeal) Act, No. 8 of 2015 | 2015-06-03 |
| `act-2015-009/` | Inland Revenue (Amendment) Act, No. 9 of 2015 | 2015-10-30 |
| `act-2015-010/` | Finance Act, No. 10 of 2015 | 2015-10-30 |
| `act-2015-011/` | Value Added Tax (Amendment) Act, No. 11 of 2015 | 2015-10-30 |
| `act-2015-016/` | Appropriation Act, No. 16 of 2015 | 2015-12-19 |
| `act-2016-003/` | National Minimum Wage of Workers Act, No. 3 of 2016 | 2016-03-23 |
| `act-2016-004/` | Budgetary Relief Allowance of Workers Act, No. 4 of 2016 | 2016-03-23 |
| `act-2016-006/` | Microfinance Act, No. 6 of 2016 | 2016-05-20 |
| `act-2016-007/` | Asian Infrastructure Investment Bank Agreement (Ratification) Act, No. 7 of 2016 | 2016-05-30 |
| `act-2016-010/` | Homoeopathy Act, No. 10 of 2016 | 2016-07-27 |
| `act-2016-011/` | National Research Council of Sri Lanka Act, No. 11 of 2016 | 2016-07-27 |
| `act-2016-012/` | Right to Information Act, No. 12 of 2016 | 2016-08-04 |
| `act-2016-014/` | Office on Missing Persons (Establishment, Administration and Discharge of Functions) Act, No. 14 of 2016 | 2016-08-23 |
| `act-2016-018/` | Code of Criminal Procedure (Amendment) Act, No. 18 of 2016 | 2016-10-17 |
| `act-2016-020/` | Value Added Tax (Amendment) Act, No. 20 of 2016 | 2016-11-01 |
| `act-2016-024/` | Appropriation Act, No. 24 of 2016 | 2016-12-10 |
| `act-2017-004/` | Engineering Council, Sri Lanka Act, No. 4 of 2017 | 2017-03-09 |
| `act-2017-005/` | Revocation of Irrevocable Deeds of Gift on the ground of Gross Ingratitude Act, No. 5 of 2017 | 2017-04-04 |
| `act-2017-008/` | Civil Procedure Code (Amendment) Act, No. 8 of 2017 | 2017-06-07 |
| `act-2017-012/` | Foreign Exchange Act, No. 12 of 2017 | 2017-07-28 |
| `act-2017-015/` | Ceylon German Technical Training Institute Act, No. 15 of 2017 | 2017-08-24 |
| `act-2017-019/` | Sri Lanka Sustainable Development Act, No. 19 of 2017 | 2017-10-03 |
| `act-2017-024/` | Inland Revenue Act, No. 24 of 2017 | 2017-10-24 |
| `act-2017-026/` | Judicature (Amendment) Act, No. 26 of 2017 | 2017-11-17 |
| `act-2017-030/` | Appropriation Act, No. 30 of 2017 | 2017-12-09 |
| `act-2018-002/` | Anti-Dumping and Countervailing Duties Act, No. 2 of 2018 | 2018-03-19 |
| `act-2018-003/` | Safeguard Measures Act, No. 3 of 2018 | 2018-03-19 |
| `act-2018-005/` | International Convention for the Protection of All Persons from Enforced Disappearance Act, No. 5 of 2018 | 2018-03-21 |
| `act-2018-007/` | Intellectual Property (Amendment) Act, No. 7 of 2018 | 2018-03-28 |
| `act-2018-008/` | Active Liability Management Act, No. 8 of 2018 | 2018-03-28 |
| `act-2018-009/` | Judicature (Amendment) Act, No. 9 of 2018 | 2018-05-15 |
| `act-2018-010/` | Penal Code (Amendment) Act, No. 10 of 2018 | 2018-05-21 |
| `act-2018-011/` | Code of Criminal Procedure (Amendment) Act, No. 11 of 2018 | 2018-05-21 |
| `act-2018-014/` | Shop and Office Employees (Regulation of Employment and Remuneration) (Amendment) Act, No. 14 of 2018 | 2018-06-18 |
| `act-2018-018/` | 1990 Suwaseriya Foundation Act, No. 18 of 2018 | 2018-07-04 |
| `act-2018-019/` | National Audit Act, No. 19 of 2018 | 2018-07-17 |
| `act-2018-025/` | Value Added Tax (Amendment) Act, No. 25 of 2018 | 2018-08-16 |
| `act-2018-027/` | Amaradeva Aesthetic and Research Centre Act, No. 27 of 2018 | 2018-09-03 |
| `act-2018-029/` | Carriage by Air Act, No. 29 of 2018 | 2018-09-28 |
| `act-2018-032/` | New Villages Development Authority for Plantation Region Act, No. 32 of 2018 | 2018-10-04 |
| `act-2018-034/` | Office for Reparations Act, No. 34 of 2018 | 2018-10-22 |
| `act-2018-035/` | Finance Act, No. 35 of 2018 | 2018-11-01 |
| `act-2019-002/` | Recovery of Damages for the Death of a Person Act, No. 2 of 2019 | 2019-01-17 |
| `act-2019-005/` | Judicature (Amendment) Act, No. 5 of 2019 | 2019-04-05 |
| `act-2019-006/` | Appropriation Act, No. 6 of 2019 | 2019-04-05 |
| `act-2019-012/` | Revival of Underperforming Enterprises or Underutilized Assets (Repeal) Act, No. 12 of 2019 | 2019-06-28 |
| `act-2019-013/` | Companies (Amendment) Act, No. 13 of 2019 | 2019-08-06 |
| `act-2019-019/` | Value Added Tax (Amendment) Act, No. 19 of 2019 | 2019-10-31 |
| `act-2019-021/` | Finance Act, No. 21 of 2019 | 2019-10-31 |
| `act-2019-022/` | National Innovation Agency Act, No. 22 of 2019 | 2019-11-15 |
| `act-2019-024/` | Prevention of Offences relating to Sports Act, No. 24 of 2019 | 2019-11-18 |
| `act-2020-006/` | Appropriation Act, No. 6 of 2020 | 2020-11-20 |
| `act-2020-007/` | Appropriation Act, No. 7 of 2020 | 2020-12-10 |
| `act-2021-001/` | Shop and Office Employees (Regulation of Employment and Remuneration) (Amendment) Act, No. 1 of 2021 | 2021-01-18 |
| `act-2021-002/` | Employment of Women, Young Persons and Children (Amendment) Act, No. 2 of 2021 | 2021-01-18 |
| `act-2021-003/` | Minimum Wages (Indian Labour) (Amendment) Act, No. 3 of 2021 | 2021-01-18 |
| `act-2021-005/` | Penal Code (Amendment) Act, No. 5 of 2021 | 2021-01-18 |
| `act-2021-008/` | Intellectual Property (Amendment) Act, No. 8 of 2021 | 2021-01-18 |
| `act-2021-010/` | Inland Revenue (Amendment) Act, No. 10 of 2021 | 2021-05-13 |
| `act-2021-011/` | Colombo Port City Economic Commission Act, No. 11 of 2021 | 2021-05-27 |
| `act-2021-014/` | Code of Criminal Procedure (Amendment) Act, No. 14 of 2021 | 2021-07-15 |
| `act-2021-017/` | Coronavirus Disease 2019 (COVID -19) (Temporary Provisions) Act, No. 17 of 2021 | 2021-08-23 |
| `act-2021-018/` | Finance Act, No. 18 of 2021 | 2021-09-15 |
| `act-2021-019/` | Securities and Exchange Commission of Sri Lanka Act, No. 19 of 2021 | 2021-09-21 |
| `act-2021-021/` | Petroleum Resources Act, No. 21 of 2021 | 2021-10-08 |
| `act-2021-023/` | Employees' Provident Fund (Amendment) Act, No. 23 of 2021 | 2021-10-13 |
| `act-2021-025/` | Penal Code (Amendment) Act, No. 25 of 2021 | 2021-10-26 |
| `act-2021-028/` | Minimum Retirement Age of Workers Act, No. 28 of 2021 | 2021-11-17 |
| `act-2021-030/` | Appropriation Act, No. 30 of 2021 | 2021-12-10 |
| `act-2022-002/` | Code of Criminal Procedure (Amendment) Act, No. 2 of 2022 | 2022-02-17 |
| `act-2022-003/` | Prohibition of Anti-Personnel Mines Act, No. 3 of 2022 | 2022-02-17 |
| `act-2022-004/` | Judicature (Amendment) Act, No. 4 of 2022 | 2022-02-17 |
| `act-2022-005/` | Civil Procedure Code (Amendment) Act, No. 5 of 2022 | 2022-02-17 |
| `act-2022-008/` | Intellectual Property (Amendment) Act, No. 8 of 2022 | 2022-03-16 |
| `act-2022-009/` | Personal Data Protection Act, No. 9 of 2022 | 2022-03-19 |
| `act-2022-010/` | Workmen's Compensation (Amendment) Act, No. 10 of 2022 | 2022-03-19 |
| `act-2022-013/` | Value Added Tax (Amendment) Act, No. 13 of 2022 | 2022-03-31 |
| `act-2022-014/` | Surcharge Tax Act, No. 14 of 2022 | 2022-04-08 |
| `act-2022-017/` | Civil Procedure Code (Amendment) Act, No. 17 of 2022 | 2022-06-23 |
| `act-2022-018/` | Code of Criminal Procedure (Amendment) Act, No.18 of 2022 | 2022-06-23 |
| `act-2022-019/` | Industrial Disputes (Special Provisions) Act, No. 19 of 2022 | 2022-06-23 |
| `act-2021-029/` | Termination of Employment of Workmen (Special Provisions) (Amendment) Act, No. 23 of 2022 | 2022-09-16 |
| `act-2022-022/` | Industrial Disputes (Amendment) Act, No. 22 of 2022 | 2022-09-16 |
| `act-2022-023/` | Termination of Employment of Workmen (Special Provisions) (Amendment) Act, No. 23 of 2022 | 2022-09-16 |
| `act-2022-024/` | Industrial Disputes (Amendment) Act, No. 24 of 2022 | 2022-09-16 |
| `act-2022-025/` | Social Security Contribution Levy Act, No. 25 of 2022 | 2022-09-20 |
| `act-2022-033/` | Small Claims Courts' Procedure Act, No. 33 of 2022 | 2022-11-17 |
| `act-2022-034/` | Judicature (Amendment) Act, No. 34 of 2022 | 2022-11-17 |
| `act-2022-036/` | Civil Procedure Code (Amendment) Act, No. 36 of 2022 | 2022-11-17 |
| `act-2022-038/` | Code of Criminal Procedure (Amendment) Act, No. 38 of 2022 | 2022-11-17 |
| `act-2023-042/` | Appropriation (Amendment) Act, No. 42 of 2022 | 2022-11-30 |
| `act-2022-043/` | Appropriation Act, No. 43 of 2022 | 2022-12-08 |
| `act-2022-044/` | Value Added Tax (Amendment) Act, No. 44 of 2022 | 2022-12-14 |
| `act-2022-045/` | Inland Revenue (Amendment) Act, No. 45 of 2022 | 2022-12-19 |
| `act-2023-002/` | Bureau of Rehabilitation Act, No. 2 of 2023 | 2023-01-24 |
| `act-2023-003/` | Regulation of Election Expenditure Act, No. 3 of 2023 | 2023-01-24 |
| `act-2023-004/` | Inland Revenue (Amendment) Act, No. 4 of 2023 | 2023-05-08 |
| `act-2023-006/` | Parliamentary Budget Office Act, No. 6 of 2023 | 2023-06-27 |
| `act-2023-009/` | Anti-Corruption Act, No. 9 of 2023 | 2023-08-08 |
| `act-2023-010/` | Assistance to and Protection of Victims of Crime and Witnesses Act, No. 10 of 2023 | 2023-08-08 |
| `act-2023-014/` | Inland Revenue (Amendment) Act, No. 14 of 2023 | 2023-09-08 |
| `act-2023-016/` | Central Bank of Sri Lanka Act, No. 16 of 2023 | 2023-09-14 |
| `act-2023-020/` | Civil Procedure Code (Amendment) Act, No. 20 of 2023 | 2023-10-17 |
| `act-2023-022/` | National Eye Bank Trust of Sri Lanka Act, No. 22 of 2023 | 2023-10-17 |
| `act-2023-023/` | Sri Lanka Ports Authority (Amendment) Act, No. 23 of 2023 | 2023-10-17 |
| `act-2023-024/` | Civil Aviation (Amendment) Act, No. 24 of 2023 | 2023-10-17 |
| `act-2023-026/` | Conferring the Honour of Senior Instructing Attorneys-at-Law Act, No. 26 of 2023 | 2023-11-01 |
| `act-2023-027/` | Fisheries and Aquatic Resources (Amendment) Act, No. 27 of 2023 | 2023-11-17 |
| `act-2023-028/` | Anti-Corruption (Amendment) Act, No. 28 of 2023 | 2023-11-17 |
| `act-2023-029/` | Civil Procedure Code (Amendment) Act, No. 29 of 2023 | 2023-11-17 |
| `act-2023-031/` | Galaha Bhaddrawathie National Bhikkhu Care Centre Trust Act, No. 31 of 2023 | 2023-11-24 |
| `act-2023-032/` | Value Added Tax (Amendment) Act, No. 32 of 2023 | 2023-12-13 |
| `act-2023-033/` | Finance Act, No. 33 of 2023 | 2023-12-13 |
| `act-2023-034/` | Appropriation Act, No. 34 of 2023 | 2023-12-13 |
| `act-2024-003/` | Powers of Attorney (Amendment) Act, No. 3 of 2024 | 2024-01-23 |
| `act-2024-004/` | Prevention of Frauds (Amendment) Act, No. 4 of 2024 | 2024-01-23 |
| `act-2024-005/` | Recognition and Enforcement of International Settlement Agreements Resulting from Mediation Act, No. 5 of 2024 | 2024-01-31 |
| `act-2024-007/` | National Hydrographic Act, No. 7 of 2024 | 2024-02-01 |
| `act-2024-008/` | Contempt of a Court, Tribunal or Institution Act, No. 8 of 2024 | 2024-02-01 |
| `act-2024-009/` | Online Safety Act, No. 9 of 2024 | 2024-02-01 |
| `act-2024-015/` | Social Security Contribution Levy (Amendment) Act, No. 15 of 2024 | 2024-03-20 |
| `act-2024-017/` | Secured Transactions Act, No. 17 of 2024 | 2024-04-01 |
| `act-2024-019/` | Trust Receipts (Amendment) Act, No. 19 of 2024 | 2024-04-01 |
| `act-2024-021/` | Finance Leasing (Amendment) Act, No. 21 of 2024 | 2024-04-01 |
| `act-2024-022/` | Inland Trust Receipts (Amendment) Act, No. 22 of 2024 | 2024-04-01 |
| `act-2024-023/` | Companies (Amendment) Act, No. 23 of 2024 | 2024-04-01 |
| `act-2024-025/` | Code of Criminal Procedure (Amendment) Act, No. 25 of 2024 | 2024-05-03 |
| `act-2024-026/` | Recovery of Loans by Banks (Special Provisions) (Amendment) Act, No. 26 of 2024 | 2024-05-08 |
| `act-2024-028/` | Shop and Office Employees (Regulation of Employment and Remuneration) (Amendment) Act, No. 28 of 2024 | 2024-05-13 |
| `act-2024-033/` | Public Debt Management Act, No. 33 of 2024 | 2024-06-18 |
| `act-2024-036/` | Sri Lanka Electricity Act, No. 36 of 2024 | 2024-06-27 |
| `act-2024-037/` | Women Empowerment Act, No. 37 of 2024 | 2024-07-02 |
| `act-2024-038/` | Sri Lanka National Commission for the UNESCO Act, No. 38 of 2024 | 2024-07-02 |
| `act-2024-039/` | Sri Lanka Telecommunications (Amendment) Act, No. 39 of 2024 | 2024-07-17 |
| `act-2024-043/` | Civil Procedure Code (Amendment) Act, No. 43 of 2024 | 2024-08-02 |
| `act-2024-044/` | Public Financial Management Act, No. 44 of 2024 | 2024-08-08 |
| `act-2024-045/` | Economic Transformation Act, No. 45 of 2024 | 2024-08-09 |
| `act-2024-046/` | Medical (Amendment) Act, No. 46 of 2024 | 2024-08-15 |
| `act-2024-049/` | Reciprocal Recognition, Registration and Enforcement of Foreign Judgments Act, No. 49 of 2024 | 2024-09-13 |
| `act-2024-050/` | Code of Criminal Procedure (Amendment) Act, No. 50 of 2024 | 2024-09-13 |
| `act-2025-002/` | Inland Revenue (Amendment) Act, No. 2 of 2025 | 2025-03-20 |
| `act-2025-003/` | Appropriation Act, No. 3 of 2025 | 2025-03-21 |
| `act-2025-004/` | Value Added Tax (Amendment) Act, No. 4 of 2025 | 2025-04-11 |
| `act-2025-005/` | Proceeds of Crime Act, No. 5 of 2025 | 2025-04-30 |
| `act-2025-006/` | Foreign Loans (Repeal) Act, No. 6 of 2025 | 2025-05-23 |
| `act-2025-007/` | Code of Criminal Procedure (Amendment) Act, No. 7 of 2025 | 2025-06-18 |
| `act-2025-008/` | National Transport Commission (Amendment) Act, No. 8 of 2025 | 2025-06-19 |
| `act-2025-009/` | Budgetary Relief Allowance of Workers (Amendment) Act, No. 9 of 2025 | 2025-07-23 |
| `act-2025-010/` | Budgetary Relief Allowance of Workers (Amendment) Act, No.10 of 2025 | 2025-07-23 |
| `act-2025-011/` | National Minimum Wage of Workers (Amendment) Act, No. 11 of 2025 | 2025-07-23 |
| `act-2025-012/` | Companies (Amendment) Act, No. 12 of 2025 | 2025-08-04 |
| `act-2025-013/` | Bills of Exchange (Amendment) Act, No. 13 of 2025 | 2025-08-15 |
| `act-2025-014/` | Sri Lanka Electricity (Amendment) Act, No. 14 of 2025 | 2025-08-18 |
| `act-2025-015/` | Samurdhi (Amendment) Act, No. 15 of 2025 | 2025-08-22 |
| `act-2025-016/` | Rubber Control (Amendment) Act, No. 16 of 2025 | 2025-08-22 |
| `act-2025-017/` | Gambling Regulatory Authority Act, No. 17 of 2025 | 2025-09-03 |
| `act-2025-018/` | Presidents' Entitlements (Repeal) Act, No. 18 of 2025 | 2025-09-10 |
| `act-2025-019/` | National Audit (Amendment) Act, No. 19 of 2025 | 2025-09-22 |
| `act-2025-020/` | National Building Research Institute Act, No. 20 of 2025 | 2025-10-07 |
| `act-2025-022/` | Personal Data Protection (Amendment) Act, No. 22 of 2025 | 2025-10-30 |
| `act-2025-023/` | Appropriation Act, No. 23 of 2025 | 2025-12-05 |
| `act-2025-024/` | Social Security Contribution Levy (Amendment) Act, No. 24 of 2025 | 2025-12-17 |
| `act-2025-025/` | Betting and Gaming Levy (Amendment) Act, No. 25 of 2025 | 2025-12-17 |
| `act-2025-026/` | Strategic Development Projects (Amendment) Act, No. 26 of 2025 | 2025-12-17 |
| `act-2026-001/` | Colombo Port City Economic Commission (Amendment) Act, No. 1 of 2026 | 2026-01-20 |
| `act-2026-002/` | Universities (Amendment) Act, No. 2 of 2026 | 2026-02-03 |
| `act-2026-003/` | Licensing of Container Depot Operators Act, No. 3 of 2026 | 2026-02-17 |
| `act-2026-004/` | Licensing of Shipping Agents, Freight Forwarders, Non-Vessel Operating Common Carriers and Container Operators (Amendment) Act, No. 4 of 2026 | 2026-02-17 |
| `act-2026-005/` | Parliamentary Pensions (Repeal) Act, No. 5 of 2026 | 2026-02-17 |
| `act-2026-006/` | Institute of Real Estate Professionals, Sri Lanka Act, No. 6 of 2026 | 2026-02-19 |
| `act-2026-007/` | Poisons, Opium and Dangerous Drugs (Amendment) Act, No. 7 of 2026 | 2026-03-06 |
| `act-2026-008/` | Judicature (Amendment) Act, No. 8 of 2026 | 2026-03-06 |
| `act-2026-010/` | Social Security Contribution Levy (Amendment) Act, No. 10 of 2026 | 2026-04-09 |
| `act-2026-011/` | Inland Revenue (Amendment) Act, No. 11 of 2026 | 2026-06-03 |
| `act-2026-012/` | Rescue, Rehabilitation and Insolvency (Corporate and Personal) Act, No. 12 of 2026 | 2026-06-17 |
| `act-2026-013/` | Mediation (Civil and Commercial Disputes) Act, No. 13 of 2026 | 2026-06-30 |
| `act-2026-014/` | Value Added Tax (Amendment) Act, No. 14 of 2026 | 2026-06-30 |
| `act-2026-015/` | National Environmental (Amendment) Act, No. 15 of 2026 | 2026-07-21 |
| `act-2026-016/` | Prevention of Money Laundering (Amendment) Act, No. 16 of 2026 | 2026-08-04 |
| `act-2026-018/` | Convention on the Suppression of Terrorist Financing (Amendment) Act, No. 18 of 2026 | 2026-08-04 |
| `act-2026-020/` | National Water Supply and Drainage Board (Amendment) Act, No. 20 of 2026 | 2026-08-18 |
| `act-2026-021/` | Employment of Women, Young Persons and Children (Amendment) Act, No. 21 of 2026 | 2026-09-08 |
| `act-2026-023/` | Judicature (Amendment) Act, No. 23 of 2026 | 2026-09-25 |
| `act-2026-024/` | Promotion of Export Agriculture (Amendment) Act, No. 24 of 2026 | 2026-10-06 |
