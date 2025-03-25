class MinimumStack:
    def __init__(self):
        self.stack = list()
        self.min_stack = list()

    def push(self, value):
        if not len(self.stack):
            self.stack.append(value)
            self.min_stack.append(value)
            return

        minimum_value = self.min_stack[len(self.min_stack) - 1]
        self.stack.append(value)
        self.min_stack.append(min(minimum_value, value))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[len(self.stack) - 1]

    def get_min(self):
        return self.min_stack[len(self.min_stack) - 1]


minimum_stack = MinimumStack()
minimum_stack.push(1)
minimum_stack.push(2)
minimum_stack.push(0)
print(minimum_stack.get_min())
minimum_stack.pop()
print(minimum_stack.top())
print(minimum_stack.get_min())
