from math import factorial, ceil

X = 10
PI = 3.1415
R = X * PI / 180

total = 0

for n in range(5):
    total += (-1) ** n * ((R ** (2 * n)) / factorial(2 * n))


fourth_place = int(total * 10000 % 10)

if fourth_place >= 7:
    total = ceil(total * 1000) / 1000

print(total)
