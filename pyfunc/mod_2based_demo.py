# Modulo operation can be replaced with a simple bitwise
# "and" operation and make the operation faster if dealing
# with 2-based numbers

for i in range(10):
    print "i:", i, "    ", bin(i)
    print i % 4, "-->", i & 3
    print ""
