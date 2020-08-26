
# arr = [6, 2, 4]
# arr = [6, 5, 4, 3, 5, 6]
arr = [6, 5, 4, 3, 5, 2, 3]

stack = [float("INF")]
res = 0

for n in arr:

    while n >= stack[-1]:
        res += stack.pop() * min(stack[-1], n)

    stack.append(n)

while len(stack) > 2:
    res += stack.pop() * stack[-1]

print res
