import collections

s = "cdadabcc"
s = "ecbacba"


stack = []
freq = collections.Counter(s)
flag = collections.defaultdict(int)

for c in s:

    freq[c] -= 1

    if flag[c] != 1:

        while stack and stack[-1] > c and freq[stack[-1]] > 0:
            flag[stack[-1]] = 0
            stack.pop()

        flag[c] = 1
        stack.append(c)

print "".join(stack)
