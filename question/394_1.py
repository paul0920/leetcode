
s = "3[a]2[bc]"
s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
# s = "2[3[a]]"

stack = []

for c in s:

    if c == ']':
        current = ''
        d = ''

        while stack[-1] != '[':
            # Instead of using current += stack.pop()[::-1],
            # this can prevent from reversing stack later on
            current = stack.pop() + current

        stack.pop()

        while stack and stack[-1].isdigit():
            # Instead of using d += stack.pop(),
            # this can prevent from reversing d later on
            d = stack.pop() + d

        stack.append(int(d) * current)

    else:
        stack.append(c)

    print stack

print "".join(stack)
