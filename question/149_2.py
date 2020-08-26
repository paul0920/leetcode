# points = [[1,1],[2,2],[3,3]]
# points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# points = [[1,1],[1,1],[2,2],[2,2]]
# points = [[0,0],[1,1],[0,0]]
points = [[0,0],[94911151,94911150],[94911152,94911151]]

# Import the Decimal() function and set the precision
# However, by doing this, the runtime is large! (1564 ms)
from decimal import *
getcontext().prec = 25

n = len(points)

if n < 3:
    print n
    exit()

res = 0

for i in range(len(points)):

    c_map = {}
    overlap = 1
    count = 0

    for j in range(i + 1, len(points)):

        if i != j:

            if points[i][1] == points[j][1]:
                d = 0

            if points[i][0] == points[j][0]:
                d = float('INF')

                if points[i][1] == points[j][1]:
                    overlap += 1
                    continue

            else:
                d = Decimal(points[j][1] - points[i][1]) / Decimal(points[j][0] - points[i][0])

            if d in c_map:
                c_map[d] += 1

            else:
                c_map[d] = 1

            count = max(count, c_map[d])

    res = max(res, count + overlap)

print res