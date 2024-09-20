from _stack import Stack


def valid_parentheses(parentheses: str) -> bool:
    stack = Stack()
    open_brackets = ["(", "{", "["]
    closed_brackets_map = {
        ")": open_brackets[0],
        "}": open_brackets[1],
        "]": open_brackets[2],
    }

    for bracket in parentheses:
        if bracket in open_brackets:
            stack.push(bracket)
            continue

        if bracket in closed_brackets_map:
            if not len(stack) or closed_brackets_map[bracket] != stack.pop():
                return False

            return False

    return not len(stack)


# print(valid_parentheses("()"))
# print(valid_parentheses("()[]{}"))
# print(valid_parentheses("([])"))
# print(valid_parentheses("["))
# print(valid_parentheses("(("))
# print(valid_parentheses("){"))
# print(valid_parentheses(")(){}"))
