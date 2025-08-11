cards = [
    "10 20 30 40",
    "10 20 30 50",
]

danette_cards = []
silvio_cards = []
danette_score = 0
silvio_score = 0
ties = 0

for _ in range(len(cards) // 2):
    attribute1, attribute2, attribute3, attribute4 = cards.pop(0).split()
    danette_cards.append(
        (int(attribute1), int(attribute2), int(attribute3), int(attribute4))
    )

for card in cards:
    attribute1, attribute2, attribute3, attribute4 = card.split()
    silvio_cards.append(
        (int(attribute1), int(attribute2), int(attribute3), int(attribute4))
    )


for danette_card, silvio_card in zip(danette_cards, silvio_cards):
    index = 0
    while index < 4 and danette_card[index] == silvio_card[index]:
        index += 1

    if index < 4:
        if danette_card[index] > silvio_card[index]:
            danette_score += 1
        else:
            silvio_score += 1
    else:
        ties += 1


print(f"danette venceu: {danette_score}")
print(f"silvio venceu: {silvio_score}")
print(f"empates: {ties}")
