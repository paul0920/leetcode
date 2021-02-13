# Time complexity: O(mn) by DP
# Space complexity: O(mn x min(m, n))


def shortestCommonSupersequence(self, str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    if not str1 and not str2:
        return ""

    res = ""
    pointer1 = 0
    pointer2 = 0

    for c in self.find_LCS(str1, str2):
        while c != str1[pointer1]:
            res += str1[pointer1]
            pointer1 += 1

        while c != str2[pointer2]:
            res += str2[pointer2]
            pointer2 += 1

        res += c
        pointer1 += 1
        pointer2 += 1

    return res + str1[pointer1:] + str2[pointer2:]


def find_LCS(self, str1, str2):
    n = len(str1)
    m = len(str2)
    dp = [[""] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]

            else:
                dp[i][j] += max(dp[i - 1][j], dp[i][j - 1], key=len)

    return dp[n][m]
