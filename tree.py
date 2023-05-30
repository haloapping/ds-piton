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


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Preorder Traversal  :", end=" ")
preoroder_traversal(root)
print()

print("Inorder Traversal   :", end=" ")
inorder_traversal(root)
print()

print("Postorder Traversal :", end=" ")
postorder_traversal(root)
