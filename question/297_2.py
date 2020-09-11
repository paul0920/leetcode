import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(-1)
root.left = TreeNode(0)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.left.right.left = TreeNode(7)
# root.left.right.right = TreeNode(8)
root.right = TreeNode(1)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(5)
# root.right.left.left = TreeNode(9)
# root.right.left.right = TreeNode(10)

def serialize(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """

    if not root:
        return None

    q = collections.deque([root])
    res = []

    while q:

        node = q.popleft()

        if node:
            q.append(node.left)
            q.append(node.right)

        res += [str(node.val) if node else "x"]

    return ",".join(res)


def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """

    if not data:
        return None

    data_arr = data.split(",")
    idx = 0
    root_node = TreeNode(int(data_arr[idx]))
    q = collections.deque([root_node])
    idx += 1

    while q:

        node = q.popleft()

        if data_arr[idx] != "x":
            node.left = TreeNode(int(data_arr[idx]))
            q.append(node.left)

        idx += 1

        if data_arr[idx] != "x":
            node.right = TreeNode(int(data_arr[idx]))
            q.append(node.right)

        idx += 1

    return root_node


print serialize(root)
print ""

new = deserialize(serialize(root))
print ""
print new.val
print new.left.val
print new.right.val

# print new.val
# print new.left.val
# print new.right.val
# print new.right.left.val
# print new.right.right.val
