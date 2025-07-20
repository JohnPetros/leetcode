from sys import stdin

names = []

try:
    names = stdin.readlines()
except EOFError:
    ...


for name in names:
    if len(name) <= 2:
        print(f"{name[0]} {name[0]}")
    print(
        " ".join(
            [
                name[index]
                if index == 0 or index == len(name) - 1
                else f"{name[index][0]}."
                for index in range(len(name))
            ]
        )
    )
