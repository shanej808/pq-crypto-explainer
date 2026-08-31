"""
Cryptopals Set 1, Challenge 2: Fixed XOR

Concept:
    XOR compares two bits and outputs 1 if they differ, 0 if they match.
    Applied byte-by-byte across two equal-length byte sequences, this
    produces a new byte sequence of the same length. XOR is its own
    inverse: if A XOR B = C, then C XOR B = A — this reversibility is
    why XOR underlies stream ciphers (encrypt and decrypt are the same
    operation).

Validation:
    Inputs must be equal length (otherwise the operation is undefined)
    and even length (each byte = 2 hex characters). Both checks raise
    loudly via ValueError rather than failing silently or returning None,
    since silent failures in crypto code are dangerous.
"""


def fixed_xor(hex_str1, hex_str2):
    # 1. Validation check: Ensure input strings are equal length
    if len(hex_str1) != len(hex_str2):
        raise ValueError(
            f"Hex strings must be of equal length. ({len(hex_str1)} vs {len(hex_str2)})"
        )

    # 2. Validation check: Ensure both strings have even length
    #    (each byte = 2 hex characters, so odd length is invalid)
    if len(hex_str1) % 2 != 0:
        raise ValueError(
            f"Hex strings must have even length to represent whole bytes. Got length {len(hex_str1)}."
        )

    # 3. Convert hexadecimal strings into raw byte objects
    bytes_1 = bytes.fromhex(hex_str1)
    bytes_2 = bytes.fromhex(hex_str2)

    # 4. Perform byte-by-byte XOR
    xor_bytes = bytes(b1 ^ b2 for b1, b2 in zip(bytes_1, bytes_2))

    # 5. Return the hex-encoded string of the resulting bytes
    return xor_bytes.hex()


if __name__ == "__main__":
    # --- Cryptopals Set 1 Challenge 2 Test ---
    string_1 = "1c0111001f010100061a024b53535009181c"
    string_2 = "686974207468652062756c6c277320657965"
    expected = "746865206b696420646f6e277420706c6179"

    result = fixed_xor(string_1, string_2)

    print("Hex Result:", result)
    print("Expected:  ", expected)
    print("Match:     ", result == expected)
    print(
        "ASCII Representation:",
        bytes.fromhex(result).decode("ascii", errors="ignore"),
    )
