def lock(correct_set, current_set):
    steps_senquence = []

    for correct_digit, current_digit in zip(correct_set, current_set):
        if correct_digit == current_digit:
            steps_senquence.append("0")
            continue

        if (correct_digit == "0" and current_digit == "5") or (
            correct_digit == "5" and current_digit == "0"
        ):
            steps_senquence.append("1" * 5)
            continue

        if int(correct_digit) > int(current_digit):
            direction, steps = min(
                ("up", int(correct_digit) - int(current_digit)),
                ("down", 10 - int(correct_digit) + int(current_digit)),
                key=lambda x: x[1],
            )
        else:
            direction, steps = min(
                ("down", int(current_digit) - int(correct_digit)),
                ("up", 10 - int(current_digit) + int(correct_digit)),
                key=lambda x: x[1],
            )

        steps_senquence.append("1" * steps if direction == "up" else "-1" * steps)

    return " ".join(steps_senquence)


# print(lock("911007", "312914"))
# print(lock("911007", "312914"))
# print(lock("249", "672"))
# print(lock("1111", "3209"))
# print(lock("12345678", "22042013"))
print(lock("05", "50"))
