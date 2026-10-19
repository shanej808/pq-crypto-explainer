# CLAUDE.md

Instructions for Claude Code working in this repo. Read this at the start of every session.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt   # requirements.txt + ruff, for local lint/test
```

## Run

```bash
streamlit run app/app.py   # once it has real content (Phase 2+)
```

## Test

```bash
pytest          # full suite
pytest -q       # quiet
ruff check .    # lint
```

CI (`.github/workflows/ci.yml`) runs both on every push and PR to `main`. A red build blocks merge — do not bypass this.

Current suite is placeholder stubs (`tests/test_cryptopals.py`, `tests/test_rsa_core.py`) pending real
Cryptopals and `rsa_core` implementations. As each challenge or RSA primitive lands, add a real test for
it in the matching file — do not leave the placeholder as the only coverage once there's real code to test.

## Data and network

This project has no external data pipeline. Cryptopals and `rsa_core` work is self-contained (no network
calls). Phase 4 (`liboqs`/PQC) will need `liboqs-python` installed via pip — that's a package install, not
a runtime data fetch, so it's fine. If a future phase needs to fetch data or call an external API at
runtime, document the dependency in `DECISIONS.md` and flag it before building around it, the same way the
football project documented its sandbox network restriction.

## Commit conventions

- One commit per meaningful unit of work (one Cryptopals challenge, one RSA primitive, one test).
- Descriptive messages: what changed and why, not just "update file".
- Each Cryptopals solution file follows the existing template: docstring explaining the concept, one clean
  function, a `main` self-verification block.

## DECISIONS.md

This file is a persistent methodology log, not a changelog. Add an entry whenever a design decision is
made (scope trims, library choices, approach changes) — see existing entries for the format (Decision /
Why / Trade-off). If a session makes a decision of this kind and DECISIONS.md hasn't been touched yet,
add it before ending the session.

## Verification rule

Never state that a test passes, code works, or output is correct without showing the actual run (test
output, command output) in the same turn. "This should work" is not a substitute for running it.
