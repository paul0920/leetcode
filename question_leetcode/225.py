class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue_1 = collections.deque()
        self.queue_2 = collections.deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue_1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for _ in range(len(self.queue_1) - 1):
            self.queue_2.append(self.queue_1.popleft())

        val = self.queue_1.popleft()
        self.queue_1, self.queue_2 = self.queue_2, self.queue_1

        return val

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        val = self.pop()
        self.push(val)

        return val

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if not self.queue_1:
            return True

        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
