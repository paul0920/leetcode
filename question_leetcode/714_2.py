def maxProfit(prices, fee):
    """
    :type prices: List[int]
    :type fee: int
    :rtype: int
    """
    if not prices:
        return 0

    cost = float("INF")
    profit = 0

    for price in prices:
        cost = min(cost, price - profit)
        profit = max(profit, price - cost - fee)

    return profit


prices = [1, 3, 2, 8, 4, 9]
fee = 2
prices = [1, 3, 7, 5, 10, 3]
fee = 3
print maxProfit(prices, fee)
