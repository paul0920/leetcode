
points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]

cmap = {}
res = 0

for i in points:

    for j in points:

        x = i[0] - j[0]
        y = i[1] - j[1]

        if x ** 2 + y ** 2 in cmap:
            cmap[x ** 2 + y ** 2] += 1

        else:
            cmap[x ** 2 + y ** 2] = 1

    # c(k, 2) x 2 = k!/(2! * (k-2)!) x 2 = k * (k-1)
    # this is due to 2 combinations from 1 set: (p1, p0, p2) and (p2, p0, p1)
    for k in cmap:
        res += cmap[k] * (cmap[k] - 1)

    cmap = {}

print res