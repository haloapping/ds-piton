from typing import Any


class Deque:
    max_cap: int
    rear: int
    items: list[Any]

    def __init__(self, max_cap: int) -> None:
        self.max_cap = max_cap
        self.rear = -1
        self.items = []

    def is_empty(self) -> bool:
        return self.rear == -1

    def is_full(self) -> bool:
        return self.rear + 1 == self.max_cap

    def peek_front(self) -> str | list[Any]:
        if self.is_empty():
            return "stack is empty"

        return self.items[0]

    def peek_rear(self) -> str | list[Any]:
        if self.is_empty():
            return "stack is empty"

        return self.items[-1]

    def enqueue_front(self, item: Any) -> str:
        if self.is_full():
            return "queue is full"

        self.rear += 1
        self.items.insert(0, item)

        return f"enqueue front {self.items[0]}"

    def enqueue_rear(self, item: Any) -> str:
        if self.is_full():
            return "queue is full"

        self.rear += 1
        self.items.append(item)

        return f"enqueue front {self.items[-1]}"

    def dequeue_front(self) -> str:
        if self.is_empty():
            return "queue is empty"

        self.rear -= 1
        front = self.items.pop(0)

        return f"dequeue front {front}"

    def dequeue_rear(self) -> str:
        if self.is_empty():
            return "queue is empty"

        self.rear -= 1
        front = self.items.pop()

        return f"dequeue front {front}"

    def all_items(self) -> str | list[Any]:
        if self.is_empty():
            return "queue is empty"

        return self.items
