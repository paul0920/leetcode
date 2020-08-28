import collections


s = "QWER"
# s = "QRWWQQRQ"


count = collections.Counter(s)
res = len(s)
s_len = len(s)
start = 0

for idx, c in enumerate(s):

    count[c] -= 1

    # Remember to include "start < s_len" statement
    while start < s_len and all(n <= len(s) / 4 for n in count.values()):

        # Keep tracking the window size in the while loop!
        res = min(res, idx - start + 1)
        count[s[start]] += 1
        start += 1

print res
