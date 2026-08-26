# PQ Crypto Explainer

An interactive, from-first-principles explainer of RSA cryptography, how
quantum computers break it via Shor's algorithm, and how post-quantum
cryptography (PQC) fixes it. Built as a portfolio project to demonstrate
applied cryptography and security engineering, not just library usage.

## Phase roadmap

1. **Cryptopals foundation** — [Cryptopals](https://cryptopals.com/) sets 1, 5,
   and 6 (`cryptopals/`), building the number theory and attack intuition
   RSA depends on.
2. **RSA explainer app** — an RSA implementation from scratch (`rsa_core/`,
   no external crypto libraries for the primitives themselves) with a
   Streamlit front end (`app/`) that visualizes key generation, encryption,
   and signing.
3. **Shor's algorithm / Qiskit simulation** — simulate Shor's algorithm
   against small RSA moduli to demonstrate the quantum attack.
4. **Post-quantum cryptography layer** — integrate `liboqs` to demonstrate a
   PQC key exchange / signature scheme (e.g. Kyber/ML-KEM, Dilithium/ML-DSA)
   as the practical mitigation.
5. **Stretch: OSS contribution** — an upstream contribution to the
   [Open Quantum Safe](https://openquantumsafe.org/) project.

See [DECISIONS.md](DECISIONS.md) for the reasoning behind this structure and
ongoing design decisions.

## Repo layout

```
cryptopals/   # Cryptopals challenge solutions, organized by set (set1/, set5/, set6/)
rsa_core/     # RSA implementation from scratch
app/          # Streamlit front end
tests/        # pytest test suite
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the test suite:

```bash
pytest
```

Run the Streamlit app (once it has real content):

```bash
streamlit run app/app.py
```

## Status

Phase 1 in progress — Cryptopals solutions, `rsa_core` implementation, and
the Streamlit scaffold.
