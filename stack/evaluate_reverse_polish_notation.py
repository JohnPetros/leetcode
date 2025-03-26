def evaluate_reverse_polish_notation(tokens: list[str]) -> int:
    if len(tokens) == 1:
        return int(tokens[0])

    stack = list()

    def is_number(string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    for token in tokens:
        if is_number(token):
            stack.append(token)
        else:
            second_operand = int(stack.pop())
            first_operand = int(stack.pop())
            match token:
                case "+":
                    stack.append(first_operand + second_operand)
                case "-":
                    stack.append(first_operand - second_operand)
                case "*":
                    stack.append(first_operand * second_operand)
                case "/":
                    stack.append(int(first_operand / second_operand))

    return stack.pop()


print(evaluate_reverse_polish_notation(["2", "1", "+", "3", "*"]))
print(evaluate_reverse_polish_notation(["4", "13", "5", "/", "+"]))
print(
    evaluate_reverse_polish_notation(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)
print(evaluate_reverse_polish_notation(["4", "3", "-"]))
print(evaluate_reverse_polish_notation(["4", "-2", "/", "2", "-3", "-", "-"]))
