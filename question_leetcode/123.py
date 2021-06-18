def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    cost_1 = float("INF")
    profit_1 = 0
    cost_2 = float("INF")
    profit_2 = 0

    for price in prices:
        if price < cost_1:
            cost_1 = price

        elif cost_1 + profit_1 < price:
            profit_1 = price - cost_1

        new_price = price - profit_1

        if new_price < cost_2:
            cost_2 = new_price

        elif cost_2 + profit_2 < price:
            profit_2 = price - cost_2

    return profit_2


prices = [3, 3, 5, 0, 0, 3, 1, 4]
print maxProfit(prices)
