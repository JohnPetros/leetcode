def first_unique_character_in_a_string(string):
    hash_table = {}

    for char in string:
        hash_table[char] = hash_table.get(char, 0) + 1

    for i, char in enumerate(string):
        if hash_table[char] == 1:
            return i

    return -1


print(first_unique_character_in_a_string("leetcode"))
