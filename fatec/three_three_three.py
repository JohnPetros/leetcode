def three_three_three(number):
    three_number_count = 0

    for current_number in range(0, number):
        if "3" in str(current_number):
            three_number_count += 1

    return number - three_number_count


print(three_three_three(10))
print(three_three_three(45))
print(three_three_three(578))
