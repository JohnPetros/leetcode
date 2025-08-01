positions = [1, 4, 2]

odd_numbers_count = 0

for position in positions:
    if position > 1:
        odd_numbers_count += 1

if odd_numbers_count % 2 == 0:
    print("par")
else:
    print("impar")
