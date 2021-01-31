
str = "   -42"


sign = 1
num = 0
# Use strip() to remove all the white spaces
# as leading/trailing characters
res = list(str.strip(" "))

if not res:
    print 0
    exit()

if res[0] in ("+", "-"):

    if res[0] == "-":
        sign = -1

    res.pop(0)
    # del res[0]

for idx, n in enumerate(res):

    if n.isdigit():
        num = num * 10 + int(n)

    else:
        break

print max(-2**31 , min(2**31 - 1, num * sign))
