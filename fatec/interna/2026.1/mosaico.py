TESTE = True


def mosaico(black_bricks: int):
    def calc(n: int):
        return 4 * (n + 1)

    scale = 1
    white_bricks = 0

    while True:
        black_bricks -= calc(scale)
        if black_bricks < 0:
            break

        white_bricks += scale * scale
        scale += 1

    print(white_bricks)


if TESTE:
    mosaico(80)
    mosaico(108)
    mosaico(5)
    mosaico(8)
    mosaico(10)
else:
    mosaico(int(input()))
