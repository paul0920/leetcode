import bisect
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
        return bisect.bisect(self.pro, seed)


w = [1, 2, 3]
obj = Solution(w)

for _ in range(6):
    print obj.pickIndex()
