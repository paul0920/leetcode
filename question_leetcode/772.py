
s = "2*(5+5*2)/3+(6/2+8)"
s = "(2+6* 3+5- (3*14/7+2)*5)+3"

num = 0
stack = []
sign = "+"


def operate(sign, num):
    # Process the previous number & sign
    if sign == "+":
        stack.append(num)

    elif sign == "-":
        stack.append(num * -1)

    elif sign == "*":
        stack.append(stack.pop() * num)

    elif sign == "/":
        stack.append(int(stack.pop() / float(num)))


for c in s:

    if c.isdigit():
        num = num * 10 + int(c)

    elif c in ["+", "-", "*", "/", ")"]:
        operate(sign, num)

        # Process ")" immediately instead of waiting for another cycle
        if c == ")":

            # Remember to reset num's value
            num = 0

            # Need to use isinstance() to check whether the element is a number
            while isinstance(stack[-1], int):
                num += stack.pop()

            sign = stack.pop()
            operate(sign, num)

        num = 0
        sign = c

    elif c == "(":
        stack += [sign]
        num = 0
        sign = "+"

    # print stack

operate(sign, num)

print sum(stack)
