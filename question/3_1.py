
s = 'tmmzuxt'

start = maxLength = 0
usedChar = {}

for i in range(len(s)):
    if s[i] in usedChar: # and start <= usedChar[s[i]]:
        start = usedChar[s[i]] + 1
        print s[i], start
    else:
        print s[i], 'new'
        maxLength = max(maxLength, i - start + 1)

    usedChar[s[i]] = i

print maxLength