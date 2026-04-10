TESTE = True


def tres(n: int):
    count = 0

    for number in range(n + 1):
        if "3" not in str(number):
            count += 1

    print(count)


if TESTE:
    tres(10)
    tres(45)
    tres(578)
    # tres(1000000)
else:
    try:
        while True:
            n = int(input())
            tres(n)
    except EOFError:
        pass
