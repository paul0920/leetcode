# pop & top are O(1) average time complexity since every element gets into and out once
# of stack/heap/hashset
import heapq


class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.heap = []
        self.popped_item = []
        self.id_count = 0

    def clear_stack(self):
        while self.stack and self.stack[-1] in self.popped_item:
            self.popped_item.remove(self.stack[-1])
            self.stack.pop()

    def clear_heap(self):
        while self.heap and self.heap[0] in self.popped_item:
            self.popped_item.remove(self.heap[0])
            heapq.heappop(self.heap)

    # O(log n)
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Use negative number and id for min heap
        item = (-x, -self.id_count)
        self.stack.append(item)
        heapq.heappush(self.heap, item)
        self.id_count += 1

    # O(1)
    def pop(self):
        """
        :rtype: int
        """
        self.clear_stack()
        item = self.stack.pop()
        self.popped_item.append(item)

        return -item[0]

    # O(1)
    def top(self):
        """
        :rtype: int
        """
        self.clear_stack()

        return -self.stack[-1][0]

    # O(log n)
    def peekMax(self):
        """
        :rtype: int
        """
        self.clear_heap()

        return -self.heap[0][0]

    # O(log n)
    def popMax(self):
        """
        :rtype: int
        """
        self.clear_heap()
        item = heapq.heappop(self.heap)
        self.popped_item.append(item)

        return -item[0]

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
