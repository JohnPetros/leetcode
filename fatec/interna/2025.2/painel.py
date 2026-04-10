TESTE = True


def painel(string: str):
    numbers = [int(string)]
    for i in range(1, 6):
        new_string = list(string)
        new_string[i - 1], new_string[i] = new_string[i], new_string[i - 1]
        numbers.append(int("".join(new_string)))

    print(str(min(numbers)).rjust(6, "0"))


if TESTE:
    painel("100000")
    painel("654321")
    painel("823460")
else:
    painel(input())
