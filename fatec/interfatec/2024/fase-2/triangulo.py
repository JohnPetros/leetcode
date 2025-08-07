from math import sqrt

sides = list(map(float, "8.00 6.00 10.00".split()))

peremeter = sum(sides) / 2

area = sqrt(
    peremeter * (peremeter - sides[0]) * (peremeter - sides[1]) * (peremeter - sides[2])
)

print(round(area, 2))
