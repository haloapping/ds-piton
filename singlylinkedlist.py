class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.len = 0

    def is_empty(self) -> bool:
        return self.head is None

    def peek_front(self) -> int | None:
        if self.is_empty():
            return None

        return self.head.val

    def peek_rear(self) -> int | None:
        if self.is_empty():
            return None

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        return current_node.val

    def insert_front(self, val: int) -> str:
        new_node = Node(val)

        new_node.next = self.head
        self.head = new_node
        self.len += 1

        return f"insert front {self.head.val}"

    def remove_front(self) -> str:
        if self.is_empty():
            return "linked list is empty"

        front = self.head.val
        self.head = self.head.next
        self.len -= 1

        return f"remove front {front}"

    def insert_rear(self, val: int) -> str:
        new_node = Node(val)

        if self.is_empty():
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head

            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node

        self.len += 1

        return f"insert rear {self.head.val}"

    def remove_rear(self) -> str:
        if self.is_empty():
            return "linked list is empty"
        elif self.len == 1:
            self.head = None
            self.len -= 1
        else:
            current_node = self.head

            while current_node.next.next is not None:
                current_node = current_node.next

            rear = current_node.next.val
            current_node.next = None

            self.len -= 1
            return f"remove rear {rear}"

    def search(self, val: int) -> tuple[bool, int]:
        items = self.all_items()

        try:
            return True, items.index(val)
        except ValueError:
            return False, -1

    def all_items(self) -> list:
        current_node = self.head
        nodes: list = []

        while current_node is not None:
            nodes.append(current_node.val)
            current_node = current_node.next

        return nodes
