"""
Cryptopals Set 1, Challenge 1: Convert hex to base64

Concept:
    Bytes are the underlying data; hex and base64 are just different
    text encodings of those same bytes. Hex = 4 bits per char,
    base64 = 6 bits per char. Converting between them means:
    hex string -> raw bytes -> base64 string.

Rule applied:
    Always operate on raw bytes, never on encoded strings directly.
"""

import base64


def hextobase64(hex_string):
    # Convert hexadecimal string to raw bytes
    raw_bytes = bytes.fromhex(hex_string)

    # Encode raw bytes to base64, then decode from ASCII bytes to a string
    base64_string = base64.b64encode(raw_bytes).decode("ascii")

    return base64_string


if __name__ == "__main__":
    hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    result = hextobase64(hex_string)
    print(f"Input:    {hex_string}")
    print(f"Output:   {result}")
    print(f"Expected: {expected}")
    print(f"Match:    {result == expected}")
