# This gets TLE!
# 45 / 47 test cases passed

import collections

# text = "ababa"
# text = "aaabaaa"
# text = "aaabbaaa"
# text = "abcdef"
text = "aaaaa"

count = collections.Counter(text)
stack = []
res = 0

for i in range(len(text)):

    stack.append(text[i])
    enter = 0

    for j in range(i+1, len(text)):

        if stack[-1] == text[j] and enter <= 1:
            if count[stack[-1]] - len(stack) > 0:
                stack.append(stack[-1])

        elif stack[-1] != text[j]:
            if count[stack[-1]] - len(stack) > 0 and enter == 0:
                stack.append(stack[-1])
            enter += 1

    res = max(res, len(stack))
    stack = []

print res
