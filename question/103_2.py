# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        res = []
        stack = []
        flag = 1
        q = collections.deque()
        q.append(root)

        while q:

            for _ in range(len(q)):

                curr_node = q.popleft()
                stack.append(curr_node.val)

                for next_node in (curr_node.left, curr_node.right):

                    if next_node:
                        q.append(next_node)

            res.append(stack[::flag])
            stack = []
            flag *= -1

        return res
