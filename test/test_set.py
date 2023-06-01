import os
import sys
import unittest

sys.path.append(os.getcwd()[: len(os.getcwd()) - 5])
from main.set import Set


class TestSet(unittest.TestCase):
    def test_set_when_collection_is_empty(self):
        sets = Set()

        self.assertTupleEqual(sets.show(), ())

    def test_set_when_collection_is_not_empty(self):
        sets = Set(1, 2, 3, 4, 5)

        self.assertTupleEqual(sets.show(), (1, 2, 3, 4, 5))

    def test_set_when_collection_is_not_empty_duplicate(self):
        sets = Set(1, 2, 3, 4, 5, 1, 4, 5, 5)

        self.assertTupleEqual(sets.show(), (1, 2, 3, 4, 5))

    def test_add_when_empty(self):
        sets = Set()

        sets.add(1)
        sets.add(2)
        sets.add(3)

        self.assertTupleEqual(sets.show(), (1, 2, 3))

    def test_add_when_not_empty(self):
        sets = Set(1, 2)

        sets.add(3)
        sets.add(4)

        self.assertTupleEqual(tuple(sorted(sets.show())), (1, 2, 3, 4))


if __name__ == "__main__":
    unittest.main()
