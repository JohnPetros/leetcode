def chamada(students: set[int], day1: set[int], day2: set[int]):
    both_days_count = 0
    none_days_count = 0

    for student in students:
        if student in day1 and student in day2:
            both_days_count += 1

        if student not in day1 and student not in day2:
            none_days_count += 1

    print(both_days_count)
    print(none_days_count)


################################################### Teste

# chamada(set([5, 3, 2, 1, 4]), set([5, 2, 4]), set([3, 4]))
# chamada(set([7, 3, 10, 2, 4, 1, 5]), set([3, 2, 4, 1]), set([7, 3, 4, 1, 5]))

################################################### Final

try:
    while True:
        total_students, total_day1, total_day2 = map(int, input().split())

        students = set(map(int, input().split()))
        day1 = set(map(int, input().split()))
        day2 = set(map(int, input().split()))

        chamada(students, day1, day2)

except EOFError:
    pass
