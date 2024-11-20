def multiply_strings(number1: str, number2: str) -> str:
    if number1 == "0" or number2 == "0":
        return "0"

    number1 = number1[::-1]
    number2 = number2[::-1]
    result = [0] * (len(number1) + len(number2))

    for i in range(len(number1)):
        for j in range(len(number2)):
            product = int(number1[i]) * int(number2[j])
            sum = result[i + j] + product
            result[i + j] = sum % 10
            result[i + j + 1] += int(sum / 10)

    result.reverse()

    while result[0] == 0:
        result.pop(0)

    return "".join(map(str, result))


# print(multiply_strings("2", "3"))
print(multiply_strings("123", "456"))
print(multiply_strings("21", "43"))
