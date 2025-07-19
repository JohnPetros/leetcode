position = [3, 3]
max_line = 5
max_column = 5
colisions = 0
battery = 10
moves = "EEEEEEDDDDDD"

for move in moves:
    match move:
        case "C":
            position[0] -= 1
            if position[0] == 0:
                position[0] = 1
                colisions += 1

        case "B":
            position[0] += 1
            if position[0] > max_line:
                position[0] = max_line
                colisions += 1

        case "E":
            position[1] -= 1
            if position[1] == 0:
                position[1] = 1
                colisions += 1

        case "D":
            position[1] += 1
            if position[1] > max_column:
                position[1] = max_column
                colisions += 1

    battery -= 1
    if battery == 0:
        break


print(f"{position[0]} {position[1]} {colisions}")
