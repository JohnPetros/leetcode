size = 5
original_number = 12496
number = original_number


for _ in range(size):
    number = sum(n for n in range(1, number) if number % n == 0)


print("sim" if number == original_number else "nao")
