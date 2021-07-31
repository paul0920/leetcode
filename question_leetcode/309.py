def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2:
        return 0

    cost = float("INF")
    pre_profit = 0
    profit = 0

    for price in prices:
        cost = min(cost, price - pre_profit)
        # Use pre_profit and profit to track 2 virtual threads with one cool down period
        pre_profit = profit
        profit = max(profit, price - cost)

    return profit


prices = [1, 2, 3, 0, 2]
print maxProfit(prices)
