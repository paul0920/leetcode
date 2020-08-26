
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(4)
root.left = TreeNode(1)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(3)

def rob(root):
    if not root:
        return 0

    money = 0

    if root.left:
        money += rob(root.left.left) + rob(root.left.right)

    if root.right:
        money += rob(root.right.left) + rob(root.right.right)

    return max(money + root.val, rob(root.left) + rob(root.right))


print rob(root)
