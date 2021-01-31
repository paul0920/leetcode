import collections


s = "PAYPALISHIRING"
numRows = 4


if not s or numRows == 1:
    print s
    exit()

y, x = 0, 0
idx = 0
flag = 0
h_map = collections.defaultdict(list)

while y < numRows:

    h_map[(y, x)] = s[idx]
    idx += 1

    # print y, x, flag

    if idx == len(s):
        break

    if 0 < y < numRows and flag == 1:
        y -= 1
        x += 1

    else:
        if y == 0 and flag == 1:
            flag = 0

        y += 1

        if y == numRows - 1:
            flag = 1

# for key in sorted(h_map):
#     print key, h_map[key]

print "".join([h_map[key] for key in sorted(h_map)])
