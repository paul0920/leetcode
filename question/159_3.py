import collections

s = "ecebaa"
s = "bacc"


start = 0
count = collections.defaultdict(int)
res = 0
res_string = []

for idx, c in enumerate(s):

    count[c] += 1

    if len(count) > 2:
        count[s[start]] -= 1

        if not count[s[start]]:
            count.pop(s[start])

        start += 1

    res = max(res, idx - start + 1)
    res_string.append(s[start:idx+1])

print res
print res_string
