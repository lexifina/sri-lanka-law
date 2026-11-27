# Structure

- `constitution/constitution/`: the Constitution of 1978, one file per Article (`art-137.md`) and Schedule.
- `act/<year>/<number>/`: an Act of Parliament (public or private) by its year and number, e.g. `act/2007/007/`
  (Companies Act, No. 7 of 2007).
- `law/<year>/<number>/`: a Law of the National State Assembly (1972-1978), e.g. `law/1977/006/`.
- `ordinance/<year>/<number>/`: an Ordinance (before 1948), e.g. `ordinance/1883/002/` (Penal Code).
- In each folder: `preamble.md` (long title, enacting words, and for consolidations the list of enactments),
  `sec-NNN.md` (one file per section, `sec-002a.md` for section 2A; the marginal note is the heading),
  `schedule-NN.md`, and a `README.md` index.
- An amending law is its own folder; a consolidated text is a later version (commit) in the folder of the enactment it
  consolidates.
- `data/laws.csv`: every law, with its days and source; `data/paths.json`: old folder names (before 2026-11-10).
- No folder holds more than 1,000 entries (the largest year has fewer than 100 Acts).
