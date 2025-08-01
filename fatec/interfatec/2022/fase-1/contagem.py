numbers = [1, 2, 3, 4, 5]

last_number = numbers[len(numbers) - 1]
numbers_inclusion = [False] * last_number

for number in numbers:
    numbers_inclusion[number - 1] = True

is_good_work = False not in numbers_inclusion

if is_good_work:
    print("bom trabalho")
else:
    for index in range(last_number):
        if not numbers_inclusion[index]:
            print(index + 1)
