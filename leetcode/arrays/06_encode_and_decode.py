''' question says to encode a list of strings, create a encoding function
the encoded version should be decoded to its original form when passed on
to the decode function'''


def encode(strs: list[str]) -> str:
    # encode a string using length and special char to create separation
    result = ""
    for string in strs:
        result += str(len(string)) + "#" + string

    return result


def decode(s: str) -> list[str]:
    result = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] != "#":
            j += 1
        length = int(s[i:j])
        i = j + 1
        result.append(str(s[i: i + length]))
        i += length

    return result


dummy_input = ["Hello", "World"]
print(encode(dummy_input))
string_encoded = encode(dummy_input)
print(decode(string_encoded))
