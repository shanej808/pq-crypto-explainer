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

def hex_to_base64(hex_string: str) -> str:
    raw_bytes = bytes.fromhex(hex_string)
    import base64
    return base64.b64encode(raw_bytes).decode()


if __name__ == "__main__":
    input_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f75736d75736869726f6f6d"
    expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    result = hex_to_base64(input_hex)
    print(f"Input:    {input_hex}")
    print(f"Output:   {result}")
    print(f"Expected: {expected}")
    print(f"Match:    {result == expected}")
