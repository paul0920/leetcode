
A = [3, 1, 2, 4]

res = 0
stack = []

# Add [0] to the head and tail
A = [0] + A + [0]

for i in range(len(A)):

    while stack and A[stack[-1]] > A[i]:
        j = stack.pop()
        k = stack[-1]

        # A[j] is the min value of the left group + right group
        print "A[j]:", A[j], "  ", "i:", i, "j:", j, "k:", k
        res += A[j] * (i - j) * (j - k)

    stack.append(i)

print res % (10 ** 9 + 7)
