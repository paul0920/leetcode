
class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.queue = [0] * self.size

        # Number of elements seen so far
        self.count = 0

        self.head = 0
        self.window_sum = 0

    def next(self, val):

        print ""

        self.count += 1

        # Calculate the new sum by shifting the window
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val

        print self.queue

        # move on to the next head
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val

        print self.queue

        return float(self.window_sum) / min(self.size, self.count)


obj = MovingAverage(3)

print obj.next(1)
print obj.next(10)
print obj.next(3)
print obj.next(5)
