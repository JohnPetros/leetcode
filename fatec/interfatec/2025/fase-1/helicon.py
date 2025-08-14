integers = list(map(int, "3 -1 4 -1 5 -9".split()))
integer_count = len(integers)

step = 1
max_sum = float("-inf")

for end in range(1, integer_count // 2 + 1):
    for start in range(end):
        print(integers[start::end])
        max_sum = max(sum(integers[start::end]), max_sum)

print(max_sum)
