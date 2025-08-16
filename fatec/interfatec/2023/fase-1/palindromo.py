from sys import stdin
from unicodedata import normalize, category
from string import (
    punctuation,
    ascii_letters,
    ascii_lowercase,
    ascii_uppercase,
    digits,
    capwords,
)

print(capwords("olá mundo, ação e coração".index))

# try:
#     for string in stdin.readlines():
#         string = normalize(string)
#         left, right = 0, len(string) - 1
#         is_palindrome = False

#         while left <= right:
#             if string[left] != string[right]:
#                 is_palindrome = True
#                 break
#             left += 1
#             right += 1

#         if is_palindrome:
#             print("Parabens, voce encontrou o Palindromo Perdido!")
#         else:
#             print("A busca continua, o Palindromo Perdido ainda nao foi encontrado.")

# except EOFError:
#     pass


def remove_accentuation(string):
    return "".join(
        char for char in normalize("NFD", string) if category(char) != "Mn"
    ).replace(" ", "")


string = "4r4R4"
string = remove_accentuation(string).lower().strip()
left, right = 0, len(string) - 1
is_palindrome = True

while left <= right:
    if string[left] != string[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("Parabens, voce encontrou o Palindromo Perdido!")
else:
    print("A busca continua, o Palindromo Perdido ainda nao foi encontrado.")
