# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        if not root1 or not root2:
            return False

        def get_the_other_nums(node):
            if not node:
                return

            get_the_other_nums(node.left)
            visited.add(target - node.val)
            get_the_other_nums(node.right)

        def find_matched_num(node):
            if not node:
                return False

            if node.val in visited:
                return True

            return find_matched_num(node.left) or find_matched_num(node.right)

        visited = set()
        get_the_other_nums(root1)

        return find_matched_num(root2)
