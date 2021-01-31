
nums = [-1, 0, 1, 2, -1, -4]

if len(nums) < 3:
    print []

dist = {}
ans = []
ans1 = []
ans2 = []

# We can solve the problem by the following methodology.
# However, this will get Time Limit Exceeded.

for i in range(len(nums)):
    target = 0 - nums[i]
    for j in range(len(nums)):

        if target - nums[j] in dist and i != j and dist[target - nums[j]] != i:
            ans.append([target - nums[j], nums[j], nums[i]])

        dist[nums[j]] = j

    dist = {}

for i in ans:
    for j in i:
        ans1.append(j)

    ans1.sort()

    if not ans1 in ans2:
        ans2.append(ans1)

    ans1 = []

print ans2