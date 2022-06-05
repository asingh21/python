class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def least_common_ancestor(root, a, b):
    if not root:
        return
    if root.data == a or root.data == b:
        return root
    left = least_common_ancestor(root.left, a ,b)
    right = least_common_ancestor(root.right, a, b)
    if left and right:
        return root
    else:
        return left if left else right

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.left.left.left = BinaryTreeNode(8)

result = least_common_ancestor(root, 4, 6)
print result.data
