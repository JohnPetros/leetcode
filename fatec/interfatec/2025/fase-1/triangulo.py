from math import sin, radians

a = 10.00
b = 10.00
g = 30.00


height = round(sin(radians(g)), 15) * a
print(f"{round(b * height / 2, 4):.4f}")
