import unittest

from main.doublylinkedlist import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def test_is_empty(self):
        dll = DoublyLinkedList()

        self.assertTrue(dll.is_empty())

    def test_insert_front_when_empty(self):
        dll = DoublyLinkedList()

        self.assertEqual(dll.insert_front(1), f"insert front {dll.head.val}")

    def test_remove_front_when_empty(self):
        dll = DoublyLinkedList()

        self.assertEqual(dll.remove_front(), f"linked list is empty")

    def test_remove_front_when_not_empty(self):
        dll = DoublyLinkedList()

        for val in range(5):
            dll.insert_front(val)

        self.assertEqual(dll.remove_front(), f"remove front 4")

    def test_remove_rear_when_empty(self):
        dll = DoublyLinkedList()

        self.assertEqual(dll.remove_rear(), f"linked list is empty")

    def test_remove_rear_when_not_empty(self):
        dll = DoublyLinkedList()

        for val in range(5):
            dll.insert_rear(val)

        self.assertEqual(dll.remove_rear(), f"remove rear 4")

    def test_insert_front_when_not_empty(self):
        dll = DoublyLinkedList()

        for val in range(5):
            dll.insert_front(val)

        self.assertEqual(dll.insert_front(5), f"insert front {dll.head.val}")

    def test_insert_rear_when_empty(self):
        dll = DoublyLinkedList()

        self.assertEqual(dll.insert_rear(1), f"insert rear {dll.head.val}")

    def test_insert_rear_when_not_empty(self):
        dll = DoublyLinkedList()

        for val in range(5):
            dll.insert_rear(val)

        self.assertEqual(dll.insert_rear(5), f"insert rear 5")

    def test_peek_front_when_empty(self):
        dll = DoublyLinkedList()

        self.assertEqual(dll.peek_front(), "linked list is empty")

    def test_peek_front_when_not_empty(self):
        dll = DoublyLinkedList()

        for val in range(5):
            dll.insert_front(val)

        self.assertEqual(dll.peek_front(), f"peek 4")

    def test_peek_rear_when_empty(self):
        dll = DoublyLinkedList()

        self.assertEqual(dll.peek_rear(), "linked list is empty")

    def test_peek_rear_when_not_empty(self):
        dll = DoublyLinkedList()

        for val in range(5):
            dll.insert_rear(val)

        self.assertEqual(dll.peek_rear(), f"peek 4")

    def test_all_nodes_when_empty(self):
        dll = DoublyLinkedList()

        self.assertListEqual(dll.all_nodes(), [])

    def test_all_nodes_when_after_insert_front(self):
        dll = DoublyLinkedList()

        for val in range(5):
            dll.insert_front(val)

        self.assertListEqual(dll.all_nodes(), [4, 3, 2, 1, 0])

    def test_all_nodes_when_after_insert_rear(self):
        dll = DoublyLinkedList()

        for val in range(5):
            dll.insert_rear(val)

        self.assertListEqual(dll.all_nodes(), [0, 1, 2, 3, 4])

    def test_all_nodes_when_after_remove_front(self):
        dll = DoublyLinkedList()

        for val in range(5):
            dll.insert_front(val)

        for _ in range(3):
            dll.remove_front()

        self.assertListEqual(dll.all_nodes(), [1, 0])

    def test_all_nodes_when_after_remove_rear(self):
        dll = DoublyLinkedList()

        for val in range(5):
            dll.insert_rear(val)

        for _ in range(3):
            dll.remove_rear()

        self.assertListEqual(dll.all_nodes(), [0, 1])


if __name__ == "__main__":
    unittest.main()
