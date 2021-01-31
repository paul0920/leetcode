
# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 3
# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 0
nums = [1, 1, 3, 1]
target = 3


left = 0
right = len(nums) - 1

# "=" needs to be consider to cover the following case:
# nums = [1]; target = 1
while left <= right:

    mid = (left + right) / 2

    if nums[mid] == target:
        print True
        exit()

    # fail to estimate which side is sorted
    if nums[mid] == nums[right]:
        right -= 1

    # check whether this section is sorted, mid -> right
    elif nums[mid] > nums[right]:

        # No need to check target == nums[mid]
        if nums[left] <= target < nums[mid]:

            if nums[left] == target:
                print True
                exit()

            else:
                right = mid - 1

        # left jumps to mid + 1 instead of mid
        # since we already checked whether target == nums[mid] previously
        else:
            left = mid + 1

    # check whether this section is sorted, left -> mid
    else:

        if nums[mid] < target <= nums[right]:

            if nums[right] == target:
                print True
                exit()

            else:
                left = mid + 1

        else:
            right = mid - 1

print False
