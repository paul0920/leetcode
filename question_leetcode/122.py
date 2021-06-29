def maxProfit1(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0

    profit = 0

    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            profit += prices[i + 1] - prices[i]

    return profit


def maxProfit2(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0

    cost = float("INF")
    profit = 0

    for price in prices:
        if cost > price:
            cost = price

        elif price - cost > 0:
            profit += price - cost
            cost = price

    return profit


prices = [7, 1, 5, 3, 6, 4]
print maxProfit1(prices)
print maxProfit2(prices)
