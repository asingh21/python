import Queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

ptr = 0
def diameter_binary_tree_recursive_1(root):
    global ptr
    if not root:
        return 0
    left = diamere_binary_tree_recursive(root.left)
    right = diamere_binary_tree_recursive(root.right)
    left += 1
    right += 1
    if right + left > ptr:
        ptr = right + left
    return max(left, right) + 1

def diameter_binary_tree_recursive_2(root):
    if not root:
        return 0
    lHeight = height(root.left)
    rHeight = height(root.right)
    #print "lHeight = {}".format(lHeight)
    #print "rHeight = {}".format(rHeight)
    lDiameter = diameter_binary_tree_recursive_2(root.left)
    rDiameter = diameter_binary_tree_recursive_2(root.right)
    return max(lHeight + rHeight + 1, max(lDiameter, rDiameter))

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.left.left.right = BinaryTreeNode(8)

print diameter_binary_tree_recursive_2(root)
