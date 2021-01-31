# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # Create a dummy node and insert it on top of the BST tree
        dummy_node = TreeNode(float('-INF'), None, root)
        self.stack = [dummy_node]
        self.leftmost = root
        self.rightmost = root

        # Find the minimum value
        while self.leftmost.left:
            self.leftmost = self.leftmost.left

        # Find the maximum value
        while self.rightmost.right:
            self.rightmost = self.rightmost.right

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack[-1].val < self.rightmost.val:
            return True

        return False

    def next(self):
        """
        :rtype: int
        """
        node = self.stack[-1]

        # Handle --> dummy node, 1, 3, 4
        if node.right:
            n = node.right

            while n:
                self.stack += [n]
                n = n.left

        else:
            # Handle --> x, 1, x, 4
            n = self.stack.pop()

            # Handle --> x, 3, x, 4, 5
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()

        return self.stack[-1].val

    def hasPrev(self):
        """
        :rtype: bool
        """
        if self.stack[-1].val > self.leftmost.val:
            return True

        return False

    def prev(self):
        """
        :rtype: int
        """
        node = self.stack[-1]

        if node.left:
            n = node.left

            while n:
                self.stack += [n]
                n = n.right

        else:
            n = self.stack.pop()

            while self.stack and self.stack[-1].left == n:
                n = self.stack.pop()

        return self.stack[-1].val


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)

obj = BSTIterator(root)
print "beginning:", obj.stack[-1].val
print ""
print "output:", obj.next()
print "output:", obj.next()
print "output:", obj.next()
print "output:", obj.next()
print "output:", obj.next()
print ""
print "output:", obj.prev()
print "output:", obj.prev()
print "output:", obj.prev()
print "output:", obj.prev()
