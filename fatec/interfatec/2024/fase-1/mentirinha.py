# number = int(input())

# integer = 7
# integer = 4
# integer = 994009
integer = 999983
counter = 0
for number in range(1, integer + 1):
    if integer % number == 0:
        counter += 1

answer = "sim" if counter == 3 else "não"
print(answer)
