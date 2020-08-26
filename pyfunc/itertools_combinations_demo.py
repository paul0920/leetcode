import itertools


points = [1, 2, 3, 4, 5]
count = 0

for i, j, k in itertools.combinations(points, 3):
	count += 1
	print count, ":", i, j, k
