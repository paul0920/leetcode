
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
        return node.val, 0

    if node.left:
        left_curr_max, left_next_max = walk(node.left)

    else:
        left_curr_max, left_next_max = 0, 0

    if node.right:
        right_curr_max, right_next_max = walk(node.right)

    else:
        right_curr_max, right_next_max = 0, 0

    curr_curr_max = max(left_next_max + right_next_max + node.val, left_curr_max + right_curr_max)

    return curr_curr_max, left_curr_max + right_curr_max


if not root:
    print 0

curr_max, next_max = walk(root)

print curr_max
