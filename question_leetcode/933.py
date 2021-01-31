
class RecentCounter(object):

    def __init__(self):
        self.q = []

    def ping(self, t):

        self.q.append(t)

        # Find the number of requests between the window of
        # [t-3000, t]
        while self.q[0] < t - 3000:

            print self.q[0], t, self.q

            self.q.pop(0)

            print self.q[0], t, self.q
            print ""

        return len(self.q)


obj = RecentCounter()

print obj.ping(642)
print obj.ping(1849)
print obj.ping(4921)
print obj.ping(5936)
print obj.ping(5957)
