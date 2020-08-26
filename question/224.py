s = "2-(5-6)"

res, num = 0, 0
stack = []
sign = 1

for c in s:

    if c.isdigit():
        num = num * 10 + int(c)

    elif c in ["+", "-"]:
        res += sign * num
        num = 0

        if c == "+":
            sign = 1

        else:
            sign = -1

    elif c == "(":
        stack += [res] + [sign]
        res, num, sign = 0, 0, 1

    elif c == ")":
        res = stack.pop(-2) + stack.pop(-1) * (res + sign * num)
        num = 0

res += sign * num

print res