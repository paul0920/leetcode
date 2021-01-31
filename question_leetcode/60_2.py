class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # num needs to be an array since index matters
        # in the while loop
        num = range(1, n + 1)
        # this is because index starts from 0
        k -= 1
        permutation = ""

        while n > 0:
            n -= 1
            remaining_combinations = self.factorial(n)
            index = k // remaining_combinations
            k %= remaining_combinations
            permutation += str(num[index])
            del num[index]

        return permutation

    def factorial(self, num):
        total = 1

        for i in range(1, num + 1):
            total *= i

        return total


n = 4
k = 9

obj = Solution()
print obj.getPermutation(n, k)
