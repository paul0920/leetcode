
# nums = [4, 3, 2, 7, 8, 2, 3, 1]
nums = [4, 4, 2, 3]

for i in range(len(nums)):

    while i != nums[i] - 1 and nums[i] != nums[nums[i] - 1]:

        nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # !!! The following order is incorrect because the 2nd element,
        # nums[nums[i] - 1], uses the new nums[i] value !!!
        # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]

        print nums

print [nums[i] for i in range(len(nums)) if i != nums[i] - 1]
