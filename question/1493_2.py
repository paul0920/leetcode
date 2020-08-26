
# nums = [0,1,1,1,0,1,1,0,1]
# nums = [1,1,1]
# nums = [0,0,0]

      # 0 1 2 3 4 5 6 7 8 9 10
nums = [1,1,0,0,0,1,1,1,0,1,0]


zero = 1 # initialize
# zero = 0 (1 zero)
# zero = -1 (2 zeros)

j = 0

for i in range(len(nums)):

    print "i:", i, "j:", j, "zero:", zero

    if nums[i] == 0:
        zero -= 1

    print "i:", i, "j:", j, "zero:", zero

    # zero < 0 means window has 2 zeros at least
    if zero < 0:
        if nums[j] == 0:
            zero += 1

        j += 1

    print "i:", i, "j:", j, "zero:", zero
    print ""

print i - j
