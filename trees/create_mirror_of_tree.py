class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_mirror_tree(root):
    if not root:
        return
    create_mirror_tree(root.left)
    create_mirror_tree(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp
    return root

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.left.left.left = BinaryTreeNode(8)
