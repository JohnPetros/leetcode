def valid_parentheses(parentheses: str) -> bool:
    parentheses_pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    stack = []

    for parenthese in parentheses:
        if parenthese in parentheses_pairs:
            stack.append(parenthese)
        elif stack:
            parenthese_pair = stack.pop()
            if parenthese != parentheses_pairs[parenthese_pair]:
                return False
        else:
            return False

    return not stack


# print(valid_parentheses("()"))
# print(valid_parentheses("()[]{}"))
# print(valid_parentheses("([])"))
# print(valid_parentheses("["))
# print(valid_parentheses("(("))
# print(valid_parentheses("){"))
# print(valid_parentheses(")(){}"))
