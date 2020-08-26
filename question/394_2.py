
s = "3[a]2[bc]"
# s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
s = "2[3[a]]"

stack = [["", 1]]
num = ""

for ch in s:
    if ch.isdigit():
        num += ch

    elif ch == '[':
        stack.append(["", int(num)])
        num = ""

    elif ch == ']':
        st, k = stack.pop()
        stack[-1][0] += st * k

    else:
        stack[-1][0] += ch

    print stack

print stack[0][0]
