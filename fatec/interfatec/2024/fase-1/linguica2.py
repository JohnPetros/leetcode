n = 8
tree = [11, 7, 3, 19, 13, 7, 17, 5]

eh_tipo_1 = True
eh_tipo_2 = True

for i in range(n):
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2

    # Verifica o filho esquerdo
    if left_child_index < n:
        if eh_tipo_1 and tree[i] > tree[left_child_index]:
            eh_tipo_1 = False
        if eh_tipo_2 and tree[i] < tree[left_child_index]:
            eh_tipo_2 = False

    # Verifica o filho direito
    if right_child_index < n:
        if eh_tipo_1 and tree[i] > tree[right_child_index]:
            eh_tipo_1 = False
        if eh_tipo_2 and tree[i] < tree[right_child_index]:
            eh_tipo_2 = False

if eh_tipo_1 and not eh_tipo_2:
    print(1)
elif not eh_tipo_1 and eh_tipo_2:
    print(2)
else:
    print(0)
