import string

TESTE = True


def convert(s: str):
    return sum([string.ascii_letters.index(char) + 1 for char in s.lower()])


def snakedor(names: list[str]):
    print(string.ascii_letters)
    names.sort(key=lambda name: (convert(name), name.lower()))
    print(" ".join(names))


if TESTE:
    snakedor(["Clara", "Bianca", "Amanda"])
    snakedor(["Gabrielle", "Isabela", "Isaura", "Jessica", "Leticia", "Marya", "Wendy"])
else:
    snakedor(input().split())
