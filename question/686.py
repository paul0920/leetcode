
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        for i in range(len(B) / len(A) + 3):

            print i, A * i
            if B in A * i:
                return i

        return -1


app = Solution()
A = "abc"
B = "cabcabca"

ans = app.repeatedStringMatch(A, B)
print ""
print ans
