
s = "1226"
# s = "1121"
# s = "0226"
# s = "226"


if not s or int(s[0]) == 0:
    print 0
    exit()

# dp = [0 for _ in range(len(s) + 1)]
dp = [0] * (len(s) + 1)
dp[0:2] = [1, 1]

print dp
print ""

for i in range(2, len(s) + 1):

    if 0 < int(s[i - 1: i]):
        dp[i] = dp[i - 1]

    print "one digit ", dp

    if 10 <= int(s[i - 2: i]) <= 26:
        dp[i] += dp[i - 2]

    print "two digits", dp
    print ""

print dp[-1]
