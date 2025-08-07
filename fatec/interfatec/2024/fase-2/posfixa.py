inputs = [
    "A+B",
    "A/2",
    "A+B*C",
    "(A+B)*C",
    "(A+B)/(C-D)",
    "X^Y/Z",
    "X^(Y/Z)",
    "2*A+B",
    "X+Y^2",
    "(X+Y)^2",
]

priotity = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

for input in inputs:
    infix = input
    stack = []
    posfix = ""

    for char in infix:
        if char.isalnum():
            posfix += char
        elif char == "(":
            stack.append(char)
        elif char == ")":
            operand = ""
            while True:
                operand = stack.pop()
                if operand == "(":
                    break
                posfix += operand
        else:
            while (
                stack
                and stack[-1] != "("
                and priotity.get(stack[-1], 0) >= priotity.get(char, 0)
            ):
                posfix += stack.pop()
            stack.append(char)

    while stack:
        posfix += stack.pop()

    print(posfix)
