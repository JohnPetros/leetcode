def product_of_array_except_self(numbers: list[int]) -> list[int]:
    previous_product = 1
    products = []

    for number in numbers:
        products.append(previous_product)
        previous_product *= number

    previous_product = 1

    for index in range(len(numbers) - 1, -1, -1):
        products[index] *= previous_product
        previous_product *= numbers[index]

    return products


def _product_of_array_except_self(numbers: list[int]) -> list[int]:
    previous_product = 1
    prefix_products = []
    postfix_products = []
    products = []

    for number in numbers:
        prefix_products.append(previous_product * number)
        previous_product = previous_product * number

    previous_product = 1

    for index in range(len(numbers) - 1, -1, -1):
        postfix_products.append(previous_product * numbers[index])
        previous_product = previous_product * numbers[index]

    postfix_products.reverse()

    for index in range(len(numbers)):
        if index == 0:
            products.append(postfix_products[index + 1])
        elif index == len(numbers) - 1:
            products.append(prefix_products[index - 1])
        else:
            products.append(prefix_products[index - 1] * postfix_products[index + 1])

    return products


print(product_of_array_except_self([1, 2, 3, 4]))
