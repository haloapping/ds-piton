import unittest

from queue_ import Queue


class TestQueue(unittest.TestCase):
    def test_queue_is_empty(self):
        queue = Queue(5)

        self.assertTrue(queue.is_empty())

    def test_queue_is_full(self):
        queue = Queue(5)

        for i in range(5):
            queue.enqueue(i)

        self.assertTrue(queue.is_full())

    def test_enqueue_when_empty(self):
        queue = Queue(5)

        self.assertEqual(queue.enqueue(5), "enqueue 5")

    def test_enqueue_when_full(self):
        queue = Queue(5)

        for i in range(5):
            queue.enqueue(i)

        self.assertEqual(queue.enqueue(5), "queue is full")

    def test_dequeue_when_empty(self):
        queue = Queue(5)

        self.assertEqual(queue.dequeue(), "queue is empty")

    def test_dequeue_when_not_empty(self):
        queue = Queue(5)

        for i in range(5):
            queue.enqueue(i)

        self.assertEqual(queue.dequeue(), "dequeue 0")

    def test_search_when_empty(self):
        queue = Queue(5)

        self.assertEqual(queue.search(5), "queue is empty")

    def test_search_when_not_empty_found(self):
        queue = Queue(5)

        for i in range(5):
            queue.enqueue(i)

        self.assertEqual(queue.search(2), (3, True))

    def test_search_when_not_empty_not_found(self):
        queue = Queue(5)

        for i in range(5):
            queue.enqueue(i)

        self.assertEqual(queue.search(5), (-1, False))
