from collections import Counter

TESTE = True


def jogo(matrix: list[str]):

    for row_index in range(len(matrix)):
        row = matrix[row_index]
        counter = Counter(row)
        if len(counter) > 1:
            column_index = 0
            for char, count in counter.items():
                if count == 1:
                    column_index = row.index(char)

            print(f"LINHA {row_index + 1} COLUNA {column_index + 1}")
            return


if TESTE:
    jogo(
        [
            "DDDDD",
            "DDBDD",
            "DDDDD",
        ]
    )
    jogo(
        [
            "aaa",
            "aaa",
            "aaa",
            "aaa",
            "aaa",
            "aaa",
            "aaa",
            "a5a",
        ]
    )
    jogo(
        [
            "Zzz",
        ]
    )
    jogo(
        [
            "MMM",
            "M7M",
        ]
    )
else:
    import sys

    matrix = [line.rstrip("\n") for line in sys.stdin]
    jogo(matrix)
