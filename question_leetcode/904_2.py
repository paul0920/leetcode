
tree = [1, 2, 3, 2, 2]

res = cur = count_b = a = b = 0

for c in tree:

    print a, b, c

    if c in (a, b):
        cur = cur + 1

    else:
        cur = count_b + 1

    if c == b:
        count_b += + 1

    else:
        count_b = 1

    if b != c:
        a, b = b, c

    res = max(res, cur)

    print cur, count_b, a, b
    print ""

print res
