class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x):
        self.stack.append(x)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def empty(self):
        return self.size == 0
