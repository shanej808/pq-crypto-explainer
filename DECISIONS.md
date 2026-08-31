# Decision Log

## 2026-08-26 — Repo created, phase plan set

Created `pq-crypto-explainer` as a portfolio project demonstrating RSA cryptography,
quantum attacks via Shor's algorithm, and post-quantum cryptography, built in
incremental phases rather than as a single monolithic build:

1. **Cryptopals foundation** — work through the relevant Cryptopals sets (1, 5, 6)
   to build up the number-theory and attack intuition RSA depends on.
2. **RSA explainer app** — a from-scratch RSA implementation (`rsa_core/`, no
   external crypto libraries for the core primitives) wired up to a Streamlit
   front end (`app/`) that visualizes key generation, encryption, and signing.
3. **Shor's algorithm / Qiskit simulation** — simulate Shor's algorithm against
   small RSA moduli to demonstrate why RSA breaks under a sufficiently large
   quantum computer.
4. **Post-quantum cryptography layer** — integrate `liboqs` to show a PQC
   key exchange / signature scheme (e.g. Kyber/ML-KEM, Dilithium/ML-DSA) as
   the practical mitigation, side-by-side with the broken RSA flow.
5. **Stretch: OSS contribution** — attempt an upstream contribution to the
   Open Quantum Safe project based on what's learned building phases 3–4.

`pycryptodome` is included in `requirements.txt` only as a reference/testing
oracle to validate the from-scratch RSA implementation against a trusted
library — it is not used to implement `rsa_core` itself.

## Cryptopals scope trim (Phase 1)

Original plan was Set 1 (full) → Set 2 (full) → Set 5 → Set 6, but a full
walkthrough was estimated at 15-20+ hours against a few-hours-a-week budget
across two parallel projects. Trimmed to protect Phase 1 delivery timeline:

- Set 1: full (foundational, short)
- Set 2: cherry-picked only — Ch12 (byte-at-a-time ECB decryption) and
  Ch15 (PKCS#7 padding validation). Both build attack intuition that
  transfers directly to RSA padding attacks. Rest of Set 2 skipped.
- Set 5: skipped entirely. DH concepts (modular exponentiation) get
  covered anyway during RSA keygen implementation.
- Set 6: Ch39 (RSA implementation) and Ch40 (RSA broadcast attack, e=3)
  — this is the actual point of Phase 1 and feeds directly into rsa_core
  and the attack demo in the app.

Revised estimate: ~6-10 hours total vs. 15-20+ for the full original scope.
