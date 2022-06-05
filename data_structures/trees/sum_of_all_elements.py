class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
sum = 0
def sum_of_all_elements(root):
    global sum
    if not root:
        return 0
    sum += root.data
    sum_of_all_elements(root.left)
    sum_of_all_elements(root.right)

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.left.left.left = BinaryTreeNode(8)

sum_of_all_elements(root)
print sum
