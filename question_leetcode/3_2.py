
# s = "pwwkew"
s = "abcabcbb"
# s = "vvvvvv"
# s = " "
# s = "au"
# s = "dvdf"

l = 0
r = 0
word = set()
res = 0

while l < len(s) and r < len(s):

    if not s[r] in word:
        word.add(s[r])
        r += 1
        res = max(res, r - l)

    else:
        word.remove(s[l])
        l += 1

    print l, r, word

print res
