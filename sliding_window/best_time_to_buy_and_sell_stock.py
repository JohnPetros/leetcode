def best_time_to_buy_and_sell_stock(stocks: list[int]) -> int:
    minimum_price = float("inf")
    maximum_profit = 0

    for stock in stocks:
        if stock < minimum_price:
            minimum_price = stock
        else:
            maximum_profit = max(maximum_profit, stock - minimum_price)

    return maximum_profit


print(best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4]))
print(best_time_to_buy_and_sell_stock([10, 1, 5, 6, 7, 1]))
