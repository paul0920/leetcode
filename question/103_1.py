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
        count = 1
        q = collections.deque()
        q.append((root, 1))

        while q:

            curr_node, layer = q.popleft()

            if layer > count:
                res += [stack] if not layer % 2 else [stack[::-1]]
                count += 1
                stack = []

            stack.append(curr_node.val)

            for next_node in (curr_node.left, curr_node.right):

                if next_node:
                    q.append((next_node, layer + 1))

        res += [stack] if not (layer + 1) % 2 else [stack[::-1]]

        return res
