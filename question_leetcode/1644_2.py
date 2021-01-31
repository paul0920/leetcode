# Time: O(n)
# Space: O(n)
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.res = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.search_LCA(root, p, q)

        return self.res

    def search_LCA(self, node, p, q):
        if node:
            left = self.search_LCA(node.left, p, q)
            right = self.search_LCA(node.right, p, q)

            # If both find, the current node is LCA
            if left and right:
                self.res = node

                return False

            # If either branch finds and the other node exists, the current node is LCA
            elif (left or right) and (node == p or node == q):
                self.res = node

                return False

            # Check whether p or q is in the tree
            elif node == p or node == q:

                return True

            # For everything else, return left or right if either finds something, otherwise return false
            else:

                return left or right


root = TreeNode(3)
root.right = TreeNode(1)
root.right.right = TreeNode(2)
obj = Solution()
print obj.lowestCommonAncestor(root, root.right, root.right.right).val
