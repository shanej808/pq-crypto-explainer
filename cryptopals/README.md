# Cryptopals

Solutions to the [Cryptopals](https://cryptopals.com/) crypto challenges, organized by set:

- `set1/` — basics (XOR, base64/hex, single/repeating-key XOR, AES-ECB)
- `set5/` — Diffie-Hellman and RSA fundamentals (leads directly into `rsa_core/`)
- `set6/` — RSA and DSA attacks (padding oracles, signature forgery, related-message attacks)

Each set gets its own module with one file per challenge (e.g. `set1/challenge01.py`), plus tests under `tests/`.
