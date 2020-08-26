import collections

s = "AABABBA"
# k = 0
k = 1

maxf = res = 0
count = collections.defaultdict(int)

for i, c in enumerate(s):

    count[c] += 1
    maxf = max(maxf, count[c])

    if res - maxf < k:
        res += 1

    else:
        count[s[i - res]] -= 1

print res
