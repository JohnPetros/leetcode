TESTE = True


def quermesse(tickets: list[int]):
    winner = 0
    for index, ticket in enumerate(tickets):
        if index + 1 == ticket:
            winner = ticket
            break
    print(winner)


if TESTE:
    quermesse([4, 5, 3, 1])
    quermesse([9, 8, 7, 6, 1, 4, 3, 2, 12, 10])
else:
    n = int(input())
    tickets = list(map(int, input().split()[:n]))
    quermesse(tickets)
