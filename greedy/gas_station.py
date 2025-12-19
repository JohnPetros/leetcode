def gas_station(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1

    n = len(gas)
    diff = [0] * n
    for index in range(n):
        diff[index] = gas[index] - cost[index]

    total = 0
    start = 0
    for index in range(n):
        total += diff[index]
        if total < 0:
            total = 0
            start = index + 1

    return start

print(gas_station([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
