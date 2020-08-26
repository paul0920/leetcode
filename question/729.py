
class TreeNode(object):

    def __init__(self, st, en):
        self.st = st
        self.en = en
        self.left = None
        self.right = None


class MyCalendar(object):

    def __init__(self):
        self.root = None

    def create(self, node, start, end):

        if start >= node.en:
            if node.right:
                return self.create(node.right, start, end)

            else:
                node.right = TreeNode(start, end)

            return True

        if end <= node.st:
            if node.left:
                return self.create(node.left, start, end)

            else:
                node.left = TreeNode(start, end)

            return True

        else:
            return False

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """

        if not self.root:
            self.root = TreeNode(start, end)
            return True

        return self.create(self.root, start, end)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
