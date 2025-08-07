from collections import deque

# text = "O rato roeu a roupa do rei de Roma"
text = "O rato roeu a roupa do rei de Roma"
total_space = 12

words = deque(text.split())
lines = []
line = []
gaps = []

while words:
    word = words[0]
    line.append(word)
    space = sum(len(word) for word in line)
    minimum_left_space = len(line) - 1

    if space + minimum_left_space > total_space:
        line.pop()
        lines.append(line)
        line = []
    else:
        last_word = words.popleft()
        if not words and last_word:
            lines.append(line)


for index in range(len(lines)):
    if index == len(lines) - 1:
        gap = 1
    elif len(lines[index]) == 1:
        gap = 0
    else:
        left_space = total_space - sum(len(word) for word in lines[index])
        gap = left_space / (len(lines[index]) - 1)
    gaps.append(round(gap, 3))

print(gaps)
