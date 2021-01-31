class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return ""

        max_str = ""
        for idx_middle in range(len(s)):

            sub_str = self.sub_palindrome(s, idx_middle, idx_middle)

            if len(sub_str) > len(max_str):
                max_str = sub_str

            sub_str = self.sub_palindrome(s, idx_middle, idx_middle + 1)

            if len(sub_str) > len(max_str):
                max_str = sub_str

        return max_str

    def sub_palindrome(self, sub_str, left, right):

        while 0 <= left and right < len(sub_str):

            if sub_str[left] != sub_str[right]:
                break

            left -= 1
            right += 1

        return sub_str[left + 1: right]
