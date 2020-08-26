import collections

s = "AABABBA"
# k = 0
k = 1


count = collections.defaultdict(int)
curr_max_count = 0
curr_max_len = 0
start = 0

for idx, c in enumerate(s):

    count[c] += 1
    curr_max_count = max(count.values())

    if idx - start + 1 - curr_max_count > k:
        count[s[start]] -= 1
        start += 1

    curr_max_len = max(curr_max_len, idx - start + 1)

print curr_max_len
