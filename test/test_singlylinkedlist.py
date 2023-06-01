import os
import sys
import unittest

sys.path.append(os.getcwd()[: len(os.getcwd()) - 5])
from main.singlylinkedlist import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    def test_is_empty(self):
        sll = SinglyLinkedList()

        self.assertTrue(sll.is_empty())

    def test_insert_front_when_empty(self):
        sll = SinglyLinkedList()

        self.assertEqual(sll.insert_front(1), f"insert front {sll.head.val}")

    def test_insert_front_when_head_not_empty(self):
        sll = SinglyLinkedList()

        for val in range(5):
            sll.insert_front(val)

        self.assertEqual(sll.insert_front(5), f"insert front {sll.head.val}")

    def test_all_items_when_empty(self):
        sll = SinglyLinkedList()

        self.assertListEqual(sll.all_nodes(), [])

    def test_all_items_when_not_empty_insert_front(self):
        sll = SinglyLinkedList()

        for val in range(5):
            sll.insert_front(val)

        self.assertListEqual(sll.all_nodes(), [4, 3, 2, 1, 0])

    def test_all_items_when_not_empty_insert_rear(self):
        sll = SinglyLinkedList()

        for val in range(5):
            sll.insert_rear(val)

        self.assertListEqual(sll.all_nodes(), [0, 1, 2, 3, 4])

    def test_remove_front(self):
        sll = SinglyLinkedList()

        for val in range(5):
            sll.insert_front(val)

        self.assertEqual(sll.remove_front(), f"remove front {4}")

    def test_remove_rear(self):
        sll = SinglyLinkedList()

        for val in range(5):
            sll.insert_front(val)

        self.assertEqual(sll.remove_rear(), f"remove rear {0}")

    def test_peek_front_when_empty(self):
        sll = SinglyLinkedList()

        self.assertIsNone(sll.peek_front())

    def test_peek_front_when_not_empty(self):
        sll = SinglyLinkedList()

        for val in range(5):
            sll.insert_front(val)

        self.assertEqual(sll.peek_front(), 4)

    def test_peek_rear_when_empty(self):
        sll = SinglyLinkedList()

        self.assertIsNone(sll.peek_rear())

    def test_peek_rear_when_not_empty(self):
        sll = SinglyLinkedList()

        for val in range(5):
            sll.insert_front(val)

        self.assertEqual(sll.peek_rear(), 0)

    def test_search_when_empty(self):
        sll = SinglyLinkedList()

        self.assertTupleEqual(sll.search(5), (False, -1))

    def test_search_when_not_empty(self):
        sll = SinglyLinkedList()

        for val in range(5):
            sll.insert_front(val)

        self.assertTupleEqual(sll.search(4), (True, 0))

    def test_len_when_empty(self):
        sll = SinglyLinkedList()

        self.assertEqual(sll.len, 0)

    def test_len_when_insert_front(self):
        sll = SinglyLinkedList()

        for val in range(5):
            sll.insert_front(val)

        self.assertEqual(sll.len, 5)

    def test_len_when_insert_rear(self):
        sll = SinglyLinkedList()

        for val in range(5):
            sll.insert_rear(val)

        self.assertEqual(sll.len, 5)

    def test_len_when_remove_front(self):
        sll = SinglyLinkedList()

        for val in range(5):
            sll.insert_front(val)

        for _ in range(3):
            sll.remove_front()

        self.assertEqual(sll.len, 2)

    def test_len_when_remove_rear(self):
        sll = SinglyLinkedList()

        for val in range(5):
            sll.insert_rear(val)

        for _ in range(2):
            sll.remove_rear()

        self.assertEqual(sll.len, 3)


if __name__ == "__main__":
    unittest.main()
