# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        column_lookup = collections.defaultdict(list)
        res = []

        def DFS(col, row, node):

            if node:
                column_lookup[col] += [(row, node.val)]
                DFS(col - 1, row + 1, node.left)
                DFS(col + 1, row + 1, node.right)

        DFS(0, 0, root)

        for pos in range(min(column_lookup), max(column_lookup) + 1):
            column_lookup[pos].sort(key=lambda x: x[0])
            res += [[val for row, val in column_lookup[pos]]]

        return res
