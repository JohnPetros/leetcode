integer = 27

triangles = []
letter_index = -1
triangle_count = 1
alphabet = "ABCDEFGHI"

for number in range(integer):
    if letter_index == 9:
        letter_index = 0
        triangle_count += 1
    letter_index += 1


print(f"{triangle_count}{alphabet[letter_index]}")
