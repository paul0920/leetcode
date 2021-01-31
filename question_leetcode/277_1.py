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

        if not n:
            return -1

        status = True

        for i in range(n):
            for j in range(n):

                if i != j and knows(i, j) or not knows(j, i):
                    status = False
                    break

            if status:
                return i

            status = True

        return -1
