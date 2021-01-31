
# This is O(n) 1 pass in-place solution
# Dutch national flag problem

nums = [2,0,2,1,1,0]

red, white, blue = 0, 0, len(nums) - 1

while white <= blue:

    print nums
    print red, white, blue

    if nums[white] == 0:
        nums[red], nums[white] = nums[white], nums[red]
        white += 1
        red += 1
    elif nums[white] == 1:
        white += 1
    else:
        nums[white], nums[blue] = nums[blue], nums[white]
        blue -= 1

    print nums
    print red, white, blue
    print ""