class Stack:
    def __init__(self, max_cap: int = 5):
        self.top: int = -1
        self.max_cap: int = max_cap
        self.items: list[int] = []

    def is_empty(self) -> bool:
        return self.top == -1

    def is_full(self) -> bool:
        return self.top + 1 == self.max_cap

    def peek(self) -> str:
        if self.is_empty():
            return "stack is empty"

        return f"top {self.items[-1]}"

    def pop(self) -> str:
        if self.is_empty():
            return "stack is empty"

        top = self.items[-1]
        self.top -= 1
        self.items.pop()

        return f"pop {top}"

    def push(self, item: int) -> str:
        if self.is_full():
            return "stack is full"

        self.top += 1
        self.items.append(item)

        return f"push {self.items[-1]}"

    def search(self, item: int) -> str | tuple[int, bool]:
        if self.is_empty():
            return "stack is empty"

        for idx, i in enumerate(self.items):
            if i == item:
                return (idx + 1, True)

        return (-1, False)

    def show_all_items(self) -> str | list[int]:
        if self.is_empty():
            return "stack is empty"

        return self.items
