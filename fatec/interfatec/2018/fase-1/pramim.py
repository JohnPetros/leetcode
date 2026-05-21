TEST = True


def pramim(turn: str, notes: list[int]):
    voce, amigo = 0, 0
    index = 0
    total = len(notes)

    while index < total:
        if turn == "V":
            turn = "A"
            voce += notes[index]
        else:
            turn = "V"
            amigo += notes[index]
        index += 1

    print(f"VOCE: {voce} AMIGO: {amigo}")


if TEST:
    pramim("V", [10, 20, 50, 2])
    pramim("A", [10, 10, 50, 20, 100, 2, 5])
else:
    turn, note_count = input().split()
    notes = []
    for _ in range(int(note_count)):
        notes.append(int(input()))
    pramim(turn, notes)
