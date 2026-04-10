TESTE = True


def competencias(main_student: int, students: int, points: int, criteria: int):
    points_per_student = points // students
    rest = points % students
    table = []

    for i in range(students):
        student_points = (
            points_per_student + rest if i + 1 == main_student else points_per_student
        )
        student_row = []
        for _ in range(criteria):
            if student_points >= 3:
                student_points -= 3
                student_row.append(3)
            elif student_points >= 2:
                student_points -= 2
                student_row.append(2)
            elif student_points >= 1:
                student_points -= 1
                student_row.append(1)
            else:
                student_row.append(0)

        table.append(student_row)

    for row in table:
        print(" ".join(map(str, row)))


if TESTE:
    # competencias(2, 5, 38, 6)
    # competencias(3, 4, 35, 3)
    competencias(1, 4, 7, 6)
else:
    main_student, students, points, criteria = list(map(int, input().split()))
    competencias(main_student, students, points, criteria)
