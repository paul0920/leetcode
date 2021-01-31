# Without using visited array, this solution would
# lead to TLE

nums = [5,4,0,3,1,6,2]

def finding(nums, idx, t):
	if nums[idx] == t:
		return 1

	else:
		return finding(nums, nums[idx], t) + 1


curr_max = 0

for i in range(len(nums)):
	curr_max = max(curr_max, finding(nums, i, i))

print curr_max