import collections

p1 = [0, 0]
p2 = [1, 1]
p3 = [1, 0]
p4 = [0, 1]


def distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


box = collections.Counter()
points = [p1, p2, p3, p4]

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        box[distance(points[i], points[j])] += 1

# print box
# print box.values()

print len(box) == 2 and 4 in box.values() and 2 in box.values()
