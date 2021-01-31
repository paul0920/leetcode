
T = [73, 74, 75, 71, 69, 72, 76, 73]

res = [0] * len(T)
stack = []

for i, t in enumerate(T):

    print stack

    while stack and T[stack[-1]] < t:
        idx = stack.pop()
        res[idx] = i - idx

        print "res:", res

    # Remember it's index instead of value
    # storing into the stack
    stack.append(i)

    print stack
    print ""

print res
