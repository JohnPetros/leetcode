def best_time_to_buy_and_sell_stock_ii(prices: list[int]):
    lower_point = prices[0]
    higher_point = prices[0]
    profit = 0
    index = 0
    n = len(prices)

    while index < n - 1:
        while index < n - 1 and prices[index] >= prices[index + 1]:
            index += 1
        lower_point = prices[index]

        while index < n - 1 and prices[index] <= prices[index + 1]:
            index += 1
        higher_point = prices[index]

        profit += higher_point - lower_point

    return profit
    # Time: O(n)
    # Space: O(1)


print(best_time_to_buy_and_sell_stock_ii([7, 6, 4, 1, 5, 8, 3, 6, 4]))
print(best_time_to_buy_and_sell_stock_ii([7, 1, 5, 3, 6, 4]))
print(best_time_to_buy_and_sell_stock_ii([1, 2, 3, 4, 5]))
print(best_time_to_buy_and_sell_stock_ii([7, 6, 4, 3, 1]))
print(best_time_to_buy_and_sell_stock_ii([2, 1, 2, 1, 0, 0, 1]))
print(best_time_to_buy_and_sell_stock_ii([1, 4, 2]))
print(best_time_to_buy_and_sell_stock_ii([8, 6, 4, 3, 3, 2, 3, 5, 8, 3, 8, 2, 6]))
