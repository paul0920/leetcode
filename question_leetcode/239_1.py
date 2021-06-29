import collections

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

res = []
q = collections.deque()

for i in range(len(nums)):

    # Start sliding the window, q, in the size of k
    if q and i - q[0] >= k:
        q.popleft()

    # Compare the new element, nums[i], in the window
    # and make sure q[0] is the largest value in this window
    while q:
        if nums[q[-1]] < nums[i]:
            q.pop()

        else:
            break

    q.append(i)

    # This is the start of the 1st window
    if i >= k - 1:
        res.append(nums[q[0]])

print res
