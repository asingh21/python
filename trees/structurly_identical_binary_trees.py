import Queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def structurally_identical_trees(root1, root2):
    if (not root1.left and not root2.left) and (not root1.right and not root2.right) and \
        (root1.data == root2.data):
        return True

    if (root1.data != root2.data) or (root1.left and not root2.left) or \
       (not root1.left and root2.left) or (root1.right and not root2.right) or \
       (not root1.right and root2.right):
       return False

    if root1.left and root2.left:
        left = structurally_identical_trees(root1.left, root2.left)
    else:
        return True

    if root1.right and root2.right:
        right = structurally_identical_trees(root1.right, root2.right)
    else:
        return True

    return left and right

root1 = BinaryTreeNode(1)
root1.left = BinaryTreeNode(2)
root1.right = BinaryTreeNode(3)
root1.left.left = BinaryTreeNode(4)
root1.left.right = BinaryTreeNode(5)
root1.right.left = BinaryTreeNode(6)
root1.right.right = BinaryTreeNode(7)
root1.left.left.left = BinaryTreeNode(8)

root2 = BinaryTreeNode(10)
root2.left = BinaryTreeNode(2)
root2.right = BinaryTreeNode(3)
root2.left.left = BinaryTreeNode(4)
root2.left.right = BinaryTreeNode(5)
root2.right.left = BinaryTreeNode(6)
root2.right.right = BinaryTreeNode(7)
root2.left.left.left = BinaryTreeNode(8)

print structurally_identical_trees(root1, root2)
