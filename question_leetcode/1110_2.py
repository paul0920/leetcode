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

    # Make searching elements faster by using set()
    des = set(to_delete)
    self.res = []

    def find(node, parent):

        if not node:
            return None

        if node.val in des:

            # Parent of node.left and node.right
            # will be deleted. Pass False
            node.left = find(node.left, False)
            node.right = find(node.right, False)

            return None

        else:

            # node has no parent and not in des
            if not parent:
                self.res.append(node)

            # node.left and node.right have parent
            node.left = find(node.left, True)
            node.right = find(node.right, True)

            return node

    # root has no parent
    find(root, False)

    return self.res
