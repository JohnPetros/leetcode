height = 3
leaf_inputs = [
    "2 2NSWZBJXMMZQ17YRF4TBSPCBSHN8L26WVRFX",
    "7 0QRB4ZL3DGHSOEA77SL5TXK2UMBE36EPJ",
    "12 QWL392VYHDVQMZZ2CZOBSBN0HQMAVXGOLYHO5NSY",
    "13 Aa",
]
decisions = [False]

leafs = {int(pos): val for pos, val in (line.split() for line in leaf_inputs)}

current_node = 1

for decision in decisions:
    if decision:
        current_node = current_node * 2 + 1
    else:
        current_node = current_node * 2

print(leafs[current_node])
