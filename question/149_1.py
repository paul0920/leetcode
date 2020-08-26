# points = [[1,1],[2,2],[3,3]]
# points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# points = [[1,1],[1,1],[2,2],[2,2]]
# points = [[0,0],[1,1],[0,0]]
points = [[0,0],[94911151,94911150],[94911152,94911151]]

n = len(points)

if n < 3:
    print n
    exit()

def gcd(a, b):
    if b == 0:
        return a

    else:
        return gcd(b, a % b)

p_map = {}
res = 0

for i in range(len(points)):

    p_map = {}

    # Remember to count i-node itself
    dul_node = 1
    count = 0

    for j in range(i + 1, len(points)):

        if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
            dul_node += 1
            continue

        dy = points[j][1] - points[i][1]
        dx = points[j][0] - points[i][0]

        if dx == 0:
            slope = float('INF')

        # Use gcd() is easier and to prevent from dividing very large numbers, dy/dx, directly!
        else:
            d = gcd(dy, dx)
            slope = (dy / d, dx / d)

        if slope in p_map:
            p_map[slope] += 1

        else:
            p_map[slope] = 1

        count = max(count, p_map[slope])

    res = max(res, count + dul_node)

print res