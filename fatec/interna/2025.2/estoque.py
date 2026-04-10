TESTE = True


def estoque(purchase: list[str], storage: list[str]):
    storage_set = set(storage)
    missing = [item for item in purchase if item not in storage_set]
    if len(missing) == 0:
        print("ESTOQUE OK")
    else:
        print(" ".join(map(str, missing)))


if TESTE:
    estoque(
        [
            "1461392111001",
            "1461392111004",
            "1461392111005",
            "1461392111006",
            "1461392111009",
        ],
        ["1461392111004", "1461392111005", "1461392111004", "1461392111005"],
    )
    estoque(
        [
            "1461392111001",
            "1461392111004",
            "1461392111005",
            "1461392111006",
            "1461392111009",
        ],
        [
            "1461392111001",
            "1461392111004",
            "1461392111005",
            "1461392111006",
            "1461392111009",
        ],
    )
    purchase = set()
    storage = set()
else:
    purchase_count = int(input())
    storage_count = int(input())
    purchase = list()
    storage = list()
    for item in input().split()[:purchase_count]:
        purchase.append(item)
    for item in input().split()[:storage_count]:
        storage.append(item)
    estoque(purchase, storage)
