import unittest

from main.deque import Deque


class TestDeque(unittest.TestCase):
    def test_deque_is_empty(self):
        deque = Deque(5)

        self.assertTrue(deque.is_empty())

    def test_deque_is_full_when_enqueue_front(self):
        deque = Deque(5)

        for item in range(5):
            deque.enqueue_front(item)

        self.assertTrue(deque.is_full())

    def test_deque_is_full_when_enqueue_rear(self):
        deque = Deque(5)

        for item in range(5):
            deque.enqueue_rear(item)

        self.assertTrue(deque.is_full())

    def test_peek_front_when_empty(self):
        deque = Deque(5)

        self.assertEqual(deque.peek_front(), "stack is empty")

    def test_peek_rear_when_empty(self):
        deque = Deque(5)

        self.assertEqual(deque.peek_rear(), "stack is empty")

    def test_enqueue_front_when_not_empty(self):
        deque = Deque(5)

        for item in range(4):
            deque.enqueue_front(item)

        self.assertEqual(deque.enqueue_front(4), "enqueue front 4")

    def test_enqueue_front_when_full(self):
        deque = Deque(5)

        for item in range(5):
            deque.enqueue_front(item)

        self.assertEqual(deque.enqueue_front(5), "queue is full")

    def test_enqueue_rear_when_not_empty(self):
        deque = Deque(5)

        for item in range(4):
            deque.enqueue_rear(item)

        self.assertEqual(deque.enqueue_rear(4), "enqueue front 4")

    def test_enqueue_rear_when_full(self):
        deque = Deque(5)

        for item in range(5):
            deque.enqueue_rear(item)

        self.assertEqual(deque.enqueue_rear(5), "queue is full")

    def test_all_items_when_empty(self):
        deque = Deque(5)

        self.assertEqual(deque.all_items(), "queue is empty")

    def test_all_items_when_not_empty_enqueue_front(self):
        deque = Deque(5)

        for item in range(5):
            deque.enqueue_front(item)

        self.assertEqual(deque.all_items(), [4, 3, 2, 1, 0])

    def test_all_items_when_not_empty_enqueue_rear(self):
        deque = Deque(5)

        for item in range(5):
            deque.enqueue_rear(item)

        self.assertEqual(deque.all_items(), [0, 1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
