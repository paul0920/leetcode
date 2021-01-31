
nums = [1, 2, 2, 3, 1]

idx_loc = {}

for i, n in enumerate(nums):

	if n in idx_loc:
		idx_loc[n].append(i)

	else:
		idx_loc[n] = [i]

degree = max([len(v) for v in idx_loc.values()])

res = float('INF')

for n in nums:
	if len(idx_loc[n]) == degree:
		res = min(res, idx_loc[n][-1] - idx_loc[n][0] + 1)

print res
