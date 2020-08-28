
s = "aaacba"


# print ord('a')

res, last = 0, [-1] * 3

for i, c in enumerate(s):

    last[ord(c) - 97] = i
    res += 1 + min(last)

    # print last

print res
