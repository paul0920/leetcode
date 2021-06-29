def change(amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    if not coins:
        return 0

    dp = [0] * (amount + 1)
    dp[0] = 1  # initialize each coin itself

    for coin in coins:
        for dollar in range(coin, amount + 1):
            dp[dollar] += dp[dollar - coin]

    return dp[-1]


amount = 5
coins = [1, 2, 5]
print change(amount, coins)
