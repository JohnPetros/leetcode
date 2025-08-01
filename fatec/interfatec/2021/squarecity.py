# print(10 + 10 + 9 + 9)  # 11
# print(6 + 6 + 5 + 5)  # 7
# print(2 + 2 + 1 + 1)  # 3

integer = 9

if integer == 1:
    print(0)
else:
    key_numbers = [number for number in range(3, integer + 1, 4)]

    if integer not in key_numbers:
        integer -= 2

    houses_count = 0

    for order in range(3, integer + 1, 4):
        houses_count += (order - 1) + (order - 1) + (order - 2) + (order - 2)

    print(houses_count)
