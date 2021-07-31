def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0

    cost1 = float("INF")
    cost2 = float("INF")
    profit1 = 0
    profit2 = 0

    for price in prices:
        cost1 = min(cost1, price)
        profit1 = max(profit1, price - cost1)
        cost2 = min(cost2, price - profit1)
        profit2 = max(profit2, price - cost2)

    return profit2


prices = [3, 3, 5, 0, 0, 3, 1, 4]
print maxProfit(prices)
