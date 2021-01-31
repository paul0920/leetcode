
# nums = [1, 1, 3, 2, 3, 1, 2, 4, 5, 5]
nums = [1, 1, 1, 1, 2, 2, 2, 2] # this code reports index = len(nums)/2 - 1 as the median
# nums = [1, 1, 1, 1, 1, 2, 2, 2, 2]
# nums = [1, 1, 1, 1, 6, 4, 4, 7] # this code reports index = len(nums)/2 - 1 as the median
# nums = [1, 1, 1, 6, 4, 4, 7]
# nums = [1, 1, 1, 19, 20, 21, 22]
# nums = [1, 1, 1, 4, 4, 7, 7, 7]
# nums = [1, 2, 1, 1, 3, 100, 90, 91, 92, 93, 61, 1, 1]
# nums = [1, 2, 4, 9, 10, 11] # this code reports index = len(nums)/2 - 1 as the median
# nums = [12, 13, 15, 16, 24, 15, 22, 10, 9, 13, 13, 18, 16, 25, 23, 24]
# nums = [1, 1, 2, 2, 3, 3]
# nums = [7, 7, 7, 12, 12, 13] # this code reports index = len(nums)/2 - 1 as the median
# nums = [7, 7, 7, 7, 12, 13]
# nums = [1.2, 1.3, 1.4, 2.2, 2.3] # Not working!
# nums = [-1, -1, -2, -10, 10, 23, 5, -5, -20, -20, -20]
# nums = [1, 2, 3, 4, 5, 6, 8, 9]

# Time complexity: O(n log 2^6) + o(n) = O(n)
# Space complexity: O(1)

# this code can find median of odd size array. However, for even size array,
# it reports the element with index = len(nums)/2 - 1

if len(nums) % 2 == 1:
	idx = len(nums)/2

else:
	idx = len(nums)/2 - 1

print "Sorted:", sorted(nums), "Size:", len(nums)
print "Median:", sorted(nums)[idx], "Index:", idx
print ""

# Make sure the element values are in the range of left and right
left, right = -2 ** 5, 2 ** 5
# Need to use float() to detect odd/even size of the array
half = float(len(nums)) / 2

while left <= right:

	count = 0
	mid = (left + right) / 2

	print "Left:", left, "Mid:", mid, "Right:", right

	for n in nums:

		# "=" needs to be included since we need to make sure
		# 4 is counted and treated as median instead of 5 in
		# [1, 1, 1, 4, 4, 6, 7]
		if n <= mid:
			count += 1

	print "Median?", mid, "	", "Count:", count, "Half size:", half

	# "=" makes index = len(nums)/2 as the median
	if count < half:
		left = mid + 1

	# "=" makes index = len(nums)/2 - 1 as the median
	elif count >= half:
		right = mid - 1

	print "Left:", left, "Mid:", mid, "Right:", right
	print ""


next_left = float("INF")
update_count = 0

# Handle the case of even size array
if len(nums) % 2 == 0:
	for n in nums:
		if n > left:
			next_left = min(next_left, n)
			update_count += 1

	if update_count == half:
		left = float(left+next_left) / 2

# print next_left, update_count

print ""
print "Final Median Number:", left
