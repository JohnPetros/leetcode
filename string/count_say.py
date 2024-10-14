def count_say(n: int) -> str:
    if n == 1:
        return "1"

    previous_string = count_say(n - 1)
    new_string = ""
    count = 1

    for index in range(len(previous_string)):
        char = previous_string[index]
        if index < len(previous_string) - 1 and char == previous_string[index + 1]:
            count += 1
        else:
            new_string += f"{count}{char}"
            count = 1

    return new_string


print(count_say(5))  # 111221
