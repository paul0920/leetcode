# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def delNodes(self, root, to_delete):
    """
    :type root: TreeNode
    :type to_delete: List[int]
    :rtype: List[TreeNode]
    """

    des = set(to_delete)
    self.res = []

    def find(node):

        if not node:
            return None

        if node.val in des:
            self.res.append(node.left)
            node.left = find(node.left)
            self.res.append(node.right)
            node.right = find(node.right)

            return None

        node.left = find(node.left)
        node.right = find(node.right)

        return node

    self.res.append(find(root))

    table = []

    # Since there is no information about
    # whether the parent exists in find(),
    # code needs to process some cases by removing
    # elements in self.res in the final stage
    for n in self.res:
        if n is not None and not n.val in des:
            table.append(n)

    return table
