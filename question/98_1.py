# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(node, lo=float('-INF'), hi=float('INF')):

            if not node:
                return True

            if not lo < node.val < hi:
                return False

            return dfs(node.left, lo, min(hi, node.val)) and dfs(node.right, max(lo, node.val), hi)

        return dfs(root)
