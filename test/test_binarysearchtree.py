import unittest

from main.binarysearchtree import BST


class TestBST(unittest.TestCase):
    def test_tree_is_empty(self):
        bst = BST()

        self.assertTrue(bst.is_empty())

    def test_insert_when_tree_is_empty(self):
        bst = BST()

        self.assertEqual(bst.insert(1), "insert 1 to root")

    def test_insert_to_left(self):
        bst = BST()

        bst.insert(2)

        self.assertEqual(bst.insert(1), "insert 1 to left")

    def test_insert_to_right(self):
        bst = BST()

        bst.insert(2)

        self.assertEqual(bst.insert(3), "insert 3 to right")

    def test_insert_when_val_is_exist(self):
        bst = BST()

        bst.insert(2)

        self.assertEqual(bst.insert(2), "value 2 is exist")

    def test_min_when_tree_is_empty(self):
        bst = BST()

        self.assertIsNone(bst.min())

    def test_min_when_tree_is_not_empty(self):
        bst = BST()
        nums = [3, 2, 10, 4, 1, 23, 100, 3]

        for num in nums:
            bst.insert(num)

        self.assertEqual(bst.min(), 1)

    def test_max_when_tree_is_empty(self):
        bst = BST()

        self.assertIsNone(bst.max())

    def test_max_when_tree_is_not_empty(self):
        bst = BST()
        nums = [3, 2, 10, 4, 1, 23, 100, 3]

        for num in nums:
            bst.insert(num)

        self.assertEqual(bst.max(), 100)

    def test_prorder_traversal_when_tree_is_empty(self):
        bst = BST()

        self.assertListEqual(bst.preorder_traversal(), [])

    def test_prorder_traversal_when_tree_is_not_empty(self):
        bst = BST()
        nums = [3, 2, 10, 4, 1, 23, 100, 3]

        for num in nums:
            bst.insert(num)

        self.assertListEqual(bst.preorder_traversal(), [3, 2, 1, 10, 4, 23, 100])

    def test_inorder_traversal_when_tree_is_empty(self):
        bst = BST()

        self.assertListEqual(bst.inorder_traversal(), [])

    def test_inorder_traversal_when_tree_is_not_empty(self):
        bst = BST()
        nums = [3, 2, 10, 4, 1, 23, 100, 3]

        for num in nums:
            bst.insert(num)

        self.assertListEqual(bst.inorder_traversal(), [1, 2, 3, 4, 10, 23, 100])

    def test_postorder_traversal_when_tree_is_empty(self):
        bst = BST()

        self.assertListEqual(bst.postorder_traversal(), [])

    def test_postorder_traversal_when_tree_is_not_empty(self):
        bst = BST()
        nums = [3, 2, 10, 4, 1, 23, 100, 3]

        for num in nums:
            bst.insert(num)

        self.assertListEqual(bst.postorder_traversal(), [1, 2, 4, 100, 23, 10, 3])

    def test_find_when_tree_is_empty(self):
        bst = BST()

        self.assertFalse(bst.find(1))

    def test_find_true_when_tree_is_not_empty(self):
        bst = BST()
        nums = [3, 2, 10, 4, 1, 23, 100, 3]

        for num in nums:
            bst.insert(num)

        print(bst.inorder_nodes)

        self.assertTrue(bst.find(100))

    def test_find_false_when_tree_is_not_empty(self):
        bst = BST()
        nums = [3, 2, 10, 4, 1, 23, 100, 3]

        for num in nums:
            bst.insert(num)

        print(bst.inorder_nodes)

        self.assertFalse(bst.find(5))

    def test_remove_when_tree_is_empty(self):
        bst = BST()

        self.assertEqual(bst.remove(1), "tree is empty")

    def test_remove_when_not_have_child_node(self):
        bst = BST()
        nums = [3, 2, 10, 4, 1, 23, 100, 3]

        for num in nums:
            bst.insert(num)

        self.assertEqual(bst.remove(100), "remove 100")

    def test_remove_when_have_one_child_node(self):
        bst = BST()
        nums = [3, 2, 10, 4, 1, 23, 100, 3]

        for num in nums:
            bst.insert(num)

        self.assertEqual(bst.remove(23), "remove 23")

    def test_remove_when_have_two_child_nodes(self):
        bst = BST()
        nums = [3, 2, 10, 4, 1, 23, 100, 3]

        for num in nums:
            bst.insert(num)

        self.assertEqual(bst.remove(10), "remove 10")

    # def test_preorder_traversal_after_remove(self):
    #     bst = BST()
    #     nums = [3, 2, 10, 4, 1, 23, 100, 3]

    #     for num in nums:
    #         bst.insert(num)

    #     # bst.remove(100)
    #     bst.remove(23)
    #     bst.remove(10)

    #     self.assertListEqual(bst.preorder_traversal(), [1])
