# This gets TLE

class StockSpanner(object):

    def __init__(self):
        self.price_arr = [10 ** 5 + 1]

    def next(self, price):

        self.price_arr.append(price)
        size_arr = len(self.price_arr)
        stack = []
        res = [0] * size_arr

        for i in range(size_arr - 1, -1, -1):

            while stack and self.price_arr[stack[-1]] < self.price_arr[i]:
                idx = stack.pop()
                res[idx] = idx - i

            stack.append(i)

        print res[-1]


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
