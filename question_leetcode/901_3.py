
class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """

        count = 1

        # It's important to remember "<=" instead of "<"
        # due to the definition of the problem
        while self.stack and self.stack[-1][0] <= price:

            # Once remove the item from the stack,
            # +1 to the count for the future calculation
            count += self.stack.pop()[1]

        self.stack.append([price, count])

        print count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

S = StockSpanner()
S.next(100)
S.next(80)
S.next(60)
S.next(70)
S.next(60)
S.next(75)
S.next(85)
