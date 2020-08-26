import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(4)
root.left = TreeNode(1)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(3)


def walk(node):
    if not node:
        return 0

    if node in box:
        return box[node]

    money = 0

    if node.left:
        money += walk(node.left.left) + walk(node.left.right)

    if node.right:
        money += walk(node.right.left) + walk(node.right.right)

    box[node] = max(money + node.val, walk(node.left) + walk(node.right))

    return box[node]


box = collections.defaultdict(int)
print walk(root)
