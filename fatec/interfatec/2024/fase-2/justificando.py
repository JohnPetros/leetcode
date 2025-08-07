# text = "O rato roeu a roupa do rei de Roma"
text = "O rato roeu a roupa do rei de Roma"
total_width = 12

words = text.split()


width = 0
gaps = []

index = 0
start = 0
end = 0

while end < len(words):
    word = words[end]
    width += len(word)
    window = words[start : end + 2]

    if end == len(words) - 1 or width + len(window) >= total_width:
        window = words[start : end + 1]
        if len(window) == 1:
            gap = 0
        else:
            left_space = total_width - sum(len(word) for word in window)
            gap = left_space / (len(window) - 1)
        gaps.append(gap)
        start += len(window)
        end += 1
        width = 0
    else:
        end += 1


print(gaps)
