def permutation_in_string(string1, string2):
    string1_length = len(string1)
    string2_length = len(string2)

    if string1_length > string2_length:
        return False

    string1_alphabet_frequency = [0] * 26
    string2_alphabet_frequency = [0] * 26

    for index in range(string1_length):
        string1_alphabet_frequency[ord(string1[index]) - 97] += 1
        string2_alphabet_frequency[ord(string2[index]) - 97] += 1

    if string1_alphabet_frequency == string2_alphabet_frequency:
        return True

    for index in range(string1_length, string2_length):
        string2_alphabet_frequency[ord(string2[index]) - 97] += 1
        string2_alphabet_frequency[ord(string2[index - string1_length]) - 97] -= 1

        print(string1_alphabet_frequency, string2_alphabet_frequency)
        if string1_alphabet_frequency == string2_alphabet_frequency:
            return True

    return False
    # Time Complexity: O(n)
    # Space Complexity: O(1)


print(permutation_in_string("ab", "eidbaooo"))
