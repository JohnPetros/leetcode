import math


def tree_height(n):
    if n <= 0:
        return -1

    altura = math.floor(math.log2(n))

    return altura


n = 8  # Número de nós
height = tree_height(n)
print(f"A altura da árvore é {height}")
