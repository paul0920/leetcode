# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        self.res = []

        def bfs(node):

            if not node:
                return

            q = collections.deque()
            q.append((node, 0))

            while q:

                curr_node, curr_layer = q.popleft()

                if len(self.res) == curr_layer:
                    self.res.append(curr_node.val)

                curr_layer += 1

                if curr_node.right:
                    q.append((curr_node.right, curr_layer))

                if curr_node.left:
                    q.append((curr_node.left, curr_layer))

        bfs(root)

        return self.res
