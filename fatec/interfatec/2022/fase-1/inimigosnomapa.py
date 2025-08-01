enimies_count = 10
inputs = [
    "1 1",
    "1 -1",
    "-1 1",
    "-1 -1",
    "2 2",
]

squarei = 0
squareii = 0
squareiii = 0
squareiv = 0

for input in inputs:
    x, y = input.split()
    x = int(x)
    y = int(y)

    if x > 0 and y > 0:
        squarei += 1
    elif x > 0 and y < 0:
        squareii += 1
    elif x < 0 and y < 0:
        squareiii += 1
    else:
        squareiv += 1


print(f"I = {squarei}")
print(f"II = {squareii}")
print(f"III = {squareiii}")
print(f"IV = {squareiv}")
