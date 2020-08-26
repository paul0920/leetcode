# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):

        self.res = []
        self.path = []

        def find(node, target):

            if not node:
                return

            self.path.append(node.val)

            if node.val == target:
                if not node.left and not node.right:
                    # Remember to use deep copy, self.path[:],
                    # instead of self.path
                    self.res.append(self.path[:])

            find(node.left, target - node.val)
            find(node.right, target - node.val)

            self.path.pop()

        find(root, sum)

        return self.res
