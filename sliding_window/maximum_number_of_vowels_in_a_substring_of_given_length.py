def maximum_number_of_vowels_in_a_substring_of_given_length(s: str, k: int) -> int:
    n = len(s)
    vowels = set("aeiou")
    if n == 1:
        if s in vowels:
            return 1
        else:
            return 0

    maximum = 0
    left = 0
    count = 0

    for right in range(n):
        if right < k - 1:
            if s[right] in vowels:
                count += 1
                maximum = max(maximum, count)
        else:
            if s[right] in vowels:
                count += 1
                maximum = max(maximum, count)

            if s[left] in vowels:
                count -= 1
                maximum = max(maximum, count)
                left += 1
            else:
                left += 1

    return maximum


print(set("aeiou"))
