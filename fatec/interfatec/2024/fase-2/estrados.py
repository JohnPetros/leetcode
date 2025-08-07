inputs = [
    "88 8 8",
    "88 8 5",
    "88 6 4",
    "88 6 3",
    "96 4 3",
    "96 7 3",
    "96 10 4",
    "120 8 3",
    "120 10 4",
    "200 8 3",
    "200 12 4",
    "200 14 5",
]

for input in inputs:
    total, quantity, width = list(map(int, input.split()))
    gap = (total - quantity * width) / (quantity - 1)
    if gap < 10:
        print("projeto superdimensionado")
    elif gap > 20:
        print("projeto subdimensionado")
    else:
        print("projeto ok")
