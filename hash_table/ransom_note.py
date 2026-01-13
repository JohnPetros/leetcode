from collections import Counter


def ransom_note(note: str, magazine: str) -> bool:
    counter = Counter(magazine)

    for letter in note:
        if letter not in counter:
            return False

        counter[letter] -= 1
        if counter[letter] == 0:
            del counter[letter]

    return True
    # Time: O(N + M)
    # Space: O(M)


# print(ransom_note("a", "b"))
# print(ransom_note("aa", "ab"))
print(ransom_note("aa", "aab"))
