def best_time_to_buy_and_sell_stock(prices: list[int]):
    max_profit = 0
    min_prince = float("inf")

    for price in prices:
        if price < min_prince:
            min_prince = price
        else:
            max_profit = max(max_profit, price - min_prince)

    return max_profit


print(best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4]))
print(best_time_to_buy_and_sell_stock([7, 6, 4, 3, 1]))
