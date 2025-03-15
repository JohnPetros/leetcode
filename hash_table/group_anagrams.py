def group_anagrams(anagrams: list[str]) -> list[list[str]]:
    alphabet = "abcdefghijklmnoqrstuvwxyz"
    hash_table = dict()

    for anagram in anagrams:
        key = []
        for character in alphabet:
            key.append(anagram.count(character))

        if str(key) in hash_table:
            hash_table[str(key)].append(anagram)
        else:
            hash_table[str(key)] = [anagram]

    return list(hash_table.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams([""]))
print(group_anagrams(["a"]))
