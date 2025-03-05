def merge_strings_alternately(word1: str, word2: str):
    max_len = max(len(word1), len(word2))
    merged_string = ""
    index = 0

    while index < max_len:
        if index <= len(word1) - 1:
            merged_string += word1[index]

        if index <= len(word2) - 1:
            merged_string += word2[index]

        index += 1

    return merged_string


print(merge_strings_alternately("ab", "pqrs"))
print(merge_strings_alternately("ab", "pqrs"))
print(merge_strings_alternately("abcd", "pq"))
