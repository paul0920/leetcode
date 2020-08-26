from collections import deque

s = "the sky is blue"

left, right = 0, len(s) - 1
# remove leading spaces
while left <= right and s[left] == ' ':
    left += 1

# remove trailing spaces
while left <= right and s[right] == ' ':
    right -= 1

d, word = deque(), []

# push word by word in front of deque
while left <= right:
    if s[left] == ' ' and word:
        d.appendleft(''.join(word))
        print d
        word = []

    elif s[left] != ' ':
        word.append(s[left])
        #print word

    left += 1

d.appendleft(''.join(word))
print ' '.join(d)