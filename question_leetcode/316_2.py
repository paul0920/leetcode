
s = "cdadabcc"
s = "ecbacba"


stack = []
idx_mapping = {c: i for i, c in enumerate(s)}

for idx, c in enumerate(s):

    if not c in stack:

        while stack and stack[-1] > c and idx < idx_mapping[stack[-1]]:
            stack.pop()

        stack.append(c)

print "".join(stack)
