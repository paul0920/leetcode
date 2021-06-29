def maxProfit(k, prices):
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    if not prices or k == 0:
        return 0

    cost = [float("INF")] * k
    profit = [0] * k

    for price in prices:
        for i in range(k):
            if i == 0:
                pre_cost = 0

            else:
                pre_cost = profit[i - 1]  # reinvest the previous profit to buy stock

            cost[i] = min(cost[i], price - pre_cost)
            profit[i] = max(profit[i], price - cost[i])

    return profit[-1]


k = 3
prices = [2, 6, 8, 7, 8, 7, 9, 4, 1, 2, 4, 5, 8]
print maxProfit(k, prices)
