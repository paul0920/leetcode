
s = "ab(c)(d"

stack = []
cur = ""

for c in s:

    if c == "(":
        stack += [cur]
        cur = ""

    elif c == ")":
        if stack:
            cur = stack.pop() + "(" + cur + ")"

    else:
        cur += c

# This is to handel edge cases of missing  ")"
while stack:

    cur = stack.pop() + cur

print cur
