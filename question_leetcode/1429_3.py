class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.duplicates = set()
        self.dummy = ListNode(0)
        self.tail = self.dummy
        self.num_to_prev_node = {}

        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        if self.dummy.next:
            return self.dummy.next.val

        return -1

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        # Check whether there is any duplicate first
        if value in self.duplicates:
            return

        if value not in self.num_to_prev_node:
            self.extend_link_list(value)

            return

        self.duplicates.add(value)
        self.remove(value)

    def extend_link_list(self, value):
        self.tail.next = ListNode(value)
        self.num_to_prev_node[value] = self.tail
        self.tail = self.tail.next

    def remove(self, value):
        prev_node = self.num_to_prev_node[value]
        prev_node.next = prev_node.next.next

        # Need to check whether the next node is valid value or None
        if prev_node.next:
            node_value = prev_node.next.val
            # Update hash table
            self.num_to_prev_node[node_value] = prev_node

        else:
            # Update & move self.tail
            self.tail = prev_node

        del self.num_to_prev_node[value]

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
