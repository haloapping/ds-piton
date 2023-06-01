class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.prev: Node = None
        self.next: Node = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.len: int = 0

    def is_empty(self) -> bool:
        return self.head is None

    def peek_front(self) -> str:
        if self.is_empty():
            return "linked list is empty"

        return f"peek {self.head.val}"

    def peek_rear(self) -> str:
        if self.is_empty():
            return "linked list is empty"

        pointer_node = self.head

        while pointer_node.next is not None:
            pointer_node = pointer_node.next

        return f"peek {pointer_node.val}"

    def insert_front(self, val: int) -> str:
        new_node = Node(val)

        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        return f"insert front {self.head.val}"

    def remove_front(self) -> str:
        if self.is_empty():
            return "linked list is empty"

        front = self.head.val
        self.head = self.head.next

        return f"remove front {front}"

    def remove_rear(self) -> str:
        if self.is_empty():
            return "linked list is empty"

        pointer_node = self.head

        while pointer_node.next.next is not None:
            pointer_node = pointer_node.next

        rear = pointer_node.next.val
        pointer_node.next.prev = None
        pointer_node.next = None

        return f"remove rear {rear}"

    def insert_rear(self, val) -> str:
        new_node = Node(val)

        if self.is_empty():
            self.head = new_node

            return f"insert rear {self.head.val}"
        else:
            pointer_node = self.head

            while pointer_node.next is not None:
                pointer_node = pointer_node.next

            pointer_node.next = new_node
            new_node.prev = pointer_node.next

            return f"insert rear {pointer_node.next.val}"

    def all_nodes(self) -> list:
        if self.is_empty():
            return []

        pointer_node = self.head
        nodes = []

        while pointer_node is not None:
            nodes.append(pointer_node.val)
            pointer_node = pointer_node.next

        return nodes
