
trips = [[3, 2, 7], [3, 7, 9], [8, 3, 9]]
capacity = 11

# 0 <= trips[i][1] < trips[i][2] <= 1000
stops = [0] * 1001

for n, i, j in trips:
    stops[i] += n
    stops[j] -= n

for v in stops:
    capacity -= v
    if capacity < 0:
        print False

print True
