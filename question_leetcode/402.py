
num = "1432219"
k = 5
# num = "10"
# k = 2


stack = []

for n in num:

    # Make an ascending array
    while stack and k and stack[-1] > n:
        stack.pop()
        k -= 1

    stack.append(n)

# Remove elements from right to left
if k:
    stack[:] = stack[:-k]

# Strip the leading "0"
print "".join(stack).lstrip("0") or "0"
