from collections import deque

class CircularBuffer:
    def __init__(self, size: int):
        self.buffer = deque(maxlen=size)
        self.size = size

    def enqueue(self, value):
        if self.is_full():
            self.dequeue()
        self.buffer.append(value)

    def dequeue(self):
        return self.buffer.popleft() if self.buffer else None

    def is_full(self):
        return len(self.buffer) == self.size

    def __str__(self):
        return f"Buffer: {list(self.buffer)}"

buf = CircularBuffer(3)
buf.enqueue(1)
buf.enqueue(2)
buf.enqueue(3)
buf.enqueue(4)
print(buf)
