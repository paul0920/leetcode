import random


class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """

        self.pro = []
        total = sum(w)

        for i in range(len(w)):
            self.pro.append(float(w[i]) / total)

            if i > 0:
                self.pro[i] += self.pro[i - 1]

    def pickIndex(self):
        """
        :rtype: int
        """

        seed = random.random()

        left = 0
        right = len(self.pro) - 1

        while left < right:

            mid = left + (right - left) / 2

            if self.pro[mid] < seed:

                left = mid + 1

            else:

                right = mid

        return left


w = [1, 2, 3]
obj = Solution(w)

for _ in range(6):
    print obj.pickIndex()
