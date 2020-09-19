import random


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.idx = {}
        self.num = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if not val in self.idx:
            self.idx[val] = len(self.num)
            self.num += [val]

            return True

        else:
            return False

    # This is the KEY part!!!
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """

        if val in self.idx:
            idx_val = self.idx[val]

            self.num[idx_val] = self.num[-1]
            self.idx[self.num[-1]] = idx_val

            self.num.pop()
            self.idx.pop(val)

            return True

        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """

        return self.num[random.randint(0, len(self.num) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
