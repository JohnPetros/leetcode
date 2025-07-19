input = [2, 3, 4, 0]

for number in input:
    if number == 0:
        break

    result = []
    index = 1
    perfect_square = index**2
    while perfect_square <= number:
        result.append(str(perfect_square))
        index += 1

    print(" ".join(result))
