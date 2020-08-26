# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """

        self.box = {}

        def cache_knows(a, b):

            if (a, b) in self.box:
                return self.box[(a, b)]

            self.box[(a, b)] = knows(a, b)

            return self.box[(a, b)]

        if not n:
            return -1

        candidate = 0

        for i in range(1, n):

            if cache_knows(candidate, i):
                candidate = i

        for j in range(n):

            if candidate != j and cache_knows(candidate, j) or not cache_knows(j, candidate):
                return -1

        return candidate
