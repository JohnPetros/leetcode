def mercado(total: int, stocks: list[int]):
    greatest_stock = stocks[0]
    worst_loss = 0

    for index in range(1, total):
        current = stocks[index]
        worst_loss = max(worst_loss, greatest_stock - current)
        greatest_stock = max(greatest_stock, current)

    if worst_loss <= 0:
        print(0)
    else:
        print(-worst_loss)


################################################### Teste

# mercado(6, [3, 2, 4, 2, 1, 5])
# mercado(6, [5, 3, 4, 2, 3, 1])
# mercado(5, [1, 2, 3, 4, 5])

################################################### Final

total = int(input())
stocks = list(map(int, input().split()[:total]))
mercado(total, stocks)
