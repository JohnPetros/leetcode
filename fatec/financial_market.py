def financial_market(values_count: int, values: list[int]):
    worst_loss = 0

    for index in range(values_count):
        if index == values_count - 1:
            break

        loss = values[index] - min(values[index + 1 :])
        if loss > worst_loss:
            worst_loss = loss

    print(-worst_loss)


values_count = "6"
data = "3 2 4 2 1 5".split()
# values_count = "6"
# data = "5 3 4 2 3 1".split()
# values_count = "5"
# data = "1 2 3 4 5".split()
financial_market(int(values_count), list(map(int, data)))

# 0412578440
# 0412199803
# 0468892011
# 112
# 15
