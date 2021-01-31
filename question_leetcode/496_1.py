
# nums1 = [4, 1, 2]
# nums2 = [1, 3, 4, 2]

nums1 = [1, 3, 5, 2, 4]
nums2 = [6, 5, 4, 3, 2, 1, 7]

stack = []
res = [-1] * len(nums1)
j = 0

for i in range(len(nums1)):

    for j in range(nums2.index(nums1[i]), len(nums2)):

        if nums2[j] > nums1[i]:
            res[i] = nums2[j]
            break

print res
