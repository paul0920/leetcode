
nums = [10**5+1, 100, 80, 60, 70, 60, 75, 85]
# nums = [10**5+1, 31, 41, 48, 59, 79]

stack = []
res = [0] * len(nums)

for i in range(len(nums) - 1, -1, -1):

    # The span of the stock's price today is defined as
    # the maximum number of consecutive days
    # (starting from today and going backwards)
    # for which the price of the stock was
    # less than or equal to today's price.
    while stack and nums[stack[-1]] < nums[i]:

        print stack

        idx = stack.pop()
        res[idx] = idx - i

        print res
        print ""

    stack.append(i)
    
print res
