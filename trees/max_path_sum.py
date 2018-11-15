class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

result = 0
def max_path_sum(root, max_single_sum):
    global result
    if not root:
        return 0
    left = max_path_sum(root.left, max_single_sum)
    right = max_path_sum(root.right, max_single_sum)
    max_single_sum = max(max(left, right) + root.data, root.data)
    max_top = max(max_single_sum, left + right + root.data)
    result = max(result, max_top)
    return max_single_sum

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.left.left.left = BinaryTreeNode(-8)

max_path_sum(root, 0)
print result
