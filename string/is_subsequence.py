def is_subsequence(substring: str, string: str):
    for character in string:
        if not substring:
            return True

        if character == substring[0]:
            substring = substring[1:]

    return not bool(substring)
    # O(n) time complexity
    # O(1) space complexity


print(is_subsequence("abc", "ahbgdc"))
print(is_subsequence("axc", "ahbgdc"))
