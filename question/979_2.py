
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(2)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.right = TreeNode(2)


def distributeCoins(root, pre=None):

    if not root:
        return 0

    res = distributeCoins(root.left, root) + distributeCoins(root.right, root)

    print pre.val if pre else "x", "pre"
    print root.val, "root"
    print res, "res"

    if pre:
        pre.val += root.val - 1

        print pre.val, "pre"

    print res + abs(root.val - 1), "return"
    print ""

    return res + abs(root.val - 1)


print distributeCoins(root)
