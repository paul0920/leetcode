
s = "babad"
s = "cbbd"


res = ""

def find_str(left, right):
    while 0 <= left and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return s[left + 1: right]


for i in range(len(s)):
    res = max(res, find_str(i, i), find_str(i, i+1), key=len)

print res
