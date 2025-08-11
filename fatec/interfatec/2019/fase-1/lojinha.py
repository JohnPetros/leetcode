inputs = [
    "5 35.80",
    "2 155.10",
    "10 26.50",
]

total = 0

for input in inputs:
    qtd, price = input.split()
    total += int(qtd) * float(price)

print(total)
