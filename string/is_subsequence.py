def is_subsequence(substring: str, string: str):
    for character in string:
        if character == substring[0]:
            substring = substring[1:]

    return not bool(substring)


print(is_subsequence("abc", "ahbgdc"))
print(is_subsequence("axc", "ahbgdc"))
