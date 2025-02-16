def pow(number: int, exponent: int) -> float:
    if exponent == 0:
        return 1.0

    if exponent < 0:
        number = 1 / number
        exponent = -exponent

    result = pow(number, exponent // 2)

    if exponent % 2 == 0:
        return result * result

    return result * result * number


print(pow(5, 2))
