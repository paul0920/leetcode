
height = [0,1,0,2,1,0,1,3,2,1,2,1]

stack = []  # store (height, index)
ans = 0

for i in range(1, len(height)):

    print "index:", i

    # skip the cases where height[i-1] = height[i]
    if height[i - 1] > height[i]:
        stack.append((height[i - 1], i - 1))

    if height[i - 1] < height[i]:
        prevI = i - 1
        print "prevI (1):", prevI

        while stack:

            print stack
            print "i =", i, "height[i] =",  height[i]

            if stack[-1][0] <= height[i]:

                # if the right elevation height is greater than the left one
                # we pop the left elevation since all the gatherable rain water
                # has been collected
                prevH, index = stack.pop()
                ans += (min(height[i], prevH) - height[prevI]) * (i - index - 1)
                prevI = index  # update the reference height

                print "prevI_if (2):", prevI, "ans:", ans

            else:

                # if the right elevation height is less than the left one
                # we can still gather rain water, but we keep the left
                # elevation for future right pillars to collect water
                prevH, index = stack[-1]
                ans += (min(height[i], prevH) - height[prevI]) * (i - index - 1)

                print "prevI_else (2):", prevI, "ans:", ans
                break

    print ""

print ans