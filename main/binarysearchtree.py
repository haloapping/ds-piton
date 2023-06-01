class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.left: Node = None
        self.right: Node = None


class BST:
    def __init__(self) -> None:
        self.root: Node = None
        self.preorder_nodes: list[int] = []
        self.inorder_nodes: list[int] = []
        self.postorder_nodes: list[int] = []

    def is_empty(self) -> bool:
        return self.root is None

    def insert(self, val: int) -> str:
        if self.root is None:
            self.root = Node(val)
            return f"insert {self.root.val} to root"
        else:
            return self.__insert(self.root, val)

    def __insert(self, root: Node, val: int) -> str:
        if val < root.val:
            if root.left is None:
                root.left = Node(val)
                return f"insert {root.left.val} to left"
            else:
                return self.__insert(root.left, val)
        elif val > root.val:
            if root.right is None:
                root.right = Node(val)
                return f"insert {root.right.val} to right"
            else:
                return self.__insert(root.right, val)
        else:
            return f"value {val} is exist"

    def min(self) -> None | int:
        if self.is_empty():
            return None
        else:
            return self.__min(self.root).val

    def __min(self, root: Node) -> Node:
        current_node = self.root

        while current_node.left is not None:
            current_node = current_node.left

        return current_node

    def max(self) -> None | int:
        if self.is_empty():
            return None
        else:
            return self.__max(self.root).val

    def __max(self, root: Node) -> Node:
        current_node = self.root

        while current_node.right is not None:
            current_node = current_node.right

        return current_node

    def find(self, val: int) -> bool:
        return self.__find(self.root, val)

    def __find(self, root: Node, val: int) -> bool:
        if root is None:
            return False
        elif val == root.val:
            return True
        elif val < root.val:
            return self.__find(root.left, val)
        elif val > root.val:
            return self.__find(root.right, val)
        else:
            return False

    def remove(self, val: int) -> str:
        return self.__remove(self.root, val)

    def __remove(self, root: Node, val: int) -> str:
        if root is None:
            return "tree is empty"

        if val < root.val:
            return self.__remove(root.left, val)
        elif val > root.val:
            return self.__remove(root.right, val)
        else:
            del_node: int

            if root.left is None:
                temp: Node = root.right
                del_node = root.val
                root = None
                return f"remove {del_node}"
            elif root.right is None:
                temp = root.left
                del_node = root.val
                root = None
                return f"remove {del_node}"

            temp = self.__min(root.right)
            root.val = temp.val

            root.right = self.__remove(root.right, temp.val)

        return f"remove {root.right}"

    def preorder_traversal(self) -> list[int]:
        return self.__preorder(self.root)

    def __preorder(self, root: Node) -> list[int]:
        if root is not None:
            self.preorder_nodes.append(root.val)
            self.__preorder(root.left)
            self.__preorder(root.right)
        else:
            return []

        return self.preorder_nodes

    def inorder_traversal(self) -> list[int]:
        return self.__inorder(self.root)

    def __inorder(self, root: Node) -> list[int]:
        if root is not None:
            self.__inorder(root.left)
            self.inorder_nodes.append(root.val)
            self.__inorder(root.right)
        else:
            return []

        return self.inorder_nodes

    def postorder_traversal(self) -> list[int]:
        return self.__postorder(self.root)

    def __postorder(self, root: Node) -> list[int]:
        if root is not None:
            self.__postorder(root.left)
            self.__postorder(root.right)
            self.postorder_nodes.append(root.val)
        else:
            return []

        return self.postorder_nodes
