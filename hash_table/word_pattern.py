def word_pattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False

    map1 = dict()
    map2 = dict()

    for letter, word in zip(pattern, words):
        if letter in map1 and map1[letter] != word:
            return False

        if word in map2 and map2[word] != letter:
            return False

        map1[letter] = word
        map2[word] = letter

    return True
    # Time: O(n + m)
    # Space: O(n + m)


# print(word_pattern("abba", "dog cat cat dog"))
# print(word_pattern("abba", "dog cat cat fish"))
print(word_pattern("aaaa", "dog cat cat dog"))
