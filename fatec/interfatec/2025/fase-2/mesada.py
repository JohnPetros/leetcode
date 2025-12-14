sons = 4
money = 70
categories = 6


def divide_per_category(money, times):
    cells = [30, 20, 10]
    cell_index = 0
    while money >= 10:
        while cells[cell_index] > money:
            cell_index += 1
        money -= cells[cell_index]
        print(cells[cell_index], end=" ")
        times -= 1
        if times == 0:
            break

    for _ in range(times):
        print(0, end=" ")


def mesada(sons, money, categories):
    base = money // sons // 10 * 10
    rest = money - (base * sons)
    last_son_base = base + rest

    for _ in range(sons - 1):
        divide_per_category(base, categories)
        print()
    divide_per_category(last_son_base, categories)


mesada(sons, money, categories)
