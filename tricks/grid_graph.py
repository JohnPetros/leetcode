input_texto = """0000000000
1100011111
0110010000
0011110000
0010011110
1110000010
0011110000
0000011111
0000010000
0000010000"""


maze = []

for row in input_texto.strip().split("\n"):
    row = [int(char) for char in row]
    maze.append(row)

print(maze)
