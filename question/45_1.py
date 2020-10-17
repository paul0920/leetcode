
nums = [2, 3, 1, 1, 4]
nums = [3, 2, 2, 0, 4]
nums = [2, 0, 1, 1, 4]


if len(nums) == 1:
    print 0
    exit()

the_previous_idx = 0
the_farest_idx = 0
jump_count = 0

for idx in range(len(nums)):

    the_farest_idx = max(the_farest_idx, idx + nums[idx])

    print idx, the_previous_idx, the_farest_idx

    if idx == the_previous_idx:

        the_previous_idx = the_farest_idx
        jump_count += 1

        # Check whether this is the last jump to the last index
        if the_farest_idx >= len(nums) - 1:
            print jump_count
            exit()

print -1
