def maximum_number_of_vowels_in_a_substring_of_given_length(s: str, k: int) -> int:
    vowels = "aeiou"
    maximum = count = left = 0

    for right in range(len(s)):
        if s[right] in vowels:
            count += 1

        if right >= k:
            if s[left] in vowels:
                count -= 1
            left += 1

        if count > maximum:
            maximum = count

    return maximum
    # Time: O(N)
    # Space: O(1)


print(maximum_number_of_vowels_in_a_substring_of_given_length("aeiou", 2))
