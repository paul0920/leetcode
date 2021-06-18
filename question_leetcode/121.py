def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    cost = float("INF")
    profit = 0

    for price in prices:
        if price < cost:
            cost = price

        elif cost + profit < price:
            profit = price - cost

    return profit


prices = [7, 1, 5, 3, 6, 4]
print maxProfit(prices)
