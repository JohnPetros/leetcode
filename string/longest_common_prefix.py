def longest_common_prefix(strings: list[str]) -> str:
    longest_prefix = ""

    if not strings:
        return longest_prefix

    min_length = min(len(string) for string in strings)

    for index in range(min_length):
        current_character = strings[0][index]

        if all(string[index] == current_character for string in strings):
            longest_prefix += current_character
        else:
            break

    return longest_prefix


print(longest_common_prefix(["flower", "flow", "flight"]))
