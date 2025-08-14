n = 8
tree = [11, 7, 3, 19, 13, 7, 17, 5]

for i in range(n):
    node = tree[i]
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2

    if left_child_index < n:
        left_child = tree[left_child_index]
        print(
            f"Nó ({node}) no índice ({i}) tem filho esquerdo no índice {left_child_index} ({left_child})"
        )

    if right_child_index < n:
        right_child = tree[right_child_index]
        print(
            f"Nó ({node}) no índice ({i}) tem filho esquerdo no índice {left_child_index} ({left_child})"
        )
