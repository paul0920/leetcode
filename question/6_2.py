
s = "PAYPALISHIRING"
numRows = 4


if not s or numRows == 1:
    print s
    exit()

res = [""] * numRows
i = 0
forward = 0

for c in s:

    res[i] += c

    if i == 0:
        forward = 1

    elif i == numRows - 1:
        forward = -1

    i += forward

print "".join(res)
