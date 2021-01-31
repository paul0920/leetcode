# This one gets TLE

A = [3, 1, 2, 4]

count = 1
stack = []
res = 0

while count <= len(A):

    for n in A:

        stack.append(n)

        if len(stack) == count:
            res += min(stack)
            # print stack, min(stack), res
            stack.pop(0)

    stack = []
    count += 1

print res % (10 ** 9 + 7)
