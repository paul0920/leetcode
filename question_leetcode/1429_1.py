import collections


class FirstUnique(object):
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.count = {}
        self.queue = collections.deque()

        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        for num in self.queue:
            if self.count[num] == 1:
                return num

        return -1

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value not in self.count:
            self.count[value] = 1
            self.queue.append(value)

        else:
            self.count[value] += 1

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
