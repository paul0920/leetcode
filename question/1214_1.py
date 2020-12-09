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

        def tree_to_array(node):

            res = []

            if not node:
                return

            if node.left:
                res += tree_to_array(node.left)

            res += [node.val]

            if node.right:
                res += tree_to_array(node.right)

            return res

        def check_valid(num1, num2):

            if num1 in root1_array and num2 in root2_array:
                return True

            elif num2 in root1_array and num1 in root2_array:
                return True

            return False

        root1_array = tree_to_array(root1)
        root2_array = tree_to_array(root2)
        nums = root1_array + root2_array
        hashset = set()

        for num in nums:

            if target - num in hashset and check_valid(target - num, num):
                return True

            hashset.add(num)

        return False
