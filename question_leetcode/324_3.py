import random

# nums = [1, 2, 3, 4, 5, 6]
nums = [1, 5, 1, 1, 6, 4]


def nsmallest(nums, n):
    print "Kth smallest:", n
    start, end = 0, len(nums) - 1

    while True:

        pivot = nums[random.randint(start, end)]
        i, k, j = start, start, end
        print "pivot value:", pivot
        print "i:", i, "k:", k, "j:", j

        while k <= j:

            print "i:", i, "k:", k, "j:", j
            print nums

            # This is Dutch National Flag
            # Separate elements into 3 groups (S, pivot, L)
            if nums[k] < pivot:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k += 1
            elif nums[k] > pivot:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1
            else:
                k += 1

            print "i:", i, "k:", k, "j:", j
            print nums
            print ""

        if i <= n - 1 <= j:
            return pivot
        elif n - 1 < i:
            end = i - 1
        else:
            start = i + 1


n = len(nums)
# Translate n into Kth smallest
mid = nsmallest(nums, (n + 1) // 2)
print "median:", mid

# This lambda mapping only works for LLMSS order, not for SSMLL order
# meaning, > mid: i+=1; k+=1, < mid: j-=1
mapIdx = lambda i: (1 + 2 * i) % (n | 1)
i, k, j = 0, 0, n - 1

# This is also Dutch National Flag
# Separate elements into 3 groups (S, median, L)
while k <= j:

    if nums[mapIdx(k)] > mid:
        nums[mapIdx(k)], nums[mapIdx(i)] = nums[mapIdx(i)], nums[mapIdx(k)]
        i += 1
        k += 1
    elif nums[mapIdx(k)] < mid:
        nums[mapIdx(k)], nums[mapIdx(j)] = nums[mapIdx(j)], nums[mapIdx(k)]
        j -= 1
    else:
        k += 1

print nums
