# i = H × 100 ÷ C

inputs = [
    [0.8, 16.0, 1.2],
    [1.0, 25.5, 0.7],
    [1.2, 30.0, 1.2],
    [1.5, 32.5, 1.2],
    [1.5, 20.0, 0.9],
    [1.8, 20.0, 0.9],
    [1.8, 30.0, 0.9],
    [3.0, 40.0, 1.0],
    [3.0, 36.0, 1.0],
    [3.0, 30.0, 1.0],
]


for input in inputs:
    H, C, L = input
    i = H * 100 / C
    if L >= 0.8 and i <= 8.334:
        print("PROJETO SIMPLES")
    else:
        print("PROJETO ESPECIAL")
