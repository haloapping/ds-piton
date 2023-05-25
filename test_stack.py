import unittest

from stack import Stack


class TestStack(unittest.TestCase):
    def test_stack_is_empty(self):
        stack = Stack(5)

        self.assertTrue(stack.is_empty())

    def test_stack_is_full(self):
        stack = Stack(5)

        for i in range(1, 6):
            stack.push(i)

        self.assertTrue(stack.is_full())

    def test_peek_stack_when_is_empty(self):
        stack = Stack(5)

        self.assertEqual(stack.peek(), "stack is empty")

    def test_peek_stack_when_is_not_empty(self):
        stack = Stack(5)

        for i in range(1, 6):
            stack.push(i)

        self.assertEqual(stack.peek(), "top 5")

    def test_pop_when_stack_is_empty(self):
        stack = Stack(5)

        self.assertEqual(stack.pop(), "stack is empty")

    def test_pop_when_stack_is_not_empty(self):
        stack = Stack(5)

        for i in range(1, 6):
            stack.push(i)

        self.assertEqual(stack.pop(), "pop 5")

    def test_push_when_stack_is_empty(self):
        stack = Stack(5)

        self.assertEqual(stack.push(5), "push 5")

    def test_push_when_stack_is_full(self):
        stack = Stack(5)

        for i in range(5):
            stack.push(i)

        self.assertEqual(stack.push(5), "stack is full")

    def test_search_when_empty(self):
        stack = Stack(5)

        self.assertEqual(stack.search(5), "stack is empty")

    def test_search_when_not_empty_found(self):
        stack = Stack(5)

        for i in range(5):
            stack.push(i)

        self.assertEqual(stack.search(2), (3, True))

    def test_search_when_not_empty_not_found(self):
        stack = Stack(5)

        for i in range(5):
            stack.push(i)

        self.assertEqual(stack.search(5), (-1, False))

    def test_show_all_items_when_stack_is_empty(self):
        stack = Stack(5)

        self.assertEqual(stack.show_all_items(), "stack is empty")

    def test_show_all_items_when_stack_is_not_empty(self):
        stack = Stack(5)

        for i in range(5):
            stack.push(i)

        self.assertEqual(stack.show_all_items(), [0, 1, 2, 3, 4])
