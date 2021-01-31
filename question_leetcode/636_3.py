
n = 2
logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]

n = 3
logs = ["0:start:0", "1:start:2", "1:end:3", "2:start:4", "2:end:7", "0:end:8"]


class SuperStack(object):

    def __init__(self):
        self.A = []

    def append(self, x):
        self.A.append([x, 0])

    def pop(self):
        x, y = self.A.pop()

        if self.A:
            self.A[-1][1] += y

        return x + y

    def add_across(self, y):

        if self.A:
            self.A[-1][1] += y

    def show(self):
        print self.A


res = [0] * n
stack = SuperStack()

for proc in logs:

    u_id, func_type, time = proc.split(":")
    u_id = int(u_id)
    time = int(time)

    if func_type == "start":
        stack.append(time)

    else:
        delta = time + 1 - stack.pop()
        res[u_id] += delta
        stack.add_across(delta)

        # This way is inefficient
        # stack = [t + delta for t in stack]

    # stack.show()
    # print "res:", res
    # print ""

print res
