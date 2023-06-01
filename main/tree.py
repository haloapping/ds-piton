class Node:
    def __init__(self, val) -> None:
        self.val: int = val
        self.left: Node = None
        self.right: Node = None


def preoroder_traversal(root: Node):
    if root is not None:
        print(root.val, end=" ")
        preoroder_traversal(root.left)
        preoroder_traversal(root.right)


def inorder_traversal(root: Node):
    if root is not None:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)


def postorder_traversal(root: Node):
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=" ")
