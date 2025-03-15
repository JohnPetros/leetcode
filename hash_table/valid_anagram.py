def valid_anagram(string_1: str, string_2: str) -> bool:
    if len(string_1) != len(string_2):
        return False

    hash_table_1 = dict()
    hash_table_2 = dict()

    for character in string_1:
        if character in hash_table_1:
            hash_table_1[character] += 1
        else:
            hash_table_1[character] = 1

    for character in string_2:
        if character in hash_table_2:
            hash_table_2[character] += 1
        else:
            hash_table_2[character] = 1

    return hash_table_1 == hash_table_2


print(valid_anagram("anagram", "nagaram"))
