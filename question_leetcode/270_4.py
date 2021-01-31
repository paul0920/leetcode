class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(5)

target = 3.714286

num = root.val

while root:

    num = min(root.val, num, key = lambda x: abs(target - x))

    if target < root.val:
        root = root.left

    else:
        root = root.right


print num
