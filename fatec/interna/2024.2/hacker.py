def tenta_caminho(matrix, key, rows, cols, start_col):
    k = 0  # índice atual na chave
    col = start_col
    row = 0  # começa na primeira linha

    while k < len(key):
        achou = False

        if k % 2 == 0:
            # índice par → desce a coluna
            for next_row in range(row + 1, rows):
                if matrix[next_row][col] == key[k]:
                    row = next_row
                    achou = True
                    break
        else:
            # índice ímpar → avança na linha
            for next_col in range(col + 1, cols):
                if matrix[row][next_col] == key[k]:
                    col = next_col
                    achou = True
                    break

        if not achou:
            return False
        k += 1

    return True


def hacker(rows, cols, matrix, key):
    for start_col in range(cols):
        if tenta_caminho(matrix, key, rows, cols, start_col):
            print("VALIDA")
            return
    print("INVALIDA")
