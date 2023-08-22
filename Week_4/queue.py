class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def push(self, x):
        self.queue = [x] + self.queue
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.queue.pop()

    def peek(self):
        return self.queue[-1]

    def empty(self):
        return self.size == 0
