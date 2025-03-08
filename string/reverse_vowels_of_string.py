def reverse_vowels_of_string(string: str) -> str:
    vowels = "aeiou"
    letters = list(string)
    string_vowels = [letter for letter in letters if letter.lower() in vowels]

    index = 0
    while index < len(letters) and len(string_vowels) != 0:
        if letters[index].lower() in vowels:
            letters[index] = string_vowels.pop()
        index += 1

    return "".join(letters)


print(reverse_vowels_of_string("IceCreAm"))
