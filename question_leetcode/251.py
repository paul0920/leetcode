v = [[1, 2, 10], [3], [4]]


class Vector2D(object):

    def __init__(self, a):

        def it():
            for line in a:
                for val in line:

                    # self.size is linked to the one below
                    self.size -= 1
                    # print self.size, "SIZE"
                    yield val

        self.it = it()
        self.size = sum(len(line) for line in a)

    def next(self):
        return next(self.it)

    def hasNext(self):
        return self.size


vec = Vector2D(v)

for i in range(vec.size):
    print vec.size, "current size"
    print vec.next()
