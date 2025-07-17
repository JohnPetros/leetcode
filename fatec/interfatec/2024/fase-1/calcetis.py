from itertools import combinations
import random

# current_price, items_count = list(map(int, input().split())) 
# target_price = 200 - current_price
# items_prices = []
# for _ in range(items_count):
#   items_prices.append(int(input()))

items_prices = []
current_price = 53
target_price = 200 - current_price
items_prices = [
  50,
  30,
  33,
  91,
  68,
  40,
  30,
  32,
  41,
  39,
]
items_prices_set = set(items_prices)
items_count = len(items_prices)

is_free = False


for item_1_index in range(items_count - 1):
  for item_2_index in range(item_1_index + 1, items_count):
    item_1_price = items_prices[item_1_index]
    item_2_price = items_prices[item_2_index]
    needed_price = target_price - item_1_price - item_2_price
    
    if needed_price in items_prices_set:
      is_free = True
      
print("fretegratis" if is_free else "fretepago")
