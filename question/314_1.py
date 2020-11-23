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
        q = collections.deque([(root, 0)])

        while q:

            curr_node, curr_column = q.popleft()

            if curr_node:
                column_lookup[curr_column] += [curr_node.val]
                q.append((curr_node.left, curr_column - 1))
                q.append((curr_node.right, curr_column + 1))

        return [column_lookup[pos] for pos in sorted(column_lookup)]
