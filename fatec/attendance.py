def attendance(
    students: list[str], day_1_students: list[str], day_2_students: list[str]
):
    absents_count = 0
    attendances_count = 0

    for student in students:
        if student in day_1_students and student in day_2_students:
            attendances_count += 1

        if student not in day_1_students and student not in day_2_students:
            absents_count += 1

    print(attendances_count)
    print(absents_count)


input()
students = input().split()
absents = input().split()
attendances = input().split()

attendance(students, absents, attendances)
# attendance((5, 3, 2, 1, 4), (5, 2, 4), (3, 4))
# attendance((7, 3, 10, 2, 4, 1, 5), (3, 2, 4, 1), (7, 3, 4, 1, 5))
