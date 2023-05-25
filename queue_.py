class Queue:
    def __init__(self, max_cap) -> None:
        self.rear: int = -1
        self.max_cap: int = max_cap
        self.items: list[int] = []

    def is_empty(self) -> bool:
        return self.rear == -1

    def is_full(self) -> bool:
        return self.rear + 1 == self.max_cap

    def peek(self) -> str:
        if self.is_empty():
            return "queue is empty"

        return f"front: {self.items[0]}"

    def enqueue(self, item: int) -> str:
        if self.is_full():
            return "queue is full"

        self.items.append(item)
        self.rear += 1

        return f"enqueue {self.items[0]}"

    def dequeue(self) -> str:
        if self.is_empty():
            return "queue is empty"

        front = self.items[0]
        self.items.pop(0)
        self.rear -= 1

        return f"dequeue {front}"

    def search(self, item: int) -> str | tuple[int, bool]:
        if self.is_empty():
            return "queue is empty"
        else:
            try:
                idx = self.items.index(item) + 1
                return (idx, True)
            except ValueError:
                return (-1, False)
