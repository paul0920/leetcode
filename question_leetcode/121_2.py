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
        cost = min(cost, price)
        profit = max(profit, price - cost)

    return profit


prices = [7, 1, 5, 3, 6, 4]
print maxProfit(prices)

# 6 stock questions:
# 1) 121. Best Time to Buy and Sell Stock
# 2) 122. Best Time to Buy and Sell Stock II
# 3) 123. Best Time to Buy and Sell Stock III
# 4) 188. Best Time to Buy and Sell Stock IV
# 5) 714. Best Time to Buy and Sell Stock with Transaction Fee
# 6) 309. Best Time to Buy and Sell Stock with Cooldown
