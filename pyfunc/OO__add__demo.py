class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        print 'Vector(%d, %d)' % (self.a, self.b)
        return 'This is the result: %d, %d' % (self.a, self.b)

    # Overloading Operators
    def __add__(self, c):
        return Vector(self.a + c.a, self.b + c.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)

print str(v2)
print ""
print v1 + v2
