
# Time complexity: O( len(nums2)*2 + len(nums1) )
# Space complexity: O( len(nums2) + len(nums1) )

# nums1 = [4, 1, 2]
# nums2 = [1, 3, 4, 2]

nums1 = [1, 3, 5, 2, 4]
nums2 = [6, 5, 4, 3, 2, 1, 7]

greater = {}
stack = []
res = []

for n in nums2:

	# Use "while" instead of "if" according to
	# the definition of "the next greater number"
	while stack and n > stack[-1]:
		greater[stack.pop()] = n

	stack.append(n)

print greater
print stack
print ""

for n in nums1:

	if n in greater:
		res.append(greater[n])

	else:
		res.append(-1)

print res
print [greater[n] if n in greater else -1 for n in nums1]
