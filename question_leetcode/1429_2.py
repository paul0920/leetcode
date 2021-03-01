import collections


class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.is_unique = {}
        self.queue = collections.deque()

        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        while self.queue:
            n = self.queue[0]

            if not self.is_unique[n]:
                self.queue.popleft()

            else:
                return n

        return -1

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value not in self.is_unique:
            self.is_unique[value] = True
            self.queue.append(value)

        else:
            self.is_unique[value] = False

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
