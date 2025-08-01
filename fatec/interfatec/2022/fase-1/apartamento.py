# M = C * (1 + i)t


initial = 500000.00
target = 350000.00
interest = 0.5 / 100

if initial >= target:
    print("pode comprar agora")

else:
    months = 0

    while initial <= target:
        months += 1
        initial *= 1 + interest

    print(f"possível em {months} {'mes' if months == 1 else 'meses'}")
