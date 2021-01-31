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
        return "None"

    return str(root.val) + "," + str(serialize(root.left)) + "," + str(serialize(root.right))


def build_tree( arr, i):
    i += 1

    # print i, arr, arr[i]

    # Don't use (not arr[i]) since number "0" will be counted!
    # if i >= len(arr) or (not arr[i]):
    if i >= len(arr) or arr[i] is None:
        return None, i

    node = TreeNode(arr[i])
    node.left, i = build_tree(arr, i)
    node.right, i = build_tree(arr, i)

    return node, i


def deserialize( data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """

    data_arr = data.split(",")

    for idx, n in enumerate(data_arr):

        if n == "None":
            data_arr[idx] = None

        else:
            data_arr[idx] = int(n)

    node, pos = build_tree(data_arr, -1)

    return node


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
