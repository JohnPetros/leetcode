from string import ascii_uppercase, ascii_lowercase

[count, case] = input().split()
alphabet = ascii_uppercase if case == "maiusculas" else ascii_lowercase

for index in range(1, int(count) + 1):
    print(("." * (26 - index)) + alphabet[0:index])
