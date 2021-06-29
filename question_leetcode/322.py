def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    if not amount:
        return 0

    if not coins:
        return -1

    n = len(coins)
    dp = [float("INF")] * (amount + 1)  # dp stores the minimum number of coins to make up each amount
    dp[0] = 0

    for coin in coins:
        for dollar in range(coin, amount + 1):
            dp[dollar] = min(dp[dollar], dp[dollar - coin] + 1)
                                                           # ^ --> +1 is for coin itself

    if dp[amount] == float("INF"):
        return -1

    return dp[-1]


coins = [1, 2, 5]
amount = 11
print coinChange(coins, amount)
