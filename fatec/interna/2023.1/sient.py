def sient(numbers: list[str]):
    trie = {}
    count = 0

    for number in numbers:
        current = trie
        for digit in number:
            if digit not in current:
                current[digit] = {}
                count += 1
            current = current[digit]

    print(count)


################################################### Teste


# sient(["0467123456"])
# sient(["0123456789", "0123"])
# sient(["0412578440", "0412199803", "0468892011", "112", "15"])

################################################### Final

try:
    while True:
        total = int(input())
        numbers = []
        for _ in range(total):
            numbers.append(input())

        sient(numbers)
except EOFError:
    pass
