events = [
    3,
    -5,
    3,
]

balance = 0
deficit = 0

for evento in events:
    balance += evento

    if balance < deficit:
        deficit = balance


print(abs(deficit))
