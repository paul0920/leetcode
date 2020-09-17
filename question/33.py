
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0


left = 0
right = len(nums) - 1

while left <= right:

    mid = (left + right) / 2

    if nums[mid] == target:
        print mid
        exit()

    elif nums[mid] > nums[right]:

        if nums[left] <= target < nums[mid]:

            if nums[left] == target:
                print left
                exit()

            else:
                right = mid - 1

        else:
        # elif target < nums[left] or nums[mid] < target:

            left = mid + 1
            # if left >= len(nums):
            # print -1

    else:
    # elif nums[mid] <= nums[right]:

        if nums[mid] < target <= nums[right]:

            if nums[right] == target:
                print right
                exit()

            else:
                left = mid + 1

        else:
        # elif target < nums[mid] or nums[right] < target:

            right = mid - 1
            # if right < 0:
            # print -1

print -1
