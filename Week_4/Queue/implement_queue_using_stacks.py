class MyQueue:

    def __init__(self):
        self.queue = []
        self.size = 0

    def push(self, x: int) -> None:
        self.queue = [x] + self.queue
        self.size += 1

    def pop(self) -> int:
        self.size -= 1
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return self.size == 0
