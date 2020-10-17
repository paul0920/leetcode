
nums = [2, 3, 1, 1, 4]
nums = [3, 2, 2, 0, 4]
nums = [2, 1, 0, 1, 4]
nums = [1, 1, 1, 1, 0]


if len(nums) <= 1:
    print 0
    exit()

cur_pos = 0
next_pos = nums[0]
the_farest_pos = 0
jump_count = 1

while next_pos < len(nums) - 1:

    for pos in range(cur_pos, next_pos + 1):
        the_farest_pos = max(the_farest_pos, pos + nums[pos])

    cur_pos, next_pos = next_pos, the_farest_pos

    if cur_pos == next_pos:
        print -1
        exit()

    jump_count += 1

print jump_count
