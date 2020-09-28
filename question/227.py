
s = "3+2*2"
s = "14-3/2"

num = 0
stack = []

# Initialize sign & s
sign = "+"
s += " "

for i in range(len(s)):

    if s[i].isdigit():
        num = num * 10 + int(s[i])

    elif (not s[i].isdigit() and s[i] != " ") or i == len(s) - 1:

        # Check previous sign and do operation
        if sign == "+":
            stack += [num]

        elif sign == "-":
            stack += [num * -1]

        elif sign == "*":
            stack += [stack.pop() * num]

        elif sign == "/":
            stack += [int(stack.pop() / float(num))]

        # Save the current sign
        sign = s[i]
        num = 0

print sum(stack)
