class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack_1.append(x)

    def stack1_to_stack2(self):
        if self.stack_2:
            return

        for _ in range(len(self.stack_1)):
            self.stack_2.append(self.stack_1.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.stack1_to_stack2()

        return self.stack_2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.stack1_to_stack2()

        return self.stack_2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack_1 and not self.stack_2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
