# Time complexity: O(nlogn) ~ O(n^2)
# Space complexity: O(1)


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node = TreeNode(3)
node.left = TreeNode(2)
node.left.left = TreeNode(-1)
node.left.left.left = TreeNode(1)
node.left.left.left.left = TreeNode(5)


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        self.res = 0

        def pathSum(node, target):

            if not node:
                return

            if node.val == target:
                self.res += 1

            pathSum(node.left, target - node.val)
            pathSum(node.right, target - node.val)

        def find(node, target):

            if not node:
                return

            pathSum(node, target)
            find(node.left, target)
            find(node.right, target)

        find(root, sum)

        return self.res


sum = 5
obj = Solution()
print obj.pathSum(node, sum)
