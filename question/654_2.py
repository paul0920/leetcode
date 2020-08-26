
nums = [3, 2, 1, 6, 0, 5]


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# stack is in decreasing order
stack = []

for next_node in nums:
    n = TreeNode(next_node)

    while stack and next_node > stack[-1].val:
        n.left = stack.pop()

    if stack:
        stack[-1].right = n

    stack.append(n)

    for node in stack:
        print node.val,
    print ""

print stack[0]
