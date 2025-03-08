def product_of_array_except_self(numbers: list[int]) -> list[int]:
    previous_product = 1
    products = []

    for number in numbers:
        products.append(previous_product)
        previous_product = previous_product * number

    previous_product = 1

    for index in range(len(numbers) - 1, -1, -1):
        products[index] = products[index] * previous_product
        previous_product = previous_product * numbers[index]

    return products


print(product_of_array_except_self([1, 2, 3, 4]))
