class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}
        self.idx = 0

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        if number in self.lookup:
            self.lookup[number] += [self.idx]

        else:
            self.lookup[number] = [self.idx]

        self.idx += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """

        for n in self.lookup:

            if value - n in self.lookup:

                if self.lookup[n] != self.lookup[value - n]:
                    return True

                elif len(self.lookup[n]) >= 2:
                    return True

        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
