class MyStack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.size += 1

    def pop(self) -> int:
        self.size -= 1
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return self.size == 0
