class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
sum = 0
stack = []
def path_with_given_sum(root, target_sum):
    global sum
    global stack
    if not root:
        return 0
    sum += root.data
    stack.append(root.data)
    if sum == target_sum:
        print stack
    path_with_given_sum(root.left, target_sum)
    path_with_given_sum(root.right, target_sum)
    sum -= root.data
    stack.pop()



root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(7)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(8)
root.left.left.left = BinaryTreeNode(9)

print path_with_given_sum(root, 10)
