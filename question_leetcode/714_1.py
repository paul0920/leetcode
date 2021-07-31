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
        if cost > price:
            cost = price

        elif price - cost - fee > 0:
            profit += price - cost - fee
            # [1, 3, 7, 5, 10, 3]
            #  ^     ^  profit = 7 - 1 - 3 = 3, cost = 7 - 3 = 4
            #              ^  3 + (10 - 4 - 3) = 3 + 3 = 6 -> only get charged fee once because max profit is from
            #  monotonic increasing price points [1, 7, 10] (10 - 1 - 3 = 6)
            cost = price - fee

    return profit


prices = [1, 3, 2, 8, 4, 9]
fee = 2
prices = [1, 3, 7, 5, 10, 3]
fee = 3
print maxProfit(prices, fee)
