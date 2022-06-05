class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

total_sum = []
stack = []
def sum_of_all_paths(root):
    if not root:
        return
    stack.append(root.data)
    sum_of_all_paths(root.left)
    if not root.left and not root.right:
        sum = 0
        for i in stack:
            sum = (sum * 10) + i
        total_sum.append(sum)
    sum_of_all_paths(root.right)
    stack.pop()


root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.left.left.left = BinaryTreeNode(8)

sum_of_all_paths(root)
print total_sum
