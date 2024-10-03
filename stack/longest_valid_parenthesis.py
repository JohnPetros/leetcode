from _stack import Stack


def longest_valid_parenthesis(parenthesis: str) -> list[int]:
    max_length = 0

    if not parenthesis:
        return max_length

    stack = Stack()
    stack.push(-1)

    for index, symbol in enumerate(parenthesis):
        if symbol == "(":
            stack.push(index)
        else:
            stack.pop()
            if not stack:
                stack.push(index)
            else:
                max_length = max(index - stack.peek(), max_length)

    return max_length


print(longest_valid_parenthesis(")()())"))
