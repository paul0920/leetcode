# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        self.res = collections.defaultdict(list)

        def dfs(node):
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)
            idx = max(l, r) + 1

            self.res[idx] += [node.val]

            return idx

        dfs(root)

        return list(self.res.values())
