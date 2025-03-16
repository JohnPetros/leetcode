DELEMITER = "#"


def encode_strings(strings: list[str]) -> str:
    encoded_string = ""

    for string in strings:
        encoded_string += f"{len(string)}{DELEMITER}{string if string else 0}"

    return encoded_string


def decode_strings(string: str) -> list[str]:
    decoded_strings = []

    index = 0
    while index < len(string) - 2:
        string_length_string = ""
        while string[index].isnumeric():
            string_length_string += string[index]
            index += 1

        if string_length_string and string[index] == DELEMITER:
            string_length = int(string_length_string)
            if string_length == 0:
                decoded_strings.append("")
                string_length += 1
            else:
                word = string[index + 1 : index + 1 + string_length]
                decoded_strings.append(word)
        index += 1 + string_length

    return decoded_strings


encoded_string = encode_strings(["we", "say", ":", "yes", "!@#$%^&*()"])
print(decode_strings(encoded_string))
