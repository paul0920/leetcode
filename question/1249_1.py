
s = "ab(c)(d"

stack = []
pos = set()
res = ""

for idx, c in enumerate(s):

    if c == "(":
        stack += [(idx, c)]
        pos.add(idx)

    elif c == ")":
        if stack and stack[-1][-1] == "(":
            pos.remove(stack[-1][0])
            stack.pop()

        else:
            stack += [(idx, c)]
            pos.add(idx)

for idx, c in enumerate(s):

    if not idx in pos:
        res += c

print res
