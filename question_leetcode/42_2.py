height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

if len(height) < 3:
    print 0

v_left = []
l_max = 0

for i, n in enumerate(height):
    l_max = max(l_max, n)
    v_left.append(l_max)

r_max = 0
res = 0

for i in range(len(height) - 1, -1, -1):
    r_max = max(r_max, height[i])
    res += (min(v_left[i], r_max) - height[i])

print res