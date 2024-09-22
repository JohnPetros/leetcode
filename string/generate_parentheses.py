def generate_parentheses(parentheses_count: int):
    parentheses_list = []

    def backtrack(
        generated_parentheses: str, open_brackets_count: int, closed_brackets_count: int
    ):
        print(generated_parentheses)
        if len(generated_parentheses) == 2 * parentheses_count:
            parentheses_list.append(generated_parentheses)
            return

        if open_brackets_count < parentheses_count:
            backtrack(
                generated_parentheses + "(",
                open_brackets_count + 1,
                closed_brackets_count,
            )
        if closed_brackets_count < open_brackets_count:
            backtrack(
                generated_parentheses + ")",
                open_brackets_count,
                closed_brackets_count + 1,
            )

    backtrack("", 0, 0)
    return parentheses_list


print(generate_parentheses(2))
