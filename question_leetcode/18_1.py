nums = [-1,0,-5,-2,-2,-4,0,1,-2]; target = -9

# Overall, we can use recursive way to solve the problem from
# 2 Sum ---> N Sum

def threeSum(n, t):
    if len(n) < 3:
        return []

    res = set()
    dist = {}

    for i in range(len(n) - 2):

        t1 = t - n[i]

        # This is to identify those unnecessary looping cases
        if n[i] * 3 > t or n[-1] * 3 < t:
            break

        if i > 0 and n[i] == n[i - 1]:
            continue

        for j in range(i + 1, len(n)):

            if t1 - n[j] in dist:
                res.add((n[i], n[j], t1 - n[j]))

            dist[n[j]] = j

        dist = {}

    return map(list, res)


nums.sort()
res3sum = []
ans = []
dist = {}

for i in range(len(nums) - 3):

    if len(nums) < 4:
        print ans
        exit()

    new_target = target - nums[i]

    # This is to identify those unnecessary looping cases
    # by taking advantage of sorted array
    if nums[i] * 4 > target or nums[-1] * 4 < target:
        break

    if i > 0 and nums[i] == nums[i - 1]:
        continue

    res3sum[:] = threeSum(nums[i + 1:], new_target)

    for j in res3sum:
        ans.append(j + [nums[i]])

print ans