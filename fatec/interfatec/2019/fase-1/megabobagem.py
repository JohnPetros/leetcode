from collections import Counter

string = "SALASANNASALASANNA"

character_count = Counter(string)
odd_number_count = 0
is_valid = True

for count in character_count.values():
    if count % 2 != 0:
        odd_number_count += 1

    if odd_number_count >= 2:
        is_valid = False

print("VERDADEIRO" if is_valid else "FALSO")
