def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0

    cost = float("INF")
    profit = 0

    for price in prices:
        # Re-invest all the profit into purchasing the next stock
        # Codes are almost the same as 121_2.py except for the reinvestment
        cost = min(cost, price - profit)
        profit = max(profit, price - cost)

    return profit


prices = [7, 1, 5, 3, 6, 4]
print maxProfit(prices)
