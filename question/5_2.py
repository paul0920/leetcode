
s = "baabaad"
s = "aacabdkacaa"
# s = "cbbd"

s_len = len(s)
dp = [[0] * s_len for _ in range(s_len)]
max_len = 0
res = ""

# Create a DP table for each char
for i in range(s_len):
    dp[i][i] = True
    max_len = 1
    res = s[i]

# Check whether the neighbor is the same char in length = 2
for i in range(s_len-1):

    if s[i] == s[i+1]:
        dp[i][i+1] = True
        max_len = 2
        res = s[i:i+2]

# Get the longest palindrome
for j in range(s_len):
    for i in range(0, j-1):

        # Check whether i ~ j and i+1 ~ j-1 are palindrome
        if s[i] == s[j] and dp[i+1][j-1]:
            dp[i][j] = True
            max_len = max(max_len, j - i + 1)

            if len(res) < max_len:
                res = s[i:j+1]

print res
