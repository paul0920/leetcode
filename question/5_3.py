class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return ""

        for window_len in range(len(s), 0, -1):
            for i in range(len(s) - window_len + 1):

                if self.is_palindrome(s, i, i + window_len - 1):

                    return s[i: i + window_len]

        return ""


    def is_palindrome(self, s, left, right):

        while left < right and s[left] == s[right]:
            left += 1
            right -= 1

        return left >= right


s = "babad"
obj = Solution()
print obj.longestPalindrome(s)
