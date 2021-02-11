# Time complexity: O(n x a x sqrt(value)), a = factor counts

def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if not nums:
        return []

    nums.sort()
    dp = {}
    pre = {}

    for num in nums:
        dp[num] = 1
        pre[num] = -1

    last_num = nums[0]

    for n in nums:
        # Return factors, which doesn't include n itself
        for factor in get_factors(n):
            if factor not in dp:
                continue

            # Here is the key:
            if dp[factor] + 1 > dp[n]:
                dp[n] = dp[factor] + 1
                pre[n] = factor

        if dp[last_num] < dp[n]:
            last_num = n

    return find_path(pre, last_num)


def find_path(pre, last_num):
    path = []

    while last_num != -1:
        path.append(last_num)
        last_num = pre[last_num]

    return path[::-1]


def get_factors(n):
    if n == 1:
        return []

    factor = 1
    factors = []

    while factor * factor <= n:

        if n % factor == 0:
            factors.append(factor)

            if factor * factor != n and factor != 1:
                factors.append(n // factor)

        factor += 1

    return factors


nums = [1, 2, 4, 8]
print largestDivisibleSubset(nums)
