class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bst_predecessor(root):
    temp = None
    if root.left:
        temp = root.left
        while temp.right:
            temp = temp.right
    return temp

def bst_sucessor(root):
    temp = None
    if root.right:
        temp = root.right
        while temp.left:
            temp = temp.left
    return temp

root = BinaryTreeNode(8)
root.left = BinaryTreeNode(3)
root.right = BinaryTreeNode(10)
root.left.left = BinaryTreeNode(1)
root.left.right = BinaryTreeNode(6)
root.right.left = BinaryTreeNode(9)
root.right.right = BinaryTreeNode(14)

node = bst_predecessor(root)
print node.data
node = bst_sucessor(root)
print node.data
