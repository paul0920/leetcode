
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# root = TreeNode(0)
# root.left = TreeNode(0)
# root.left.left = TreeNode(0)
# root.right = TreeNode(0)


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root in (None, p, q):
            return root

        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if not left:
            return right

        if not right:
            return left

        # return root if left and right else left or right
