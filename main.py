from main.binarysearchtree import BST

bst = BST()

for val in range(5):
    bst.insert(val)

print(bst.preorder_traversal())
print(bst.inorder_traversal())
print(bst.postorder_traversal())
