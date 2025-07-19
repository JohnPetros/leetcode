from collections import deque

# force = int(input())
# rows, columns = list(map(int, "4 7".split()))

# map = []
# count = 1

# map = []
# for _ in range(rows):
#     row = input().split()
#     map.append(row)

force = 10
rows, columns = list(map(int, "4 7".split()))
map = [
    ["S", ".", ".", "2", ".", ".", "."],
    [".", ".", "3", ".", "#", ".", "."],
    [".", ".", ".", "#", ".", ".", "."],
    [".", ".", "1", ".", "1", ".", "K"],
]
seen = set((0, 0))
queue = deque([(0, 0, 0)])
movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
final_steps = 0

while queue:
    row, column, steps = queue.popleft()

    for row_movement, column_movement in movements:
        row, column = row + row_movement, column + column_movement

        if 0 <= row < rows and 0 <= column < columns:
            if (row, column) not in seen:
                cell = map[row][column]

                if cell == "K":
                    final_steps = steps + 1
                    queue = deque()
                    break

                can_pass = False
                if cell == ".":
                    can_pass = True
                elif cell.isdigit() and force >= int(cell):
                    can_pass = True

                if can_pass:
                    seen.add((row, column, steps))
                    queue.append((row, column, steps + 1))


if final_steps == 0:
    print("N")
else:
    print(final_steps)
