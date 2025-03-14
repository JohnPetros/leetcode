def group_anagrams(anagrams: list[str]) -> list[list[str]]:
    if not anagrams:
        return [[""]]

    anagrams_table = dict()

    for anagram in anagrams:
        sorted_anagram = "".join(sorted(anagram))

        if sorted_anagram in anagrams_table:
            anagrams_table[sorted_anagram].append(anagram)
        else:
            anagrams_table[sorted_anagram] = [anagram]

    return sorted(list(anagrams_table.values()), key=lambda anagram: len(anagram))


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams([""]))
print(group_anagrams(["a"]))
