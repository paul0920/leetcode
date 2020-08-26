
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        val = []

        def dfs(root):

            if not root:
                return

            else:
                val.append(root.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return len(set(val)) == 1
