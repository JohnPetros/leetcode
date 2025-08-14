integers = list(map(int, "-5 2 1 7 -3 -4 -8 10 -6 1 -1 3".split()))
integer_count = len(integers)

step = 1
start = 0
max_sum = 0

while step < integer_count:
    max_sum = max(sum(integers[start::step]), max_sum)
    step += 1

print(max_sum)
