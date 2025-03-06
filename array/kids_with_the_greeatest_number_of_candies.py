def kids_with_the_greeatest_number_of_candies(candies: list[int], extra_candies: int):
    greatest_candies_number = max(candies)

    return [candy + extra_candies >= greatest_candies_number for candy in candies]


print(kids_with_the_greeatest_number_of_candies([2, 3, 5, 1, 3], 3))
print(kids_with_the_greeatest_number_of_candies([4, 2, 1, 1, 2], 1))
print(kids_with_the_greeatest_number_of_candies([12, 1, 12], 10))
