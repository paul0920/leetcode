import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(9)
root.right.left.right = TreeNode(10)

g = collections.defaultdict(list)
q = [(root, 0)]

while q:

    g_tmp = collections.defaultdict(list)
    q_temp = []

    for curr_node, idx in q:

        g_tmp[idx] += [curr_node.val]

        if curr_node.left:
            q_temp.append((curr_node.left, idx - 1))

        if curr_node.right:
            q_temp.append((curr_node.right, idx + 1))

    for i in g_tmp:
        g[i] += [val for val in sorted(g_tmp[i])]

    q = q_temp

print [g[i] for i in sorted(g)]
